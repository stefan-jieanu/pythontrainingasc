# Custom exceptions
# Create an exception class called InvalidNameException
# Create a function called check_name(name) which check if a string is a valid name (only contains letters)
# If the name valid the function should return True, otherwise it should raise our exception


class InvalidNameException(Exception):
    pass


def check_name(name):
    if name.isalpha():
        return True
    raise InvalidNameException(f"'{name}' is not a valid name.")


print(check_name("Alice"))

try:
    check_name("Alice123")
except InvalidNameException as e:
    print(e)
