import pytest


@pytest.mark.parametrize("levels", [1, 5, 10])
def test_make_bunnies(levels: int):
    """Make sure there are equal open and close parens."""
    from bunnies.reproduce.runner import make_bunnies

    bunny_reproduction: str = make_bunnies(levels)
    open_parens: int = 0
    close_parens: int = 0
    for char in bunny_reproduction:
        if char == "(":
            open_parens += 1
        if char == ")":
            close_parens += 1
    assert open_parens == close_parens
