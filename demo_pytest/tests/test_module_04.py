"""
8. group test

CMD Example:
pytest -vv -m g1
pytest -vv -m g2
"""

import pytest 

@pytest.mark.g1
def test_a():
    assert 1 == 1

@pytest.mark.g1
def test_b():
    assert 2 == 2

@pytest.mark.g2
def test_c():
    assert 3 == 3