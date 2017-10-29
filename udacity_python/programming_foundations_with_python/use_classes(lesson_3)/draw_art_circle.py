import turtle
import random

def draw_art_circle():
    window = turtle.Screen()
    window.bgcolor('white')
    
    jony = turtle.Turtle()
    jony.shape('arrow')
    jony.speed(20)
    window.colormode(255)

    
    a = 1
    for i in range(200):
        draw_circle(jony, i, a)

    window.exitonclick()

def draw_art_square():
    window = turtle.Screen()
    window.bgcolor('white')
    
    jony = turtle.Turtle()
    jony.shape('arrow')
    jony.speed(30)
    window.colormode(255)

    for c in range(20, 200, 10): 
        for i in range(36):
            draw_square(jony, c)
            jony.right(10)
        jony.right(60)
        jony.forward(c * 3)

    window.exitonclick()

def draw_circle(t, size, angle):
    t.color(random_RGB())
    t.circle(size)
    t.right(angle)

def random_RGB():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return r, g, b

def draw_square(t, size):
    t.color(random_RGB())
    for i in range(4):
        t.forward(size)
        t.right(90)
