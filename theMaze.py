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
    
def isAValidMove(x, y, size, canPlay):
    if(not win):
        canPlay = isInTheStart(x, y, size, canPlay)
        if(canPlay):
            if(x-size>40*3-2 and x+size<40*5-2 and y-size>40*8-2 and y+size<40*10-2):
                return True
            if(x-size>40*3-2 and x+size<40*5-2 and y-size>40*8-2 and y+size<40*10-2):
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
    if(x-size>40*8-2 and x+size<40*9-2 and y-size>40*0-2 and y+size<40*1-2):
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

def initializeColors():
    white = (255, 255, 255)
    black = (51,51,51)
    red = (255,0,0)
    green = (0,255,0)
    yellow = (255,204,0)
    blue = (0,0,255)
    colors = dict(white = white, black = black, red = red, green = green, yellow = yellow, blue = blue)
    return colors

def main(win):
    size = 5
    canPlay = False
    startGame = False
    colors = initializeColors()
    pygame.init()
    pygame.display.set_caption('The Maze (The Game)')
    screen = pygame.display.set_mode((398, 398))
    screen.fill((255,255,255))
    cap = cv2.VideoCapture(0)
    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
        if(not startGame):
            font = pygame.font.SysFont("Helvetica", 36)            
            text = font.render("¡Prueba tu pulso!", True, (0, 0, 0))
            text1 = font.render("Ingrese llave para iniciar el juego", True, (0, 0, 0))
            text2 = font.render("el juego", True, (0,0,0))            
            screen.blit(text, (315 -text1.get_width() // 2, 145 - text1.get_height() // 2))
            screen.blit(text1, (265 -text1.get_width() // 2, 195 - text1.get_height() // 2))
            screen.blit(text2, (400 -text1.get_width() // 2, 245 - text1.get_height() // 2))
            pygame.display.flip()
        else:
            drawScenario(screen, colors)
        _, frame = cap.read()
        blurred_frame = cv2.GaussianBlur(frame, (5, 5), 0)
        hsv = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)
        lower_blue = np.array([38, 86, 0])
        upper_blue = np.array([121, 255, 255])
        mask = cv2.inRange(hsv, lower_blue, upper_blue)

        _, contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)    
        for contour in contours:
            area = cv2.contourArea(contour)
            print(area)
            if( area > 700 and area < 2000):
                startGame = True
                cv2.drawContours(frame, contours, -1, (0,0,255), 3)
                # calculate moments of binary image
                M = cv2.moments(contour)

                # calculate x,y coordinate of center
                x = int((M["m10"] / M["m00"]))
                y = int((M["m01"] / M["m00"]))
                canPlay = isAValidMove(x, y, size, canPlay)
                if(canPlay):
                    if(increaseSize(x, y, size) == 1):
                        size = size + 0.1
                    elif(increaseSize(x, y, size) == 2):
                        size = size + 0.2
                    pygame.draw.circle(screen, colors['red'], (x, y), size)
                    if(didWin(x, y, size)):
                        gameExit = True
                        win = True
                else:
                    size = 5
                pygame.display.update()
        cv2.imshow("Cámara", frame)    
        if cv2.waitKey(10)==ord('q'):
            break
    cap.release()
    if(win):
        screen.fill((255,255,255))
        font = pygame.font.SysFont("Helvetica", 72)
        winText = font.render("¡Ganaste!", True, (0, 0, 0))
        screen.blit(winText, (280 -text1.get_width() // 2, 175 - text1get_height() // 2))
        pygame.display.flip()
        pygame.time.delay(10000)
    
    cv2.destroyAllWindows()
    
win = False  
main(win)