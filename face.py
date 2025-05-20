from turtle import *

def __init__(self,xpos,ypos ):
    self.size = 90
    self.coord = (xpos,ypos)
    self.nosesize = "small"

    def setsize(self, radius):
        self.size = radius

    def draw(self):
        self.gohome()
        pensize(3)
        speed(0)
        self.drawoutline()
        self.draweyes(135)
        self.draweyes(45)
        self.drawmouth()
        self.drawnose()

        pensize (5)

    def gohome(self):
        penup()
        goto (self.coord)
        
        setheading(0)

    def drawoutline(self):
        penup()
        forward (self.size)
        left (90)
        pendown()
        circle (self.size)
        self.gohome()

    def draweyes(self, turn):
        penup()
        left (turn)
        forward (self.size / 2)
        pendown()
        dot (self.size / 10)
        self.gohome()

    def drawmouth(self):
        penup()
        