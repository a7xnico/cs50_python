from plates import is_valid

def test_platelength():
    assert is_valid("test34567") == False
    assert is_valid("h") == False
    assert is_valid("hola") == True

def test_first_two_letters():
    assert is_valid("50cs") == False
    assert is_valid("cs50") == True
    assert is_valid("c50") == False

def test_letter_after_number():
    assert is_valid("cs50") == True
    assert is_valid("cs50p") == False
    assert is_valid("nic10a") == False

def test_is_alphanumeric():
    assert is_valid("cs50") == True
    assert is_valid("cs%*") == False
    assert is_valid("hola,.") == False

def test_first_number_not_zero():
    assert is_valid("cs50") == True
    assert is_valid("cs05") == False
    assert is_valid("ni01as") == False

