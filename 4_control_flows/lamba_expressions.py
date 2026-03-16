# 1. Scrieti o functie care ia ca paramtru o lista de cuvinte si creeaza o lista noua doar cu prima litera.
# Ex input: ['appla', 'banana', 'cherry']
# output: ['a', 'b', 'c']
from functools import reduce

list_1 = ['appla', 'banana', 'cherry']
first_letters = list(map(lambda w: w[0], list_1))
print('Ex1: ')
print(first_letters)

# 2. Scrieti o functie care elimina numerele mai mici decat zero dintr-o lista de numere.
# Ex input: [1, -1, 5, 6, -3]
# output: [1, 5, 6]
list_2 = [1, -1, 5, 6, -3]
no_negatives = list(filter(lambda x: x > 0, list_2))
print('Ex2: ')
print(no_negatives)

# 3. Scrieti o functie care converteste o lista de strings intr-un singur string
# Ex input: ["Hello", "lambda", "functions", "!"]
# output: "Hello lamba functions !"
list_3 = ["Hello", "lambda", "functions", "!"]
prop = reduce(lambda x, y: x + ' ' + y, list_3)
print("Ex3: ")
print(prop)

# 4. Scrieti o functie care determina cuvintele palindrom dintr-o lista de cuvinte.
# Un palindrom este un cuvant care se citeste la fel de la stanga la dreapta si invers.
# Ex input: ["rotor", "level", "radar", "mama"]
# output: ["rotor", "level", "radar"]
list_4 = ["rotor", "level", "radar", "mama"]
palindromes = list(filter(lambda x: x == x[::-1], list_4))
print("Ex4:")
print(palindromes)

# 5. O functie care returneaza cel mai lung cuvant dintr-o lista
# Ex input: ["apple", "banana", "cherry", "kiwi"]
# output: cherry
print("Ex5: ")
words = ["apple", "banana", "cherry", "kiwi"]
longest = reduce(lambda x, y: x if len(x) > len(y) else y, words)
print(longest)