"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
"""

from turtle import *
from freegames import vector
import math


def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()

    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def draw_circle(start, end):
    """Draw circle from start to end."""

    radius = math.sqrt(
        (end.x - start.x) ** 2 +
        (end.y - start.y) ** 2
    )

    up()
    goto(start.x, start.y - radius)
    down()

    begin_fill()

    for _ in range(36):
        forward(2 * math.pi * radius / 36)
        left(10)

    end_fill()


def rectangle(start, end):
    """Draw rectangle from start to end."""

    width = end.x - start.x
    height = end.y - start.y

    up()
    goto(start.x, start.y)
    down()

    begin_fill()

    forward(width)
    left(90)

    forward(height)
    left(90)

    forward(width)
    left(90)

    forward(height)
    left(90)

    end_fill()


def triangle(start, end):
    """Draw triangle from start to end."""

    side = end.x - start.x

    up()
    goto(start.x, start.y)
    down()

    begin_fill()

    for count in range(3):
        forward(side)
        left(120)

    end_fill()


def tap(x, y):
    """Store starting point or draw shape."""

    start = state['start']

    if start is None:
        state['start'] = vector(x, y)

    else:
        shape = state['shape']
        end = vector(x, y)

        shape(start, end)

        state['start'] = None


def store(key, value):
    """Store value in state at key."""

    state[key] = value


state = {'start': None, 'shape': line}

setup(420, 420, 370, 0)

onscreenclick(tap)

listen()

onkey(undo, 'u')

# Colors
onkey(lambda: color('purple'), 'p')
onkey(lambda: color('black'), 'k')
onkey(lambda: color('white'), 'w')
onkey(lambda: color('green'), 'g')
onkey(lambda: color('blue'), 'b')
onkey(lambda: color('red'), 'R')

# Shapes
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', draw_circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')

done()
