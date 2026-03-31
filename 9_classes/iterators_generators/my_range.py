# You're probably familiar with the range() function which we can use to iterate over numbers
# for i in range(0, 10):
#     print (i)

# Let's implement the range() function ourselves and call it myrange. It should take the same parameters as the original range() function
# and have the same behaviour. You can do so using iterators or generators (or try both approaches).

def myrange(*args):
    if len(args) == 1:
        start, stop, step = 0, args[0], 1
    elif len(args) == 2:
        start, stop, step = args[0], args[1], 1
    elif len(args) == 3:
        start, stop, step = args

    n = start
    if step > 0:
        while n < stop:
            yield n
            n += step
    else:
        while n > stop:
            yield n
            n += step


print(list(myrange(5))) 
print(list(myrange(2, 5)))
print(list(myrange(5, 1, -1)))
print(list(myrange(0, 10, 2)))