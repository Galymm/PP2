import pygame

pygame.init()
size = width, hight = (400, 200)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Bad - Media - Player')
music_list = [
    '/Users/galymkumiskhan/Desktop/ПП2/repositories/TSIS7/Tones And I - Dance Monkey.mp3',
    '/Users/galymkumiskhan/Desktop/ПП2/repositories/TSIS7/Wallem - Харизма.mp3',
    '/Users/galymkumiskhan/Desktop/ПП2/repositories/TSIS7/MDee_serdce_a_oskolky.mp3'
]

c = 0

done = False
while not done:
    pygame.mixer.music.load(music_list[c])
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                if bool(pygame.mixer.music.pause()):
                    pygame.mixer.music.unpause()
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(music_list[c])
                    pygame.mixer.music.play(c)
                else:
                    pygame.mixer.music.pause()
            if event.key==pygame.K_n:
                c=c+1
                pygame.mixer.music.stop()
                pygame.mixer.music.load(music_list[c])
                pygame.mixer.music.play(c)
                if c==3:
                    c=0
            if event.key==pygame.K_p and c>0:
                c=c-1
                pygame.mixer.music.stop()
                pygame.mixer.music.load(music_list[c])
                pygame.mixer.music.play()
                if c==-1:
                    c=0
            if event.key==pygame.K_ESCAPE:
                done=True
    screen.fill((255, 255, 255))
    pygame.display.flip()


pygame.quit()