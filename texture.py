import turtle
import random
import math

screen = turtle.Screen()
screen.setup(width=1200, height=800)
screen.title("ESAGONO")
screen.colormode(255)

R = 30
G = 158
B = 175
screen.bgcolor(R, G, B)

drawing = turtle.Turtle()
drawing.speed(0)


def disegno(x, y, color, pixel_size):
    drawing.penup()
    drawing.goto(x, y)
    drawing.pendown()
    drawing.fillcolor(color)
    drawing.begin_fill()
    for b in range(6):
        drawing.forward(pixel_size)
        drawing.right(60)
    drawing.end_fill()

pixel_size = 40
colonne = 14
righe = 8


spazio_x = pixel_size * math.sqrt(3)
spazio_y = pixel_size * 1.5


for r in range(righe):
    for c in range(colonne):

        x = -550 + c * spazio_x
        y = 350 - r * spazio_y

        
        if r % 2 == 1:
            x += spazio_x / 2

        colore = (
            random.randint(100, 255),
            random.randint(100, 255),
            random.randint(100, 255)
        )

        disegno(x, y, colore, pixel_size)

turtle.done()
