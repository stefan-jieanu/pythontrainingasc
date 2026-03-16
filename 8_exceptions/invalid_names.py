# Custom exceptions
# Create an exception class called InvalidNameException
# Create a function called check_name(name) which check if a string is a valid name (only contains letters)
# If the name valid the function should return True, otherwise it should raise our exception

class InvalidNameException(Exception):
    pass

    # Or with default message
    # def __init__(self, message):
    #     message = "Name must contain only letters"
    #     super().__init__(message)


def check_name(name):
    if not name.isalpha():
        raise InvalidNameException("Name must contain only letters.")
    
    return True

print(check_name("Alic1e"))