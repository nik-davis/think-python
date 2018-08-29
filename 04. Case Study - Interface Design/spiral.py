import turtle


def draw_spiral(t, n, length=3, a=0.05, b=0.0003):
    """Draws an Archimedian spiral starting at the origin.

    Args:
      n: how many line segments to draw
      length: how long each segment is
      a: how loose the initial spiral starts out (larger is looser)
      b: how loosly coiled the spiral is (larger is looser)

    http://en.wikipedia.org/wiki/Spiral
    """
    theta = 0.0

    for i in range(n):
        t.fd(length)
        dtheta = 1 / (a + b * theta)

        t.lt(dtheta)
        theta += dtheta
        print(theta)


# create the world and bob
bob = turtle.Turtle()
draw_spiral(bob, n=1000)

turtle.mainloop()
