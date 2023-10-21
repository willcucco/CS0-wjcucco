import fallingapart


def test_answer():
    assert fallingapart.answer([3, 1, 2]) == (4, 2)


def test_answer2():
    assert fallingapart.answer([1, 2, 2, 1]) == (3, 3)


def test_answer3():
    assert fallingapart.answer([5, 6, 7]) == (12, 6)


def test_answer4():
    assert fallingapart.answer([1, 2, 3, 4]) == (6, 4)


def test_answer5():
    assert fallingapart.answer([3, 4, 5]) == (8, 4)