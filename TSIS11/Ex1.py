import pygame
import time

pygame.init()

WHITE=(255, 255, 255)
BLACK=(0, 0, 0)
GREEN=(50, 200, 50)
RED=(200, 30, 30)
GREEN=(20, 20, 20)

clock=pygame.time.Clock()

WIDTH, HEIGTH=400, 600
screen=pygame.display.set_mode((WIDTH, HEIGTH))
pygame.display.set_caption('Phone Book')

font=pygame.font.SysFont(None, 32)

font_b=pygame.font.SysFont(None, 18)

font_s=pygame.font.SysFont(None, 21)

class PhoneBook:
    def __init__(self):
        self.input_name=''
        self.input_phone=''
        self.contacts={}
    def search_records(self, name):
        self.input_phone=self.contacts[name]

    def add_record(self, name, phone):
        self.contacts[name]=phone
    
    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]

    def draw_ui(self):
        pygame.draw.rect(screen, BLACK, (50, 50, 200, 32), 2)
        pygame.draw.rect(screen, BLACK, (50, 100, 200, 32), 2)
        name_text=font.render(self.input_name, True, BLACK)
        screen.blit(name_text, (55, 55))
        phone_text=font.render(self.input_phone, True, BLACK)
        screen.blit(phone_text, (55, 105))

        pygame.draw.rect(screen, GREEN, (270, 50, 110, 32))
        add_=font_b.render("Add-RETURN", True, WHITE)
        screen.blit(add_, (285, 55))

        pygame.draw.rect(screen, RED, (270, 100, 110, 32))
        del_=font_b.render("Delete-RSHIFT", True, BLACK)
        screen.blit(del_, (285, 105))

        pygame.draw.rect(screen, BLACK, (100, 20, 200, 25), 2)
        search=font_s.render("Search-TAB", True, GREEN)
        screen.blit(search, (150, 25))

    def display_contact(self, screen):
        if self.contacts:
            y_offset=150
            for name, number in self.contacts.items():
                contact_text=font.render(f"{name}: +{number}", True, BLACK)
                screen.blit(contact_text, (50, y_offset))
                y_offset+=40
    
    def handle_event(self, event):
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_BACKSPACE:
                if pygame.mouse.get_pos()[0]>50 and pygame.mouse.get_pos()[0]<250 and pygame.mouse.get_pos()[1]>50 and pygame.mouse.get_pos()[1]<82:
                    self.input_name=self.input_name[:-1]
                elif pygame.mouse.get_pos()[0] > 50 and pygame.mouse.get_pos()[0] < 250 and pygame.mouse.get_pos()[1] > 100 and pygame.mouse.get_pos()[1] < 132:
                    self.input_phone=self.input_phone[:-1]
            elif event.key==pygame.K_RETURN:
                self.add_record(self.input_name, self.input_phone)
                self.input_name=''
                self.input_phone=''
            elif event.key==pygame.K_RSHIFT:
                self.delete_contact(self.input_name)
                self.input_name=''
                self.input_phone=''
                if self.input_name in self.contacts.items():
                    del self.contacts[self.input_name]
            elif event.key==pygame.K_TAB:
                self.search_records(self.input_name)
            else:
                if pygame.mouse.get_pos()[0] > 50 and pygame.mouse.get_pos()[0] < 250 and pygame.mouse.get_pos()[1] > 50 and pygame.mouse.get_pos()[1] < 82:
                    self.input_name+=event.unicode
                elif pygame.mouse.get_pos()[0] > 50 and pygame.mouse.get_pos()[0] < 250 and pygame.mouse.get_pos()[1] > 100 and pygame.mouse.get_pos()[1] < 132:
                    self.input_phone+=event.unicode
    def run(self):
        running=True
        while running:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running=False
                else:
                    self.handle_event(event)
            screen.fill(WHITE)

            self.draw_ui()

            self.display_contact(screen)

            pygame.display.flip()
            clock.tick(60)
        pygame.quit()
if __name__=="__main__":
    phonebook=PhoneBook()
    phonebook.run()
