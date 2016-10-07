from turtle import *
import math

def init():
    hideturtle()
    delay(1)

def draw_line(x0, y0, length, angle):
    penup()
    goto(x0, y0)
    setheading(math.degrees(angle))
    pendown()
    forward(length)

def draw_curve(x, y, depth, length, angle, odd=True):
    if depth == 1:
        draw_line(x, y, length, angle)
    else:
        angle += math.radians(-45 if odd else 45)
        length /= pow(2, 1/2)
        draw_curve(x, y, depth-1, length, angle, False)
        x += length*math.cos(angle)
        y += length*math.sin(angle)
        angle += math.radians(90 if odd else -90)
        draw_curve(x, y, depth-1, length, angle, True)


if __name__ == '__main__':
    init()
    color('black', 'white')
    begin_fill()
    draw_curve(0, 0, 8, 256, 0)
