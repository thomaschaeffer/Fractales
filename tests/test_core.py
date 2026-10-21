from fractales.core import escape_iterations

def test_zero_does_not_escape():
    assert escape_iterations( 0 + 0j, 50)==50

def test_two_escapes_quickly():
    assert escape_iterations( 2 + 0j, 50)<50

def test_two_escapes_quickly():
    result = escape_iterations( 1 + 0j, 25)
    assert 0 <= result <= 25