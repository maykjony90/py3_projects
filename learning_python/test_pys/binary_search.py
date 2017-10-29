def binary_search(searched_num, scope, count=1):


    if scope[0] > searched_num or searched_num > scope[-1]:
        print("searched number must be in scope")
        return 1


    if searched_num == scope[len(scope)//2]:
        print(count)
        return 0
    elif searched_num < scope[len(scope)//2]:
        count = count + 1
        scope = scope[:len(scope)//2]
        binary_search(searched_num, scope, count)

    elif searched_num > scope[len(scope)//2]:
        count = count + 1
        scope = scope[len(scope)//2+1:]
        binary_search(searched_num, scope, count)
    else:
        return "not found"



scope = list(range(1, 100))
print(binary_search(3, scope))



