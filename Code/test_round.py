"""Real-browser check of RPS-001: play a round, then play again."""

import pytest
from playwright.sync_api import Page, expect

import app as web

pytestmark = pytest.mark.e2e


def test_round_and_replay_in_real_browser(page: Page, live_server, monkeypatch):
    """Two clicks in Chromium each play an independent round with the real rules.

    Only the computer's random choice is fixed (always scissors).
    """
    monkeypatch.setattr(web.random, "choice", lambda _moves: "scissors")
    page.goto(live_server)
    expect(page.locator("[data-outcome]")).to_have_count(0)

    # Round 1: rock beats scissors.
    page.get_by_role("button", name="Rock", exact=True).click()
    expect(page.get_by_role("heading", name="You win!")).to_be_visible()
    expect(page.locator("[data-outcome]")).to_have_attribute("data-outcome", "win")
    expect(page.get_by_label("This round’s choices")).to_contain_text("Rock")
    expect(page.get_by_label("This round’s choices")).to_contain_text("Scissors")

    # Replay: a new round replaces the first; paper loses to scissors.
    page.get_by_role("button", name="Paper", exact=True).click()
    expect(page.get_by_role("heading", name="Computer wins")).to_be_visible()
    expect(page.locator("[data-outcome]")).to_have_attribute("data-outcome", "lose")
    expect(page.get_by_label("This round’s choices")).to_contain_text("Paper")
    expect(page.get_by_role("heading", name="You win!")).to_have_count(0)
