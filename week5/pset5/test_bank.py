from bank import value

def test_value():
    assert value('HELLO') == 0
    assert value('hello') == 0
    assert value('Hey') == 20
    assert value("What's that?") == 100