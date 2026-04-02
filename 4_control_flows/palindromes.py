# Given a string, the task is to check whether it is a palindrome.
# A palindrome is a string that reads the same forward and backward. 
# For example, "madam" is a palindrome, while "hello" is not.

def is_palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False

def is_palindrome2(s):
    a = list(s)
    print(a)
    print(len(a))
    for i in range(len(a) // 2):
        if a[i] != a[-(i + 1)]:
            return False

print(is_palindrome2("madam"))
print(is_palindrome("madam"))
print(is_palindrome("hello"))
print(is_palindrome2("hello"))