import pytest
from tennis_scoring import game_score, set_winner, match_status


# ---------- game_score ----------
def test_negative_a():
    with pytest.raises(ValueError):
        game_score(-1, 0)

def test_negative_b():
    with pytest.raises(ValueError):
        game_score(0, -1)

def test_deuce():
    assert game_score(3, 3) == "deuce"

def test_deuce_higher():
    assert game_score(6, 6) == "deuce"

def test_game_a_after_deuce():
    assert game_score(5, 3) == "game A"

def test_game_b_after_deuce():
    assert game_score(3, 5) == "game B"

def test_advantage_a():
    assert game_score(4, 3) == "advantage A"

def test_advantage_b():
    assert game_score(3, 4) == "advantage B"

def test_game_a_straight():
    assert game_score(4, 0) == "game A"

def test_game_b_straight():
    assert game_score(2, 4) == "game B"

@pytest.mark.parametrize("a,b,expected", [
    (0, 0, "0-0"),
    (1, 0, "15-0"),
    (2, 1, "30-15"),
    (3, 2, "40-30"),
    (2, 3, "30-40"),
])
def test_regular_scores(a, b, expected):
    assert game_score(a, b) == expected


# ---------- set_winner ----------
def test_set_a_wins():
    assert set_winner(6, 3) == "A"

def test_set_a_wins_extended():
    assert set_winner(7, 5) == "A"

def test_set_b_wins():
    assert set_winner(2, 6) == "B"

def test_tiebreak_a():
    assert set_winner(7, 6) == "A"

def test_tiebreak_b():
    assert set_winner(6, 7) == "B"

@pytest.mark.parametrize("a,b", [(3, 2), (6, 5), (5, 6), (6, 6), (0, 0)])
def test_set_undecided(a, b):
    assert set_winner(a, b) is None


# ---------- match_status ----------
@pytest.mark.parametrize("sa,sb,bo,expected", [
    (2, 0, 3, "A wins"),
    (3, 2, 5, "A wins"),
    (0, 2, 3, "B wins"),
    (1, 3, 5, "B wins"),
    (1, 1, 3, "decider"),
    (2, 2, 5, "decider"),
    (0, 0, 3, "in progress"),
    (2, 1, 5, "in progress"),
    (1, 2, 5, "in progress"),
])
def test_match_status(sa, sb, bo, expected):
    assert match_status(sa, sb, bo) == expected
