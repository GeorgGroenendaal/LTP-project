import os
from datasets import load_dataset
import pandas as pd
from transformers import AutoModelForCausalLM, AutoTokenizer
from dotenv import load_dotenv

load_dotenv()


def get_few_shots():
    train = pd.read_csv("data/corpus_train.csv")
    few_shots = train.sample(20, random_state=42)
    few_shots.to_csv("data/cache/few_shots.csv")


def get_prompted_validation():
    try:
        few_shots = pd.read_csv("data/cache/few_shots.csv")
    except Exception:
        print("Could not find file, please run prepare first")
        exit(1)

    all_data = load_dataset(
        "csv",
        data_files={
            "train": ["data/corpus_train.csv"],
            "validation": ["data/corpus_valid.csv"],
            "test": ["data/corpus_test.csv"],
        },
    )

    def apply_prompt(inp):
        prompt = ""

        for _, row in few_shots.iterrows():
            prompt += f"{row['sentence']}####{row['label']}<|endoftext|>\n"

        prompt += f"{inp['sentence']}####"

        return {"prompt": prompt}

    return all_data["validation"].map(apply_prompt)


def load_gpt_j():
    cache_dir = os.getenv("CACHE_DIR", "NOT SET")
    model = AutoModelForCausalLM.from_pretrained(
        "EleutherAI/gpt-j-6B", cache_dir=cache_dir
    )
    tokenizer = AutoTokenizer.from_pretrained(
        "EleutherAI/gpt-j-6B", cache_dir=cache_dir
    )

    return model, tokenizer


def prompt(model, tokenizer, prompt):
    input_ids = tokenizer(prompt, return_tensors="pt").input_ids

    gen_tokens = model.generate(
        input_ids,
        do_sample=True,
        temperature=0.9,
        max_length=50,
    )

    return tokenizer.batch_decode(gen_tokens)[0]
