"""RPS-001 checks: nine literal rule outcomes and one real request/result round."""

# pytest injects fixtures by their function names.
# pylint: disable=redefined-outer-name

import pytest

import app as web
from Code.game import determine_winner


@pytest.mark.unit
@pytest.mark.parametrize(
    ("player", "computer", "expected"),
    [
        ("rock", "rock", "tie"),
        ("rock", "paper", "lose"),
        ("rock", "scissors", "win"),
        ("paper", "rock", "win"),
        ("paper", "paper", "tie"),
        ("paper", "scissors", "lose"),
        ("scissors", "rock", "lose"),
        ("scissors", "paper", "win"),
        ("scissors", "scissors", "tie"),
    ],
)
def test_determine_winner_matches_spec(player, computer, expected):
    """Each player/computer pair returns the result listed in SPEC.md."""
    assert determine_winner(player, computer) == expected


@pytest.fixture
def client():
    """A Flask test client for the real application."""
    web.app.config.update(TESTING=True)
    return web.app.test_client()


@pytest.mark.integration
@pytest.mark.parametrize(
    ("moves", "outcome", "heading"),
    [
        (("rock", "paper"), "lose", "Computer wins"),
        (("paper", "rock"), "win", "You win!"),
        (("scissors", "scissors"), "tie", "It’s a tie"),
    ],
)
def test_submitted_round_uses_real_rules(client, monkeypatch, moves, outcome, heading):
    """A posted move runs the real rules and shows both choices and the result.

    Only the computer's random choice is fixed; determine_winner is not replaced.
    """
    player, computer = moves
    monkeypatch.setattr(web.random, "choice", lambda _moves: computer)
    response = client.post("/", data={"move": player})
    page = response.get_data(as_text=True)
    assert response.status_code == 200
    assert heading in page
    assert f'data-outcome="{outcome}"' in page
    assert f"{player.capitalize()} <span" in page
    assert f"{computer.capitalize()} <span" in page
    assert "game rules not built yet" not in page
