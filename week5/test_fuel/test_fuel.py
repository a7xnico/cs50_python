from fuel import convert, gauge
import pytest

def test_zero_div():
    with pytest.raises(ZeroDivisionError):
        convert("3/0")
    assert convert("1/1") == 100

def test_not_integers():
    with pytest.raises(ValueError):
        convert("H/i")
    with pytest.raises(ValueError):
        convert("1/h")

def test_y_less_than_x():
    with pytest.raises(ValueError):
        convert("4/2")
    with pytest.raises(ValueError):
        convert("3/2")

def test_not_division():
    with pytest.raises(ValueError):
        convert("3 4")
    with pytest.raises(ValueError):
        convert("3 + 4")

def test_percentage():
    assert gauge(100) == 'F'
    assert gauge(0) == 'E'
    assert gauge(50) == f"{50}%"
    assert gauge(1) == 'E'
    assert gauge(30) == f"{30}%"
    assert gauge(99) == 'F'

