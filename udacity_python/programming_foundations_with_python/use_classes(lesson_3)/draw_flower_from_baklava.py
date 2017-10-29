import turtle

def draw_flower_from_baklava():
    window = turtle.Screen()
    window.bgcolor("yellow")
    
    jony = turtle.Turtle()
    jony.shape('turtle')
    jony.color('blue')
    jony.speed(20)
    
    for i in range(36):
        draw_baklava(jony)

    #jony.right(90)
    #jony.forward(100)
    #jony.left(90)
    
    for i in range(36):
        draw_circle(jony)
        jony.right(10)

    for i in range(12):
        draw_triangle(jony)
        jony.right(30)


    for i in range(18):
        draw_square(jony)
        jony.right(20)
        
    window.exitonclick()

def draw_baklava(some_turtle):
    some_turtle.right(10)
    for i in range(0,2):
        some_turtle.forward(50)
        some_turtle.right(30)
        some_turtle.forward(50)
        some_turtle.right(150)


def draw_circle(some_turtle):
    some_turtle.speed(20)
    some_turtle.color('white')
    some_turtle.circle(70)

def draw_triangle(s):
    s.speed(20)
    s.color('red')
    for i in range(3):
        s.forward(160)
        s.left(120)

def draw_square(s):
    s.color('green')
    for i in range(4):
        s.forward(200)
        s.right(90)
        
    

    
