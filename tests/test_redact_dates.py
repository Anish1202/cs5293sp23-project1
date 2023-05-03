import pytest
import main 
def test_redact_dates():
    # Test with a string containing a date in the format "month day, year"
    text = "On Mon, 28 Aug 2000 06:40:00 -0700 (PDT), something happened."
    expected_output = "On █████████████████████████████████████, something happened."
    assert main.redact_dates(text) == expected_output
