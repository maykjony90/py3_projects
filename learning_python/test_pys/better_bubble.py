import random

input_list = random.sample(list(range(10)), 10)


def bubble(input_list, c=1):
    sorted_list = []

    while input_list != []:
        e = 0
        for i in range(len(input_list)-1):
            if input_list[i] > input_list[i+1]:
                input_list[i], input_list[i+1] = input_list[i+1], input_list[i]
                e += 1
            c += 1

        if e < 1:
            print(input_list+sorted_list)
            return c

        sorted_list = [input_list.pop()] + sorted_list

    return sorted_list, c
