import pygame
import sys

pygame.init()

w=800
h=600

white=(255, 255, 255)
red=(255, 0, 0)

ball_r=25
ball_d=ball_r*2

ball_x=w//2
ball_y=h//2

screen=pygame.display.set_mode((w, h))
pygame.display.set_caption("RED BALL")

clock=pygame.time.Clock()

run=True

while run:
    screen.fill(white)

    pygame.draw.circle(screen, red, (ball_x, ball_y), ball_r)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                if ball_y-20>=ball_r:
                    ball_y-=20
            elif event.key==pygame.K_DOWN:
                if ball_y+20<=h-ball_r:
                    ball_y+=20
            elif event.key==pygame.K_LEFT:
                if ball_x-20>=ball_r:
                    ball_x-=20
            elif event.key==pygame.K_RIGHT:
                if ball_x+20<=w-ball_r:
                    ball_x+=20
            elif event.key==pygame.K_ESCAPE:
                run=False
        pygame.display.flip()
        clock.tick(30)
        pygame.display.update()
