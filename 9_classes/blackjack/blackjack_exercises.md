# Blackjack — Python Exercises

## Exercise 1: `deck.py` — Card functions

Create a `deck.py` module with the following functions:

- **`create_deck()`** — returns a list of 52 cards; each card is a dictionary with `"suit"` (e.g. `"Hearts"`) and `"rank"` (e.g. `"A"`, `"K"`, `"10"`, `"2"`)
- **`print_card(card)`** — prints a card on one line, e.g. `A of Spades`
- **`card_value(card)`** — returns the blackjack value of a single card (face cards = 10, Ace = 11, number cards = their number)
- **`hand_value(cards)`** — takes a list of cards and returns the total value; Aces should be reduced from 11 to 1 when the total exceeds 21

> **Hint:** Use a `while` loop to reduce Aces one at a time until the total is 21 or less.

---

## Exercise 2: `player.py` — Player class

Using `deck.py` from the previous exercise, create a `Player` class with:

**Attributes:**
- `name` — the name of the player
- `cash` — credits available (default 0)
- `hand` — the list of cards the player is holding (starts empty)
- `bet` — the current bet amount (starts at 0)

**Methods:**
- `show_hand()` — prints all cards in the player's hand (use `print_card` from `deck.py`)
- `place_bet(amount)` — sets the current bet
- `get_hand_value()` — returns the total blackjack value of the hand (use `hand_value` from `deck.py`)

---

## Exercise 3: `game.py` — Game logic

Using `deck.py` and `player.py` from the previous exercises, create `game.py` with the following functions:

- **`get_bet(player)`** — asks the player how much they want to bet; validates that the input is a number and doesn't exceed available cash
- **`player_turn(player, deck)`** — shows the player's hand and asks if they want to draw another card or stand; stops if the player busts
- **`dealer_turn(dealer, deck)`** — the computer draws cards until it reaches 18 or higher, then stands
- **`determine_winner(player, dealer)`** — compares hands, announces the winner, updates cash, and prints final balances

**Game flow (in `main()`):**
1. Create a deck and shuffle it
2. Create two players: one human (500 credits), one computer (500 credits)
3. Ask the human for a bet; the computer matches it
4. Deal 2 cards to each player
5. Run the human player's turn
6. If the human hasn't busted, run the dealer's turn
7. Determine and display the winner
