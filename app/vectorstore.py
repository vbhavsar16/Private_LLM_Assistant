# app/vectorstore.py
import faiss
import os
import pickle
from app.embedding import embed_text
from app.config import VECTOR_DB_PATH

class VectorStore:
    def __init__(self, dim=384, path=VECTOR_DB_PATH):
        self.index = faiss.IndexFlatL2(dim)
        self.documents = []
        self.path = path
        os.makedirs(self.path, exist_ok=True)

    def add_documents(self, chunks):
        embeddings = embed_text(chunks)
        self.index.add(embeddings.cpu().numpy())
        self.documents.extend(chunks)

    def search(self, query, top_k=5):
        if len(self.documents) == 0:
            return []
        query_embedding = embed_text([query]).cpu().numpy()
        distances, indices = self.index.search(query_embedding, top_k)
        return [self.documents[i] for i in indices[0] if i < len(self.documents)]

    def save(self):
        faiss.write_index(self.index, f"{self.path}/index.faiss")
        with open(f"{self.path}/docs.pkl", "wb") as f:
            pickle.dump(self.documents, f)

    def load(self):
        try:
            self.index = faiss.read_index(f"{self.path}/index.faiss")
            with open(f"{self.path}/docs.pkl", "rb") as f:
                self.documents = pickle.load(f)
        except Exception:
            self.index = faiss.IndexFlatL2(384)
            self.documents = []

    def reset(self):
        self.index = faiss.IndexFlatL2(384)
        self.documents = []
        if os.path.exists(f"{self.path}/index.faiss"):
            os.remove(f"{self.path}/index.faiss")
        if os.path.exists(f"{self.path}/docs.pkl"):
            os.remove(f"{self.path}/docs.pkl")
