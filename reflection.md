# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

Looked like a normal guessing game, but the hints made no sense and kept sending me the wrong way. The debug panel shows the secret, so it was easy to tell something was off.

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

- Hints were backwards (too high said go higher)
- On some tries the secret turned into text, so "9" counted as bigger than "50"
- Hard mode says 1–50 in the sidebar but the game still says 1–100

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Secret 50, guess 60 | Go LOWER | Go HIGHER | none |
| Secret 50, guess 9 | Go HIGHER | Too High | none |
| Pick Hard | Says 1 to 50 | Says 1 to 100 | none |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

I used Claude Code inside VS Code. I marked bugs with FIXME comments and asked it to explain and fix them one at a time.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
I asked Claude to move `check_guess` from app.py into logic_utils.py, fix the high/low bug, and update the import. It found that the hint messages were swapped: a guess above the secret said "Go HIGHER!". It flipped them so too high says "Go LOWER!" and too low says "Go HIGHER!". That was correct because the hint should point toward the secret, not away from it. To check, I called `check_guess(60, 50)` and `check_guess(40, 50)` and confirmed the hints point the right way. Then I had Claude write two pytest tests that look for "LOWER" and "HIGHER" in the message, and all 5 tests passed.

- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

After the refactor, I told Claude I wanted a summary before it changed anything. It saved that as a permanent preference for every future session in this project. That went further than I wanted. I only meant for this chat, and I didn't want it changing how it behaves next time without me knowing. I told it "just summary here", and it deleted the saved preference and kept the summarize-first rule only for this conversation. To check, I watched it delete the saved file, and before every change after that it showed me a summary and waited for my OK, like it did with the pytest.ini fix and the tests.




---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

I tried guesses above and below the secret and checked the hints went the right way, then ran pytest.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

I added a test where the secret is 50 and the guess is 60, and it checks the hint says LOWER. It passes now and would've failed before. pytest also showed the old tests were broken (they expected a string, not a tuple), so we fixed those too. Later I added edge case tests (decimals, negatives, empty input, etc.) and all 14 pass now.

One thing that tripped me up: when I first ran `pytest` I got `ModuleNotFoundError: No module named 'logic_utils'` and none of the tests even ran. The code was fine, pytest just wasn't looking in the project folder. `python3 -m pytest` worked, and adding a pytest.ini with `pythonpath = .` fixed it for good.

- Did AI help you design or understand any tests? How?

Yeah, Claude wrote the hint tests and made them check the message, not just "Too High". It also explained why pytest couldn't find logic_utils, and a pytest.ini fixed it.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Every time you click a button or type something, Streamlit runs your whole script again from the top. So normal variables just reset every time. Session state is like a little backpack that survives the rerun, so stuff like the secret number, score and attempts go in there or they'd get wiped every click.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

Marking the bug with a FIXME first, then fixing one bug at a time and writing a test for it. Made it way easier to know when something was actually fixed.

- What is one thing you would do differently next time you work with AI on a coding task?

Actually run the game myself after each fix. I leaned on the tests a lot and didn't play it enough.

- In one or two sentences, describe how this project changed the way you think about AI generated code.

AI code can look fine and still be totally wrong, like hints that were just backwards. I have to check it myself, I can't just trust it.
