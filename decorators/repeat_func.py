# Implementati decoratorul @repeat_func(num_times) care va repeta functia decorata de 'num_times' ori

def repeat_func(num_times):
    def inner(func):
        def wrapper(name):
            times = num_times or 1
            for _ in range(times):
                func(name)

        return wrapper
    return inner


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