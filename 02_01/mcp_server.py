from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import Any, List, Optional
from uuid import uuid4
import uvicorn
from datetime import datetime

app = FastAPI()

# In-memory stores for persistent data (for demonstration purposes)
memory_store = {}        # Stores Q&A conversation history
confidence_store = []    # Stores confidence logs for responses
feedback_store = []      # Stores user feedback (thumbs-up/thumbs-down)

# Optional Pydantic models for clarity (not strictly required)
class SearchRequest(BaseModel):
    query: str
    k: int = 1

class InsertMemoryRequest(BaseModel):
    session_id: str
    text: str

class MemoryRequest(BaseModel):
    session_id: str

@app.post("/mcp")
async def mcp_endpoint(request: Request):
    """
    Basic JSON-RPC endpoint for MCP.
    Supports:
      - search_documents: Returns dummy document(s) for a query.
      - insert_memory: Inserts a Q&A pair into memory_store.
      - fetch_memory: Retrieves conversation history.
      - insert_confidence: Logs response confidence (including model info).
      - insert_feedback: Records user feedback (thumbs-up/thumbs-down).
    """
    payload = await request.json()
    method = payload.get("method")
    params = payload.get("params")
    req_id = payload.get("id")

    # 1) search_documents: Return dummy document(s) for the given query.
    if method == "search_documents":
        query = params.get("query", "")
        k = params.get("k", 1)
        results = [{"text": f"Dummy document for query: '{query}'"} for _ in range(k)]
        return {"jsonrpc": "2.0", "result": results, "id": req_id}

    # 2) insert_memory: Log a Q&A pair into memory_store.
    elif method == "insert_memory":
        session_id = params.get("session_id")
        text = params.get("text")
        if not session_id or not text:
            return {"jsonrpc": "2.0", "error": {"code": -32602, "message": "Invalid params"}, "id": req_id}
        if session_id not in memory_store:
            memory_store[session_id] = []
        entry = {"id": str(uuid4()), "text": text}
        memory_store[session_id].append(entry)
        return {"jsonrpc": "2.0", "result": "Memory inserted", "id": req_id}

    # 3) fetch_memory: Retrieve conversation history for a session.
    elif method == "fetch_memory":
        session_id = params.get("session_id")
        if not session_id:
            return {"jsonrpc": "2.0", "error": {"code": -32602, "message": "Invalid params"}, "id": req_id}
        results = memory_store.get(session_id, [])
        return {"jsonrpc": "2.0", "result": results, "id": req_id}

    # 4) insert_confidence: Log the response's confidence details.
    elif method == "insert_confidence":
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "query": params.get("query", ""),
            "response": params.get("response", ""),
            "confidence_score": params.get("confidence_score", 0),
            "is_high_confidence": params.get("confidence_score", 0) > 0.8,
            "is_low_confidence": params.get("confidence_score", 0) < 0.4
        }
        confidence_store.append(log_entry)
        return {"jsonrpc": "2.0", "result": "Confidence log inserted", "id": req_id}

    # 5) insert_feedback: Record user feedback for a Q&A.
    elif method == "insert_feedback":
        feedback_entry = {
            "timestamp": datetime.now().isoformat(),
            "session_id": params.get("session_id", ""),
            "question": params.get("question", ""),
            "rating": params.get("rating", "")  # "thumbs_up" or "thumbs_down"
        }
        feedback_store.append(feedback_entry)
        return {"jsonrpc": "2.0", "result": "Feedback inserted", "id": req_id}

    # 6) If the method is not recognized, return an error.
    else:
        return {"jsonrpc": "2.0", "error": {"code": -32601, "message": "Method not found"}, "id": req_id}

# Debug endpoints for real-time reporting and inspection.
@app.get("/debug/memory")
async def debug_memory():
    """Return the current conversation memory for debugging."""
    return memory_store

@app.get("/debug/confidence")
async def debug_confidence():
    """Return the logged confidence data for real-time reporting."""
    return confidence_store

@app.get("/debug/feedback")
async def debug_feedback():
    """Return the recorded user feedback."""
    return feedback_store

if __name__ == "__main__":
    # Run the MCP server on host 0.0.0.0 and port 8080.
    uvicorn.run(app, host="0.0.0.0", port=8080)
