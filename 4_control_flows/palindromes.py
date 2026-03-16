# Given a string, the task is to check whether it is a palindrome.
# A palindrome is a string that reads the same forward and backward. 
# For example, "madam" is a palindrome, while "hello" is not.

# Basic solution
s = "malayalam"  
i, j = 0, len(s) - 1  
is_palindrome = True

while i < j:
    if s[i] != s[j]:  
        is_palindrome = False
        break
    i += 1
    j -= 1

if is_palindrome:
    print("Yes") 
else:
    print("No")

# Easy solution using slicing
s = "malayalam" 

if s == s[::-1]:
    print("Yes")
else:
    print("No")