# app/llm.py
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch

tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-Instruct-v0.1", use_fast=True)
model = AutoModelForCausalLM.from_pretrained(
    "mistralai/Mistral-7B-Instruct-v0.1",
    device_map="auto",
    load_in_4bit=True,  # Uses bitsandbytes
    torch_dtype=torch.float16
)

generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

def generate_response(prompt: str) -> str:
    output = generator(prompt, max_new_tokens=300, do_sample=True)[0]["generated_text"]
    return output