# You're probably familiar with the range() function which we can use to iterate over numbers
# for i in range(0, 10):
#     print (i)

# Let's implement the range() function ourselves and call it myrange. It should take the same parameters as the original range() function
# and have the same behaviour. You can do so using iterators or generators (or try both approaches).

class MyRange:
    def __init__(self, start, stop=None):
        if stop is None:
            stop = start
            start = 0
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start >= self.stop:
            raise StopIteration
        current = self.start
        self.start += 1
        return current
    
def myrange_gen(start: int, stop: int):
  i = start
  while i < stop:
    yield i
    i += 1

# Testing the MyRange class
my_range = MyRange(0, 10)
for i in my_range:
    print(i)

# Testing the myrange_gen function
for i in myrange_gen(0, 10):
    print(i)