import pygame
from variables import BOARDBLACK, BOARDWHITE, SQUAREWIDTH, SQUAREHEIGHT, BOARDXOFFSET, BOARDYOFFSET


class Square():
     def __init__(self, x, y, color):
         self.x = x
         self.y = y
         self.color = color

     def draw(self, window):
         pygame.draw.rect(window, self.color, (self.x, self.y, SQUAREWIDTH, SQUAREHEIGHT))


def createSquares(listOfSquares):
    
    color = BOARDWHITE
    
    for i in range(0,8):

        newRow = True
    
        for j in range(0,8):

            if newRow == True:
                if color == BOARDWHITE:
                    color = BOARDBLACK
                else:
                    color = BOARDWHITE
            
            newRow = False                 

            if color == BOARDWHITE:
               color = BOARDBLACK
            else:
                color = BOARDWHITE

            listOfSquares.append(Square(BOARDXOFFSET + (SQUAREWIDTH*j),BOARDYOFFSET + (SQUAREHEIGHT*i), color))


    
    
