# takes one command-line argument, user name, and tries
# to find user's password. In this example, the search is made in from 1 to 4 digits
# all possible alphabetic ascii characters(a-z, A-Z) dictionary file is used.
# By changing the dictionary file it can be made different searches, according to need

from colorama import Fore as colors
import crypt
from sys import argv
from os import path


def main():
    if len(argv) <= 1:
        print(colors.YELLOW + "What user you want to try " \
              + "to crack the password for?" + colors.CYAN)
        username = input()
    else:
        username = argv[1]

    # get generated passwords
    """
    if path.exists('gen_passwds_4D_alpha.txt') == False:
        import passwd_gen_4D_alpha # ?????
    """

    gened_passwds_file = open('gen_passwds_4D_alpha.txt')
    # get hashed string from user_passwords.txt
    user_info_file = open('user_passwords.txt')
    user_info = user_info_file.readlines()

    pw_start_point = ":"

    for user_line in user_info:

        if username == user_line[:user_line.find(pw_start_point)]:
            pw_start = user_line.find(pw_start_point)
            hashed_pw = user_line[pw_start+1:].rstrip()

            # compare it by usin generated passwords
            while True:
                pw = gened_passwds_file.readline().rstrip()
                new_hashed = crypt.crypt(pw, hashed_pw)

                print(colors.YELLOW + "Trying password... " + colors.WHITE + pw)

                if hashed_pw == new_hashed:
                    print(colors.GREEN + "Password found!")
                    print(colors.RESET + "The password for user " + colors.CYAN + username \
                         + colors.RESET + " is " + colors.LIGHTBLUE_EX + pw)

                    # create a file with cracked password and append the result
                    with open('cracked_passwords.txt', 'a') as cracked_pws_file:
                        cracked_pws_file.write("username: " + username \
                                               + ", password: " + pw + '\n')

                    user_info_file.close()
                    gened_passwds_file.close()

                    exit(0)
                else:
                    print(colors.RED + "password failed.")

    print("the user you are looking for doesn't exist")

    user_info_file.close()
    gened_passwds_file.close()

    print("no password cracked")

    exit(1)


if __name__ == "__main__":
    main()
