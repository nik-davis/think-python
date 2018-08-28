import math
import turtle

def polyline(t, n, length, angle):
    """Draws n line segments.

    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def arc(t, r, angle):
    """Draws an arc with the given radius and angle.

    t: Turtle
    r: radius
    angle: angle subtended by the arc, in degrees
    """
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n
    
    # making a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc
    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)

def draw_flower(t, petals, r, angle):
    '''Draw a turtle flower with defined number of petals
    using turtle t.
    '''
    constant = (1/petals) * 360
    for i in range(petals):
        for i in range(2):
            arc(t, r, angle)
            t.left(180-angle)
        t.left(360/petals)

def move(t, length):
    """Move Turtle (t) forward (length) units without leaving a trail.
    Leaves the pen down.
    """
    t.pu()
    t.fd(length)
    t.pd()

bob = turtle.Turtle()
bob.speed(0)

# draw a sequence of three flowers, as shown in the book.
move(bob, -100)
draw_flower(bob, 7, 60.0, 60.0)

move(bob, 100)
draw_flower(bob, 10, 40.0, 80.0)

move(bob, 100)
draw_flower(bob, 20, 140.0, 20.0)

# wait for the user to close the window
turtle.mainloop()