import turtle

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length*n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2*angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length*n)

bob = turtle.Turtle()
bob.speed(0)

bob.pu()
bob.lt(90)
bob.bk(200)
bob.pd()

draw(bob, 20, 5)

turtle.mainloop()