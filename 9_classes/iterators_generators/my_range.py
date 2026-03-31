from typing import Any

# You're probably familiar with the range() function which we can use to iterate over numbers
# for i in range(0, 10):
#     print (i)

# Let's implement the range() function ourselves and call it myrange. It should take the same parameters as the original range() function
# and have the same behaviour. You can do so using iterators or generators (or try both approaches).

def myrange_gen(start: int, stop: int, step: int = 1):
  i = start
  while i < stop:
    yield i
    i += step

print("RANGE:")
for x in range(0, 10):
  print(x)

print("\nMY_RANGE_GEN:")
for x in myrange_gen(0, 10):
  print(x)

print("\nRANGE step 2:")
for x in range(0, 10, 2):
  print(x)

print("\nMY_RANGE_GEN step 2:")
for x in myrange_gen(0, 10, 2):
  print(x)