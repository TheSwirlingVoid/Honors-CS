"""
    Description: turtle class using Zelle graphics (only partially complete).
    Author: Mr. Bloom
    Date: Spring 2020
"""

from graphics import *
from math import *
from time import sleep

###############################################################

class ZTurtle(object):
    """ Zelle Graphics Turtle """
    pass

    def __init__(self, x, y, graphWin):
        self.x = x
        self.y = y
        self.heading = 90
        self.tailup = True
        self.window = graphWin
        self.color = color_rgb(0,0,0)

    def __str__(self):
        return "x: %i, y: %i, heading: %i, tailup: %r" % (self.getX(), self.getY(), self.getHeading(), self.getTailup())

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getHeading(self):
        return self.heading

    def getTailup(self):
        return self.tailup

    def setX(self, newX):
        self.x = newX

    def setY(self, newY):
        self.y = newY
    
    def setHeading(self, heading):
        self.heading = heading

    def up(self):
        self.tailup = True

    def down(self):
        self.tailup = False

    def turn(self, angle):
        self.setHeading(self.getHeading()+angle)

    def moveTo(self, point):
        self.setX(point.getX())
        self.setY(point.getY())

    def dot(self):
        Circle(Point(self.getX(), self.getY()), 1)
    
    # you need to write:
    #
    # __init__    construct new turtle, given x,y coords and graphics win
    #             hint...use these instance variables:
    #
    #             self.x          current x position
    #             self.y          current y position
    #             self.heading    current heading (0 means East,90 North)
    #             self.tailup     True if tail is up, False if down
    #             self.window     the graphics window for drawing
    #             self.color      color used for drawing
    #
    # __str__     return string with x,y,heading, and tail up or down
    # setColor    change color of pen
    # setHeading  set turtle direction
    # turn        alter turtle direction by certain angle
    # down        put tail down
    # up          lift tail up
    # moveto      magically move turtle to location x,y (no drawing)
    # dot         drop a visible marker at current location


    def forward(self, ds):
        """ move forward a distance ds, draw if tail is down """
        curr_pt = Point(self.x, self.y)
        theta = radians(self.heading)
        dx = ds * cos(theta)
        dy = ds * sin(theta)
        nx = self.x + dx
        ny = self.y + dy
        new_pt = Point(nx, ny)
        if not self.tailup:
            L = Line(curr_pt, new_pt)
            L.draw(self.window)
            L.setFill(self.color)
            sleep(0.1)
        self.x = nx
        self.y = ny

def koch(t, order, size):
    """
       Make turtle t draw a Koch fractal of 'order' and 'size'.
       Leave the turtle facing the same direction.
    """
    if order == 0:          # The base case is just a straight line
        t.forward(size)
    else:
        koch(t, order-1, size/3)   # Go 1/3 of the way
        t.turn(60)
        koch(t, order-1, size/3)
        t.turn(-120)
        koch(t, order-1, size/3)
        t.turn(60)
        koch(t, order-1, size/3)

#------------------------------------------------------------------------------#

if __name__ == "__main__":
    gw = GraphWin("zturtle test", 500, 500)
    gw.setBackground("gray")
    t = ZTurtle(100,400,gw)
    print(t)
    t.down()
    #t.forward(100)
    koch(t,5,1)
    gw.getMouse()
