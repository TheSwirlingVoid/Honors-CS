"""
Description: Contains UI element objects for other programs to use.
Author: Raj Sugavanam
Date: Oct 2021
"""

from time import sleep
from graphics import *

class Button(object):
    """ animated single-click button object """
    def __init__(self, height, width, size, location, buttonDepth, color, text, textSize):
        self.graphicsObjects = []

        self.size = size
        self.text = text
        self.buttonDepth = buttonDepth
        self.color = color
        self.textSize = textSize
        self.location = location
        self.width = height*size
        self.length = width*size
        self.drawn = False

        halfLength = self.length/2
        halfWidth = self.width/2

        self.Point1 = Point(location.getX() - halfLength, location.getY() + halfWidth)
        self.Point2 = Point(location.getX() + halfLength, location.getY() - halfWidth)

    def getSize(self):
        return self.size

    def setSize(self, newSize):
        if self.isDrawn() == False:
            self.setLength(self.getLength()*newSize)
            self.setHeight(self.getHeight()*newSize)

    def getButtonDepth(self):
        return self.buttonDepth

    def setButtonDepth(self, newButtonDepth):
        self.buttonDepth = newButtonDepth

    def getColor(self):
        return self.color

    def setColor(self, newColor):
        self.color = newColor

    def getTextSize(self):
        return self.textSize

    def setTextSize(self, newTextSize):
        """ will update when drawn again """
        self.textSize = newTextSize

    def getPointBL(self):
        return self.Point1

    def getPointTR(self):
        return self.Point2

    def setPointBL(self, newPoint):
        self.Point1 = newPoint

    def setPointTR(self, newPoint):
        self.Point2 = newPoint

    def getLength(self):
        return self.length
    
    def getHeight(self):
        return self.width

    def setLength(self, newLen):
        """ can only be used if undrawn! """
        if self.isDrawn() == False:
            self.length = newLen
            location = self.getLocation()
            height = self.getHeight()
            self.setPointBL(Point(location.getX() - newLen/2, location.getY() + height/2))
            self.setPointTR(Point(location.getX() + newLen/2, location.getY() - height/2))
    
    def setHeight(self, newHeight):
        """ can only be used if undrawn! """
        if self.isDrawn() == False:
            self.width = newHeight
            location = self.getLocation()
            length = self.getLength()
            self.setPointBL(Point(location.getX() - newHeight/2, location.getY() + length/2))
            self.setPointTR(Point(location.getX() + newHeight/2, location.getY() - length/2))

    def getLocation(self):
        return self.location

    def setLocation(self, newLocation):
        """ can only be used if undrawn! """
        if self.isDrawn() == False:
            self.location = newLocation

            length = self.getLength()
            height = self.getHeight()

            newLocX = newLocation.getX()
            newLocY = newLocation.getY()

            self.setPointBL(Point(newLocX - length/2, newLocY + height/2))
            self.setPointTR(Point(newLocX + length/2, newLocY - height/2))

    def getText(self):
        return self.text

    def setText(self, newText):
        """ will be updated once drawn again """
        self.text = newText

    def isDrawn(self):
        return self.drawn

    def setDrawn(self, drawn):
        self.drawn = drawn

    def isPointInButton(self, point):
        """ check if a given point is contained within the area of a button"""
        pointX = point.getX()
        pointY = point.getY()

        pointTL = self.getPointTR()
        pointBR = self.getPointBL()

        if (pointX < pointTL.getX() and pointY > pointTL.getY()) \
            and (pointX > pointBR.getX() and pointY < pointBR.getY()):
            return True
        else:
            return False

    def addGraphicsObject(self, graphicsObject):
        self.graphicsObjects.append(graphicsObject)

    def getGraphicsObjects(self):
        return self.graphicsObjects

    def drawButton(self, PRESSED, graphWin):
        """ draw button to graph win """

        if self.isDrawn() == True:
            return

        size = self.getSize()
        buttonDepth = self.getButtonDepth()
        color = self.getColor()

        rectPointBL = self.getPointBL()
        rectPointTR = self.getPointTR()

        buttonUI = Rectangle(self.getPointBL(), self.getPointTR())
        buttonUI.setWidth(3)

        point3DBL = rectPointBL.clone()
        point3DTL = rectPointBL.clone()
        point3DTL.move(0, -self.getHeight()) # Move point to top left corner of rect
        rectPointTL = point3DTL.clone() # clone the point to create a rect corner
                                        # copy to keep in place
        point3DTR = rectPointTR.clone()

        moveAmount = 5*buttonDepth*size
        point3DBL.move(-moveAmount, -moveAmount)
        point3DTL.move(-moveAmount, -moveAmount)
        point3DTR.move(-moveAmount, -moveAmount)

        # Slanted lines
        line1 = Line(point3DBL, rectPointBL)
        line2 = Line(point3DTL, rectPointTL)
        line3 = Line(point3DTR, rectPointTR)

        line1.setWidth(3)
        line2.setWidth(3)
        line3.setWidth(3)

        # Horiz. Lines
        lineH1 = Line(point3DBL,point3DTL)
        lineH2 = Line(point3DTL, point3DTR)

        lineH1.setWidth(3)
        lineH2.setWidth(3)

        textObject = Text(self.getLocation(), self.getText())
        textObject.setSize(self.getTextSize())

        self.addGraphicsObject(buttonUI)
        self.addGraphicsObject(line1)
        self.addGraphicsObject(line2)
        self.addGraphicsObject(line3)
        self.addGraphicsObject(lineH1)
        self.addGraphicsObject(lineH2)
        self.addGraphicsObject(textObject)


        graphicsObjects = self.getGraphicsObjects()

        for graphicsObject in graphicsObjects:
            graphicsObject.setOutline(color)
            graphicsObject.draw(graphWin)

        if PRESSED:
            for graphicsObject in graphicsObjects:
                graphicsObject.move(-moveAmount, -moveAmount)

        self.setDrawn(True)

    def undraw(self):
        for graphicsObject in self.getGraphicsObjects():
            graphicsObject.undraw()
        self.graphicsObjects = [] # to clear the previously drawn objects out

        self.setDrawn(False)

    def clickOperation(self, clickLocation, buttonDepthPressed, colorPressed, graphWin):
        """ If the specified click location is within the button (return val True or False), a click is animated
            based on the pressed-button parameters. """
        if self.isDrawn() and self.isPointInButton(clickLocation):
            baseDepth = self.getButtonDepth()
            baseColor = self.getColor()
            self.undraw()
            self.setButtonDepth(buttonDepthPressed)
            self.setColor(colorPressed)
            self.drawButton(True, graphWin)
            sleep(0.15)
            self.undraw()
            self.setButtonDepth(baseDepth)
            self.setColor(baseColor)
            self.drawButton(False, graphWin)
            return True
        return False

if __name__ == "__main__":

    graphWin = GraphWin("UI Test", 1000, 1000)
    button = Button(25, 25, 3,Point(700,500), 0.5, color_rgb(0,200,0), "+1", 30)
    button2 = Button(25, 25, 3,Point(400,500), 0.5, color_rgb(200,0,0), "-1", 30)

    i = 0
    testText = Text(Point(550,400), "")
    testText.setSize(20)
    testText.draw(graphWin)

    button.drawButton(False,graphWin)
    button2.drawButton(False,graphWin)

    while True:
        testText.setText("Test Int: %i" % i)
        mouse = graphWin.checkMouse()
        if mouse != None:
            if button.clickOperation(mouse, 0.25,color_rgb(0,125,0),graphWin):
                i+=1
            elif button2.clickOperation(mouse, 0.25,color_rgb(125,0,0),graphWin):
                i-=1
