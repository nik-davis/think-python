import turtle
import math

def move(t, length):
    '''
    '''
    t.pu()
    t.fd(length)
    t.pd()
    
def pie(t, s):

    '''draw pie with s number of slices using t turtle
    '''
    # radians = degrees / 180.0 * math.pi
    angle_a = 360 / s
    angle_a_rad = angle_a / 180 * math.pi
    angle_b = (180 - angle_a) / 2 #180 / s + 90
    angle_b_rad = angle_b / 180 * math.pi

    length = 100
    length_a = (length / math.sin(angle_b_rad)) * math.sin(angle_a_rad)

    t.right(angle_a / 2)
    
    for i in range(s):
        t.fd(length)
        t.left(180 - angle_b)
        t.fd(length_a)
        t.left(180 - angle_b)
        t.fd(length)
        t.left(180 - angle_a * 2)
    
    t.left(angle_a / 2)

bob = turtle.Turtle()

pie(bob, 5)
move(bob, 200)

pie(bob, 6)
move(bob, -400)

pie(bob, 7)

turtle.mainloop()