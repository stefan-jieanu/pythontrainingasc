# Scrieti un decorator numit log_time care sa afiseze ora, minutul, secunda la care a rulat o functie.

import functools
from datetime import datetime

def log_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        time_now = datetime.now()
        print(f"{time_now.hour:02d}:{time_now.minute:02d}:{time_now.second:02d}")
        return func(*args, **kwargs)
    return wrapper

@log_time
def test():
    print("Bună ziua")

test()

