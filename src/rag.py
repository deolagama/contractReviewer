# src/rag.py
import chromadb
from chromadb.config import Settings
from typing import List, Dict

class RAGStore:
    def __init__(self, persist_dir: str):
        self.client = chromadb.PersistentClient(path=persist_dir)
        self.collection = self.client.get_or_create_collection("contracts")

    def add(self, ids: List[str], texts: List[str], embeddings):
        self.collection.upsert(documents=texts, ids=ids, embeddings=embeddings.tolist())

    def query(self, query_text: str, embedding, top_k: int = 3) -> List[Dict]:
        results = self.collection.query(query_embeddings=[embedding.tolist()], n_results=top_k)
        return [{"text": t, "id": i} for t, i in zip(results["documents"][0], results["ids"][0])]
