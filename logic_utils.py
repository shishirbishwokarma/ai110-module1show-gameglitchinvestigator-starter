"""Core game logic for the number guessing game.

These functions have no Streamlit dependencies, so they can be imported
and unit tested without running the app.
"""


def get_range_for_difficulty(difficulty: str) -> tuple[int, int]:
    """Return the inclusive range of possible secrets for a difficulty.

    Args:
        difficulty: One of "Easy", "Normal" or "Hard".

    Returns:
        A ``(low, high)`` tuple. Unknown difficulties fall back to the
        Normal range of 1 to 100.
    """
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


# FIX: moved this over for the edge case tests. it was letting -5 and 99999
# through, so now it checks the range too
def parse_guess(
    raw: str | None,
    low: int | None = None,
    high: int | None = None,
) -> tuple[bool, int | None, str | None]:
    """Parse the player's raw text input into an integer guess.

    Surrounding whitespace is ignored and decimal input is truncated
    toward zero (``"3.7"`` becomes ``3``). When both ``low`` and ``high``
    are given, guesses outside that inclusive range are rejected.

    Args:
        raw: The text from the guess input box. May be ``None``.
        low: Smallest allowed guess, or ``None`` to skip the range check.
        high: Largest allowed guess, or ``None`` to skip the range check.

    Returns:
        A ``(ok, value, error)`` tuple. On success it is
        ``(True, guess, None)``; on failure it is
        ``(False, None, message)`` with a message to show the player.
    """
    if raw is None:
        return False, None, "Enter a guess."

    raw = raw.strip()
    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    if low is not None and high is not None and not (low <= value <= high):
        return False, None, f"Guess must be between {low} and {high}."

    return True, value, None


# FIX: hints were backwards (too high said go higher lol). moved this
# over from app.py and had Claude flip the messages
def check_guess(guess: int, secret: int) -> tuple[str, str]:
    """Compare a guess with the secret number.

    Args:
        guess: The player's parsed guess.
        secret: The number the player is trying to find.

    Returns:
        An ``(outcome, message)`` tuple. ``outcome`` is ``"Win"``,
        ``"Too High"`` or ``"Too Low"``, and ``message`` is the hint
        shown to the player, pointing toward the secret.
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    try:
        if guess > secret:
            return "Too High", "📉 Go LOWER!"
        else:
            return "Too Low", "📈 Go HIGHER!"
    except TypeError:
        g = str(guess)
        if g == secret:
            return "Win", "🎉 Correct!"
        if g > secret:
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int) -> int:
    """Return the new score after a guess.

    A win is worth ``100 - 10 * (attempt_number + 1)`` points, with a
    minimum of 10. A "Too Low" guess costs 5 points. A "Too High" guess
    gains 5 points on even attempts and costs 5 on odd attempts. Any
    other outcome leaves the score unchanged.

    Args:
        current_score: The score before this guess.
        outcome: The outcome from :func:`check_guess`.
        attempt_number: The attempt counter after this guess.

    Returns:
        The updated score.
    """
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
