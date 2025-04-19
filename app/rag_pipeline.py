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

async def run_query_on_documents(query: str) -> str:
    top_chunks = vs.search(query)
    context = "\n".join(top_chunks)
    prompt = f"""You are an assistant that answers only based on the following context:\n\n{context}\n\nAnswer the question: {query}"""
    return generate_response(prompt)