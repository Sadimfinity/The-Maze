import os
import sys
import math
import time
import pygame
current_path = os.getcwd()
import pymunk as pm

def drawScenario(screen, colors):
    screen.fill(colors['white'])
    pygame.draw.rect(screen, colors['black'], [0,0,398,398])
    #Draw start
    pygame.draw.rect(screen, colors['green'], [-2+40*3,-2+40*9,40,40])
    pygame.draw.rect(screen, colors['green'], [-2+40*4,-2+40*9,40,40])
    #Draw scenario
    pygame.draw.rect(screen, colors['yellow'], [-2+40*3,-2+40*8,40,40])
    pygame.draw.rect(screen, colors['yellow'], [-2+40*4,-2+40*8,40,40])
    pygame.draw.rect(screen, colors['yellow'], [-2+40*2,-2+40*8,40,40])
    pygame.draw.rect(screen, colors['yellow'], [-2+40*1,-2+40*8,40,40])
    pygame.draw.rect(screen, colors['yellow'], [-2+40*1,-2+40*7,40,40])
    pygame.draw.rect(screen, colors['yellow'], [-2+40*1,-2+40*6,40,40])
    pygame.draw.rect(screen, colors['yellow'], [-2+40*1,-2+40*5,40,40])
    pygame.draw.rect(screen, colors['yellow'], [-2+40*2,-2+40*5,40,40])
    pygame.draw.rect(screen, colors['yellow'], [-2+40*3,-2+40*5,40,40])
    pygame.draw.rect(screen, colors['yellow'], [-2+40*3,-2+40*6,40,40])
    pygame.draw.rect(screen, colors['yellow'], [-2+40*4,-2+40*5,40,40])
    pygame.draw.rect(screen, colors['yellow'], [-2+40*4,-2+40*6,40,40])
    pygame.draw.rect(screen, colors['blue'], [-2+40*5,-2+40*6,40,40]) #Cuadrito de aumento de tamaño
    pygame.draw.rect(screen, colors['yellow'], [-2+40*6,-2+40*6,40,40])
    pygame.draw.rect(screen, colors['yellow'], [-2+40*6,-2+40*7,40,40])
    pygame.draw.rect(screen, colors['yellow'], [-2+40*6,-2+40*8,40,40])
    pygame.draw.rect(screen, colors['yellow'], [-2+40*7,-2+40*8,40,40])
    pygame.draw.rect(screen, colors['yellow'], [-2+40*8,-2+40*8,40,40])
    pygame.draw.rect(screen, colors['yellow'], [-2+40*8,-2+40*7,40,40])
    pygame.draw.rect(screen, colors['yellow'], [-2+40*8,-2+40*6,40,40])
    pygame.draw.rect(screen, colors['yellow'], [-2+40*8,-2+40*5,40,40])
    pygame.draw.rect(screen, colors['yellow'], [-2+40*8,-2+40*4,40,40])
    pygame.draw.rect(screen, colors['yellow'], [-2+40*7,-2+40*4,40,40])
    pygame.draw.rect(screen, colors['yellow'], [-2+40*6,-2+40*4,40,40])
    pygame.draw.rect(screen, colors['yellow'], [-2+40*5,-2+40*4,40,40])
    pygame.draw.rect(screen, colors['yellow'], [-2+40*5,-2+40*3,40,40])
    pygame.draw.rect(screen, colors['yellow'], [-2+40*4,-2+40*3,40,40])
    pygame.draw.rect(screen, colors['yellow'], [-2+40*3,-2+40*3,40,40])
    pygame.draw.rect(screen, colors['yellow'], [-2+40*2,-2+40*3,40,40])
    pygame.draw.rect(screen, colors['yellow'], [-2+40*1,-2+40*3,40,40])
    pygame.draw.rect(screen, colors['blue'], [-2+40*1,-2+40*2,40,40]) #Cuadritos de aumento de tamaño
    pygame.draw.rect(screen, colors['yellow'], [-2+40*1,-2+40*1,40,40]) 
    pygame.draw.rect(screen, colors['yellow'], [-2+40*2,-2+40*1,40,40])
    pygame.draw.rect(screen, colors['yellow'], [-2+40*3,-2+40*1,40,40])
    pygame.draw.rect(screen, colors['yellow'], [-2+40*4,-2+40*1,40,40])
    pygame.draw.rect(screen, colors['yellow'], [-2+40*5,-2+40*1,40,40])
    pygame.draw.rect(screen, colors['yellow'], [-2+40*6,-2+40*1,40,40])
    pygame.draw.rect(screen, colors['yellow'], [-2+40*7,-2+40*1,40,40])
    pygame.draw.rect(screen, colors['yellow'], [-2+40*8,-2+40*1,40,40])
    pygame.draw.rect(screen, colors['red'], [-2+40*8,-2+40*0,40,40])
    
def isAValidMove(x, y, size, canPlay):
    if(not win):
        canPlay = isInTheStart(x, y, size, canPlay)
        if(canPlay):
            if(x-size>40*3-2 and x+size<40*5-2 and y-size>40*8-2 and y+size<40*10-2):
                return True
            if(x-size>40*3-2 and x+size<40*5-2 and y-size>40*8-2 and y+size<40*10-2):
                print('Son of a bitch im in')
                return True
            if(x-size>40*1-2 and x+size<40*5-2 and y-size>40*8-2 and y+size<40*9-2):
                return True
            if(x-size>40*1-2 and x+size<40*2-2 and y-size>40*5-2 and y+size<40*9-2):
                return True
            if(x-size>40*1-2 and x+size<40*5-2 and y-size>40*5-2 and y+size<=40*6-2):
                return True
            if(x-size>40*3-2 and x+size<40*5-2 and y-size>40*5-2 and y+size<40*7-2):
                return True
            if(x-size>40*3-2 and x+size<40*7-2 and y-size>40*6-2 and y+size<=40*7-2):
                return True
            if(x-size>40*6-2 and x+size<40*7-2 and y-size>40*6-2 and y+size<40*9-2):
                return True
            if(x-size>40*6-2 and x+size<40*9-2 and y-size>40*8-2 and y+size<40*9-2):
                return True
            if(x-size>=40*8-2 and x+size<=40*9-2 and y-size>=40*4-2 and y+size<=40*9-2):
                return True
            if(x-size>40*5-2 and x+size<=40*9-2 and y-size>=40*4-2 and y+size<40*5-2):
                return True
            if(x-size>40*5-2 and x<40*6-2 and y-size>40*3-2 and y+size<40*5-2):
                return True
            if(x-size>40*1-2 and x+size<40*6-2 and y-size>40*3-2 and y+size<=40*4-2):
                return True
            if(x-size>40*1-2 and x+size<40*2-2 and y-size>40*1-2 and y+size<=40*4-2):
                return True
            if(x-size>40*1-2 and x+size<=40*9-2 and y-size>=40*1-2 and y+size<=40*2-2):
                return True
            if(x-size>40*8-2 and x+size<40*9-2 and y-size>40*0-2 and y+size<40*2-2):
                return True
        else:
            canPlay = False
            return canPlay
            
def didWin(x, y, size):
    if(x>40*8-2 and x<40*9-2 and y>40*0-2 and y<40*1-2):
        return True

def isInTheStart(x, y, size, canPlay):
    if(x>40*3-2 and x<40*5-2 and y>40*9-2 and y<40*10-2 or canPlay):
        canPlay = True
        return canPlay
    elif(canPlay == True):
        return canPlay
    else:
        canPlay = False
        return canPlay

def increaseSize(x, y, size):
    if(x>40*5-2 and x<40*6-2 and y>40*6-2 and y<40*7-2):
        return 1
    elif(x>40*1-2 and x<40*2-2 and y>40*2-2 and y<40*3-2):
        return 2

def main():
    size = 3
    canPlay = False
    white = (255, 255, 255)
    black = (51,51,51)
    red = (255,0,0)
    green = (0,255,0)
    yellow = (255,204,0)
    blue = (0,0,255)
    colors = dict(white = white, black = black, red = red, green = green, yellow = yellow, blue = blue)
    pygame.init()
    screen = pygame.display.set_mode((1200, 650))
    pygame.display.set_caption('The Maze')
    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
        drawScenario(screen, colors)
        x, y = pygame.mouse.get_pos()
        canPlay = isAValidMove(x, y, size, canPlay)
        if(canPlay):
            if(increaseSize(x, y, size) == 1):
                size = size + 0.025
            elif(increaseSize(x, y, size) == 2):
                size = size + 0.05
            pygame.draw.circle(screen, red, (x, y), size)
            if(didWin(x, y, size)):
                win = True
        else:
            size = 5

        pygame.display.update()

win = False
main()