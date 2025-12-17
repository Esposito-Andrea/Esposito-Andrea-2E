import turtle
screen = turtle.Screen()


screen.setup(width=1000, height=670)
screen.title("Quadrato")
drawing = turtle.Turtle()
drawing.speed(1)

def disegno(x, y, color, pixel_size):
    drawing.penup()
    drawing.goto(x, y)
    drawing.pendown()
    drawing.fillcolor(color)
    drawing.begin_fill()
    for b in range(4):
        drawing.forward(pixel_size)
        drawing.right(90)
    drawing.end_fill()


disegno(-100, 100, "purple", 150)