import re
import main

def test_redact_genders():
    text = "She went to see her sister, but he was not there. He said he was going to meet his friend at the park."
    expected_output = "███ went to see███r ██████, but███ was not there. ██ said███ was going to meet ███ friend at the park."
    assert main.redact_genders(text) == expected_output
