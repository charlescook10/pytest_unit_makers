from lib.counter import Counter

def test_counter_starts_at_0():
    counter = Counter()

    result = counter.report()

    assert result == "Counted to 0 so far."

def test_counter_add_1_to_10_times():
    counter = Counter()

    for i in range(1,11):
        counter.add(i)
    
    result = counter.report()

    assert result == "Counted to 55 so far."

def test_counter_add_0():
    counter = Counter()

    counter.add(0)

    result = counter.report()

    assert result == "Counted to 0 so far."


def test_counter_add_a_negative():
    counter = Counter()

    counter.add(-5)

    result = counter.report()

    assert result == "Counted to -5 so far."