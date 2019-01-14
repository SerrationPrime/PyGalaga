import pygame
from tournament_menu_btnfunc import *


display_width = 600
display_height = 1000

gameDisplay = pygame.display.set_mode((display_width, display_height))


def button_create():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 70 + 445 > mouse[0] > 70 and 425 + 50 > mouse[1] > 425:
        s = pygame.Surface((465, 50))
        s.set_alpha(50)
        s.fill((200, 0, 0))
        gameDisplay.blit(s, (70, 425))
        if click[0] == 1:
            action_create_tournament()
            pygame.quit()
            quit()
    else:
        s = pygame.Surface((445, 50))
        s.set_alpha(0)
        gameDisplay.blit(s, (70, 425))


def button_join():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 95 + 410 > mouse[0] > 95 and 485 + 50 > mouse[1] > 485:
        s = pygame.Surface((410, 50))
        s.set_alpha(50)
        s.fill((200, 0, 0))
        gameDisplay.blit(s, (95, 485))
        if click[0] == 1:
            action_join_tournament()
            pygame.quit()
            quit()
    else:
        s = pygame.Surface((410, 50))
        s.set_alpha(0)
        gameDisplay.blit(s, (95, 485))

def button_back_tour():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 20 + 81 > mouse[0] > 20 and 15 + 67 > mouse[1] > 15:
        s = pygame.Surface((81, 67))
        s.set_alpha(50)
        s.fill((200, 0, 0))
        gameDisplay.blit(s, (20, 15))
        if click[0] == 1:
            action_back_to_multi_from_tournament()
            pygame.quit()
            quit()
    else:
        s = pygame.Surface((81, 67))
        s.set_alpha(0)
        gameDisplay.blit(s, (20, 15))


def tournament_menu():
    pygame.display.set_caption('Terran Defenders')

    white = (255, 255, 255)

    clock = pygame.time.Clock()
    crashed = False
    img = pygame.image.load('menu_tournament2.png')

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

        gameDisplay.fill((white))
        gameDisplay.blit(img, (0, 0))
        pygame.display.flip()

        button_create()
        button_join()
        button_back_tour()

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()


if __name__ == '__main__':
    pygame.init()
    tournament_menu()
    pygame.quit()

