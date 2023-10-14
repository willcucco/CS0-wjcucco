import avion


def test_find_FBI():
    assert avion.find_FBI("N-FBI") == 'positive'


def test_find_FBI2():
    assert avion.find_FBI("cheese") == 'negative'


def test_find_FBI3():
    assert avion.find_FBI("FBISURVEILLANCEVAN") == 'positive'


def test_find_FBI4():
    assert avion.find_FBI("powerranger") == 'negative'


def test_find_FBI5():
    assert avion.find_FBI("supercalifragilisticexpialidociousFBIman") == 'positive'