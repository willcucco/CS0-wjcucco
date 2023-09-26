from addingtrouble import answer

def test_answer():
    ans = answer(2, 3, 5)
    expected = "correct!"
    assert ans == expected


def test_answer2():
    ans = answer(1, 1, 3)
    expected = "wrong!"
    assert ans == expected

def test_answer3():
    ans = answer(4, 5, 9)
    expected = "correct!"
    assert ans == expected