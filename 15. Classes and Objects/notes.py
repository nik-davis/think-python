# ---------------- 15. Classes and Objects: Notes -------------------- #

# Class Definition
class Point:
    """Represents a point in 2-D space"""

# Instantiation: To create, call as if function
blank = Point()     # object is an instance of the class
print(blank)        # Which class and where stored in memory
print(type(blank))

# Attributes: Assign values using dot notation
blank.x = 3.0
blank.y = 4.0

x = blank.x
print(blank.y, x)

# Passing an instance as an argument
def print_point(p):
    # print('(%g, %g)' % (p.x, p.y))
    print('({0}, {1})'.format(p.x, p.y))

print_point(blank)

# As an exercise, write a function called distance_between_points that 
# takes two Points as arguments and returns the distance between them.

from math import sqrt

def distance_between_points(p1, p2):
    # sqrt (x2-x1)**2 + (y2-y1)**2
    dx = p2.x - p1.x 
    dy = p2.y - p1.y 
    res = sqrt(dx**2 + dy**2)
    return round(res, 2)

point2 = Point()
point2.x = 3.0
point2.y = 5.0

print('Distance between points:', distance_between_points(blank, point2))

# Rectangles - corner is lower-left Point object

class Rectangle:
    """Represents a rectangle.

    Attributes: width, height, corner.
    """

box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()    # Embedded: object is an attribute of another object
box.corner.x = 0.0
box.corner.y = 0.0

# Instances as return values
def find_centre(rect):
    p = Point()
    p.x = rect.corner.x + rect.width/2
    p.y = rect.corner.y + rect.height/2
    return p

centre = find_centre(box)
print_point(centre)

# Objects are mutable
#  can change state of an object by making assignment to an attribute
box.width = box.width + 50
box.height = box.height + 100

# Can write functions that modify objects
def grow_rectangle(rect, dwidth, dheight):
    rect.width += dwidth
    rect.height += dheight

print(box.width, box.height)
grow_rectangle(box, 50, 100)
print(box.width, box.height)
# Inside function, rect is an alias for box

# As an exercise, write a function named move_rectangle that takes a Rectangle 
# and two numbers named dx and dy. It should change the location of the 
# rectangle by adding dx to the x coordinate of corner and adding dy to 
# the y coordinate of corner.

def move_rectangle(rect, dx, dy):
    rect.corner.x += dx
    rect.corner.y += dy

print(box.corner.x, box.corner.y)
move_rectangle(box, 5, 10)
print(box.corner.x, box.corner.y)


# Copying
p1 = Point()
p1.x = 3.0
p1.y = 4.0

# Shallow copy
import copy
p2 = copy.copy(p1)

# Same data, not same Point
print(p1 is p2, p1 == p2)

box2 = copy.copy(box)
print(box2 is box, box2.corner is box.corner)

# Deep copy
box3 = copy.deepcopy(box)
print(box3 is box, box3.corner is box.corner)


# As an exercise, write a version of move_rectangle that creates and 
# returns a new Rectangle instead of modifying the old one.

def move_rectangle_new(rect, dx, dy):
    newrect = copy.deepcopy(rect)
    newrect.corner.x += dx
    newrect.corner.y += dy
    return newrect


# Debugging
p = Point()
p.x = 3
print(type(p), isinstance(p, Point), hasattr(p, 'x'), hasattr(p, 'z'))

try:
    x = p.x
except:
    x = 0