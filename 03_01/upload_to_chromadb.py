import chromadb
from chromadb.utils import embedding_functions
import pandas as pd

CHROMA_PATH = "mitre_chroma_db"
EMBED_MODEL = "all-MiniLM-L6-v2"

# Only use the main MITRE and detections datasets
DATASETS = {
    "mitre": ("mitreembed_master_Chroma.csv", "Body"),
    "detections": ("master_detections.csv", None),  # We'll handle multi-col
    "cisa": ("CISA_combo_features_new.csv", "Body"),
}

client = chromadb.PersistentClient(path=CHROMA_PATH)
embed_fn = embedding_functions.SentenceTransformerEmbeddingFunction(model_name=EMBED_MODEL)

# Update these columns as needed for your detection file
DETECTION_CONTEXT_COLS = [
    "title", "description", "detection", "falsepositives", "tags", "references", "author"
]

def build_detection_docs(df):
    docs = []
    for _, row in df.iterrows():
        parts = []
        for col in DETECTION_CONTEXT_COLS:
            if col in df.columns and pd.notna(row[col]):
                parts.append(f"{col}: {row[col]}")
        doc = "\n".join(parts)
        docs.append(doc)
    return docs

for name, (csv_path, text_col) in DATASETS.items():
    print(f"Processing: {name} from {csv_path}")
    df = pd.read_csv(csv_path)

    if name == "detections":
        docs = build_detection_docs(df)
        metas = df[["title", "tags", "level", "author", "description"]].to_dict(orient="records")
    else:
        docs = df[text_col].astype(str).tolist()
        metas = df.drop(columns=[text_col]).to_dict(orient="records")

    ids = [f"{name}_{i}" for i in range(len(docs))]
    if name in [c.name for c in client.list_collections()]:
        client.delete_collection(name)
    coll = client.create_collection(name, embedding_function=embed_fn)
    coll.add(documents=docs, metadatas=metas, ids=ids)
    print(f"Loaded {len(docs)} docs into '{name}' collection.")
print("All collections uploaded.")
