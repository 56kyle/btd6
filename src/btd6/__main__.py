"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """btd6."""


if __name__ == "__main__":
    main(prog_name="btd6")  # pragma: no cover
