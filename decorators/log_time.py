# Scrieti un decorator numit log_time care sa afiseze ora, minutul, secunda la care a rulat o functie.

def log_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Time taken: {end_time - start_time} seconds")
        return result
    return wrapper

@log_time
def my_function():
    print("Hello, world!")