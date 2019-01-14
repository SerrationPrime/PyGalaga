import pygame
from main_menu_btnfunc import *

pygame.init()
display_width = 600
display_height = 1000

gameDisplay = pygame.display.set_mode((display_width, display_height))


def button_single():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 145 + 310 > mouse[0] > 145 and 435 + 50 > mouse[1] > 435:
        s = pygame.Surface((310, 50))
        s.set_alpha(50)
        s.fill((200, 0, 0))
        gameDisplay.blit(s, (145, 435))
        if click[0] == 1:
            action_signal_single()
            pygame.quit()
            quit()
    else:
        s = pygame.Surface((310, 50))
        s.set_alpha(0)
        gameDisplay.blit(s, (145, 435))


def button_multi():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 155 + 290 > mouse[0] > 155 and 490 + 50 > mouse[1] > 490:
        s = pygame.Surface((290, 50))
        s.set_alpha(50)
        s.fill((200, 0, 0))
        gameDisplay.blit(s, (155, 490))
        if click[0] == 1:
            action_open_multi()
            pygame.quit()
            quit()
    else:
        s = pygame.Surface((290, 50))
        s.set_alpha(0)
        gameDisplay.blit(s, (155, 490))


def button_exit():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 240 + 95 > mouse[0] > 240 and 550 + 50 > mouse[1] > 550:
        s = pygame.Surface((95, 50))
        s.set_alpha(50)
        s.fill((200, 0, 0))
        gameDisplay.blit(s, (255, 550))
        if click[0] == 1:
            pygame.quit()
            quit()
    else:
        s = pygame.Surface((95, 50))
        s.set_alpha(0)
        gameDisplay.blit(s, (255, 550))


def main_menu():
    pygame.display.set_caption('Terran Defenders')

    black = (0, 0, 0)
    white = (255, 255, 255)

    clock = pygame.time.Clock()
    crashed = False
    img = pygame.image.load('main_menu.png')

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

        gameDisplay.fill((white))
        gameDisplay.blit(img, (0, 0))
        pygame.display.flip()

        button_single()
        button_multi()
        button_exit()

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()


if __name__ == '__main__':

    main_menu()
    pygame.quit()

