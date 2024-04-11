import pygame
import sys
import math


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


RECTANGLE = 0
CIRCLE = 1
TRIANGLE = 2


pygame.init()


WINDOW_SIZE = (800, 600)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Простой Paint")


canvas = pygame.Surface((WINDOW_SIZE[0], WINDOW_SIZE[1]))


drawing = False
last_pos = None
brush_color = BLACK
brush_size = 3
current_shape = RECTANGLE  


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  
                drawing = True
                last_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
                last_pos = None
        elif event.type == pygame.MOUSEMOTION:
            if drawing:
                mouse_pos = event.pos
                if last_pos:
                    if current_shape == RECTANGLE:
                        pygame.draw.rect(canvas, brush_color, (last_pos, (mouse_pos[0] - last_pos[0], mouse_pos[1] - last_pos[1])), brush_size)
                    elif current_shape == CIRCLE:
                        radius = int(math.sqrt((mouse_pos[0] - last_pos[0])**2 + (mouse_pos[1] - last_pos[1])**2))
                        pygame.draw.circle(canvas, brush_color, last_pos, radius, brush_size)
                    elif current_shape == TRIANGLE:
                        pygame.draw.polygon(canvas, brush_color, [(last_pos[0], mouse_pos[1]), mouse_pos, ((last_pos[0] + mouse_pos[0]) // 2, last_pos[1])], brush_size)
                last_pos = mouse_pos
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:  
                canvas.fill(WHITE)
            elif event.key == pygame.K_s:  
                pygame.image.save(canvas, "painting.png")
            elif event.key == pygame.K_b:  
                brush_color = BLACK
            elif event.key == pygame.K_w:
                brush_color = WHITE
            elif event.key == pygame.K_p:  
                brush_size += 1
            elif event.key == pygame.K_m:  
                brush_size = max(1, brush_size - 1)
            elif event.key == pygame.K_1:  # rectangle
                current_shape = RECTANGLE
            elif event.key == pygame.K_2:  # circle
                current_shape = CIRCLE
            elif event.key == pygame.K_3:  #triangle 
                current_shape = TRIANGLE

    
    screen.fill(WHITE)
    screen.blit(canvas, (0, 0))

    # Обновление экрана
    pygame.display.flip()
