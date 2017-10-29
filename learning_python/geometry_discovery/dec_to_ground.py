# takes an integer in decimal ground, return the value of the number
# in fifth ground.
from sys import argv

def main(argv):
    if len(argv) != 3:  # check arguments
        print("Usage: dec_to_ground <number> <ground>")
    result = ''
    num = int(argv[1])
    ground = int(argv[2])
    while True:
        if num >= ground:
            result += ''.join(str(num % ground))
            num = num // ground
        else:
            # add division
            result += ''.join(str(num % ground))
            # return reversed
            return int(result[::-1])



if __name__ == "__main__":
    print(main(argv))
