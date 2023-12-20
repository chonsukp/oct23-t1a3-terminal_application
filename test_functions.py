import pytest
from functions import convert_time_to_seconds

# Testing to see if pytest is working. 
def test_basic():
    assert "Hello, World!" == "Hello, World!"

# Testing conversion of time to seconds function, as it is used to calculate total time and average pace. 
def test_convert_time_to_seconds():
    assert convert_time_to_seconds("00:00:07") == 7
    assert convert_time_to_seconds("00:01:00") == 60
    assert convert_time_to_seconds("01:30:00") == 5400
    assert convert_time_to_seconds("02:45:15") == 9915

