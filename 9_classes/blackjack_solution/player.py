# Exercise 2: player.py — Player class
# Using deck.py from the previous exercise, create a Player class with:

# Attributes:

# name — the name of the player
# cash — credits available (default 0)
# hand — the list of cards the player is holding (starts empty)
# bet — the current bet amount (starts at 0)

# Methods:

# show_hand() — prints all cards in the player's hand (use print_card from deck.py)
# place_bet(amount) — sets the current bet
# get_hand_value() — returns the total blackjack value of the hand (use hand_value from deck.py)

import deck

class Player():
    
    def __init__(self, name, cash=0):
        self.name = name
        self.cash = cash
        self.hand = []
        self.bet = 0

    def show_hand(self):
        for card in self.hand:
            deck.print_card(card)

    def place_bet(self, amount):
        self.bet = amount

    def get_hand_value(self):
        return deck.hand_value(self.hand)


player = Player("Test")
# player.show_hand()
# player.place_bet(20)
# print(player.get_hand_value())