import pygame
import time
import random

pygame.init()
white=(255, 255, 255)
green=(0, 255, 10)
red=(215, 50, 80)
blue=(50, 153, 213)
black=(0, 0, 0)
yellow=(255, 255, 102)
white_green=(100, 200, 30)

w, h=800, 600

scr=pygame.display.set_mode((w, h))
pygame.display.set_caption('Snake Game')

clock=pygame.time.Clock()

snake_block=25
snake_speed=10

font_style=pygame.font.SysFont(None, 50)
font_count=pygame.font.SysFont(None, 10)

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(scr, green, [x[0], x[1], snake_block, snake_block])
def message(msg, color):
    mesg=font_style.render(msg, True, color)
    scr.blit(mesg, [w/6, h/3])

def count(points, color):
    point=font_count.render(points, True, color)
    scr.blit(point, [700, 500])

def gameLoop():
    game_over=False
    game_close=False

    x1=w/2
    y1=h/2

    move_x1=0
    move_y1=0

    snake_list=[]
    Length_of_snake=1

    food_by_x=round(random.randrange(0, w-snake_block)/25.0)*25.0
    food_by_y=round(random.randrange(0, h-snake_block)/25.0)*25.0

    while not game_over:
        while game_close:
            scr.fill(white_green)
            message("Game over! Q-quit or R-Again", red)
            our_snake(snake_block, snake_list)
            pygame.display.update()


            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        game_over=True
                        game_close=False
                    if event.key==pygame.K_r:
                        gameLoop()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_a:
                    move_x1=-snake_block
                    move_y1=0
                elif event.key==pygame.K_d:
                    move_x1=snake_block
                    move_y1=0
                elif event.key==pygame.K_w:
                    move_y1=-snake_block
                    move_x1=0
                elif event.key==pygame.K_s:
                    move_y1=snake_block
                    move_x1=0
        if x1>=w or x1<0 or y1>=h or y1<0:
            game_close=True
        x1+=move_x1
        y1+=move_y1
        scr.fill(white_green)
        pygame.draw.rect(scr, red, [food_by_x, food_by_y, snake_block, snake_block])
        snake_head=[]
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list)>Length_of_snake:
            del snake_list[0]
        for x in snake_list[:-1]:
            if x==snake_head:
                game_close=True
        our_snake(snake_block, snake_list)

        pygame.display.update()
        lvl=0
        if x1==food_by_x and y1==food_by_y:
            food_by_x=round(random.randrange(0, w-snake_block)/25.0)*25.0
            food_by_y=round(random.randrange(0, h-snake_block)/25.0)*25.0
            Length_of_snake+=1
            if Length_of_snake%10==0:
                lvl+=20
        clock.tick(snake_speed+lvl)
    pygame.quit()
    quit()
gameLoop()