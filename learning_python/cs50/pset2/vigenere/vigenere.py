# define a procedure, encode_vegenere(), that take a string
# as argument, key, which is the key that will be user to encode
# message that will be taken as user input.

import string
import sys


def encode_vigenere(key):
    # create a list to store the key
    alphabet = string.ascii_uppercase
    user_input = input('plaintext: ')

    result = ''
    n = len(alphabet)
    i = 0
    key_len = len(key)
    for char in user_input:
        if char.isalpha() == True:
            sum_char = alphabet.find(char.upper()) \
                    + alphabet.find(key[i].upper())
            # use modulo to start count from 0 again
            char_new_value = sum_char % n
            result += ''.join(alphabet[char_new_value])
        # if there is a non-alphabetic char, keep it unchanged
        elif char == ' ':
            result += ' '
        else:
            result += char
            # result += ''  # ignore non-aplhabetic chars
        i += 1
        if i >= key_len:
            i = 0

    # convert the resulting string uppercase to upper lowercase to
    # lower in respect with the given input.
    """
    res = ""
    res += "".join(result[i].upper() for i in range(len(result))) # \
                   #if user_input[i].isupper() == True else result[i])
    """

    print("ciphertext: " + result)


# ask user for key till get an input with aplhabetic chars
def check_argv(argument):
    while len(argument) != 2 or argument[1].isalpha() == False:
        argument = argument[:1]
        user_input = input('enter a valid key: ')
        argument.append(user_input)

    return encode_vigenere(argument[1])


# run check_argv() function when the script is executed
if __name__ == "__main__":
    check_argv(sys.argv)
