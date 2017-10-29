import turtle

def draw_flower_from_triangle():
    window = turtle.Screen()
    window.bgcolor("yellow")


    jony = turtle.Turtle()
    jony.shape('turtle')
    jony.color('blue')
    jony.speed(5)

    for i in range(0,36):
        draw_triangle(jony)


    window.exitonclick()

def draw_triangle(some_turtle):
    for i in range(0,3):
        some_turtle.forward(100)
        some_turtle.right(120)
    some_turtle.right(10)


