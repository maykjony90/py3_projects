import turtle


window = turtle.Screen()
window.bgcolor('black')
euclid = turtle.Turtle()
euclid.shape('triangle')
euclid.color('orange')
euclid.speed(1)
euclid.pencolor('white')
euclid.pensize(2)

# main function
def rect_func(euclid, total):
    size = total // 4
    for i in range(1, size+1):
        width = lengths(i)
        length = 80 - width
        draw_rect(euclid, width, length)

    # window.exitonclick()

# the function in given problem khan academy
def lengths(i):
    return -i * (i - 80)


def draw_rect(turt, width, length):
    for i in range(0, 2):
        turt.forward(width)
        turt.right(90)
        turt.forward(length)
        turt.right(90)


    # window.exitonclick()


def draw_triangle():
    window = turtle.Screen()
    window.bgcolor('black')
    euclid = turtle.Turtle()
    euclid.shape('triangle')
    euclid.color('orange')
    euclid.speed(10)
    euclid.pencolor('white')
    euclid.pensize(2)

    euclid.right(90)
    euclid.forward(300)
    euclid.left(90)
    euclid.forward(400)
    euclid.left(143)
    euclid.forward(525)

    window.exitonclick()

