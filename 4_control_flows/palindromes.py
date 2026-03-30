# Given a string, the task is to check whether it is a palindrome.
# A palindrome is a string that reads the same forward and backward. 
# For example, "madam" is a palindrome, while "hello" is not.

def is_palindrome(word):
    return word == word[::-1]

print(is_palindrome("madam"))
print(is_palindrome("hello"))