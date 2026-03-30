# Custom exceptions
# Create an exception class called InvalidNameException
# Create a function called check_name(name) which check if a string is a valid name (only contains letters)
# If the name valid the function should return True, otherwise it should raise our exception

class InvalidNameException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(f"Invalid name provided")

def check_name(name):
    if not name.isalpha():
        raise InvalidNameException()
    else:
        print(f"{name} is valid: True")

check_name("Mark")
check_name("Mark1 asdf!")