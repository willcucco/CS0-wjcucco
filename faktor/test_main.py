from main import faktor

def test_faktor():

    ans = faktor(38, 24)
    expected = 875
    assert ans == expected
