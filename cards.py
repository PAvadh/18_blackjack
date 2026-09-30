import random

RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
SUITS = ["C", "D", "H", "S"]


class Deck:
    def __init__(self):
        self.cards = [(rank, suit) for suit in SUITS for rank in RANKS]
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop() if self.cards else None


def hand_value(hand):
    """Return the best blackjack value for a hand, treating Aces as 1 or 11."""
    value = 0
    aces = 0

    for rank, _ in hand:
        if rank == "A":
            value += 11
            aces += 1
        elif rank in {"J", "Q", "K"}:
            value += 10
        else:
            value += int(rank)

    # Each Ace can be reduced from 11 to 1 by subtracting 10.
    while value > 21 and aces:
        value -= 10
        aces -= 1

    return value
