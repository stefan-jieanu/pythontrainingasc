# Implementati decoratorul @repeat_func(num_times) care va repeta functia decorata de 'num_times' ori

import functools

def repeat_func(num_times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper
    return decorator

# Exemple functie
@repeat_func(num_times=8)
def greet(name):
    print(f'Hello {name}')

greet('Python')


# Output:
# Hello Python
# Hello Python
# Hello Python
# Hello Python
# Hello Python