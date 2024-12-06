from bank import value

def test_lowercase():
    assert value("hello") == 0
    assert value("hi") == 20
    assert value("good morning") == 100

def test_uppercase():
    assert value("HELLO") == 0
    assert value("HI") == 20
    assert value("GOOD MORNING") == 100

def test_punctuation():
    assert value(".hello") == 100
    assert value(",hello") == 100
    assert value(" hello") == 0
