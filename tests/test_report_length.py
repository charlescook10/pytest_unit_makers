from lib.report_length import report_length

def test_on_empty_string():
    result = report_length("")

    assert result == "This string was 0 characters long."

def test_on_seven_char_string():
    result = report_length("Charles")

    assert result == "This string was 7 characters long."