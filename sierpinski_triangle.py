from turtle import *
import math

rad3 = 3**0.5

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

def draw_triangle(x, y, length, angle):
    penup()
    goto(x+length/rad3*math.cos(angle), y+length/rad3*math.sin(angle))
    pendown()
    setheading(math.degrees(angle)-150)
    forward(length)
    right(120)
    forward(length)
    right(120)
    forward(length)

def draw_sierpinski(x, y, depth, length, angle):
    if depth == 1:
        draw_triangle(x, y, length, angle)
    else:
        # draw_sierpinski(x, y+length/rad3/2, depth-1, length/2, angle)
        # draw_sierpinski(x-length/4, y-length/rad3/4, depth-1, length/2, angle)
        # draw_sierpinski(x+length/4, y-length/rad3/4, depth-1, length/2, angle)
        for a in map(lambda x: angle+x*math.pi*2/3, range(0, 3)):
            draw_sierpinski(x+length/rad3/2*math.cos(a),
                            y+length/rad3/2*math.sin(a),
                            depth-1, length/2, a)


if __name__ == '__main__':
    init()
    length = 256
    depth = 4
    draw_sierpinski(0, 0, 5, length, math.pi/2)
