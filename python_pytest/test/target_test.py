import pytest

def is_stronger(card, last):
    if last == "":
        return True
    return card[1] > last[1]

class DaifugoError(Exception):
    pass

class Player:
    def __init__(self, game):
        self._game = game

    def trick(self, card):
        last_trick = self._game.get_last_trick()
        if not is_stronger(card, last_trick):
            raise DaifugoError()
        self._game._last_trick = card

class Game:
    def __init__(self):
        self._player = Player(self)
        self._last_trick = ""

    def get_current_player(self):
        return self._player

    def get_last_trick(self):
        return self._last_trick

@pytest.fixture
def game():
    return Game()

@pytest.fixture
def player(game):
    return game.get_current_player()

def test_親がハート3を出しプレイヤー2がクラブ5を出しプレイヤー3はパスプレイヤー4がスペードAを出して親になる():
    pass

def test_親がハート3を出す(game, player):
    player.trick("H3")
    assert "H3" == game.get_last_trick()

def test_プレイヤー2がクラブ5を出す(game, player):
    player.trick("H3")
    player2 = game.get_current_player()
    player2.trick("C5")
    assert "C5" == game.get_last_trick()

@pytest.mark.parametrize("trick1,trick2", [
    ["H6", "C5"],
    ["H6", "C6"],
], ids=["weak", "same"])
def test_不正な手は出せない(game, player, trick1, trick2):
    player.trick(trick1)
    player2 = game.get_current_player()
    with pytest.raises(DaifugoError):
        player2.trick(trick2)

@pytest.mark.skip
def test_2は3より強い(game, player):
    player.trick("H2")
    player2 = game.get_current_player()
    with pytest.raises(Exception):
        player2.trick("C3")





