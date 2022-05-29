from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained(
    "EleutherAI/gpt-j-6B", cache_dir="/scratch/s4199960/cache"
)

prompt = "####"


input_ids = tokenizer(prompt, return_tensors="pt").input_ids

print(input_ids)
