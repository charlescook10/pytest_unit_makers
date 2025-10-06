from lib.greet import greet

def test_greet():
    result = greet("Charles")

    assert result == "Hello, Charles!"