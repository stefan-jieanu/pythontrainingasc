"""Blackjack game — uses deck and player modules."""

import random

from deck import create_deck
from player import Player

DEALER_STAND = 18


def get_bet(player):
    """Ask the player for a valid bet amount."""
    while True:
        try:
            amount = int(input(f"How much do you want to bet? (available: {player.cash}) "))
            if 0 < amount <= player.cash:
                return amount
            print(f"Please enter an amount between 1 and {player.cash}.")
        except ValueError:
            print("Please enter a valid number.")


def player_turn(player, deck):
    """Let the human player draw cards or stand."""
    while True:
        print(f"\n{player.name}'s hand ({player.get_hand_value()}):")
        player.show_hand()

        choice = input("Draw another card? (y/n): ").strip().lower()
        if choice != "y":
            print(f"\n{player.name} stands with {player.get_hand_value()}.")
            return

        player.hand.append(deck.pop())
        if player.get_hand_value() > 21:
            print(f"\n{player.name} busted with {player.get_hand_value()}!")
            player.show_hand()
            return


def dealer_turn(dealer, deck):
    """Dealer draws until reaching the stand threshold."""
    while dealer.get_hand_value() < DEALER_STAND:
        print(f"\n{dealer.name} draws...")
        dealer.hand.append(deck.pop())

    print(f"\n{dealer.name}'s final hand ({dealer.get_hand_value()}):")
    dealer.show_hand()

    if dealer.get_hand_value() > 21:
        print(f"{dealer.name} busted!")


def determine_winner(player, dealer):
    """Compare hands, update cash, and print results."""
    p_val = player.get_hand_value()
    d_val = dealer.get_hand_value()

    print("\n--- Final Results ---")

    if (p_val > 21 and d_val > 21) or p_val == d_val:
        print("It's a draw!")

    elif d_val > 21 or p_val > d_val:
        print(f"{player.name} wins with {p_val}!")
        player.cash += player.bet
        dealer.cash -= dealer.bet

    else:
        print(f"{dealer.name} wins with {d_val}!")
        player.cash -= player.bet
        dealer.cash += dealer.bet

    player.bet = 0
    dealer.bet = 0

    print(f"  {player.name} — cash: {player.cash}")
    print(f"  {dealer.name} — cash: {dealer.cash}")


def main():
    deck = create_deck()
    random.shuffle(deck)

    player = Player("You", 500)
    dealer = Player("Computer", 500)

    bet = get_bet(player)
    player.place_bet(bet)
    dealer.place_bet(bet)

    # Deal initial hands
    for _ in range(2):
        player.hand.append(deck.pop())
        dealer.hand.append(deck.pop())

    player_turn(player, deck)

    if player.get_hand_value() <= 21:
        dealer_turn(dealer, deck)

    determine_winner(player, dealer)


if __name__ == "__main__":
    main()
