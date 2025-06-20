from fastapi import FastAPI, Request
import chromadb
from chromadb.utils import embedding_functions
import uvicorn

CHROMA_PATH = "mitre_chroma_db"
EMBED_MODEL = "all-MiniLM-L6-v2"

client = chromadb.PersistentClient(path=CHROMA_PATH)
embed_fn = embedding_functions.SentenceTransformerEmbeddingFunction(model_name=EMBED_MODEL)

mitre_coll = client.get_collection("mitre", embedding_function=embed_fn)
detections_coll = client.get_collection("detections", embedding_function=embed_fn)
cisa_coll = client.get_collection("cisa", embedding_function=embed_fn)

app = FastAPI()

@app.post("/mcp")
async def mcp_endpoint(request: Request):
    payload = await request.json()
    method = payload.get("method")
    params = payload.get("params", {})
    req_id = payload.get("id", 1)
    k = params.get("k", 3)
    query = params.get("query", "")

    def format_res(res):
        return [
            {"text": doc, "meta": meta}
            for doc, meta in zip(res["documents"][0], res["metadatas"][0])
        ]

    if method == "search_mitre":
        res = mitre_coll.query(query_texts=[query], n_results=k)
        return {"jsonrpc": "2.0", "result": format_res(res), "id": req_id}
    elif method == "search_detections":
        res = detections_coll.query(query_texts=[query], n_results=k)
        return {"jsonrpc": "2.0", "result": format_res(res), "id": req_id}
    elif method == "search_cisa":
        res = cisa_coll.query(query_texts=[query], n_results=k)
        return {"jsonrpc": "2.0", "result": format_res(res), "id": req_id}
    else:
        return {"jsonrpc": "2.0", "error": {"code": -32601, "message": "Method not found"}, "id": req_id}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8003)
