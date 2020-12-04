import turtle as t
from itertools import cycle

colors = cycle(['yellow', 'green', 'blue', 'purple'])

def draw_circle(size, angle, shift):
    t.pencolor(next(colors))
    t.circle(size)
    t.right(angle)
    t.forward(shift)
    #ending condition: size of cirle < 120
    if size < 120:
        draw_circle(size+5, angle + 2, shift + 3)

t.bgcolor('black')
t.speed('fast')
t.pensize(4)

draw_circle(30, 0, 1)
