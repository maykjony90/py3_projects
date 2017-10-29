# python class is used to create an idea with some
# specifications. And you can use it for different
# subjects. Demem o ki, bir kavram olusturmak icin
# kullaniliyor. Bu kavrami olusturduktan sonra onu,
# farkli ozneler icin kullanabilirsin. Mesela:
# Ogrenci kavraminin bazi ozelliklerini dusunelim:
# ismi, sinifi, yasi, memleketi vb.  Bu ve benzeri
# ozellikler bir kavrama ait olup, farkli ozneleri
# tanimlamak icin kullanilabilir.
# Ornek:
# name = Ali                mehmet
# sinifi = 5                8
# yasi = 11                 14
# memleketi = Osmaniye      Luleburgaz

# Ogrenci kavramini(yapisini) yaratiyoruz
# Bu artik bizim icin bir kavrama donusuyor
class Student:
    # bu yapi cagirildiginda calistirilmasi icin
    # bir fonksiyon yaziyoruz. Ogrenci kavramamiz cagirildigi
    # zaman otomatik olarak butun ozellikleri tasiyan bir
    # kavramdan bahsediyor olacagiz.
    def __init__(self, name, dorm, favorite_class):
        # parametrelerin, kavramda hangi atifa karsilik
        # geldigini belirliyoruz.
        self.name = name
        self.dorm = dorm
        self.favorite_class = favorite_class


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

    def getGPA(self):
        return sum(self.grades.values())/len(self.grades))

