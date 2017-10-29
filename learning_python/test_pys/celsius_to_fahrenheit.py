# import necessary libraries
from sys import argv


# main function
def main(target):
    # convert Celsius into Fahrenheit
    fahrenheit = target*1.8+32
    print(fahrenheit)
    exit(0)


# principle condition
if __name__ == "__main__":
    # secondary condition
    if len(argv) != 2:
        target = float(input("give degree in Celsius: "))
        main(target)

    main(float(argv[1]))
