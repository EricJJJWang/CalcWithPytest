import pytest

def func(x):
    return x + 1

def add(x, y):
    return x + y


def test_answer():
    assert func(3) == 4

def test_answer1():
    assert func(3) == 4

def test_add():
    assert add(1,1) ==2

if __name__ == '__main__':
    pytest.main(['-s','test_01.py'])
    