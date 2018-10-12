# --------------- 15. Classes and Objects: Exercises ------------------- #


# 15.1. Write a definition for a class named Circle with attributes center
# and radius, where center is a Point object and radius is a number.
#
# Instantiate a Circle object that represents a circle with its center
# at (150, 100) and radius 75.
#
# Write a function named point_in_circle that takes a Circle and a Point
# and returns True if the Point lies in or on the boundary of the circle.
#
# Write a function named rect_in_circle that takes a Circle and a Rectangle
# and returns True if the Rectangle lies entirely in or on the boundary
# of the circle
#
# Write a function named rect_circle_overlap that takes a Circle and a
# Rectangle and returns True if any of the corners of the Rectangle fall
# inside the circle. Or as a more challenging version, return True if any
# part of the Rectangle falls inside the circle.


class Point:
    """Represents a point in 2-D space."""


class Rectangle:
    """Represents a rectangle.

    Attributes: width, height, corner.
    """


class Circle:
    """Represents a circle.

    Attributes: center, radius.
    """


ring = Circle()
ring.radius = 75.0
ring.center = Point()
ring.center.x = 150.0
ring.center.y = 100.0


def point_in_circle(c, p):
    """Checks if a point lies within, or on the boundary of, a circle.

    c: Circle
    p: Point
    """
    if p.x <= c.center.x + c.radius and p.x >= c.center.x - c.radius:
        if p.y <= c.center.y + c.radius and p.y >= c.center.y - c.radius:
            return True
    return False


dot = Point()
dot.x = 170
dot.y = 90

print('point_in_circle:', point_in_circle(ring, dot))

dot2 = Point()
dot.x = 75.0
dot.y = 25.0

print('point_in_circle:', point_in_circle(ring, dot))


def rect_in_circle(r, c):
    """Checks if a rectangle lies entirely within, or on the boundary of,
    a circle.

    r: Rectangle
    c: Circle
    """
    # Use point_in_circle to check
    p = r.corner
    if not point_in_circle(c, p):
        return False
    p.x = p.x + box.width
    if not point_in_circle(c, p):
        return False
    p.y = p.y + box.height
    if not point_in_circle(c, p):
        return False
    p.x = p.x - box.width
    if not point_in_circle(c, p):
        return False
    return True


box = Rectangle()
box.height = 10.0
box.width = 10.0
box.corner = Point()
box.corner.x = 150.0
box.corner.y = 100.0

print('rect_in_circle:', rect_in_circle(box, ring))