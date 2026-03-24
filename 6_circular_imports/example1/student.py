from course import Course

class Student:
    def __init__(self, name):
        self.name = name
        self.courses = []

    def enroll(self, course: Course):
        self.courses.append(course)
        course.add_student(self)