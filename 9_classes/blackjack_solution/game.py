# Exercise 3: game.py — Game logic
# Using deck.py and player.py from the previous exercises, create game.py with the following functions:

# get_bet(player) — asks the player how much they want to bet; validates that the input is a number and doesn't exceed available cash
# player_turn(player, deck) — shows the player's hand and asks if they want to draw another card or stand; stops if the player busts
# dealer_turn(dealer, deck) — the computer draws cards until it reaches 18 or higher, then stands
# determine_winner(player, dealer) — compares hands, announces the winner, updates cash, and prints final balances
# Game flow (in main()):

# Create a deck and shuffle it
# Create two players: one human (500 credits), one computer (500 credits)
# Ask the human for a bet; the computer matches it
# Deal 2 cards to each player
# Run the human player's turn
# If the human hasn't busted, run the dealer's turn
# Determine and display the winner

import random

import deck as dk
import player as ply

def get_bet(player: ply.Player):
    try:
        bet = int(input("How much would you like to bet? Bet size: "))
    except ValueError:
        print("Input must be a number. Please retry!")
        return get_bet(player)

    if bet > player.cash:
        print("Bet size exceeds player cash. Please retry!")
        return get_bet(player)

    return bet

def player_turn(player: ply.Player, deck):
    while True:
        player.show_hand()
        print(f"Current hand value is: {player.get_hand_value()}")

        if player.get_hand_value() > 21:
            print("You busted!")
            break

        choice = input("Do you want to draw another card or stand? (draw/stand): ")

        if choice == "draw":
            player.hand.append(deck.pop())
        elif choice == "stand":
            print("You stand.")
            break
        else:
            print("Please type 'draw' or 'stand'.")

def dealer_turn(dealer, deck):
    print("Dealer's turn")

    while dealer.get_hand_value() < 18:
        dealer.hand.append(deck.pop())
        print("Dealer draws a card.")

    dealer.show_hand()
    print(f"Dealer hand value is: {dealer.get_hand_value()}")

    if dealer.get_hand_value() > 21:
        print("Dealer busted!")
    else:
        print("Dealer stands.")

def determine_winner(player: ply.Player, dealer: ply.Player):
    player_value = player.get_hand_value()
    dealer_value = dealer.get_hand_value()

    print(f"{player.name} hand value: {player_value}")
    print(f"{dealer.name} hand value: {dealer_value}")

    if player_value > 21:
        print(f"{player.name} busted. {dealer.name} wins!")
        player.cash -= player.bet
        dealer.cash += player.bet

    elif dealer_value > 21:
        print(f"{dealer.name} busted. {player.name} wins!")
        player.cash += player.bet
        dealer.cash -= player.bet

    elif player_value > dealer_value:
        print(f"{player.name} wins!")
        player.cash += player.bet
        dealer.cash -= player.bet

    elif dealer_value > player_value:
        print(f"{dealer.name} wins!")
        player.cash -= player.bet
        dealer.cash += player.bet

    else:
        print("It's a draw!")
        player.bet = 0

    print(f"{player.name} cash: {player.cash}")

def main():
    card_deck = dk.create_deck()
    random.shuffle(card_deck)

    player = ply.Player("Player", 500)
    dealer = ply.Player("Dealer", 500)

    bet = get_bet(player)
    player.place_bet(bet)
    dealer.place_bet(bet)

    for _ in range(2):
        player.hand.append(card_deck.pop())
        dealer.hand.append(card_deck.pop())

    player_turn(player, card_deck)

    if player.get_hand_value() <= 21:
        dealer_turn(dealer, card_deck)

    determine_winner(player, dealer)

if __name__ == "__main__":
    main()