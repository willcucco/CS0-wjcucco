import lastfactorialdigit


def test_find_num():
    """Test find_num function"""
    assert lastfactorialdigit.find_num(5) == 120



def test_find_num2():
    assert lastfactorialdigit.find_num(2) == 2



def test_find_num3():
    assert lastfactorialdigit.find_num(1) == 1



def test_find_num4():
    assert lastfactorialdigit.find_num(0) == 1



def test_find_num5():
    assert lastfactorialdigit.find_num(3) == 6