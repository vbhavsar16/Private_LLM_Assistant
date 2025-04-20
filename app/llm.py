from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from app.config import LLM_MODEL_NAME

cache_dir = "./cache"

tokenizer = AutoTokenizer.from_pretrained(LLM_MODEL_NAME, cache_dir=cache_dir)
model = AutoModelForCausalLM.from_pretrained(LLM_MODEL_NAME, cache_dir=cache_dir, torch_dtype="auto")

generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

def generate_response(prompt: str) -> str:
    output = generator(prompt, max_new_tokens=300, do_sample=True)[0]["generated_text"]
    return output
