# Custom exceptions
# Create an exception class called InvalidNameException
# Create a function called check_name(name) which check if a string is a valid name (only contains letters)
# If the name valid the function should return True, otherwise it should raise our exception

class InvalidNameException(Exception):
  def __init__(self, name: str = ''):
    super().__init__(f"{name or 'This'} is not a valid name!")


def check_name(name: str) -> bool:
  if isinstance(name, str) and name.isalpha():
    return True
    
  raise InvalidNameException(str(name))


print(check_name("MyName"))

#print(check_name({"name": "MyName"}))