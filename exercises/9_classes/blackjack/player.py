"""Blackjack player module."""

from deck import hand_value, print_card


class Player:
    def __init__(self, name, cash=0):
        self.name = name
        self.cash = cash
        self.hand = []
        self.bet = 0

    def show_hand(self):
        """Print all cards in the player's hand."""
        for card in self.hand:
            print_card(card)

    def place_bet(self, amount):
        """Set the current bet amount."""
        self.bet = amount

    def get_hand_value(self):
        """Return the total blackjack value of the player's hand."""
        return hand_value(self.hand)
