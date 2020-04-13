# coding=utf-8
import cv2
import numpy as np
import pygame

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


pygame.init()
screen = pygame.display.set_mode((398, 398))
screen.fill((255,255,255))
MIN_MATCH_COUNT=30

white = (255, 255, 255)
black = (51,51,51)
red = (255,0,0)
green = (0,255,0)
yellow = (255,204,0)
blue = (0,0,255)
colors = dict(white = white, black = black, red = red, green = green, yellow = yellow, blue = blue)
detector=cv2.xfeatures2d.SIFT_create()

FLANN_INDEX_KDITREE=0
flannParam=dict(algorithm=FLANN_INDEX_KDITREE,tree=5)
flann=cv2.FlannBasedMatcher(flannParam,{})

trainImg=cv2.imread("/home/sady/Coding/The-Maze/trainImg.jpeg",0)
trainKP,trainDesc=detector.detectAndCompute(trainImg,None)

cam=cv2.VideoCapture(0)
while True:
    drawScenario(screen, colors)
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
        x = int((M["m10"] / M["m00"]) - 100)
        y = int((M["m01"] / M["m00"]) * 0.8)  - 100
        print(x, y)
        pygame.draw.circle(screen, (255,0,0), (x, y), 5)
        pygame.display.update()
        cv2.polylines(QueryImgBGR,[np.int32(queryBorder)],True,(255,0,0),5)
    #else:
    #    print ("Not Enough match found")
    cv2.imshow('result',QueryImgBGR)
    if cv2.waitKey(10)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()