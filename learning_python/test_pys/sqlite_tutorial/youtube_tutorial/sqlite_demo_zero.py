# install libraries
import sqlite3
from patients import Patient

# create an objet of database
conn = sqlite3.connect(':memory:')
# choose cursor in database
c = conn.cursor()

# # create a table (database)
# def create_table():
# 	with conn:
# 		c.execute("""CREATE TABLE patients(
# 			first text,
# 			last text,
# 			grafts int)
# 			""")

c.execute("""CREATE TABLE patients(
	first text,
	last text,
	grafts int)
	""")

# FONKSIYONLAR

# isleme fonksiyonu
def insert_patient(patient):
	with conn:
		c.execute("INSERT INTO patients VALUES (:first, :last, :grafts)",
			{'first': patient.first, 'last': patient.last, 'grafts': patient.grafts})

# cagirma fonksiyone
def get_patient_by_name(lastname):
	c.execute("SELECT * FROM patients WHERE last=:last", {'last': lastname})
	return c.fetchall()

# guncelleme fonksiyonu
def update_grafts(patient, graft):
	with conn:
		c.execute("""UPDATE patients SET grafts=:grafts WHERE first=:first AND last=:last""",
			{'first': patient.first, 'last': patient.last, 'grafts': graft})

# silme fonksiyonu
def remove_patient(patient):
	with conn:
		c.execute("""DELETE FROM patients WHERE first=:first AND last=:last""", 
			{'first': patient.first, 'last': patient.last})

# hasta objelerini olustur
pat_1 = Patient('Mayk', 'Jony', 1500)
pat_2 = Patient('Jane', 'Smith', 2100)
pat_3 = Patient('Josef', 'Smith', 2500)




# fonksiyonlari tek tek cagir
# create_table()
# save the changes
# conn.commit()

insert_patient(pat_1)
insert_patient(pat_2)
insert_patient(pat_3)

# save the changes
conn.commit()

paciente = get_patient_by_name("Smith")
print(paciente)

update_grafts(pat_3, 1800)
# save the changes
conn.commit()

paciente = get_patient_by_name("Smith")
print(paciente)

remove_patient(pat_2)
# save the changes
conn.commit()

paciente = get_patient_by_name("Smith")
print(paciente)


# close the folder
conn.close()