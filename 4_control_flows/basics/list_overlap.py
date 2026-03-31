# Take two lists, say for example these two:

# 	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# 	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# and write a program that returns a list that contains only the elements that are common 
# between the lists (without duplicates). Make sure your program works on two lists of different sizes.

def list_overlap(list1: list[int], list2: list[int]) -> list[int]:
  return set(list1) & set(list2)

print(list_overlap(
  [9, 8, 7, 6, 5, 4, 3, 2, 1],
  [1, 2, 2, 2, 2, 3, 5, 10, 11, 12]
))

# Question:
# I see that for sets python has some built-in methods and some shortcuts of the same methods.
# Here: https://www.w3schools.com/python/python_sets_methods.asp

# Which are the ones you really use in practice?
# The choice is about preference or readability or are there some differences in the way they work?