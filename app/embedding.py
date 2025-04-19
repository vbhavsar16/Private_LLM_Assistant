# app/embedding.py
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_text(texts):
    return model.encode(texts, convert_to_tensor=True)