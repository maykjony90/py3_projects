# define procedure, initials, that takes one string as its argument
# and returns initials of the given argument in uppercase.


def initials(name):
    # get name and split it from whitespaces, then take first letter
    # by indexing, convert it to uppercase, and store the value
    # in a list name_inits
    name_inits = [i[0].upper() for i in name.split(" ")]

    # either convert it into a string and store the result
    # in a variable or...
    # result = ''.join(init for init in name_inits)
    # return it directly(gelisine yapistir!)
    return ''.join(i for i in name_inits)


print(initials('mayk jony'))
