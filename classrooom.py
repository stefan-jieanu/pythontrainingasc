# Clasa de baza: Parent (Parinte)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def who_am_i(self):
        print(f'Salut! Eu sunt {self.name} si am {self.age} ani.')

    def __str__(self):
        # type(self) - ne va returna tipul obiectului care apeleaza functia
        # __name__ este un string cu numele clasei
        return f'{self.name} are {self.age} ani - {type(self).__name__}'

# Clasa copil (Child)
# Clasa Employee 'mosteneste' toate proprietatile clasei Person
class Employee(Person):
    def __init__(self, name, age, rate, working_hours):
        Person.__init__(self, name, age)
        self.rate = rate
        self.working_hours = working_hours

    def show_finance(self):
        return self.rate * self.working_hours

    def who_am_i(self):
        # In acest caz apelam metoda originala
        # Person.who_am_i(self)
        # sau folosind cuvantul 'super()' care face referire la clasa de baza
        super().who_am_i()

        # Dupa care completam functia cu cod in plus
        print(f'Si fac {self.show_finance()}')


class Student(Person):
    def __init__(self, name, age, scholarship):
        Person.__init__(self, name, age)
        self.scholarship = scholarship

    def show_finance(self):
        return self.scholarship

# Mostenire-multiple (Multiple Inheritance)
# IMPORTANT! MRO(Method Resolution Order) in python de tinut cont in cazul asta
class WorkingStudent(Employee, Student):
    def __init__(self, name, age, rate, working_hours, scholarship):
        Employee.__init__(self, name, age, rate, working_hours)
        Student.__init__(self, name, age, scholarship)

    # Override (Suprascrierea) unei functii
    # Redefinim functia din clasa de baza cu exact aceeasi parametrii si return type
    # Codul din noua functie il va inlocui pe cel vechi
    # def show_finance(self):
    #     return self.rate * self.working_hours + self.scholarship
    
    # SAU
    def show_finance(self):
        return Employee.show_finance(self) + Student.show_finance(self)


p1 = Person('Alex', 20)
p2 = Person('Maria', 25)

p1.who_am_i()
print(p2)

e1 = Employee('Mircea', 30, 100, 8)

e1.who_am_i()
# print(e1.show_finance())

s1 = Student('Tomy', 18, 1000)
print(s1)
print(s1.show_finance())

ws1 = WorkingStudent('Ion', 33, 10, 4, 500)
ws1.who_am_i()
# print(ws1.show_finance())

print('\n\n')
# Polymorphism - functionalitate comuna intre mai multe obiecte
def check_finance(obj):
    # Varianta directa care poate da eroare daca obj nu este tipul bun
    # print(f'Finantele sunt: {obj.show_finance()}')

    # Optional putem scrie un try/except pentru a prinde o posibila AttributeError
    try:
        print(f'Finantele sunt: {obj.show_finance()}')
    except AttributeError:
        print('obj nu are functia show_finance()')

check_finance(e1)
check_finance(s1)
check_finance(ws1)
check_finance(10) # -> Eroare! int nu are func show_finance()