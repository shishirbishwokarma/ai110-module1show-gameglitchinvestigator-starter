# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

<!-- Describe the goal you asked the agent to accomplish -->

**What did the agent do?**

<!-- List the steps the agent took (files edited, commands run, etc.) -->

**What did you have to verify or fix manually?**

<!-- Describe anything the agent got wrong or that required human review -->

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| Decimal like "3.7" | "write edge case tests for parse_guess and check_guess" | `parse_guess("3.7", 1, 100) == (True, 3, None)` | Yes | the old code already rounded down, good to lock it in |
| Spaces / empty input | same prompt | tests for `"  42 "`, `""` and `"   "` | Yes after fix | spaces only used to say "not a number" instead of "enter a guess", added strip() |
| Negative or huge guess | same prompt | `parse_guess("-5", 1, 100)` and `"99999"` should be rejected | Failed first, then yes | game was accepting guesses outside the range, added a range check |
| "9" vs secret 50 | same prompt | `check_guess(9, 50)` should be Too Low | Yes | this was the string secret bug, fixed it in app.py so the secret stays a number |

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
Add professional-grade docstrings to every function in logic_utils.py.
Then review my code for PEP 8 style compliance and apply the suggestions
to fix any formatting or naming issues.
```

**Linting output before:**

```
$ flake8 app.py logic_utils.py tests/
app.py:7:1: E302 expected 2 blank lines, found 1
app.py:72:80: E501 line too long (88 > 79 characters)
app.py:126:80: E501 line too long (83 > 79 characters)
logic_utils.py:3:80: E501 line too long (87 > 79 characters)
logic_utils.py:62:80: E501 line too long (87 > 79 characters)
tests/test_game_logic.py:3:1: E302 expected 2 blank lines, found 1
tests/test_game_logic.py:8:1: E302 expected 2 blank lines, found 1
tests/test_game_logic.py:13:1: E302 expected 2 blank lines, found 1
tests/test_game_logic.py:20:1: E302 expected 2 blank lines, found 1
tests/test_game_logic.py:26:1: E302 expected 2 blank lines, found 1
tests/test_game_logic.py:34:1: E402 module level import not at top of file
tests/test_game_logic.py:36:1: E302 expected 2 blank lines, found 1
tests/test_game_logic.py:39:1: E302 expected 2 blank lines, found 1
tests/test_game_logic.py:42:1: E302 expected 2 blank lines, found 1
tests/test_game_logic.py:46:1: E302 expected 2 blank lines, found 1
tests/test_game_logic.py:50:1: E302 expected 2 blank lines, found 1
tests/test_game_logic.py:54:1: E302 expected 2 blank lines, found 1
tests/test_game_logic.py:58:1: E302 expected 2 blank lines, found 1
tests/test_game_logic.py:62:1: E302 expected 2 blank lines, found 1
tests/test_game_logic.py:66:1: E302 expected 2 blank lines, found 1
(exit code 1)
```

After the fixes flake8 comes back clean (see lint_before.txt and lint_after.txt).

**Changes applied:**

Claude ran flake8 and almost everything was blank line stuff (E302, functions need 2 blank lines between them), mostly in the test file. Also a few lines over 79 chars, and one import in the middle of the test file (E402). I applied all of it:

- added the missing blank lines
- moved the `parse_guess` import up to the top of the test file
- split the long `if` in app.py into a `difficulty_changed` variable, and wrapped a long comment
- the two long lines in logic_utils.py were the leftover `NotImplementedError` stubs, so we moved the real `get_range_for_difficulty` and `update_score` over from app.py instead

It also suggested changing `low: int = None` to `low: int | None = None` since the type was wrong, I took that too. Then it added Google style docstrings (Args / Returns) to all 4 functions in logic_utils.py. No naming changes needed, everything was already snake_case. Ran pytest after and all 18 still pass.

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

I gave both the same prompt in a fresh chat: the original starter `check_guess` and "When the guess is higher than the secret, the player is told 'Go HIGHER!', which is backwards. Fix the bug and explain why it happened."

| | Model A | Model B |
|-|---------|---------|
| **Model name** | Claude (Opus 5.5, in Claude Code) | ChatGPT |
| **Response summary** | Swapped the two messages and also deleted the whole `try/except TypeError` part, so the function is just 3 `if`s with type hints | Swapped the messages in both places (normal branch and the `except TypeError` branch) and left everything else the same |
| **More Pythonic?** | Yes. Shorter, no try/except hiding problems, type hints. But it changed more than I asked for | Less Pythonic since it keeps the weird string fallback, but it's the smallest and safest fix |
| **Clearer explanation?** | Explained the hint bug and also why the string fallback is bad ("9" > "50"), which is actually my other bug | Clearer for this bug. It walks through guess > secret step by step with the code right there, easy to follow |

**Which did you prefer and why?**

ChatGPT explained the actual bug better, it was simple and showed the exact line. Claude's code is cleaner and it noticed the string comparison problem, which ChatGPT kept without saying anything. But deleting the fallback only works if the secret is always an int, and in the starter app it wasn't, so Claude's version alone would've crashed on every other guess until I fixed app.py too. So I liked ChatGPT's explanation more and Claude's code more. In my actual project I did the safe swap like ChatGPT and fixed app.py so the secret always stays an int, so the fallback never runs anymore.
