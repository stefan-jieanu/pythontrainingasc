# Implementati decoratorul @repeat_func(num_times) care va repeta functia decorata de 'num_times' ori

# Exemple functie
# @repeat_func(num_times=8)

def repeat_func(num_times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat_func(num_times=5)
def greet(name):
    print(f'Hello {name}')

greet('Python')


# Output:
# Hello Python
# Hello Python
# Hello Python
# Hello Python
# Hello Python