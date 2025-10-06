import pytest
from lib.present import Present

def test_unwraps_a_present():
    present = Present()

    present.wrap("Toy")

    result = present.unwrap()

    assert result == "Toy"

def test_raises_error_when_unwrapping_empty_present():
    present = Present()

    with pytest.raises(Exception) as error:
        present.unwrap()
    
    error_message = str(error.value)

    assert error_message == "No contents have been wrapped."

def test_raises_error_when_wrapping_twice():
    present = Present()

    present.wrap("Car")

    with pytest.raises(Exception) as error:
        present.wrap("Toy")
    
    error_message = str(error.value)

    assert error_message == "A contents has already been wrapped."