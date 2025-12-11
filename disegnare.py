import turtle
screen = turtle.Screen()


screen.setup(width=1000, height=670)
screen.title("Prugna>Waiz")
shutup_chicken = turtle.Turtle()
shutup_chicken.speed(1)

def charliekirk(x, y, color, pixel size):
    shutup_chicken.penup()
    shutup_chicken.goto(x, y)
    shutup_chicken.pendown()
    shutup_chicken.fillcolor(color)
    shutup_chicken.begin_fill()
    for b in range(4):
        shutup_chicken.forward(pixel_size)