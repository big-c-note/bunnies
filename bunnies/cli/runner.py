import click

from bunnies.reproduce.runner import reproduce


@click.group()
def cli():
    """The CLI for the bunnies package that groups the various scripts.
    """
    pass


cli.add_command(reproduce, name="reproduce")
