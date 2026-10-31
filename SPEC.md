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

**My prediction:** I chose Rock and the computer chose Paper; I expect "lose" because paper beats rock. and that is how it is programmed

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

- Pull request: https://github.com/priyabriya/rps-001/pull/2
- CI run: https://github.com/priyabriya/rps-001/actions/runs/
- Implementation: [game.py](game.py)
- Full local check: Verified in a sandbox: Black PASS, Pylint PASS, non-browser pytest PASS (25 passed).
- One test and the mistake it catches: `test_determine_winner_matches_spec[rock-paper-lose]` asserts that player rock vs computer paper returns "lose". It would catch a rule that gets the direction backwards, such as returning "win" for the weaker move. I confirmed this by swapping the win condition on purpose, and 8 tests failed..
- One round I played: I chose Rock, the computer chose Paper, the result was "Computer wins", which makes sense because paper covers rock.
- Keyboard / replay observation: Tab moves focus across the Rock, Paper, and Scissors buttons, and Enter or Space plays that move. Clicking again starts a new round that replaces the previous result, with no score kept.
- Help received: Used an AI assistant to draft `game.py`, the tests, and this SPEC template; I reviewed the diff and ran the checks myself.
