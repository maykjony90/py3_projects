# write bubble sort code

import random

input_list = random.sample(list(range(11)), 11)
print(input_list)


def bubble(input_list, sorted_list=[], c=0):
    # base case
    if len(input_list) == 0:
        print("{} sorted list:\t{}".format(c, sorted_list))
        return 0

    i = 1
    while i < len(input_list):
        if input_list[i-1] > input_list[i]:
            input_list[i], input_list[i-1] = input_list[i-1], input_list[i]
        i += 1
        c += 1
        print(str(c) + 'th ' + 'input list:\t' + str(input_list))

    sorted_list = [input_list.pop()] + sorted_list
    print("{} currently sorted list:\t{}".format(c, sorted_list))
    bubble(input_list, sorted_list, c)


print(bubble(input_list))
