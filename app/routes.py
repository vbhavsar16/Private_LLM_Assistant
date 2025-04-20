# app/routes.py
from fastapi import APIRouter, UploadFile, File, Form
from app.rag_pipeline import run_query_on_documents, index_document
from app.file_utils import process_document

router = APIRouter()

@router.post("/upload")
async def upload_doc(file: UploadFile = File(...)):
    text = await process_document(file)
    num_chunks = await index_document(text)
    return {"status": "uploaded", "chunks_indexed": num_chunks}

@router.post("/query")
async def query_docs(query: str = Form(...)):
    response = await run_query_on_documents(query)
    return {"answer": response}

@router.post("/reset")
async def reset_vector_store():
    from app.rag_pipeline import vs
    vs.reset()
    return {"status": "vector store reset"}