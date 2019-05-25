#!/usr/bin/env python3
# Figure 11-9: Sierpinski Triangle Program (continued)
import turtle
import math

def createTriangleShape(coords):
    """Creates turtle shapt from coords. Registers as 'my_triangle'."""
    turtle.penup()
    turtle.begin_poly()
    turtle.setposition(coords[0])
    turtle.setposition(coords[1])
    turtle.setposition(coords[2])
    turtle.setposition(coords[0])
    turtle.end_poly()

    tri_shape = turtle.get_poly()
    turtle.register_shape('my_triangle', tri_shape)


def triangleHeight(side):
    """Returns height of equilatiral triangle with length side."""
    return math.sqrt(3) / 2 * side


def getLeftTrianglePosition(position, side):
    """Returns position of bottom left triangle in larger triangle.

       Returns (x,y) positions for provided position and side length of
       larger triangle to be placed within.
    """
    return (position[0] - side / 4,
            position[1] - triangleHeight(side) / 4)


def getRightTrianglePosition(position, side):
    """Returns position of bottom right triangle in larger triangle.

       Returns (x,y) position for provided position and side length of larger
       triangle to be placed within.
    """
    return (position[0] + side / 4,
            position[1] - triangleHeight(side) / 4)


def getTopTrainglePosition(position, side):
    """Returns x,y position of top triangle within larger one.

       For triangle at position, with length side.
    """
    return (position[0], position[1] + triangleHeight(side) / 4)

def drawSierpinksiTriangle(t, len_side, levels):
    """Recursive function that draws a Sierpinski triangle.

       Draws the number of levels of triangle given in levels.
    """
    if levels == 0:
        t.color('back')
        t.showturtle()
        t.stamp()

        # return  ###??? error in book here

    # resize triangle to half its size
    stretch_width, stretch_length, outline = t.turtlesize()
    t.turtlesize(0.5 * stretch_width, 0.5 * stretch_length, outline)

## TODO: Finish typing this out, and then do some tests to make sure the return
##       statement is intended.

