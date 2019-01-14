import pygame
from host_menu_btnfunc import *


pygame.init()

display_width = 600
display_height = 1000

gameDisplay = pygame.display.set_mode((display_width, display_height))


def button_start():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 390 + 130 > mouse[0] > 390 and 615 + 50 > mouse[1] > 615:
        s = pygame.Surface((130, 50))
        s.set_alpha(50)
        s.fill((200, 0, 0))
        gameDisplay.blit(s, (390, 615))
        if click[0] == 1:
            action_start_multi()
            pygame.quit()
            quit()
    else:
        s = pygame.Surface((130, 50))
        s.set_alpha(0)
        gameDisplay.blit(s, (390, 615))


def button_back_host():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 20 + 81 > mouse[0] > 20 and 15 + 67 > mouse[1] > 15:
        s = pygame.Surface((81, 67))
        s.set_alpha(50)
        s.fill((200, 0, 0))
        gameDisplay.blit(s, (20, 15))
        if click[0] == 1:
            action_back_to_multi()
            pygame.quit()
            quit()
    else:
        s = pygame.Surface((81, 67))
        s.set_alpha(0)
        gameDisplay.blit(s, (20, 15))


def host_menu():
    pygame.display.set_caption('Terran Defenders')

    white = (255, 255, 255)

    clock = pygame.time.Clock()
    crashed = False
    img = pygame.image.load('menu_host_game.png')

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

        gameDisplay.fill((white))
        gameDisplay.blit(img, (0, 0))
        pygame.display.flip()

        button_start()
        button_back_host()

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()


if __name__ == '__main__':
    pygame.init()
    host_menu()
    pygame.quit()
