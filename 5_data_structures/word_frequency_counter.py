# Write a program that counts how many times each word appears in a given paragraph and 
# stores these counts in a dictionary.

# Example
# text = "apple banana apple cherry banana apple"
# Output: {'apple': 3, 'banana': 2, 'cherry': 1}

def word_frequency_counter(text):
    words = text.split()
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

print(word_frequency_counter("apple banana apple cherry banana apple"))