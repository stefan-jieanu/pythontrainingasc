# You're probably familiar with the range() function which we can use to iterate over numbers
# for i in range(0, 10):
#     print (i)

# Let's implement the range() function ourselves and call it myrange. It should take the same parameters as the original range() function
# and have the same behaviour. You can do so using iterators or generators (or try both approaches).
def my_range(start, end, step=1):
    while start < end:
        yield start
        start += step

for i in my_range(0, 10):
    print(i)