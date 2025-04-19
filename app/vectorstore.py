# app/vectorstore.py
import faiss
import os
import pickle
from app.embedding import embed_text

class VectorStore:
    def __init__(self, dim=384, path="faiss_store"):
        self.index = faiss.IndexFlatL2(dim)
        self.documents = []
        self.path = path

    def add_documents(self, chunks):
        embeddings = embed_text(chunks)
        self.index.add(embeddings.cpu().numpy())
        self.documents.extend(chunks)

    def search(self, query, top_k=5):
        query_embedding = embed_text([query]).cpu().numpy()
        distances, indices = self.index.search(query_embedding, top_k)
        return [self.documents[i] for i in indices[0]]

    def save(self):
        faiss.write_index(self.index, f"{self.path}/index.faiss")
        with open(f"{self.path}/docs.pkl", "wb") as f:
            pickle.dump(self.documents, f)

    def load(self):
        if os.path.exists(f"{self.path}/index.faiss"):
            self.index = faiss.read_index(f"{self.path}/index.faiss")
        if os.path.exists(f"{self.path}/docs.pkl"):
            with open(f"{self.path}/docs.pkl", "rb") as f:
                self.documents = pickle.load(f)