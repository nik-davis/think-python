import turtle
import math

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

def skip(t, s):
    t.pu()
    t.fd(s)
    t.pd()

def draw_a(t, s):
    t.left(90)
    t.fd(100)
    t.rt(90)
    t.fd(25)
    t.rt(90)
    t.fd(50)
    t.rt(90)
    t.fd(25)
    t.bk(25)
    t.lt(90)
    t.fd(50)
    t.lt(90)

def draw_b(t, s):
    arc(t, 25, 180)
    t.lt(180)
    arc(t, 25, 180)
    t.lt(90)
    t.fd(100)
    t.lt(90)
    
    t.pu()
    t.fd(25)
    t.pd()

def draw_c(t, s):
    t.pu()
    t.fd(50)
    t.lt(90)
    t.fd(100)
    t.lt(90)
    t.pd()

    arc(t, 50, 180)

def draw_d(t,s):
    arc(t, 50, 180)
    t.lt(90)
    t.fd(100)
    t.lt(90)

    t.pu()
    t.fd(50)
    t.pd()
    



if __name__ == '__main__':
    bob = turtle.Turtle()
    draw_c(bob, 1)

    turtle.mainloop()