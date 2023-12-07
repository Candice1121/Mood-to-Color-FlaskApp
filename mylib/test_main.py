from main import addfunction

def test_add():
    """Function calling addfunction"""

    a = 0
    b = 1
    c = 2
    assert addfunction(a,b) == 1
    assert addfunction(a,c) == 2
    assert addfunction(b,c) == 3