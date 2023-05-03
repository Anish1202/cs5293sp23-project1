import main
import pytest
def test_redact_address():
    text = "1165 East Brooks St, Norman 73071"
    expected_output = "1165 East Brooks St, Norman █████"
    assert main.redact_address(text) == expected_output

    text = "1000 Broadway Ave, Suite 200, New York NY 10001-1234"
    expected_output = "1000 Broadway Ave, Suite 200, New York NY ██████████"
    assert main.redact_address(text) == expected_output

    text = "No addresses here!"
    expected_output = "No addresses here!"
    assert main.redact_address(text) == expected_output
