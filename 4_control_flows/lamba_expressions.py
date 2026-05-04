# 1. Scrieti o functie care ia ca paramtru o lista de cuvinte si creeaza o lista noua doar cu prima litera.
# Ex input: ['appla', 'banana', 'cherry']
# output: ['a', 'b', 'c']
from functools import reduce

list_1 = ['appla', 'banana', 'cherry']

first_letters = lambda words: list(map(lambda w: w[0], words))
print("Ex1:", first_letters(list_1))


# 2. Scrieti o functie care elimina numerele mai mici decat zero dintr-o lista de numere.
# Ex input: [1, -1, 5, 6, -3]
# output: [1, 5, 6]
list_2 = [1, -1, 5, 6, -3]

remove_negatives = lambda nums: list(filter(lambda n: n >= 0, nums))
print("Ex2:", remove_negatives(list_2))


# 3. Scrieti o functie care converteste o lista de strings intr-un singur string
# Ex input: ["Hello", "lambda", "functions", "!"]
# output: "Hello lamba functions !"
list_3 = ["Hello", "lambda", "functions", "!"]

join_strings = lambda words: reduce(lambda a, b: a + " " + b, words)
print("Ex3:", join_strings(list_3))


# 4. Scrieti o functie care determina cuvintele palindrom dintr-o lista de cuvinte.
# Un palindrom este un cuvant care se citeste la fel de la stanga la dreapta si invers.
# Ex input: ["rotor", "level", "radar", "mama"]
# output: ["rotor", "level", "radar"]
list_4 = ["rotor", "level", "radar", "mama"]

find_palindromes = lambda words: list(filter(lambda w: w == w[::-1], words))
print("Ex4:", find_palindromes(list_4))


# 5. O functie care returneaza cel mai lung cuvant dintr-o lista
# Ex input: ["apple", "banana", "cherry", "kiwi"]
# output: cherry
list_5 = ["apple", "banana", "cherry", "kiwi"]

longest_word = lambda words: reduce(lambda a, b: a if len(a) > len(b) else b, words)
print("Ex5:", longest_word(list_5))
