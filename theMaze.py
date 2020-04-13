# coding=utf-8

import os
import sys
import math
import time
import cv2
import numpy as np
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

def getPosition():
        
    MIN_MATCH_COUNT=30

    detector=cv2.xfeatures2d.SIFT_create()

    FLANN_INDEX_KDITREE=0
    flannParam=dict(algorithm=FLANN_INDEX_KDITREE,tree=5)
    flann=cv2.FlannBasedMatcher(flannParam,{})

    trainImg=cv2.imread("/home/sady/Coding/The-Maze/trainImg.jpeg",0)
    trainKP,trainDesc=detector.detectAndCompute(trainImg,None)
    cam=cv2.VideoCapture(0)
    ret, QueryImgBGR=cam.read()
    QueryImg=cv2.cvtColor(QueryImgBGR,cv2.COLOR_BGR2GRAY)
    queryKP,queryDesc=detector.detectAndCompute(QueryImg,None)
    matches=flann.knnMatch(queryDesc,trainDesc,k=2)

    goodMatch=[]
    for m,n in matches:
        if(m.distance<0.75*n.distance):
            goodMatch.append(m)
    if(len(goodMatch)>MIN_MATCH_COUNT):
        tp=[]
        qp=[]
        for m in goodMatch:
            tp.append(trainKP[m.trainIdx].pt)
            qp.append(queryKP[m.queryIdx].pt)
        tp,qp=np.float32((tp,qp))
        H,status=cv2.findHomography(tp,qp,cv2.RANSAC,3.0)
        h,w=trainImg.shape
        trainBorder=np.float32([[[0,0],[0,h-1],[w-1,h-1],[w-1,0]]])
        queryBorder=cv2.perspectiveTransform(trainBorder,H)
        # convert the grayscale image to binary image
        ret,thresh = cv2.threshold(QueryImg,127,255,0)

        # calculate moments of binary image
        M = cv2.moments(thresh)

        # calculate x,y coordinate of center
        x = int(M["m10"] / M["m00"])
        y = int(M["m01"] / M["m00"])
        cv2.polylines(QueryImgBGR,[np.int32(queryBorder)],True,(255,0,0),5)
        return x, y
    else:
        return 0,0
    cv2.imshow('Camera',QueryImgBGR)
    


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
    screen = pygame.display.set_mode((398, 398))
    pygame.display.set_caption('The Maze')

    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                #cam.release()
                #cv2.destroyAllWindows()
        drawScenario(screen, colors)
        x, y = getPosition()
        canPlay = isAValidMove(x, y, size, canPlay)
        if(canPlay):
            print('melo')
            #if(increaseSize(x, y, size) == 1):
            #    size = size + 0.025
            #elif(increaseSize(x, y, size) == 2):
            #    size = size + 0.05
            pygame.draw.circle(screen, red, (x, y), size)
            if(didWin(x, y, size)):
                win = True
                
        else:
            size = 5
        pygame.display.update()
    cv2.imshow('Camera',QueryImgBGR)
    

win = False
main()