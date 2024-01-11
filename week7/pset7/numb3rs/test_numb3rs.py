from numb3rs import validate


def test_validate():
    assert validate('127.0.0.1') == True
    assert validate('10.0.0.10') == True
    assert validate('255.255.255.255') == True
    assert validate('1.1.0.1') == True
    assert validate('192.168.1.1') == True

    assert validate('255.256.256.256') == False
    assert validate('512.512.512.512') == False
    assert validate('1.2.3.1000') == False
    assert validate('1.2.3.1000.1000') == False
    assert validate('1.2.3') == False
    assert validate('cat') == False