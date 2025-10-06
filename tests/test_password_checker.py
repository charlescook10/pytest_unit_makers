import pytest
from lib.password_checker import PasswordChecker

def test_invalid_length_raises_error():
    checker = PasswordChecker()

    with pytest.raises(Exception) as error:
        checker.check("1234")
    
    error_message = str(error.value)

    assert error_message == "Invalid password, must be 8+ characters."

def test_returns_true_for_valid_length():
    checker = PasswordChecker()

    result = checker.check("password")

    assert result == True