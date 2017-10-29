# structure dosyasindan Student yapisini(kavramini)
# yukluyorum. Boylece ogrenci kavrami bu baglamda
# bilinen bir kavram haline geliyor.
from structure import Student

# ogrenci kayitlarini tutmak icin bir liste olusturuyorum
students = []

# kullanicidan kac tane kayit alcagimi belirliyorum
for i in range(2):
    name = input("name: ")
    dorm = input("dorm: ")
    favorite_class = input("favorite class: ")

    # create a variable which will cary subject with its attributes
    s = Student(name, dorm, favorite_class)
    students.append(s)


# print out all information in students list
for student in students:
    print("{} lives in {} and likes {}".format(student.name,
                                               student.dorm,
                                               student.favorite_class))
