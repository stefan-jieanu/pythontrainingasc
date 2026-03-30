# Scrieti un decorator numit log_time care sa afiseze ora, minutul, secunda la care a rulat o functie.

import datetime

def log_time(func):
    def wrapper():
        print(f"Exection was made at {datetime.datetime.now().strftime('Hour: %H, Minute: %M, Second: %S')}")
        func()
    return wrapper
        

@log_time
def do_something():
    print('Execution done')

do_something()