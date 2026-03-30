# Write a program that counts how many times each word appears in a given paragraph and 
# stores these counts in a dictionary.

# Example
# text = "apple banana apple cherry banana apple"
# Output: {'apple': 3, 'banana': 2, 'cherry': 1}

def word_freq(list):
    obj = {}
    for word in list.split(" "):
        if not obj.get(word): obj[word] = 0
        obj[word] += 1
    
    print(obj)

text = "apple banana apple cherry banana apple"
word_freq(text)