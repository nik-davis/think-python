import turtle
from math import pi

def draw_square(t, length):
    '''Draw a square with turtle t with defined side length'''
    for i in range(4):
        t.fd(length)
        t.rt(90)

def draw_poly(t, length, n):
    '''Draw an n-sided polygon with turtle t'''
    for i in range(n):
        t.fd(length)
        t.rt(360/n)

def draw_circle(t, r):
    '''Draw a circle of radius r with turtle t'''
    circumference = 2 * pi * r
    n = int(circumference / 3) + 3
    length = circumference / n
    draw_poly(t, length, n)

def draw_arc(t, r, angle):
    '''Draw an arc based on angle of radius r using turtle t'''
    circumference = 2 * 3.14 * r
    n = 360
    length = circumference / n
    for i in range(angle):
        t.fd(length)
        t.rt(360/n)

bob = turtle.Turtle()
print(bob)

radius = 50
bob.fd(radius)
bob.bk(radius)

#draw_arc(bob, r=radius, angle=360)
draw_circle(bob, r=radius)

turtle.mainloop()