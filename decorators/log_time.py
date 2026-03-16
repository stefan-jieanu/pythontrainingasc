# Scrieti un decorator numit log_time care sa afiseze ora, minutul, secunda la care a rulat o functie.
# Exemplu output
# 12:59:36
# Sorted!
# 12:59:38
# Hello World
from datetime import datetime


def log_time(func):
    def wrapper():
        h = datetime.now().hour
        m = datetime.now().minute
        s = datetime.now().second

        print(f"{h}:{m}:{s}")

        func()

    return wrapper

@log_time
def bubble_sort():
    arr = range(0, 5000) # [0, 1, 2, ...., 4999]
    n = len(arr)
    # Traverse through all elements in the list
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n - i - 1):
            # Swap if the current element is greater than the next one
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    print("Sorted!")

@log_time
def say_hello():
    print("Hello World")

bubble_sort()
say_hello()