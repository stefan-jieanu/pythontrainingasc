# Given a string, the task is to check whether it is a palindrome.
# A palindrome is a string that reads the same forward and backward.
# For example, "madam" is a palindrome, while "hello" is not.


def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]


print(is_palindrome("madam"))   # True
print(is_palindrome("hello"))   # False
print(is_palindrome("Racecar")) # True
