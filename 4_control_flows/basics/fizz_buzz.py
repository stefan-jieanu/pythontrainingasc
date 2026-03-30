# Given a number n, for every number i <= n, create a list that contains:
# FizzBuzz' if i is divisible by 3 and 5,
# 'Fizz' if i is divisible by 3,
# 'Buzz' if i is divisible by 5
# i (as a string) if none of the above conditions are true

# Example
# n = 15
# Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]


def fizz_buzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


print(fizz_buzz(15))
