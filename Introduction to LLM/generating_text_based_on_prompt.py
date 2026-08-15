"""This module is used for generating text based on prompt using Meta Llama"""

from transformers import pipeline

print("Loading the model...")
llama = pipeline("text-generation", model = "TinyLlama/TinyLlama-1.1B-Chat-v1.0")
prompt = [
    {"role": "system", "content": "You are a helpful and intelligent AI assistant."},
    {"role": "user", "content": "Whats Generative AI engineering?"}
]
output = llama(prompt, max_new_tokens = 100)

print("Output: \n", output[0]['generated_text'][-1]['content'])