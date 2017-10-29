from sys import argv
import random


def main(argv):

    # ensure proper usage
    if len(argv) != 2:
        print("Usage: fifteen <dimension>")
        return 1


    dim_min = 3
    dim_max = 9

    d = argv[1]
    if d < dim_min or d > dim_max:
        print(" board must be between {0} x {1} and {2} x {3}" \
              + " , inclusive.".format(dim_min, dim_min, dim_max, dim_max))
        return 2

    log_file = open('log.txt', 'w')

    greet()

    init()

    while True:
        # clear the screen
        clear()

        # draw the current state of the board
        draw(d)

        # log the current state of the board (for testing)
        for i in range(d):
            for j in range(d):


# clear screen
def clear():

def greet():
    clear()
    print("welcome to game of fifteen!")
    # sleep


import random
# initilize the game board with tiles
def init(d):
    input_tile = random.sample(list(range(d*d-1)), d*d-1)
    board = " "
    board += " ".join(str(i) if i%d != 0 else str(i)+'\n' \
                      for i in input_tile)
    board += "".join(" ")
    return board

print(init(3))



# prints the board in its current state
def draw(d):

    board = " "
    board += " ".join(str(i) if i%d != 0 else str(i)+'\n' \
                      for i in range(1, d*d+1))
    log_file = open('log.txt', 'w')
    log_file.write(board)
    log_file.close()

    return board


# if tile borders emprty space, moves tile and returns true
# else returns false
def move(tile):

    return False

# returns true if game is won(i.e., board is in winning configuration)
def won():
    return False


if __name__ = "__main__":
    main()
