# Given a list of words
# write a loop that iterates through the list and prints each word alongside its character count.

# Example input
# words = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]

# Example output
# Apple - 5 Banana - 6 Cherry - 6 Date - 4 Elderberry - 10

def word_length_analysis(words: list[str]) -> str:
  result: str = ""
  for word in words:
    result += f"{word} - {len(word)} "
  return result.strip()

print(word_length_analysis(["Apple", "Banana", "Cherry", "Date", "Elderberry"]))