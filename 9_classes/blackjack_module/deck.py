from dataclasses import dataclass;
## Exercise 1: `deck.py` — Card functions

## Create a `deck.py` module with the following functions:

## - **`create_deck()`** — returns a list of 52 cards; each card is a dictionary with `"suit"` (e.g. `"Hearts"`) and `"rank"` (e.g. `"A"`, `"K"`, `"10"`, `"2"`)
## - **`print_card(card)`** — prints a card on one line, e.g. `A of Spades`
## - **`card_value(card)`** — returns the blackjack value of a single card (face cards = 10, Ace = 11, number cards = their number)
## - **`hand_value(cards)`** — takes a list of cards and returns the total value; Aces should be reduced from 11 to 1 when the total exceeds 21

## > **Hint:** Use a `while` loop to reduce Aces one at a time until the total is 21 or less.

SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
RANKS = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']

class Card(dict):
    suit: str
    rank: str

    def __init__(self, **kward):
        super().__init__(**kward)

    def __str__(self):
        return f"{self['rank']} of {self['suit']}"
        

def create_deck() -> list[Card]:
    return [ Card(suit=s, rank=r) for s in iter(SUITS) for r in iter(RANKS) ]

def print_card(card: Card) -> None:
    print(str(card))

def card_value(card: Card) -> int:
    if card["rank"].isnumeric():
        return int(card["rank"])
    elif card["rank"] == 'A':
        return 11
    else:
        return 10

def hand_value(cards: list[Card]) -> int:
    total = 0
    for card in cards:
        if total >= 21 and card["rank"] == 'A':
            total += 1
        else:
            total += card_value(card)
    return total