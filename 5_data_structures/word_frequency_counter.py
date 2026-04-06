# Write a program that counts how many times each word appears in a given paragraph and 
# stores these counts in a dictionary.

# Example
# text = "apple banana apple cherry banana apple"
# Output: {'apple': 3, 'banana': 2, 'cherry': 1}
from collections import Counter

def word_frequency_counter(text):
    word_counts = {}
    words = text.split()
    
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
            
    return word_counts

def word_frequency_counter1(text):
    word_counts = {}
    words = text.split()
    
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
            
    return word_counts

def word_frequency_counter2(text):
    word_counts = {}
    words = text.split()
    single_word = set(words)
    for word in single_word:
        word_counts[word] = words.count(word)
            
    return word_counts

def word_frequency_counter3(text):
    return dict(Counter(text.split()))

print(word_frequency_counter("apple banana apple cherry banana apple"))
print(word_frequency_counter1("apple banana apple cherry banana apple"))
print(word_frequency_counter2("apple banana apple cherry banana apple"))
print(word_frequency_counter3("apple banana apple cherry banana apple"))