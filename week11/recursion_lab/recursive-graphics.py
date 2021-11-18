"""
Author: Raj Sugavanam
Description: Recursively draws flowers a certain amount of times.
Date: September 2021
"""

from graphics import Circle, GraphWin, Point, color_rgb

def drawFlower(win, point, size):
    """ draw a single flower """
    centerCircle = Circle(point, size)                    # Create center circle
    centerCircle.setFill(color_rgb(0,0,0))

    cornerTLCircle = centerCircle.clone()               # Create top-left circle
    cornerTLCircle.move(-size, -size)
    cornerTLCircle.setFill(color_rgb(255,0,255))
    cornerTLCircle.draw(win)

    cornerTRCircle = centerCircle.clone()              # Create top-right circle
    cornerTRCircle.move(size, -size)
    cornerTRCircle.setFill(color_rgb(255,0,255))
    cornerTRCircle.draw(win)

    cornerBLCircle = centerCircle.clone()            # Create bottom-left circle
    cornerBLCircle.move(-size, size)
    cornerBLCircle.setFill(color_rgb(255,0,255))
    cornerBLCircle.draw(win)

    cornerBRCircle = centerCircle.clone()           # Create bottom-right circle
    cornerBRCircle.move(size, size)
    cornerBRCircle.setFill(color_rgb(255,0,255))
    cornerBRCircle.draw(win)

    centerCircle.draw(win)         # Draw center circle last to render it on top

def drawRecursive(win, center, size, repeat):
    """ Draw object recursively """
    if repeat > 0:
        divideFactor = 3                         # How much it shrinks each time
        spreadSize = 1.5*size            # How far away it draws from each other
        drawFlower(win, center, size)         # Draw the flower for this recurse
        # draw recursed flowers in each corner
        drawRecursive(win, Point(center.getX()-spreadSize,center.getY()-spreadSize), size/divideFactor, repeat-1)
        drawRecursive(win, Point(center.getX()+spreadSize,center.getY()-spreadSize), size/divideFactor, repeat-1)
        drawRecursive(win, Point(center.getX()-spreadSize,center.getY()+spreadSize), size/divideFactor, repeat-1)
        drawRecursive(win, Point(center.getX()+spreadSize,center.getY()+spreadSize), size/divideFactor, repeat-1)

def main():

    win = GraphWin("Recursive Flower", 1000, 1000)
    drawRecursive(win, Point(500,500), 150, 6)

    win.getMouse()
main()