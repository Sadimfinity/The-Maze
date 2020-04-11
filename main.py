import os
import sys
import math
import time
import pygame
current_path = os.getcwd()
import pymunk as pm

def drawScenario(screen):
    screen.fill(white)
    pygame.draw.rect(screen, black, [0,0,398,398])
    #Draw start
    pygame.draw.rect(screen, green, [-2+40*3,-2+40*9,40,40])
    pygame.draw.rect(screen, green, [-2+40*4,-2+40*9,40,40])
    #Draw scenario
    pygame.draw.rect(screen, yellow, [-2+40*3,-2+40*8,40,40])
    pygame.draw.rect(screen, yellow, [-2+40*4,-2+40*8,40,40])
    pygame.draw.rect(screen, yellow, [-2+40*2,-2+40*8,40,40])
    pygame.draw.rect(screen, yellow, [-2+40*1,-2+40*8,40,40])
    pygame.draw.rect(screen, yellow, [-2+40*1,-2+40*7,40,40])
    pygame.draw.rect(screen, yellow, [-2+40*1,-2+40*6,40,40])
    pygame.draw.rect(screen, yellow, [-2+40*1,-2+40*5,40,40])
    pygame.draw.rect(screen, yellow, [-2+40*2,-2+40*5,40,40])
    pygame.draw.rect(screen, yellow, [-2+40*3,-2+40*5,40,40])
    pygame.draw.rect(screen, yellow, [-2+40*3,-2+40*6,40,40])
    pygame.draw.rect(screen, yellow, [-2+40*4,-2+40*5,40,40])
    pygame.draw.rect(screen, yellow, [-2+40*4,-2+40*6,40,40])
    pygame.draw.rect(screen, blue, [-2+40*5,-2+40*6,40,40]) #Cuadrito de aumento de tamaño
    pygame.draw.rect(screen, yellow, [-2+40*6,-2+40*6,40,40])
    pygame.draw.rect(screen, yellow, [-2+40*6,-2+40*7,40,40])
    pygame.draw.rect(screen, yellow, [-2+40*6,-2+40*8,40,40])
    pygame.draw.rect(screen, yellow, [-2+40*7,-2+40*8,40,40])
    pygame.draw.rect(screen, yellow, [-2+40*8,-2+40*8,40,40])
    pygame.draw.rect(screen, yellow, [-2+40*8,-2+40*7,40,40])
    pygame.draw.rect(screen, yellow, [-2+40*8,-2+40*6,40,40])
    pygame.draw.rect(screen, yellow, [-2+40*8,-2+40*5,40,40])
    pygame.draw.rect(screen, yellow, [-2+40*8,-2+40*4,40,40])
    pygame.draw.rect(screen, yellow, [-2+40*7,-2+40*4,40,40])
    pygame.draw.rect(screen, yellow, [-2+40*6,-2+40*4,40,40])
    pygame.draw.rect(screen, yellow, [-2+40*5,-2+40*4,40,40])
    pygame.draw.rect(screen, yellow, [-2+40*5,-2+40*3,40,40])
    pygame.draw.rect(screen, yellow, [-2+40*4,-2+40*3,40,40])
    pygame.draw.rect(screen, yellow, [-2+40*3,-2+40*3,40,40])
    pygame.draw.rect(screen, yellow, [-2+40*2,-2+40*3,40,40])
    pygame.draw.rect(screen, yellow, [-2+40*1,-2+40*3,40,40])
    pygame.draw.rect(screen, blue, [-2+40*1,-2+40*2,40,40]) #Cuadritos de aumento de tamaño
    pygame.draw.rect(screen, yellow, [-2+40*1,-2+40*1,40,40]) 
    pygame.draw.rect(screen, yellow, [-2+40*2,-2+40*1,40,40])
    pygame.draw.rect(screen, yellow, [-2+40*3,-2+40*1,40,40])
    pygame.draw.rect(screen, yellow, [-2+40*4,-2+40*1,40,40])
    pygame.draw.rect(screen, yellow, [-2+40*5,-2+40*1,40,40])
    pygame.draw.rect(screen, yellow, [-2+40*6,-2+40*1,40,40])
    pygame.draw.rect(screen, yellow, [-2+40*7,-2+40*1,40,40])
    pygame.draw.rect(screen, yellow, [-2+40*8,-2+40*1,40,40])
    pygame.draw.rect(screen, red, [-2+40*8,-2+40*0,40,40])
    
def isAValidMove(x, y, size, win, canPlay):
    if(not win):
        if(isInTheStart(x, y, size, canPlay)):
            if(x-size>40*3-2 & x+size<40*5-2 & y-size>40*8-2 &y+size<40*10-2):
                  return True
            if(x-size>40*3-2 & x+size<40*5-2 & y-size>40*8-2 &y+size<40*10-2):
                  return True
            if(x-size>40*1-2 & x+size<40*5-2 & y-size>40*8-2 & y+size<40*9-2):
                  return True
            if(x-size>40*1-2 & x+size<40*2-2 & y-size>40*5-2 & y+size<40*9-2):
                  return True
            if(x-size>40*1-2 & x+size<40*5-2 & y-size>40*5-2 & y+size<=40*6-2):
                  return True
            if(x-size>40*3-2 & x+size<40*5-2 & y-size>40*5-2 & y+size<40*7-2):
                  return True
            if(x-size>40*3-2 & x+size<40*7-2 & y-size>40*6-2 & y+size<=40*7-2):
                  return True
            if(x-size>40*6-2 & x+size<40*7-2 & y-size>40*6-2 & y+size<40*9-2):
                  return True
            if(x-size>40*6-2 & x+size<40*9-2 & y-size>40*8-2 & y+size<40*9-2):
                  return True
            if(x-size>=40*8-2 & x+size<=40*9-2 & y-size>=40*4-2 & y+size<=40*9-2):
                  return True
            if(x-size>40*5-2 & x+size<=40*9-2 & y-size>=40*4-2 & y+size<40*5-2):
                  return True
            if(x-size>40*5-2 & x<40*6-2 & y-size>40*3-2 & y+size<40*5-2):
                  return True
            if(x-size>40*1-2 & x+size<40*6-2 & y-size>40*3-2 & y+size<=40*4-2):
                  return True
            if(x-size>40*1-2 & x+size<40*2-2 & y-size>40*1-2 & y+size<=40*4-2):
                  return True
            if(x-size>40*1-2 & x+size<=40*9-2 & y-size>=40*1-2 & y+size<=40*2-2):
                  return True
            if(x-size>40*8-2 & x+size<40*9-2 & y-size>40*0-2 & y+size<40*2-2):
                  return True
        else:
            canPlay = False
            return canPlay
            
def didWin(x, y, size):
    if(x-size>40*8-2 & x+size<40*9-2 & y-size>40*0-2 & y+size<40*1-2):
        return True

def isInTheStart(x, y, size, canPlay):
    if((x-size>40*3-2 & x+size<40*5-2 & y-size>40*9-2 & y+size<40*10-2) | canPlay):
        canPlay = True
    else:
        canPlay = False
    return canPlay

def increaseSize(x, y, size):
    if(x-size>40*5-2 & x+size<40*6-2 & y-size>40*6-2 & y+size<40*7-2):
        return 1
    elif(x-size>40*1-2 & x+size<40*2-2 & y-size>40*2-2 & y+size<40*3-2):
        return 2

def drawPlayer(x, y, screen, size):
    pygame.draw.circle(screen, red, (x, y), size)

size = 3
canPlay = False
win = False
white = (255, 255, 255)
black = (51,51,51)
red = (255,0,0)
green = (0,255,0)
yellow = (255,204,0)
blue = (0,0,255)

pygame.init()
screen = pygame.display.set_mode((1200, 650))
pygame.display.set_caption('The Maze')
#rect = pygame.Rect(181, 1050, 50, 50)
#cropped = full_sprite.subsurface(rect).copy()

gameExit = False
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
    
    drawScenario(screen)
    x, y = pygame.mouse.get_pos()
    if(isAValidMove(x, y, size, win, canPlay)):
        if(increaseSize(x, y, size) == 1):
            size = size + 1
        elif(increaseSize(x, y, size) == 2):
            size = size + 2
        drawPlayer(x, y, screen, size)
        if(didWin(x, y, size)):
            win = True
    else:
        size = 5
        
    pygame.display.update()
