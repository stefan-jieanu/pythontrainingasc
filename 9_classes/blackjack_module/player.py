from dataclasses import dataclass
from .deck import Card, print_card, hand_value

## Exercise 2: `player.py` — Player class

## Using `deck.py` from the previous exercise, create a `Player` class with:

## **Attributes:**
## - `name` — the name of the player
## - `cash` — credits available (default 0)
## - `hand` — the list of cards the player is holding (starts empty)
## - `bet` — the current bet amount (starts at 0)

## **Methods:**
## - `show_hand()` — prints all cards in the player's hand (use `print_card` from `deck.py`)
## - `place_bet(amount)` — sets the current bet
## - `get_hand_value()` — returns the total blackjack value of the hand (use `hand_value` from `deck.py`)


@dataclass
class Player:
    name: str
    cash: float
    hand: list[Card]
    bet: float = 0

    def show_hand(self):
        for card in self.hand:
            print_card(card)
    
    def place_bet(self, amount: float):
        self.bet = amount
        self.cash -= amount

    def get_hand_value(self):
        return hand_value(self.hand)