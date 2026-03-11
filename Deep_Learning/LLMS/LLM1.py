from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

output = generator(
    "What is deep learning?",
    max_new_tokens=100,
    num_return_sequences=1
)

print(output[0]["generated_text"])