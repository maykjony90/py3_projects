import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("yellow")

    jony = turtle.Turtle()
    jony.shape("turtle")
    jony.color("red")

    count = 0
    while count < 4:
        jony.forward(100)
        jony.right(90)
        count += 1

    juliet = turtle.Turtle()
    juliet.shape("triangle")
    juliet.color("purple")

    juliet.circle(100)
    juliet.triangle(50)

    window.exitonclick()

draw_square()
