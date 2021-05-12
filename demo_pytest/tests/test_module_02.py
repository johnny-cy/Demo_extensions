"""
6. test expected exception
"""

import pytest


def test_exception():
    with pytest.raises(ValueError):
        month = -1
        if not (0 < month < 13):
            raise ValueError("this is value error exception.")
    
    with pytest.raises(TypeError):
        raise TypeError("this is type error exception.")
