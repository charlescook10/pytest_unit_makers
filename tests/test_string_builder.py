from lib.string_builder import StringBuilder

"""
Test initial string is empty
"""

def test_initial_state():
    string_builder = StringBuilder()

    result = string_builder.output()

    assert result == ""

def test_adds_single_string():
    string_builder = StringBuilder()

    string_builder.add("One")

    result = string_builder.output()

    assert result == "One"

def test_returns_correct_size_for_one_add():
    string_builder = StringBuilder()

    string_builder.add("One")

    result = string_builder.size()

    assert result == 3

def test_adds_two_strings():
    string_builder = StringBuilder()

    string_builder.add("One")

    string_builder.add("Two")

    result = string_builder.output()

    assert result == "OneTwo"

def test_returns_correct_size_for_two_adds():
    string_builder = StringBuilder()

    string_builder.add("One")

    string_builder.add("Two")

    result = string_builder.size()

    assert result == 6