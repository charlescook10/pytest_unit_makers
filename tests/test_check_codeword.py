from lib.check_codeword import check_codeword

def test_with_correct_codeword():
    result = check_codeword("horse")

    assert result == "Correct! Come in."

def test_with_almost_correct_codeword():
    result = check_codeword("house")

    assert result == "Close, but nope."

def test_with_wrong_codeword():
    result = check_codeword("cow")

    assert result == "WRONG!"