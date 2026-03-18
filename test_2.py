from example2 import reverse_string

def test_string():
    assert reverse_string("hello") == "olleh"

def test_empty():
    assert reverse_string("") == ""

def test_number():
    assert reverse_string("123") == "321"