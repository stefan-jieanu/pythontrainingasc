from blackjack_module.player import Player
from blackjack_module.deck import Card, create_deck
import random
## Exercise 3: `game.py` — Game logic

## Using `deck.py` and `player.py` from the previous exercises, create `game.py` with the following functions:

## - **`get_bet(player)`** — asks the player how much they want to bet; validates that the input is a number and doesn't exceed available cash
## - **`player_turn(player, deck)`** — shows the player's hand and asks if they want to draw another card or stand; stops if the player busts
## - **`dealer_turn(dealer, deck)`** — the computer draws cards until it reaches 18 or higher, then stands
## - **`determine_winner(player, dealer)`** — compares hands, announces the winner, updates cash, and prints final balances


def get_bet(player: Player) -> float:
    bet = 0
    def get_choice():
        nonlocal bet # needed to be able to modify a variable from an outer scope
        bet = input(f"{player.name} please make your bet (${player.cash} available): ")
        bet = int(bet) if bet.isnumeric() and int(bet) <= player.cash else None

        if not bet:
            print(f"Invalid bet, please choose a valid amount in your budget!")
            get_choice()

    get_choice()

    player.place_bet(bet)
    return bet


def player_turn(player: Player, deck: list[Card]) -> None:
    name = player.name
    print(f"{name}'s hand:")
    player.show_hand()
    
    def get_choice():
        choice = input(f"{name} do you want to stand or draw? ")
        if(choice == 'draw'):
            card = deck.pop()
            print(f"{name} draws {card}")
            player.hand.append(card)

            if(player.get_hand_value() > 21):
                print(f"{name} hand value is {player.get_hand_value()}! Busted!")
                player.hand = []  #player out of the game
                return
            return
        elif(choice == "stand"):
            print(f"{name} stands!")
        else:
            print("Invalid choice!")
            get_choice()

    get_choice()
        

def dealer_turn(dealer: Player, deck: list[Card]) -> None:
    name = dealer.name
    print(f"{name} draws cards...")
    while dealer.get_hand_value() < 18:
        dealer.hand.append(deck.pop())
        if dealer.get_hand_value() > 21:
            print(f"{name} hand value is {dealer.get_hand_value()}! Busted!")
            dealer.hand = []  #dealer out of the game
            return


def determine_winner(player: Player, dealer: Player) -> None:
    if  player.get_hand_value() > dealer.get_hand_value():
        print(f"{player.name} wins!")
        player.cash += (player.bet + dealer.bet)
    elif  dealer.get_hand_value() > player.get_hand_value():
        print(f"{dealer.name} wins!")
        dealer.cash += (player.bet + dealer.bet)
    else:
        print("It's a draw!")
        player.cash += player.bet
        dealer.cash += dealer.bet
    
    player.bet = 0
    dealer.bet = 0
    
    print(f"{player.name} cash: {player.cash}")
    print(f"{dealer.name} cash: {dealer.cash}")



def main ():
    ## 1. Create a deck and shuffle it
    deck = create_deck()
    random.shuffle(deck)
    print("Deck created and shuffled!")

    ## 2. Create two players: one human (500 credits), one computer (500 credits)
    player1 = Player( "Human", 500, [] )
    player2 = Player( "Computer", 500, [])
    print("Players ready!")

    ## 3. Ask the human for a bet; the computer matches it
    player2.place_bet(get_bet(player1))

    ## 4. Deal 2 cards to each player
    print("Dealing 2 cards to each player...")
    for _ in range(2):
        player1.hand.append(deck.pop())
        player2.hand.append(deck.pop())

    ## 5. Run the human player's turn
    player_turn(player1, deck)

    ## 6. If the human hasn't busted, run the dealer's turn
    if player1.hand:
        dealer_turn(player2, deck)

    ## 7. Determine and display the winner
    determine_winner(player1, player2)