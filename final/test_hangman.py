import art


def test_display_hangman():
    stage = art.display_hangman(6)
    hangman = """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    assert stage == hangman


def test_display_hangman2():
    stage = art.display_hangman(5) 
    hangman = """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """
    assert stage == hangman


def test_display_hangman3():
    stage = art.display_hangman(4)
    hangman = """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """
    assert stage == hangman


def test_display_hangman4():
    stage = art.display_hangman(3) 
    hangman= """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """
    assert stage == hangman


def test_display_hangman5():
    stage = art.display_hangman(2) 
    hangman = """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """
    assert stage == hangman


def test_display_hangman6():
    stage = art.display_hangman(1) 
    hangman = """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """
    assert stage == hangman


def test_display_hangman7():
    stage = art.display_hangman(0)
    hangman = """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """
    assert stage == hangman
