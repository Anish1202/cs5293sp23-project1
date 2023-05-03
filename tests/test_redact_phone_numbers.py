import main
def test_redact_phone_numbers():
    # Test with a string containing a phone number in the format "###-###-####"
    text = "My phone number is 555-123-4567."
    expected_output = "My phone number is ████████████."
    assert main.redact_phone_numbers(text) == expected_output
