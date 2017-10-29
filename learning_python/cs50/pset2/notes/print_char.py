# first of all, define what your program will do
# than write the pseudocode for it
# and in the end, yoo may start to code

def main():
    # take user input as a string
    user_input = input("s : ")
    # check if string is got properly
    if len(user_input) == 0:
        # if not quit
        exit(1)
    # print each char in given string
    for i in user_input:
        print(i)
    return 0


if __name__ == "__main__":
    main()
