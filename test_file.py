def add(a, b):
    return a + b

def test_add():
    assert add(6, 2) == 8
    assert add(2, 3) == 5
    assert add(3, 4) != 8