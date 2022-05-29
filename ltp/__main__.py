import click


@click.group()
def cli() -> None:
    pass


@cli.command()
@click.argument("index", default=0)
def probe(index: int):
    click.echo(f"Probing LTP {index}")


if __name__ == "__main__":
    cli()
