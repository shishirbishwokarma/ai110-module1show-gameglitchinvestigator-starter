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

I moved check_guess and parse_guess into logic_utils.py and flipped the hints. I took out the part that turned the secret into a string, so the game always compares real numbers now. parse_guess also checks the range, so stuff like -5 or 99999 gets rejected. Added tests for all of it, fixed the old tests, and added a pytest.ini so pytest could find logic_utils. For Hard mode, New Game and switching difficulty now pick the secret from the right range, and the prompt shows the real range. Before, Hard could give you a secret of 80 and you'd never win. Added tests that run the actual app to check that. Before vs after output is in bug_repro.txt.

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
collecting ... collected 18 items

tests/test_app.py::test_prompt_shows_range_for_difficulty PASSED         [  5%]
tests/test_app.py::test_new_game_secret_stays_in_range PASSED            [ 11%]
tests/test_app.py::test_switching_difficulty_picks_new_secret_in_range PASSED [ 16%]
tests/test_app.py::test_new_game_after_win_lets_you_play_again PASSED    [ 22%]
tests/test_game_logic.py::test_winning_guess PASSED                      [ 27%]
tests/test_game_logic.py::test_guess_too_high PASSED                     [ 33%]
tests/test_game_logic.py::test_guess_too_low PASSED                      [ 38%]
tests/test_game_logic.py::test_too_high_guess_hints_lower PASSED         [ 44%]
tests/test_game_logic.py::test_too_low_guess_hints_higher PASSED         [ 50%]
tests/test_game_logic.py::test_decimal_guess_rounds_down PASSED          [ 55%]
tests/test_game_logic.py::test_guess_with_spaces PASSED                  [ 61%]
tests/test_game_logic.py::test_empty_guess_rejected PASSED               [ 66%]
tests/test_game_logic.py::test_spaces_only_guess_rejected PASSED         [ 72%]
tests/test_game_logic.py::test_letters_rejected PASSED                   [ 77%]
tests/test_game_logic.py::test_negative_guess_rejected PASSED            [ 83%]
tests/test_game_logic.py::test_guess_above_range_rejected PASSED         [ 88%]
tests/test_game_logic.py::test_guess_at_range_edges_accepted PASSED      [ 94%]
tests/test_game_logic.py::test_one_digit_vs_two_digit_secret PASSED      [100%]

============================== 18 passed in 0.97s ==============================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
