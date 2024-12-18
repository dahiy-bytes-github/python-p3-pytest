#!/usr/bin/env python3

from not_none_functions import return_not_none

def test_return_not_none():
    '''Test that return_not_none does not return None.'''
    
    result = return_not_none()  # Call the function
    
    # Check if the result is not None
    assert result is not None, f"Expected a non-None value, but got {result}"