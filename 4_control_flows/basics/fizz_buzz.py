# Given a number n, for every number i <= n, create a list that contains:
# FizzBuzz' if i is divisible by 3 and 5,
# 'Fizz' if i is divisible by 3,
# 'Buzz' if i is divisible by 5
# i (as a string) if none of the above conditions are true

# Example
# n = 15
# Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

n = 15
result = []

for i in range(1, n + 1):
    if i % 15 == 0:
        result.append("FizzBuzz")
    elif i % 3 == 0:
        result.append("Fizz")
    elif i % 5 == 0:
        result.append("Buzz")
    else:
        result.append(str(i))

print(result)