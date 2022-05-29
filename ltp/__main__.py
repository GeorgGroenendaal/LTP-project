import click
from ltp.prompt import get_few_shots, get_prompted_validation, load_gpt_j, prompt


def _clamp(value, minValue, maxValue):
    return max(min(maxValue, value), minValue)


@click.group()
def cli() -> None:
    pass


@cli.command()
def probe():
    print("Loading data")
    prompted_validation = get_prompted_validation()
    print("Loading model")
    model, tokenizer = load_gpt_j()

    while True:
        probe_id = _clamp(
            int(input("Enter prompt to probe ")), 0, len(prompted_validation) - 1
        )
        chosen_prompt = prompted_validation[probe_id]

        print(f"prompt: {chosen_prompt['sentence']}\nlabel: {chosen_prompt['label']}")
        generated_text = prompt(model, tokenizer, chosen_prompt["prompt"])
        print(generated_text)


@cli.command()
def prepare():
    print("preparing")
    get_few_shots()
    print("done")


@cli.command()
def download_gpt_j():
    print("Starting downloading gpt-j")
    load_gpt_j()


@cli.command()
@click.argument("name")
def run(name):

    print("Loading data")
    prompted_validation = get_prompted_validation()
    print("Loading model")
    model, tokenizer = load_gpt_j()

    for i, row in enumerate(prompted_validation):
        with open(f"{name}_{i}.txt", "w") as out:
            generated_text = prompt(model, tokenizer, row["prompt"])
            out.write(generated_text)


if __name__ == "__main__":
    cli()
