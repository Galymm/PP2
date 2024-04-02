import pygame
from math import *
from datetime import *

pygame.init()
screen = pygame.display.set_mode((1000, 1000))
clock = pygame.time.Clock()
body = pygame.image.load("/Users/galymkumiskhan/Desktop/ПП2/repositories/TSIS7/bodyclock.png")
seconds = pygame.image.load("/Users/galymkumiskhan/Desktop/ПП2/repositories/TSIS7/leftarm.png")
minute = pygame.image.load("/Users/galymkumiskhan/Desktop/ПП2/repositories/TSIS7/rightarm.png")
bodyRect = body.get_rect(center=(500, 500))

status = True
while status:
    current = datetime.now()
    secondsAngle = current.second * 6
    minuteAngle = (current.minute * 6) + (current.second / 10)
    
    rotatedSecond = pygame.transform.rotate(seconds, -secondsAngle)
    rotatedMinute = pygame.transform.rotate(minute, -minuteAngle)
    
    rotatedRectMin = rotatedMinute.get_rect(center=bodyRect.center)
    rotatedRectSec = rotatedSecond.get_rect(center=bodyRect.center)
    
    screen.blit(body, bodyRect)
    screen.blit(rotatedSecond, rotatedRectSec)
    screen.blit(rotatedMinute, rotatedRectMin)
    
    pygame.display.update()
    
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            status = False
            pygame.quit()
    clock.tick(60)
