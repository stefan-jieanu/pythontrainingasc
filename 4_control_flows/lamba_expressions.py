# 1. Scrieti o functie care ia ca paramtru o lista de cuvinte si creeaza o lista noua doar cu prima litera.
# Ex input: ['appla', 'banana', 'cherry']
# output: ['a', 'b', 'c']
from functools import reduce

list_1 = ['appla', 'banana', 'cherry']

f_letters = list(map(lambda w: w[0], list_1))
print(f_letters)

# 2. Scrieti o functie care elimina numerele mai mici decat zero dintr-o lista de numere.
# Ex input: [1, -1, 5, 6, -3]
# output: [1, 5, 6]
list_2 = [1, -1, 5, 6, -3]

without_negative = list(filter(lambda n: n >= 0, list_2))
print(without_negative)

# 3. Scrieti o functie care converteste o lista de strings intr-un singur string
# Ex input: ["Hello", "lambda", "functions", "!"]
# output: "Hello lamba functions !"
list_3 = ["Hello", "lambda", "functions", "!"]

one_str = reduce(lambda a, b: a + " " + b, list_3)
print(one_str)

# 4. Scrieti o functie care determina cuvintele palindrom dintr-o lista de cuvinte.
# Un palindrom este un cuvant care se citeste la fel de la stanga la dreapta si invers.
# Ex input: ["rotor", "level", "radar", "mama"]
# output: ["rotor", "level", "radar"]
list_4 = ["rotor", "level", "radar", "mama"]

palindrom = list(filter(lambda w: w == w[::-1], list_4))
print(palindrom)


# 5. O functie care returneaza cel mai lung cuvant dintr-o lista
# Ex input: ["apple", "banana", "cherry", "kiwi"]
# output: cherry

list_5 = ["enciclopedie", "brancardierul", "rotopercutor", "interdisciplinaritate"]
longest = max(list_5, key=lambda w: len(w))
word_counts = len(longest)
print(f"{longest} = {word_counts}")