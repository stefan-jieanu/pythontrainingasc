# Given the string: "Python is a cool programming language!"
# Ask the user for a number and display the character at that index,
# followed by the message: "Done"

# Example 1
# Input: 2
# Output: 
# "t"
# "Done"

# Example 2
# Input: 10
# Output:
# "a" 
# "Done"

# Exception? If the user inputs a character insead of a string or the number is too large
# we should show an error message, followed by "Done"

# Example 3
# Input: 100
# Output:
# "Number too big"
# "Done"

# Example 4
# Input: 'a'
# Output:
# "Invalid input"
# "Done"

# Hint! Use try/except/finally

text = "Python is a cool programming language!"

try:
    user_input = input("Enter a number: ")
    number = int(user_input)

    print(text[number])

except ValueError:
    print("Invalid input")

except IndexError:
    print("Number too big")

finally:
    print("Done")