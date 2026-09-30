# Scenario 18 — Blackjack vs Dealer

A terminal blackjack game with a deck, player/dealer hands, chips, and multiple rounds.

## Provided files

- `main.py` — entry point.
- `game.py` — round flow, decisions, and chip balance.
- `cards.py` — deck operations and hand scoring.
- `requirements.txt` — dependency declaration.

## Setup

```bash
python main.py
```

## Before changing the code

Inspect the hand-value function and manually reason through hands containing one and
multiple Aces. Reproduce incorrect totals before changing it.

## Task 1 — Correct Ace scoring

Implement blackjack hand scoring so an Ace is counted as 11 when that does not bust the
hand and as 1 when necessary.

**Done when:** hands such as A+9, A+9+5, and A+A+9 receive correct totals.

## Task 2 — Complete round resolution

Handle natural blackjack, player bust, dealer bust, dealer drawing rules, and pushes
consistently. Prevent actions after a round has already ended.

## Task 3 — Multi-round bankroll

Make chips persist across rounds and add a simple wager mechanism with validation.
A round must settle exactly once.

## Task 4 — Action feedback and robustness

Add concise feedback for actual card draws and round outcomes. Invalid commands and
invalid wagers must not change the bankroll.

## Required testing

Test one/multiple Aces, blackjack, busts, dealer draws, pushes, wagers, repeated
commands, invalid wagers, empty/depleted deck handling, and quitting.


## LLM usage

You may use an LLM during the lab. The goal is to use it as a coding assistant while
retaining responsibility for understanding and testing the result.

- Inspect the existing code before asking for changes.
- Ask for explanations when you do not understand a proposed change.
- Test generated code against the stated behaviour and edge cases.
- Keep your complete LLM chat history for submission.
- Do not replace the whole project with an unrelated implementation.
- Keep all state in memory; do not add CSV, JSON, SQLite, or other persistence.

## Submission checklist

- [ ] Task 1 completed and the original defect was reproduced and fixed.
- [ ] Tasks 2–4 completed and tested.
- [ ] Boundary and invalid-input cases tested.
- [ ] No unnecessary external dependencies added.
- [ ] No persistent storage added.
- [ ] Code remains understandable and modular.
- [ ] Complete LLM chat-history link included.

## Folder structure

```text
scenario-06-blackjack/
├── README.md
├── requirements.txt
├── main.py
├── game.py
└── cards.py
```

## Submission Checklist

Submission is only the following three things:

- [ ] A 10-second video of gameplay **before** your changes, showing the bug/broken behavior
- [ ] A 10-second video of gameplay **after** your changes, showing the bug fixed and the new features working
- [ ] The Chat/LLM used page link, with the complete chat history
