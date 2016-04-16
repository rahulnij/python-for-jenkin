"""Testing modules."""


def func(x):
    """Add 1 to x."""
    return x + 3


def test_not_equal_to():
    """Test for 4 == 5."""
    assert func(3) != 5

def test_equal_to():
    """Test for 4 == 5."""
    assert func(3) == 5