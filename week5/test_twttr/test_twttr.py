from twttr import shorten

def test_lowercase():
    assert shorten("twitter") == "twttr"
    assert shorten("hello") == "hll"

def test_uppercase():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("HELLO") == "HLL"

def test_number():
    assert shorten("123") == "123"
    assert shorten("-123") == "-123"

def test_punctuation():
    assert shorten("twitter.") == "twttr."
    assert shorten("snake_case") == "snk_cs"
