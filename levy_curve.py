from turtle import *
import math

def init():
    hideturtle()
    color('black', 'white')
    begin_fill()
    delay(1)

def draw_line(x0, y0, length, angle):
    penup()
    goto(x0, y0)
    setheading(math.degrees(angle))
    pendown()
    forward(length)

def draw_curve(x, y, depth, length, angle):
    if depth == 1:
        draw_line(x, y, length, angle)
    else:
        angle += math.radians(45)
        length /= pow(2, 1/2)
        draw_curve(x, y, depth-1, length, angle)
        x += length*math.cos(angle)
        y += length*math.sin(angle)
        angle += math.radians(-90)
        draw_curve(x, y, depth-1, length, angle)


if __name__ == '__main__':
    init()
    draw_curve(0, 0, 12, 256, 0)
