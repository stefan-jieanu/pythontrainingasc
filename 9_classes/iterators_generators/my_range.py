# You're probably familiar with the range() function which we can use to iterate over numbers
# for i in range(0, 10):
#     print (i)

# Let's implement the range() function ourselves and call it myrange. It should take the same parameters as the original range() function
# and have the same behaviour. You can do so using iterators or generators (or try both approaches).


def myrange(start, stop=None, step=1):
    if stop is None:
        start, stop = 0, start
    i = start
    while (step > 0 and i < stop) or (step < 0 and i > stop):
        yield i
        i += step


print(list(myrange(5)))           # [0, 1, 2, 3, 4]
print(list(myrange(2, 8)))        # [2, 3, 4, 5, 6, 7]
print(list(myrange(0, 10, 2)))    # [0, 2, 4, 6, 8]
print(list(myrange(10, 0, -2)))   # [10, 8, 6, 4, 2]
