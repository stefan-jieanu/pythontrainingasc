# 1. Scrieti o functie care ia ca paramtru o lista de cuvinte si creeaza o lista noua doar cu prima litera.
# Ex input: ['appla', 'banana', 'cherry']
# output: ['a', 'b', 'c']
from functools import reduce

list_1 = ['appla', 'banana', 'cherry']


# 2. Scrieti o functie care elimina numerele mai mici decat zero dintr-o lista de numere.
# Ex input: [1, -1, 5, 6, -3]
# output: [1, 5, 6]
list_2 = [1, -1, 5, 6, -3]


# 3. Scrieti o functie care converteste o lista de strings intr-un singur string
# Ex input: ["Hello", "lambda", "functions", "!"]
# output: "Hello lamba functions !"
list_3 = ["Hello", "lambda", "functions", "!"]


# 4. Scrieti o functie care determina cuvintele palindrom dintr-o lista de cuvinte.
# Un palindrom este un cuvant care se citeste la fel de la stanga la dreapta si invers.
# Ex input: ["rotor", "level", "radar", "mama"]
# output: ["rotor", "level", "radar"]
list_4 = ["rotor", "level", "radar", "mama"]


# 5. O functie care returneaza cel mai lung cuvant dintr-o lista
# Ex input: ["apple", "banana", "cherry", "kiwi"]
# output: cherry
# print("Ex5: ")

list_5 = ["tiny","short", "medium", "thelargeone"]


#1.
def words_to_first_letters(words: list[str]) -> list[str]:
  return [w[0] if w else '' for w in words]

print("Ex1: ", words_to_first_letters(list_1))

#2
def keep_only_positives(numbers: list[int]) -> list[int]:
  return list(filter(lambda x: x > 0, numbers))

print("Ex2: ", keep_only_positives(list_2))

#3
def list_to_string(my_list: list[str]) -> str:
  return reduce(lambda acc, curr: f"{acc} {curr}", my_list)

print("Ex3: ", list_to_string(list_3))

#4
def determine_palindromes(my_list: list[str]) -> list[str]:
  return list(filter(lambda word: word == word[::-1], my_list))

print("Ex4: ", determine_palindromes(list_4))

#5
def get_longest_word(my_list: list) -> str:
  return reduce(lambda acc, curr: acc if len(acc) > len(curr) else curr, my_list)

print("Ex.5: ", get_longest_word(list_5))