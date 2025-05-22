# mcp_grc_server.py

from fastapi import FastAPI, Request
import chromadb
from chromadb.utils import embedding_functions
import uvicorn

# CONFIG
CHROMA_PATH = "chroma_db"

# Load Chroma vector stores
client = chromadb.PersistentClient(path=CHROMA_PATH)
embed_fn = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
company_coll = client.get_collection("company_info")
reg_coll = client.get_collection("regulations")
pdf_coll = client.get_collection("pdfs")

app = FastAPI()

@app.post("/mcp")
async def mcp_grc_endpoint(request: Request):
    payload = await request.json()
    method = payload.get("method")
    params = payload.get("params")
    req_id = payload.get("id")
    k = params.get("k", 3)

    if method == "search_company_info":
        query = params.get("query", "")
        res = company_coll.query(query_texts=[query], n_results=k)
        results = [{"text": doc, "meta": meta} for doc, meta in zip(res['documents'][0], res['metadatas'][0])]
        return {"jsonrpc": "2.0", "result": results, "id": req_id}

    elif method == "search_regulations":
        query = params.get("query", "")
        res = reg_coll.query(query_texts=[query], n_results=k)
        results = [{"text": doc, "meta": meta} for doc, meta in zip(res['documents'][0], res['metadatas'][0])]
        return {"jsonrpc": "2.0", "result": results, "id": req_id}

    elif method == "search_pdfs":
        query = params.get("query", "")
        res = pdf_coll.query(query_texts=[query], n_results=k)
        results = [{"text": doc, "meta": meta} for doc, meta in zip(res['documents'][0], res['metadatas'][0])]
        return {"jsonrpc": "2.0", "result": results, "id": req_id}

    else:
        return {"jsonrpc": "2.0", "error": {"code": -32601, "message": "Method not found"}, "id": req_id}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8002)
