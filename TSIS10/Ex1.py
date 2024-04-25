import pygame
import sys
import time

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)

clock=pygame.time.Clock()

w, h = 300, 550

font = pygame.font.Font(None, 32)
class PhoneBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, number):
        self.contacts[name] = number
        print(f"Контакт {name} добавлен.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Контакт {name} удален.")
        else:
            print(f"Контакт {name} не найден.")

    def display_contacts(self, screen):
        if self.contacts:
            y_offset = 150
            for name, number in self.contacts.items():
                contact_text = font.render(f"{name}: {number}", True, white)
                screen.blit(contact_text, (50, y_offset))
                y_offset += 40
        else:
            print("Телефонная книга пуста.")
            screen.blit(contact_text, (50, 100))

def input_line(screen, message, x, y):
    input_box = pygame.Rect(x, y, 200, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    text_color=black
    color = color_inactive
    active = False
    text = ''
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                    text_color=white
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        done = True
                        text_color=black
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        
        txt_surface = font.render(text, True, text_color)
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pygame.draw.rect(screen, color, input_box, 2)

        pygame.display.flip()

    return text

screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('Phone book')

phone_book = PhoneBook()
text=''
def active_phone_book():
    screen.fill(black)
    app_active=True
    while app_active:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                app_active=False
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_a:
                    name_input=input_line(screen, text, 50, 50)
                    number_input=input_line(screen, text, 50, 100)
                    phone_book.add_contact(name_input, number_input)
                    phone_book.display_contacts(screen)
        pygame.display.update()
    pygame.quit()
    quit()
active_phone_book()

