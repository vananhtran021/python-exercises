class School:
    def __init__(self, name):
        self.name = name
        self.courses = []
    def add_course(self, course):
        self.courses.append(course)
        print(f"{course.course_name} has been added to {self.name}.")
class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def grade(self, course, grade):
        if course in course.students:
            print(f"{self.name} received a grade of {grade} in {course.course_name}.")
        else:
            print(f"{self.name} is not enrolled in {course.course_name}.")

