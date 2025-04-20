# app/rag_pipeline.py
from app.vectorstore import VectorStore
from app.llm import generate_response
from app.config import CHUNK_SIZE, CHUNK_OVERLAP
from langchain.text_splitter import RecursiveCharacterTextSplitter

vs = VectorStore()
vs.load()

def split_into_chunks(text):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )
    return splitter.split_text(text)

async def index_document(text: str) -> int:
    chunks = split_into_chunks(text)
    vs.add_documents(chunks)
    vs.save()
    return len(chunks)

async def run_query_on_documents(query: str) -> str:
    top_chunks = vs.search(query)
    if not top_chunks:
        return "No relevant information found."
    context = "\n".join(top_chunks)
    prompt = f"""You are a helpful assistant. Based only on the following document content:\n\n{context}\n\nAnswer this question:\n{query}"""
    return generate_response(prompt)