# Custom exceptions
# Create an exception class called InvalidNameException
# Create a function called check_name(name) which check if a string is a valid name (only contains letters)
# If the name valid the function should return True, otherwise it should raise our exception


class InvalidNameException(Exception):
    pass

def check_name(name):
    if not name.isalpha():
        raise InvalidNameException(f"Name {name} is not valid. It contains numbers.")
    return True

try:
    check_name("John123")
except InvalidNameException as e:
    print(e)

try:
    check_name("John")
    print("Name is valid")
except InvalidNameException as e:
    print(e)

check_name("John")