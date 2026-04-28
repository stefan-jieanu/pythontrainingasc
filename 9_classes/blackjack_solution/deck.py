#Exercise 1: deck.py — Card functions
# Create a deck.py module with the following functions:
# create_deck() — returns a list of 52 cards; each card is a dictionary with "suit" (e.g. "Hearts") and "rank" (e.g. "A", "K", "10", "2")
# print_card(card) — prints a card on one line, e.g. A of Spades
# card_value(card) — returns the blackjack value of a single card (face cards = 10, Ace = 11, number cards = their number)
# hand_value(cards) — takes a list of cards and returns the total value; Aces should be reduced from 11 to 1 when the total exceeds 21
# Hint: Use a while loop to reduce Aces one at a time until the total is 21 or less.

def create_deck():
    card_rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    card_suit = ["hearts", "diamonds", "spades", "clubs"]

    deck = []
    for rank in card_rank:
        for suit in card_suit:
            deck.append({
                "rank": rank,
                "suit": suit
            })

    return deck

def print_card(card):
    print(f"{card['rank']} of {card['suit']}")

def card_value(card):
    max_card_value = ["J", "Q", "K"]
    if card["rank"] == "A":
        return 11
    elif card["rank"] in max_card_value:
        return 10
    else:
        return int(card["rank"])


def hand_value(cards):
    total = 0
    aces_found = 0
    for card in cards:
        if card["rank"] == "A":
            aces_found += 1
        
        total += card_value(card)

    if(total >= 21 and aces_found != 0):
        total = total - (aces_found * 10)

    return total


# print(create_deck())
# print(print_card({"rank": "7", "suit": "clubs"}))
# print(card_value({"rank": "K", "suit": "clubs"}))
# print(hand_value([{"rank": "A", "suit": "clubs"}, {"rank": "A", "suit": "clubs"}]))
