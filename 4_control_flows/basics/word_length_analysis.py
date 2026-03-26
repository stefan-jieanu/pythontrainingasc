# Given a list of words
# write a loop that iterates through the list and prints each word alongside its character count.

# Example input
# words = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]

# Example output
# Apple - 5 Banana - 6 Cherry - 6 Date - 4 Elderberry - 10

# Ciprian Serban
def word_count(words):
    for word in words:
        print(f"{word}={len(word)},")
    print()

words = ["Lemn", "Castravete", "Avion", "Enciclopedie", "Pix", "Zidari", "Gandac", "Crocodil"]
word_count(words)
