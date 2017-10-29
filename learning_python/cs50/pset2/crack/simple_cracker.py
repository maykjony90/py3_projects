# generate password accordin to given digit
# define procedure, passwd_generator, that takes as its input
# an integer, up to which starting from 1 will contain all possible
# combinations with [a-z, A-Z] characters

from sys import argv
import string
from os import path


def main():

    digit = arg_checker(argv)

    # create a string with ascii chars
    search_range = string.ascii_letters
    # check if a core dict file exist
    seed_dict = check_core_list(digit)

    if seed_dict == None:
        new_core = generate_dict_file(digit)

    current_file = open("digit_" + str(digit) + "_alpha.txt", 'a')

    while True:
        line = seed_dict.readline().rstrip()
        if line == '':
            break

        current_file.write(i + e + '\n')

    current_file.close()

    print("password generation is done...")
    exit(0)


def arg_checker(argv):
    # get arguments
    if len(argv) <= 1:
        digit = 0
        while digit > 4 or digit < 1:
            digit = input("enter the # of digits(1-4): ")
            digit = int(digit)
        argv.append(digit)
    elif argv[1] > 4 or argv[1] < 1:
        while digit > 4 or digit < 1:
            digit = input("enter the # of digits(1-4): ")
            digit = int(digit)
    else:
        digit = argv[1]

    return digit


def check_core_list(digit):
    alpha = 'alpha'
    dict_path = "./digit_" + str(digit-1) + '_' + alpha + '.txt'
    if path.exists(dict_path):
        seed_dict = open(dict_path)
        return seed_dict
    else:
        return generate_dict_file(digit)


def generate_dict_file(digit):
    return 0


if __name__ == "__main__":
    main()
