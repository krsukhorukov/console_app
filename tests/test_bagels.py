from bagels.bagels import Bagels

def test_HIDE_NUMBER_PLUS():
    test_game = Bagels(3)
    assert len(test_game.HIDE_NUMBER_PLUS(3)) == 3