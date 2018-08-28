import turtle

def koch(t, x, a):
    '''Draws a koch curve with length x and angle a.'''
    if x < 10:
        t.fd(x)
        return

    koch(t, x/3, a)
    t.lt(a)
    koch(t, x/3, a)
    t.rt(a * 2)
    koch(t, x/3, a)
    t.lt(a)
    koch(t, x/3, a)

def snowflake(t, x, a):
    '''Draws a snowflake (a triangle with a Koch curve for each side).'''
    for i in range(3):
        koch(t, x, a)
        t.rt(120)

bob = turtle.Turtle()
bob.speed(10)

bob.pu()
bob.goto(-150, 90)
bob.pd()

turtle.tracer(1, 0)

snowflake(bob, 300, 60)

turtle.update()
turtle.mainloop()