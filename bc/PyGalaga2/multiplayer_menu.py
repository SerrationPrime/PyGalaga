import pygame
from multiplayer_menu_btnfunc import *

pygame.init()
display_width = 600
display_height = 1000

gameDisplay = pygame.display.set_mode((display_width, display_height))


def button_host():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 170 + 255 > mouse[0] > 170 and 425 + 50 > mouse[1] > 425:
        s = pygame.Surface((255, 50))
        s.set_alpha(50)
        s.fill((200, 0, 0))
        gameDisplay.blit(s, (170, 425))
        if click[0] == 1:
            action_hostgame()
            pygame.quit()
            quit()
    else:
        s = pygame.Surface((250, 50))
        s.set_alpha(0)
        gameDisplay.blit(s, (170, 425))


def button_connect():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 95 + 485 > mouse[0] > 95 and 460 + 50 > mouse[1] > 460:
        s = pygame.Surface((410, 50))
        s.set_alpha(50)
        s.fill((200, 0, 0))
        gameDisplay.blit(s, (95, 485))
        if click[0] == 1:
            action_connectgame()
            pygame.quit()
            quit()
    else:
        s = pygame.Surface((410, 50))
        s.set_alpha(0)
        gameDisplay.blit(s, (95, 485))


def button_tournamnet():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 145 + 310 > mouse[0] > 145 and 540 + 50 > mouse[1] > 540:
        s = pygame.Surface((310, 50))
        s.set_alpha(50)
        s.fill((200, 0, 0))
        gameDisplay.blit(s, (145, 540))
        if click[0] == 1:
            action_tournament()
            pygame.quit()
            quit()
    else:
        s = pygame.Surface((310, 50))
        s.set_alpha(0)
        gameDisplay.blit(s, (145, 540))


def button_back_multi():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 20 + 81 > mouse[0] > 20 and 15 + 67 > mouse[1] > 15:
        s = pygame.Surface((81, 67))
        s.set_alpha(50)
        s.fill((200, 0, 0))
        gameDisplay.blit(s, (20, 15))
        if click[0] == 1:
            action_back_to_main()
            pygame.quit()
            quit()
    else:
        s = pygame.Surface((81, 67))
        s.set_alpha(0)
        gameDisplay.blit(s, (20, 15))


def multiplayer_menu():

    pygame.display.set_caption('Terran Defenders')

    white = (255, 255, 255)

    clock = pygame.time.Clock()
    crashed = False
    img = pygame.image.load('menu_multiplayer.png')

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

        gameDisplay.fill(white)
        gameDisplay.blit(img, (0, 0))
        pygame.display.flip()

        button_host()
        button_connect()
        button_tournamnet()
        button_back_multi()

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()


if __name__ == '__main__':

    multiplayer_menu()
    pygame.quit()
