import main
def test_redact_names():
    text = " Hello! John Doe, I'm Jane Smith. How are you doing today?"
    expected_output = " Hello! ████████, I'm ██████████. How are you doing today?"
    assert main.redact_names(text) == expected_output
