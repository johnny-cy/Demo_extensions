"""
1. pytest can give method a test without any import, entrypoint or inheritance
2. method namespace default 'test*'
3. use python built-in assert
4. topdown executing
5. command `pytest` itself can do auto discover
 

CMD examples:
pytest -vv {test_module_01.py}                           # -vv, show details
pytest -vv {test_module_01.py} {test_module_02.py}       # execute multiple modules
pytest --durations=0  -vv                                # --durations, show methods which consume time are greater then 0 sec
"""
import pytest


def add(x,y):
    return x + y

def test2():
    assert 2 == add(1,1)

def test1():
    assert 3 == add(1,2)