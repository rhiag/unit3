"""Testing ooop_helper_functions.py"""
import pytest
from src.helper_functions import HelperFunctions, IncorrectData

   

def test_nullcount_case1():
    """Testing if a dataframe has a null counts"""
    helper = HelperFunctions()
    with pytest.raises(IncorrectData):
        assert helper.null_count(data = None) == 3


def test_nullcount_case2():
    """Testing if a dataframe has a null counts with 3 null values"""
    helper = HelperFunctions()
    input_data = ([None, 72, 67],
	              [23, 78, 62],
	              [32, 74, None],
	              [None, 54, 76])
    actual_result =  helper.null_count(input_data )             
    assert actual_result == 3    