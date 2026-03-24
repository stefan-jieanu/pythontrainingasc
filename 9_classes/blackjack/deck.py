"""Blackjack deck module — functions for creating and working with cards."""

SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]
FACE_CARDS = {11: "J", 12: "Q", 13: "K", 14: "A"}


def create_deck():
    """Return a list of 52 card dicts, each with 'suit' and 'rank' keys."""
    cards = []
    for suit in SUITS:
        for rank in range(2, 15):
            label = FACE_CARDS.get(rank, str(rank))
            cards.append({"suit": suit, "rank": label})
    return cards


def print_card(card):
    """Print a single card in a readable format."""
    print(f"  {card['rank']} of {card['suit']}")


def card_value(card):
    """Return the blackjack value of a card (face cards = 10, Ace = 11)."""
    if card["rank"] in ("J", "Q", "K"):
        return 10
    if card["rank"] == "A":
        return 11
    return int(card["rank"])


def hand_value(cards):
    """Return the total blackjack value of a hand, adjusting Aces as needed."""
    total = sum(card_value(card) for card in cards)
    aces = sum(1 for card in cards if card["rank"] == "A")

    while total > 21 and aces:
        total -= 10
        aces -= 1

    return total
