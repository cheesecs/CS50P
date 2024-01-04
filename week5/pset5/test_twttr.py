from twttr import shorten


def test_shorten():
    assert shorten('AEIOU') == ''
    assert shorten('aeiou') == ''
    assert shorten('twitter') == 'twttr'
    assert shorten('ilovecs50') == 'lvcs50'
    assert shorten('.') == '.'