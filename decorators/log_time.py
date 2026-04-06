# Scrieti un decorator numit log_time care sa afiseze ora, minutul, secunda la care a rulat o functie.

import datetime

def log_time(func):
    def wrapper(*args, **kwargs):
        now = datetime.datetime.now()
        print(f"Function {func.__name__} ran at {now.hour}:{now.minute}:{now.second}")
        return func(*args, **kwargs)
    return wrapper

@log_time
def say_hello(name):
    print(f"Hello {name}")

say_hello("Python")
