import sqlite3
from patients import Patient


# # create an object associated with the connected database
# connection = sqlite3.connect('patients.db')


# create an object associated with the connected database
connection = sqlite3.connect(':memory:')


# create a cursur with cursor() method 
cursor = connection.cursor()

# create a database
cursor.execute("""
	CREATE TABLE patients (
	first text,	last text,
	grafts integer)
	""")


# print(pat_1.first)
# print(pat_1.last)
# print(pat_1.grafts)

def insert_patients(patient):
	with connection:
		cursor.execute("INSERT INTO patients VALUES (:first, :last, :grafts)", 
			{'first':patient.first, 'last':patient.last, 'grafts':patient.grafts})


def get_patient_by_name(lastname):
	cursor.execute("SELECT * FROM patients WHERE last=:last", {'last':lastname})
	return cursor.fetchall()


def update_grafts(patient, graft):
	with connection:
		cursor.execute("""UPDATE patients SET grafts=:grafts
			WHERE first=:name AND last=:last""",
			{'name': patient.first, 'last': patient.last, 'grafts': graft})


def remove_patient(patient):
	with connection:
		cursor.execute("""DELETE FROM patients WHERE first=:name AND last=:last""",
			{'name': patient.first, 'last': patient.last})


# create a patient object
pat_1 = Patient('Josef', 'Smith', 2600)
pat_2 = Patient('Jane', 'Smith', 1900)
pat_3 = Patient('Mayk', 'Jony', 1500)


# insert a new patient
insert_patients(pat_1)
insert_patients(pat_2)
insert_patients(pat_3)

# get patient by name
paciente = get_patient_by_name('Jony')
print(paciente)


# update an information
update_grafts(pat_1, 3200)

# remove an information
remove_patient(pat_2)

# get patient by name
paciente = get_patient_by_name('Smith')
print(paciente)





# cursor.execute("INSERT INTO patients VALUES (?, ?, ?)", (pat_1.first, pat_1.last, pat_1.grafts))
# # save(commit())
# connection.commit()
# # Insert a new data for database
# cursor.execute("INSERT INTO patients VALUES ('Mayk', 'Jony', 2100)")
# # save(commit())
# connection.commit()

# cursor.execute("INSERT INTO patients VALUES (:first, :last, :grafts)", {'first':pat_2.first, 'last':pat_2.last, 'grafts':pat_2.grafts})


# save(commit())
connection.commit()

# # Select data from database
# cursor.execute("SELECT * FROM patients WHERE last='Jony'")


# cursor.execute("SELECT * FROM patients WHERE last=:last", {'last':'Smith'})
# # print only one output
# print(cursor.fetchone())


# # print all data
# print(cursor.fetchmany(4))

# print all data
# print(cursor.fetchall())

# # save(commit())
# connection.commit()

# close the database
connection.close()
