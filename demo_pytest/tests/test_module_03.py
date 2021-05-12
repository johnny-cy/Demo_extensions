def add(x,y):
    return x+y


"""
7. use a set of test args at once.
"""

import pytest


@pytest.mark.parametrize(
    "x, y, expect_value",
    [
        (1, 1, 2),
        (0, 0, 0),
    ]
)
def test_add(x, y, expect_value):
    assert expect_value == add(x,y)



