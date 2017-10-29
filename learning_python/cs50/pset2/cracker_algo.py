# take user's password by iterating over hashed strings that
# in user_passwords.txt, take a password from generated password file,
# pass.txt, and check if it's correct by putting them in, generated password
# and hashed string, hash function and compare the result, if result is true
# indicate that password is cracked and prompt it, or return password failed.
from colorama import Fore as colors
import crypt
from sys import argv


def main():
    if len(argv) <= 1:
        print(colors.YELLOW + "What user you want to try " \
              + "to crack the password for?" + colors.CYAN)
        username = input()
    else:
        username = argv[1]

    # get generated passwords
    gened_passwds_file = open('pass.txt')
    gened_passwds = gened_passwds_file.readlines()
    # get hashed string from user_passwords.txt
    user_info_file = open('user_passwords.txt')
    user_info = user_info_file.readlines()
    # create a file with cracked passwords
    cracked_pws_file = open('cracked_passwords.txt', 'w')


    pw_start_point = ":"

    for i in user_info: # maybe i need to store in a distant var
        if username == i[:i.find(pw_start_point)]:
            pw_start = i.find(pw_start_point)
            hashed_pw = i[pw_start+1:].rstrip()

            # compare it by usin generated passwords
            for pw in gened_passwds:
                pw = pw.rstrip()
                new_hashed = crypt.crypt(pw, hashed_pw)

                print(colors.YELLOW + "Trying password... " + colors.WHITE + pw)

                if hashed_pw == new_hashed:
                    print(colors.GREEN + "Password found!")
                    print(colors.RESET + "The password for user " + colors.CYAN + username \
                         + colors.RESET + " is " + colors.LIGHTBLUE_EX + pw)

                    cracked_pws_file.write("username: " + username + "\tpassword: " + pw)

                    cracked_pws_file.close()
                    user_info_file.close()
                    gened_passwds_file.close()

                    exit(0)
                else:
                    print(colors.RED + "password failed.")

        else:
            print("the user you are looking for doesn't exist")

    cracked_pws_file.close()
    user_info_file.close()
    gened_passwds_file.close()

    print("no password cracked")

    exit(1)


if __name__ == "__main__":
    main()
