# app/config.py
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50
VECTOR_DB_PATH = "faiss_store"
LLM_MODEL_NAME = "mistralai/Mistral-7B-Instruct-v0.1"