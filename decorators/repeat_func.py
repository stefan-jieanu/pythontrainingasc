# Implementati decoratorul @repeat_func(num_times) care va repeta functia decorata de 'num_times' ori

def repeat_func(num_times=5):
    def dec(func):
        def wrapper(*args, **kwargs):
            for i in range(0, num_times):
                func(*args, **kwargs)

        return wrapper
    return dec

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