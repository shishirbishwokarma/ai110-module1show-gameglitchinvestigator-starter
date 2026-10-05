from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result[0] == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result[0] == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result[0] == "Too Low"

# FIX: asked Claude for tests on the hint bug. it also noticed the old
# tests were broken (string vs tuple) so we fixed those too
def test_too_high_guess_hints_lower():
    # Bug fix: a guess above the secret must tell the player to go LOWER
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_too_low_guess_hints_higher():
    # Bug fix: a guess below the secret must tell the player to go HIGHER
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


# Edge cases (Challenge 1)
from logic_utils import parse_guess

def test_decimal_guess_rounds_down():
    assert parse_guess("3.7", 1, 100) == (True, 3, None)

def test_guess_with_spaces():
    assert parse_guess("  42 ", 1, 100) == (True, 42, None)

def test_empty_guess_rejected():
    ok, value, err = parse_guess("", 1, 100)
    assert not ok and value is None

def test_spaces_only_guess_rejected():
    ok, value, err = parse_guess("   ", 1, 100)
    assert not ok and value is None

def test_letters_rejected():
    ok, value, err = parse_guess("abc", 1, 100)
    assert not ok and value is None

def test_negative_guess_rejected():
    ok, value, err = parse_guess("-5", 1, 100)
    assert not ok and value is None

def test_guess_above_range_rejected():
    ok, value, err = parse_guess("99999", 1, 100)
    assert not ok and value is None

def test_guess_at_range_edges_accepted():
    assert parse_guess("1", 1, 100) == (True, 1, None)
    assert parse_guess("100", 1, 100) == (True, 100, None)

def test_one_digit_vs_two_digit_secret():
    # the old app turned the secret into a string, so "9" > "50" said Too High
    outcome, message = check_guess(9, 50)
    assert outcome == "Too Low"
