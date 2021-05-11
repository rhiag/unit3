"""Basic Unit testing for example.py"""
from random import randint
import pytest
from example import increment, COLORS

def test_increment():
    """testing positive integers for increment function"""
    test_value = randint(100,1000)

    assert increment(3) == 4
    assert increment(2.8) == 3.8
    assert increment(test_value) == test_value + 1

    for i in range(0,101):
        test_value = randint(100,1000)
        assert increment(test_value) == test_value + 1

def test_increment_neg():
    """testing negative ints for increment"""
    assert increment(-2) == -1


def test_increment_floats():
    """Testing positive floats for increment function"""

    assert increment(10.8) == 11.8
    assert increment(2.8) == 3.8

def test_increment_float_neg():
    pass

def test_colors():
    """testing colors contents"""
    assert len(COLORS) == 4

def test_color_contents():
    """testing color blue is there in COLORS"""
    assert "blue" in COLORS
    assert "mauve" not in COLORS


