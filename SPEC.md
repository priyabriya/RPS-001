# Rock, Paper, Scissors

## RPS-001: Play a round

**Purpose:** one person plays a quick round against the computer.

- Choose rock, paper, or scissors. The computer chooses one move for that round.
- Display both choices and the result: **You win!**, **Computer wins**, or **It’s a tie**.
- Choosing again starts an independent round. No score or saved history.
- Keep the supplied interface and server. Name/color changes can wait until the rules work.

### Expected results

Results are from the **player’s perspective**. `determine_winner(player, computer)` in `game.py` returns `win`, `lose`, or `tie`. Inputs are the lowercase moves below; the supplied server rejects other choices.

| Player | Computer | Expected return |
| --- | --- | --- |
| rock | rock | tie |
| rock | paper | lose |
| rock | scissors | win |
| paper | rock | win |
| paper | paper | tie |
| paper | scissors | lose |
| scissors | rock | lose |
| scissors | paper | win |
| scissors | scissors | tie |

### Agreed plan

**My prediction (fill in yourself):** I chose ______ and the computer chose ______; I expect ______ because ______.
<!-- Example of the *kind* of reasoning wanted: "Rock vs paper: paper covers rock, so the player loses." Use your own matchup and words. -->

**Scope:** `determine_winner(player, computer)` in `game.py` returns `win`, `lose`, or `tie` from the player's perspective. One independent round per click. No score, storage, accounts, new framework, or AI API. The supplied `app.py`, template, and server are kept.

**Valid losing round (positive case):** player rock, computer paper -> `lose`, page shows "Computer wins".

**Input the server should reject (negative case):** a missing `move`, or an unsupported move such as `lizard`, returns HTTP 400 with "Choose Rock, Paper, or Scissors to play." and never reaches the rule function (supplied tests in `tests/test_shell.py`).

### Checks

| Level | Cases and evidence |
| --- | --- |
| Unit - positive | All nine literal results above: [tests/test_game.py](tests/test_game.py) |
| Integration - positive | A posted round uses the real rules (only the computer's random choice is fixed): [tests/test_game.py](tests/test_game.py) |
| Integration - negative | Supplied missing/unsupported-move tests, reused: [tests/test_shell.py](tests/test_shell.py) |
| E2E - positive | Real Chromium round and replay: [tests/e2e/test_round.py](tests/e2e/test_round.py) |

### Work record

- Issue: ADD YOUR ISSUE URL
- Pull request: ADD YOUR MERGED PR URL
- CI run (Python checks on final PR commit): ADD YOUR ACTUAL CI RUN URL
- Implementation: [game.py](game.py)
- Full local check: ADD THE REAL RESULT of `.venv/bin/python check.py` (Black, Pylint, non-browser pytest, Chromium E2E - each PASS/FAIL, and the date you ran it).
- One test and the mistake it catches: ______ (e.g. name the test and the specific wrong rule it would expose; write this in your own words after you read it).
- One round I played: I chose ______, the computer chose ______, result ______, which makes sense because ______.
- Keyboard / replay observation: ______ (what happened when you used Tab and Enter, and when you played again).
- Help received: Used an AI assistant to draft `game.py`, the tests, and this SPEC template; I reviewed the diff and ran the checks myself.
