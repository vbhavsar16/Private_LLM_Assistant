# app/config.py
#import os

#HF_TOKEN = os.getenv("HF_TOKEN")  # ← load token from env
#if HF_TOKEN is None:
#    raise ValueError("HF_TOKEN environment variable not set")

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50
VECTOR_DB_PATH = "faiss_store"
LLM_MODEL_NAME = "microsoft/phi-2"