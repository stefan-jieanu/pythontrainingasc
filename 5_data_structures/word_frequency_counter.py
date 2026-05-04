# Write a program that counts how many times each word appears in a given paragraph and
# stores these counts in a dictionary.

# Example
# text = "apple banana apple cherry banana apple"
# Output: {'apple': 3, 'banana': 2, 'cherry': 1}


def word_frequency(text):
    counts = {}
    for word in text.split():
        counts[word] = counts.get(word, 0) + 1
    return counts


text = "apple banana apple cherry banana apple"
print(word_frequency(text))
