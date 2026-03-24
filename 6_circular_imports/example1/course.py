from student import Student

class Course:
    def __init__(self, title):
        self.title = title
        self.students = []

    def add_student(self, student: Student):
        self.students.append(student)