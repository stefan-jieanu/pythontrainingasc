# Custom exceptions
# Create an exception class called InvalidNameException
# Create a function called check_name(name) which check if a string is a valid name (only contains letters)
# If the name valid the function should return True, otherwise it should raise our exception

class InvalidNameException(Exception):
    def __init__(self, name):
        super().__init__(f"The name should contain only letters: {name} is invalid.")

def check_name(name):
    if not name.isalpha():
        raise InvalidNameException(name)
    return True

# Test cases
try:
    print(check_name("John"))       # True
    print(check_name("John123"))    # Raises InvalidNameException
except InvalidNameException as e:
    print(e)                        # Output: Invalid name: John123

