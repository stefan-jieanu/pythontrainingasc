# Given a string, the task is to check whether it is a palindrome.
# A palindrome is a string that reads the same forward and backward. 
# For example, "madam" is a palindrome, while "hello" is not.

palindrome_word = 'madam'
not_palindrome_word = 'hello'
def check_plaindrome(word):
    return word == word[::-1]

print(f"Is {palindrome_word} a palindrome? Result: {check_plaindrome(palindrome_word)}")
print(f"Is {not_palindrome_word} a palindrome? Result: {check_plaindrome(not_palindrome_word)}")