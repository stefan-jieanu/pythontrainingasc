# 1. Scrieti o functie care ia ca paramtru o lista de cuvinte si creeaza o lista noua doar cu prima litera.
# Ex input: ['appla', 'banana', 'cherry']
# output: ['a', 'b', 'c']
from functools import reduce

list_1 = ['appla', 'banana', 'cherry']
first_letter = reduce(lambda acc, word: acc + [word[0]], list_1, [])
print(first_letter)

# 2. Scrieti o functie care elimina numerele mai mici decat zero dintr-o lista de numere.
# Ex input: [1, -1, 5, 6, -3]
# output: [1, 5, 6]
list_2 = [1, -1, 5, 6, -3]
lower_then_zero = list(filter(lambda n: n > 0, list_2))
print(lower_then_zero) 


# 3. Scrieti o functie care converteste o lista de strings intr-un singur string
# Ex input: ["Hello", "lambda", "functions", "!"]
# output: "Hello lamba functions !"
list_3 = ["Hello", "lambda", "functions", "!"]
print_string = (lambda list: " ".join(list))(list_3)
print(print_string)

# 4. Scrieti o functie care determina cuvintele palindrom dintr-o lista de cuvinte.
# Un palindrom este un cuvant care se citeste la fel de la stanga la dreapta si invers.
# Ex input: ["rotor", "level", "radar", "mama"]
# output: ["rotor", "level", "radar"]
list_4 = ["rotor", "level", "radar", "mama"]
check_palindrome = list(filter(lambda s: s == s[::-1], list_4))
print(check_palindrome)

# 5. O functie care returneaza cel mai lung cuvant dintr-o lista
# Ex input: ["apple", "banana", "cherry", "kiwi"]
# output: cherry
list_5 = ["apple", "banana", "cherry", "kiwi"]
longest_word = reduce(lambda acc, word: word if len(word) > len(acc) else acc, list_5, "")
print(longest_word)
