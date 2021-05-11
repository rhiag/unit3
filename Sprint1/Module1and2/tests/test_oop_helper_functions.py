"""Testing ooop_helper_functions.py"""
import pytest
from oop_examples import oop_helper_functions as oo
#from oop_helper_functions import HelperFunctions 


def test_nullcount():
    """Testing if a dataframe has a null counts"""
    helper = oo.HelperFunctions()
    assert helper.null_count(data = None) == 3