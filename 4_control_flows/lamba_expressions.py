# 1. Scrieti o functie care ia ca paramtru o lista de cuvinte si creeaza o lista noua doar cu prima litera.
# Ex input: ['appla', 'banana', 'cherry']
# output: ['a', 'b', 'c']
from functools import reduce

list_1 = ['appla', 'banana', 'cherry']

def list_word_to_first_letter(list1):
    return list(map(lambda word: word[0], list1))

def list_word_to_first_letter1(list1):
    return reduce(lambda acc, word: acc + [word[0]], list1, [])

def list_word_to_first_letter2(list1):
    list2 = []
    for word in list1:
        list2.append(word[0])
    return list2

print(list_word_to_first_letter(list_1))
print(list_word_to_first_letter1(list_1))
print(list_word_to_first_letter2(list_1))

# 2. Scrieti o functie care elimina numerele mai mici decat zero dintr-o lista de numere.
# Ex input: [1, -1, 5, 6, -3]
# output: [1, 5, 6]
list_2 = [1, -1, 5, 6, -3]
def positive_numbers(list1):
    return list(filter(lambda x: x >= 0, list1))

def positive_numbers1(list1):
    return reduce(lambda acc, x: acc + [x] if x >= 0 else acc, list1, [])

def positive_numbers2(list1):
    list2 = []
    for x in list1:
        if x >= 0:
            list2.append(x)
    return list2

print(positive_numbers(list_2))
print(positive_numbers1(list_2))
print(positive_numbers2(list_2))

# 3. Scrieti o functie care converteste o lista de strings intr-un singur string
# Ex input: ["Hello", "lambda", "functions", "!"]
# output: "Hello lamba functions !"
list_3 = ["Hello", "lambda", "functions", "!"]

def list_to_string(list1):
    return " ".join(list1)

def list_to_string2(list1):
    return reduce(lambda acc, x: acc + " " + x, list1)

def list_to_string3(list1):
    result = ""
    for word in list1:
        result += word + " "
    return result.strip()

print(list_to_string(list_3))
print(list_to_string2(list_3))
print(list_to_string3(list_3))

# 4. Scrieti o functie care determina cuvintele palindrom dintr-o lista de cuvinte.
# Un palindrom este un cuvant care se citeste la fel de la stanga la dreapta si invers.
# Ex input: ["rotor", "level", "radar", "mama"]
# output: ["rotor", "level", "radar"]
list_4 = ["rotor", "level", "radar", "mama"]
def palindromes(list1):
    return reduce(lambda acc, x: acc + [x] if x == x[::-1] else acc, list1, [])

def palindromes2(list1):
    return list(filter(lambda x: x == x[::-1], list1))

def palindromes3(list1):
    list2 = []
    for word in list1:
        if word == word[::-1]:
            list2.append(word)
    return list2

print(palindromes(list_4))
print(palindromes2(list_4)) 
print(palindromes3(list_4))

# 5. O functie care returneaza cel mai lung cuvant dintr-o lista
# Ex input: ["apple", "banana", "cherry", "kiwi"]
# output: cherry
print("Ex5: ")

def longest_word(list1):
    return reduce(lambda acc, x: x if len(x) > len(acc) else acc, list1, "")

def longest_word2(list1):
    word_longest= ""
    for word in list1:
        if len(word) > len(word_longest):
            word_longest = word
    return word_longest

print(longest_word(["apple", "banana", "cherry", "kiwi"]))
print(longest_word2(["apple", "banana", "cherry", "kiwi"]))
