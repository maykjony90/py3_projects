from colorama import Fore as colors
from os import getuid
from crypt import crypt
from sys import argv
from spwd import getspnam


def main():
    if getuid() != 0:
        print(colors.YELLOW + "you have to be root to run this utility!")
        exit(1)

    if len(argv) <= 1:
        print(colors.YELLOW + "What user you want to try " \
              + "to crack the password for?" + colors.CYAN)
        username = input()
    else:
        username = argv[1]

    dict_file = open('johnTheRipper.txt')
    encrypted_passwd = getspnam(username)[1]

    print(colors.YELLOW + "Cracking UNIX password for user... " \
          + colors.CYAN + username)
    print(colors.YELLOW + "Encrypted password is: " \
          + colors.CYAN + encrypted_passwd)

    for password in dict_file.readlines():
        password = password.rstrip()
        new_passwd = crypt(password, encrypted_passwd)
        print(colors.YELLOW + "Trying password... " + colors.WHITE + password)

        if encrypted_passwd == new_passwd:
            print(colors.GREEN + "Password found!")
            print(colors.RESET + "The password for user " + colors.CYAN + username \
                  + colors.RESET + " is " + colors.LIGHTBLUE_EX + password)
            dict_file.close()
            exit(0)
        else:
            print(colors.RED + "password failed.")

    dict_file.close()
    print(colors.YELLOW + "no password cracked. Try another dictionary file.")
    exit(1)

if __name__ == "__main__":
    main()
