import anewalphabet


def test_newdict():
    assert anewalphabet.newdict('hello') == '[-]3110'


def test_newdict2():
    assert anewalphabet.newdict('lose') == '10$3'


def test_newdict3():
    assert anewalphabet.newdict('hi') == '[-]|'


def test_newdict4():
    assert anewalphabet.newdict('beg') == '836'


def test_newdict5():
    assert anewalphabet.newdict('ask') == '@$|<'