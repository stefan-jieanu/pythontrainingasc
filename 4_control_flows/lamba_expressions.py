# 1. Scrieti o functie care ia ca paramtru o lista de cuvinte si creeaza o lista noua doar cu prima litera.
# Ex input: ['appla', 'banana', 'cherry']
# output: ['a', 'b', 'c']
from functools import reduce

list_1 = ['appla', 'banana', 'cherry']

def first_letter_list(words):
    return list(map(lambda word: word[0], words))

print(first_letter_list(list_1))

# 2. Scrieti o functie care elimina numerele mai mici decat zero dintr-o lista de numere.
# Ex input: [1, -1, 5, 6, -3]
# output: [1, 5, 6]
list_2 = [1, -1, 5, 6, -3]

def remove_negative_numbers(numbers):
    return list(filter(lambda number: number > 0, numbers))
print(remove_negative_numbers(list_2))


# 3. Scrieti o functie care converteste o lista de strings intr-un singur string
# Ex input: ["Hello", "lambda", "functions", "!"]
# output: "Hello lamba functions !"
list_3 = ["Hello", "lambda", "functions", "!"]

def convert_to_string(words):
    return reduce(lambda x, y: x + " " + y, words)
print(convert_to_string(list_3))


# 4. Scrieti o functie care determina cuvintele palindrom dintr-o lista de cuvinte.
# Un palindrom este un cuvant care se citeste la fel de la stanga la dreapta si invers.
# Ex input: ["rotor", "level", "radar", "mama"]
# output: ["rotor", "level", "radar"]
list_4 = ["rotor", "level", "radar", "mama"]

def palindrom_words(words):
    return list(filter(lambda word: word == word[::-1], words))
print(palindrom_words(list_4))

# 5. O functie care returneaza cel mai lung cuvant dintr-o lista
# Ex input: ["apple", "banana", "cherry", "kiwi"]
# output: cherry
list_5 = ["apple", "banana", "cherry", "kiwi"]

def longest_word(words):
    return max(words, key=lambda word: len(word))
print(longest_word(list_5))
