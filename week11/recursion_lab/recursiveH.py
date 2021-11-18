from graphics import *
import math

def drawH(window, location, size, degree):

    if degree > 0:
        centerPoint = location

        p1LE = centerPoint.clone()
        p1LE.move(-size,-size) #move to top left area
        p2LE = centerPoint.clone()
        p2LE.move(-size,size) #move to bottom left area
        leftEdge = Line(p1LE, p2LE)
        leftEdge.draw(window)

        p1Horizontal = centerPoint.clone()
        p1Horizontal.move(-size,0)
        p2Horizontal = centerPoint.clone()
        p2Horizontal.move(size,0)
        horizontalLine = Line(p1Horizontal,p2Horizontal)
        horizontalLine.draw(window)

        p1RE = centerPoint.clone()
        p1RE.move(size,-size) #move to top left area
        p2RE = centerPoint.clone()
        p2RE.move(size,size) #move to bottom left area
        rightEdge = Line(p1RE, p2RE)
        rightEdge.draw(window)

        divideFactor = 4
        drawH(window, p1LE, size/divideFactor, degree-1) #TOP LEFT
        drawH(window, p2LE, size/divideFactor, degree-1) #BOTTOM LEFT
        drawH(window, p1RE, size/divideFactor, degree-1) #TOP RIGHT
        drawH(window, p2RE, size/divideFactor, degree-1) #BOTTOM RIGHT


def main():
    win = GraphWin("Letter H", 600, 600)
    degree = int(sys.argv[1])
    drawH(win, Point(win.getWidth()/2,win.getHeight()/2), 100, degree)

    win.getMouse()
main()