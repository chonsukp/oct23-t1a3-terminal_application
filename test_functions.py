import os
from unittest.mock import patch

import pytest

from functions import convert_time_to_seconds, log_run, view_log

runs_file = "test_runs.csv"

def test_basic():
    """Basic test to see if pytest is working."""

    assert "Hello, World!" == "Hello, World!"

def test_log_run(capsys):
    """Test Case 1: Testing the Log run function, using capsys fixture provided by pytest"""

    # Assign test CSV file.
    test_runs_file = "test_log_run.csv"

    # Simulate user inputs for Log run function.
    user_inputs = [
        "Test Run",
        "21/12/2023",
        "5.0",
        "00:30:00",
        "Test Notes"
    ]

    # Use patch function to mock the user inputs function with given information.
    with patch("builtins.input", side_effect = user_inputs):
        log_run(test_runs_file)

    # Capture the outputs for assertions.
    captured = capsys.readouterr()

    # Expected output.
    assert "Successfully logged run." in captured.out

    # Remove the test CSV file.
    os.remove("test_log_run.csv")
        
def test_convert_time_to_seconds():
    """Test Case 2.0: testing conversion of time to seconds function, as it is used to calculate total time and average pace."""
    # Expected conversion results.
    assert convert_time_to_seconds("00:00:07") == 7
    assert convert_time_to_seconds("00:01:00") == 60
    assert convert_time_to_seconds("01:30:00") == 5400
    assert convert_time_to_seconds("02:45:15") == 9915

def test_view_log(capsys):
    """Test Case 2.1: Testing the View log function, using capsys fixture provided by pytest."""

    # Creating a test CSV file.
    with open("test_view_log.csv", "w") as f:
        f.write("TITLE,DATE,DISTANCE,TIME TAKEN,NOTES\n")
        f.write("Test 1,2023-12-19,5,30:00,Test Notes\n")
        f.write("Test 2,2023-12-20,7,45:00,Test Notes\n")

    # Use patch function to mocking the test for conversion of time to seconds function.
    with patch("functions.convert_time_to_seconds", side_effect = lambda x: sum(int(t) *60**i for i, t in enumerate(reversed(x.split(":"))))):
        view_log("test_view_log.csv")

        # Capture the outputs for assertions.
        captured = capsys.readouterr()

        # Expected outputs. 
        assert "View runs" in captured.out
        assert "Stats" in captured.out
        assert "Total runs: 2" in captured.out
        assert "Total distance: 12.0 kilometers." in captured.out
        assert "Total time: 1 hours, 15 minutes, 0 seconds." in captured.out
        assert "Average pace: 6.25 minutes/kilometer" in captured.out

        # Remove the test CSV file.
        os.remove("test_view_log.csv")




