# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

It's a number guessing game made with Streamlit. You pick a difficulty, guess the secret number, and the game tells you to go higher or lower until you get it or run out of tries.

When I played it the hints were backwards, too high told me to go higher. The secret also turned into text on some tries, so "9" counted as bigger than "50". And Hard mode says 1-50 in the sidebar but the game still says 1-100.

I moved check_guess and parse_guess into logic_utils.py and flipped the hints. I took out the part that turned the secret into a string, so the game always compares real numbers now. parse_guess also checks the range, so stuff like -5 or 99999 gets rejected. Added tests for all of it, fixed the old tests, and added a pytest.ini so pytest could find logic_utils. Haven't fixed the Hard mode range thing yet.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Start on Normal, open the debug panel to see the secret (it was 50)
2. Guess 40, game says "Go HIGHER!", score goes to -5
3. Guess 70, game says "Go LOWER!", score goes to -10
4. Guess 50, game says "Correct!", balloons show up, final score is 40
5. Game's over after the win, it tells you to start a new game

**Screenshot:** none, walkthrough above

## 🗺️ Architecture

How the UI, game logic and tests connect (source in architecture.mmd):

![Architecture diagram](architecture.png)

## 🧪 Test Results

```
$ pytest -v
============================= test session starts ==============================
plugins: anyio-4.15.1
collecting ... collected 14 items

tests/test_game_logic.py::test_winning_guess PASSED                      [  7%]
tests/test_game_logic.py::test_guess_too_high PASSED                     [ 14%]
tests/test_game_logic.py::test_guess_too_low PASSED                      [ 21%]
tests/test_game_logic.py::test_too_high_guess_hints_lower PASSED         [ 28%]
tests/test_game_logic.py::test_too_low_guess_hints_higher PASSED         [ 35%]
tests/test_game_logic.py::test_decimal_guess_rounds_down PASSED          [ 42%]
tests/test_game_logic.py::test_guess_with_spaces PASSED                  [ 50%]
tests/test_game_logic.py::test_empty_guess_rejected PASSED               [ 57%]
tests/test_game_logic.py::test_spaces_only_guess_rejected PASSED         [ 64%]
tests/test_game_logic.py::test_letters_rejected PASSED                   [ 71%]
tests/test_game_logic.py::test_negative_guess_rejected PASSED            [ 78%]
tests/test_game_logic.py::test_guess_above_range_rejected PASSED         [ 85%]
tests/test_game_logic.py::test_guess_at_range_edges_accepted PASSED      [ 92%]
tests/test_game_logic.py::test_one_digit_vs_two_digit_secret PASSED      [100%]

============================== 14 passed in 0.01s ==============================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
