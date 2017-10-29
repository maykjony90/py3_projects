from student_teacher_info_turkey import population


turkey = population(17000000, 950000, 60000000)

total_pop = turkey.students + turkey.teachers + turkey.other

ratio_of_students = turkey.students / total_pop
ratio_of_teachers = turkey.teachers / total_pop


print("ratio of students in turkey: %.5f"%ratio_of_students)
print("ratio of teachers in turkey: %.5f"%ratio_of_teachers)


each_student = total_pop / turkey.students
each_teacher = total_pop / turkey.teachers

print("1 of %.2f people is student in Turkey."%each_student)
print("1 of %.2f people is teacher in Turkey."%each_teacher)
print("Ogrenci basina dusen ogretmen sayisi: %.2f"%(each_teacher/each_student))
