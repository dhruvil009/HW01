# content of __init__.py
import pytest

def inc(x):
    return x + 1

def test_answer():
    assert inc(3) == 5
