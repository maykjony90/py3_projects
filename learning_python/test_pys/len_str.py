from sys import argv


def main(string):
    n = 0
    for i in string:
        n += 1

    print(n)
    return 0

def check_argv(argv):
    if len(argv) <= 1:
        argv.append('')
        while argv[1] == '':
            user_input = input("enter a string: ")
            argv[1] = user_input
        main(user_input)
    else:
        main(argv[1])




if __name__ == "__main__":
    check_argv(argv)
