from fastapi import FastAPI, Request
from uuid import uuid4
from datetime import datetime
import uvicorn

app = FastAPI()
memory_store = {}

@app.get("/debug/memory")
async def debug_memory():
    """Return the entire memory store for debugging."""
    return memory_store

@app.post("/mcp")
async def mcp_memory_endpoint(request: Request):
    payload = await request.json()
    method = payload.get("method")
    params = payload.get("params", {})
    req_id = payload.get("id", 1)
    if method == "insert_memory":
        session_id = params.get("session_id")
        text = params.get("text")
        if not session_id or not text:
            return {"jsonrpc": "2.0", "error": {"code": -32602, "message": "Invalid params"}, "id": req_id}
        if session_id not in memory_store:
            memory_store[session_id] = []
        memory_store[session_id].append({
            "id": str(uuid4()),
            "text": text,
            "timestamp": datetime.now().isoformat()
        })
        return {"jsonrpc": "2.0", "result": "Memory inserted", "id": req_id}
    elif method == "fetch_memory":
        session_id = params.get("session_id")
        results = memory_store.get(session_id, [])
        return {"jsonrpc": "2.0", "result": results, "id": req_id}
    else:
        return {"jsonrpc": "2.0", "error": {"code": -32601, "message": "Method not found"}, "id": req_id}

if __name__ == "__main__":
    uvicorn.run("mcp_memory_server:app", host="0.0.0.0", port=8001, reload=True)
