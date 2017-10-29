import turtle


def draw_circle_from_square():
    window = turtle.Screen()
    window.bgcolor("red")
    
    jony = turtle.Turtle()
    jony.shape("turtle")
    jony.color("white")
    jony.speed(10)
    jony.pencolor("pink")
    jony.pensize(2)

    pencolors = [1, 1, 1]
    count = 0
    for_square = 0
    while count < 36:
        jony.right(10)
        jony.pencolor(pencolors)
        while for_square < 4:
            jony.forward(100)
            jony.right(90)
            for_square += 1
        count += 1
        for_square = 0


    window.exitonclick()
    
