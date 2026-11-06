from app.streak import calculate_streak


def test_streak_empty():
    assert calculate_streak([]) == 0


def test_streak_one():
    assert calculate_streak([True]) == 1


def test_streak_broken():
    assert calculate_streak([True, False, True]) == 1


def test_streak_is_capped_at_365():
    long_streak = [True] * 400
    assert calculate_streak(long_streak) == 365