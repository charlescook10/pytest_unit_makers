from lib.gratitudes import Gratitudes

def test_no_gratitudes():
    gratitudes = Gratitudes()

    result = gratitudes.format()

    assert result == "Be grateful for: "

def test_add_one_gratitudes():
    gratitudes = Gratitudes()

    gratitudes.add("Food")

    result = gratitudes.format()

    assert result == "Be grateful for: Food"

def test_add_two_gratitudes():
    gratitudes = Gratitudes()

    gratitudes.add("Food")

    gratitudes.add("Water")

    result = gratitudes.format()

    assert result == "Be grateful for: Food, Water"