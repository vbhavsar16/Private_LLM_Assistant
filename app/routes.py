# app/routes.py
from fastapi import APIRouter, UploadFile, File, Form
from app.rag_pipeline import run_query_on_documents
from app.file_utils import process_document

router = APIRouter()

@router.post("/upload")
async def upload_doc(file: UploadFile = File(...)):
    text = await process_document(file)
    return {"status": "success", "length": len(text)}

@router.post("/query")
async def query_docs(query: str = Form(...)):
    response = await run_query_on_documents(query)
    return {"answer": response}
