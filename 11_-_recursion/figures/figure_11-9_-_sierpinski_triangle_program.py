#!/usr/bin/env python3
# Sierpinski Triangle Program

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
    return (position[0] - side / 4, \
            position[1] - triangleHeight(side) / 4)


#### TODO: Finish typing this out... figure is on p 468.

