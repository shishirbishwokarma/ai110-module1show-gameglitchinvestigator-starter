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
<!-- Paste the prompt you gave the AI -->
```

**Linting output before:**

```
<!-- Paste relevant linter warnings/errors -->
```

**Changes applied:**

<!-- Describe what you changed based on the AI's suggestions -->

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->

| | Model A | Model B |
|-|---------|---------|
| **Model name** | | |
| **Response summary** | | |
| **More Pythonic?** | | |
| **Clearer explanation?** | | |

**Which did you prefer and why?**

<!-- Your conclusion -->
