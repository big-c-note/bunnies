from typing import List, IO, Any
import logging

import click

log = logging.getLogger(__name__)


# Bunny
bunny: str = """(\\_/)\n(•_•)\n/ > 🎷🐇 """

# Indent
indent: str = ". . "


def fib(n: int):
    """Recursive function for fibonacci sequence."""
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


def make_bunnies(levels: int) -> str:
    """Create bunny reproduction according to the fibonacci sequence.

    Parameters
    levels : int
        Number of levels to reproduction.
    save_path : str
        Save path as a string.

    Returns
    -------
    bunny_reproduction : str
    """
    bunny_reproduction: str = ""
    bunny_holders: List[str] = []
    for i in range(1, levels):
        num_bunnies: int = fib(i)
        bunny_parts: List[str] = bunny.split("\n")
        indents: str = indent * (i - 1)
        indented_bunny_parts: List[str] = [indents + part for part in bunny_parts]
        indented_bunny: str = "\n".join(indented_bunny_parts) + "\n"
        bunnies: str = (indented_bunny * num_bunnies)[:-2] + " (\n"
        bunny_reproduction += bunnies
        bunny_holder: str = indents + ")\n"
        bunny_holders.append(bunny_holder)
    for i in range(1, levels):
        bunny_holder = bunny_holders.pop()
        bunny_reproduction += bunny_holder
    return bunny_reproduction


def dump_bunnies(bunny_reproduction: str, save_path: str) -> None:
    """Dump bunnies to a text file.

    Parameters
    ----------
    bunny_reproduction : str
        Bunny reproduction string.
    save_path : str
        Path to text file.
    """
    bunny_dump: IO[Any] = open(save_path, "w")
    bunny_dump.write(bunny_reproduction)
    bunny_dump.close()


@click.command()
@click.option("--levels", default=25, help="Number of levels to reproduction.")
@click.option("--save_path", default="./bunnies.txt", help="Save path.")
def reproduce(levels: int, save_path: str) -> None:
    """Create bunny reproduction according to the fibonacci sequence.

    Parameters
    levels : int
        Number of levels to reproduction.
    save_path : str
        Save path as a string.
    """
    log.info("Bunnies are reproducing.")
    bunny_reproduction: str = make_bunnies(levels)
    dump_bunnies(bunny_reproduction, save_path)


if __name__ == "__main__":
    reproduce()
