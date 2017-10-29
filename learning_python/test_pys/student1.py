# import neccesery libraries
from structure1 import Student

mayk = Student("mayk", 28, "male", 12, grades=None)
josef = Student("josef", 25, "male", 14, {"math": 3.9})

print(josef.getGPA())


mayk.setGrade("math", 4.2)
mayk.setGrade("pysics", 4.7)
josef.setGrade("physics", 3.7)
print(mayk.getGrade("math"))

print(mayk.getGPA())
