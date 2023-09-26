from main import faktor

def test_faktor():
    ans = faktor(38, 24)
    expected = 875
    assert ans == expected


def test_faktor2():
    ans = faktor(1, 100)
    expected = 100
    assert ans == expected


def test_faktor3():
    ans = faktor(10, 10)
    expected = 91
    assert ans == expected