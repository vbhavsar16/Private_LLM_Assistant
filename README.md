# Private_LLM_Assistant

## Private Document QA Assistant

### Features
- Upload private PDFs, DOCX, txts
- Ask questions (RAG-based)
- Local-only LLM (Mistral 7B)
- Embeddings with sentence-transformers
- FAISS vector store
- FastAPI backend

### Run Locally

```bash
uvicorn app.main:app --reload
