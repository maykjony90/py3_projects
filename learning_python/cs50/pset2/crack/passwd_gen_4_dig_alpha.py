import string
from os import path


whole_range = string.ascii_letters

dict_file = open('gen_passwds_4D_alpha.txt', 'w')

# add \0 to end of each password
suffix = '\n'
# one digit possible passwords
for i in whole_range:
    dict_file.write(i + suffix)

# two digit possible passwords
double = []
for i in whole_range:
    for e in range(len(whole_range)):
        double.append(i + whole_range[e])

for pw in double:
    dict_file.write(pw + suffix)

# three digit possible passwords
triple = []
for i in double:
    for e in whole_range:
        triple.append(i + e)

for pw in triple:
    dict_file.write(pw + suffix)

# four digit possible passwords
quad = []
for i in triple:
    for e in whole_range:
        quad.append(i + e)

for pw in quad:
    dict_file.write(pw + suffix)

dict_file.close()
