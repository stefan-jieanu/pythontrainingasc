# You're probably familiar with the range() function which we can use to iterate over numbers
# for i in range(0, 10):
#     print (i)

# Let's implement the range() function ourselves and call it myrange. It should take the same parameters as the original range() function
# and have the same behaviour. You can do so using iterators or generators (or try both approaches).

class MyRange:
    def __init__(self, start, stop=None, step=1):
        if stop is None:
            stop = start
            start = 0
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        current = self.start
        while current < self.stop:
            yield current
            current += self.step



for i in MyRange(0, 10):
    print(i)

