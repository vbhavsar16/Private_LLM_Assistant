# Private_LLM_Assistant

## Private Document QA Assistant

### Architecture Overview
- Upload private PDFs, DOCX, txts
- Ask questions (RAG-based)
- Local-only LLM (Mistral 7B)
- Embeddings with sentence-transformers
- FAISS vector store
- FastAPI backend

### Setup: Run Locally

```bash
uvicorn app.main:app --reload
```

### Or Setup: Run with Docker

```bash
docker build -t docqa .
docker run -p 8000:8000 docqa
```
