# Write a program that counts how many times each word appears in a given paragraph and 
# stores these counts in a dictionary.

# Example
# text = "apple banana apple cherry banana apple"
# Output: {'apple': 3, 'banana': 2, 'cherry': 1}

def word_counts(text):
    counts = {}
    for word in text.split():
        counts[word.lower()] = counts.get(word.lower(), 0) + 1
    return counts

text="Last week I brought home some soil I put the soil in the yard last week Good clayey soil for the lawn A lawn that's healthy and will grow"
print(word_counts(text))