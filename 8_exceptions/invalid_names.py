# Custom exceptions
# Create an exception class called InvalidNameException
# Create a function called check_name(name) which check if a string is a valid name (only contains letters)
# If the name valid the function should return True, otherwise it should raise our exception

class InvalidNameException(Exception):
    pass

def check_name(name):
    if name.isalpha():
        return True
    raise InvalidNameException

try:
    print(check_name("Ciprian1"))
except InvalidNameException:
    print("Nume invalid.")

try:
    print(check_name("Ciprian"))
except InvalidNameException:
    print("Nume valid.")






