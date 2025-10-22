"""Command-line interface."""

import typer


app: typer.Typer = typer.Typer()


@app.command(name="btd6")
def main() -> None:
    """Btd6."""


if __name__ == "__main__":
    app()  # pragma: no cover
