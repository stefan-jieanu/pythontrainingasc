# Implementati decoratorul no_bad_words(to_exclude) care nu va rula functia daca parametrul ei nu contine cuvantul to_exclude
# Exemplu functie

def no_bad_words(to_exclude):
    def dec(func):
        def wrapper(*args, **kwargs):
            if to_exclude not in args[0]:
                func(*args, **kwargs)

        return wrapper

    return dec

@no_bad_words('sad')
def greet_world(msg):
    print(f"{msg}")

greet_world("Hello happy world!")
greet_world("It's raining, sad world...")
greet_world("It's sunny, hello wonderful world")

# Output
# Hello happy world!
# It's sunny, hello wonderful world