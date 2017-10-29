class Student(object):
    def __init__(self, name, age, gender, level, grades=None):
        self.name = name
        self.age = age
        self.gender = gender
        self.level = level
        self.grades = grades or {}

    # grades is a dictionary with course and grade value, key pair.
    def setGrade(self, course, grade):
        self.grades[course] = grade

    # return grade of given course
    def getGrade(self, course):
        return self.grades[course]

    # calculate and return GPA of a given student
    def getGPA(self):
        return sum(self.grades.values())/len(self.grades)
