import pytest

from my_package import add, subtract, multiply, divide

from src.my_package import my_module


def test_add():
    assert my_module.add(1, 2) == 3
    assert my_module.add(3, 4) == 7

def test_subtract():
    assert my_module.subtract(1, 2) == -1
    assert my_module.subtract(3, 4) == -1

def test_multiply():
    assert my_module.multiply(1, 2) == 2
    assert my_module.multiply(3, 4) == 12

def test_divide():
    assert my_module.divide(1, 2) == 0.5
    assert my_module.divide(3, 4) == 0.75
