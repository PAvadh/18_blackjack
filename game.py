from cards import Deck, hand_value


class Blackjack:
    def __init__(self):
        self.chips = 100
        self._round_settled = False

    def show(self, player, dealer, hide=True):
        shown_dealer = ["??"] if hide else [f"{r}{s}" for r, s in dealer]
        print("Dealer:", " ".join(shown_dealer))
        print("Player:", " ".join(f"{r}{s}" for r, s in player),
              "=", hand_value(player))

    def _draw(self, deck, hand, owner="Player"):
        """Draw one card and give clear feedback about who drew it."""
        card = deck.draw()
        if card is None:
            print("No cards left in the deck.")
            return False
        hand.append(card)
        print(f"{owner} draws: {card[0]}{card[1]} (total: {hand_value(hand)})")
        return True

    def _wager(self):
        while True:
            raw = input(f"Wager (1-{self.chips}, or q to quit): ").strip()
            if raw.lower() == "q":
                return None

            try:
                wager = int(raw)
            except (TypeError, ValueError):
                print("Invalid wager. Enter a whole number greater than 0.")
                continue

            if wager <= 0:
                print("Invalid wager. Wager must be greater than 0.")
                continue

            if wager > self.chips:
                print(f"Invalid wager. You only have {self.chips} chips.")
                continue

            return wager

    def _settle(self, result, wager):
        """Settle a round at most once."""
        if self._round_settled:
            return False

        self._round_settled = True

        if result == "win":
            self.chips += wager
            print(f"You win! +{wager} chips. Bankroll: {self.chips}")
        elif result == "lose":
            self.chips -= wager
            print(f"You lose. -{wager} chips. Bankroll: {self.chips}")
        else:
            print(f"Push — tie. Your wager is returned. Bankroll: {self.chips}")
        return True

    def round(self):
        if self.chips <= 0:
            print("You have no chips left. Game over.")
            return False

        wager = self._wager()
        if wager is None:
            print("Leaving the game.")
            return False

        self._round_settled = False
        deck = Deck()
        player = []
        dealer = []

        # Deal the initial two cards to each side.
        for _ in range(2):
            if not self._draw(deck, player, "Player") or not self._draw(deck, dealer, "Dealer"):
                print("Round canceled because the deck is depleted. No wager was settled.")
                return False

        self.show(player, dealer)

        player_value = hand_value(player)
        dealer_value = hand_value(dealer)

        # Resolve natural blackjacks before asking for any action.
        player_blackjack = player_value == 21
        dealer_blackjack = dealer_value == 21

        if player_blackjack or dealer_blackjack:
            self.show(player, dealer, hide=False)
            if player_blackjack and dealer_blackjack:
                print("Both have blackjack.")
                self._settle("push", wager)
            elif player_blackjack:
                print("Blackjack! You win.")
                self._settle("win", wager)
            else:
                print("Dealer has blackjack.")
                self._settle("lose", wager)
            return True

        # Player turn.
        while hand_value(player) < 21:
            key = input("[h]it [s]tand [q]uit: ").strip().lower()

            if key == "q":
                print("Round abandoned. Your wager is not settled.")
                return False

            if key == "s":
                print(f"You stand at {hand_value(player)}.")
                break

            if key == "h":
                if not self._draw(deck, player, "Player"):
                    return False
                self.show(player, dealer)

                player_value = hand_value(player)
                if player_value > 21:
                    print(f"Player busts with {player_value}.")
                    self._settle("lose", wager)
                    return True

                if player_value == 21:
                    print("Player has 21. Dealer's turn.")
                    break
                continue

            print("Invalid command. Use h, s, or q.")

        # Dealer turn. Dealer stands on 17 or higher.
        print("Dealer's turn...")
        while hand_value(dealer) < 17:
            if not self._draw(deck, dealer, "Dealer"):
                print("Round canceled because the deck is depleted. No wager was settled.")
                return False

        dealer_value = hand_value(dealer)
        player_value = hand_value(player)
        self.show(player, dealer, hide=False)

        if dealer_value > 21:
            print(f"Dealer busts with {dealer_value}.")
            self._settle("win", wager)
        elif player_value > dealer_value:
            print(f"Your {player_value} beats the dealer's {dealer_value}.")
            self._settle("win", wager)
        elif player_value < dealer_value:
            print(f"Dealer's {dealer_value} beats your {player_value}.")
            self._settle("lose", wager)
        else:
            print(f"Both have {player_value} — push.")
            self._settle("push", wager)

        return True

    def run(self):
        print("Blackjack — starting chips:", self.chips)
        while self.chips > 0:
            if not self.round():
                return

            if self.chips <= 0:
                print("Bankroll reached 0. Game over.")
                return

            if input("Play again? [y/n]: ").strip().lower() != "y":
                print(f"Thanks for playing! Final bankroll: {self.chips}")
                return
