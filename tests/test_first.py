"""
Jenkin not working with current user and shell??????.

Testing modules.
"""


def func(x):
    """Add 1 to x."""
    return x + 3


def test_not_equal_to():
    """Test for 4 == 5."""
    assert func(2) != 5


def test_equal_to():
    """Test for 5 == 5."""
    assert func(2) == 5
