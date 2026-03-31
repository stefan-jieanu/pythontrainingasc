# Write a program that counts how many times each word appears in a given paragraph and 
# stores these counts in a dictionary.

# Example
text = "apple banana apple cherry banana apple"
# Output: {'apple': 3, 'banana': 2, 'cherry': 1}

def count_each_word_frequency(paragraph: str) -> dict[str, int]:
  frq = {}
  for word in paragraph.split():
    frq[word] = frq[word] + 1 if word in frq else 1
  return frq


print(count_each_word_frequency(''))

print(count_each_word_frequency(text))

print(count_each_word_frequency("  asdasdasdas       asdasd asdasdas asdasdas  "))
