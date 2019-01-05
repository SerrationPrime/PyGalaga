import pygame
from multiplayer_menu_btnfunc import action_connectgame, action_hostgame


def button_host():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 165 + 245 > mouse[0] > 165 and 405 + 50 > mouse[1] > 405:
        s = pygame.Surface((245, 50))
        s.set_alpha(50)
        gameDisplay.blit(s, (165, 405))
        if click[0] == 1:
            action_hostgame()
            pygame.quit()
            quit()
    else:
        s = pygame.Surface((245, 50))
        s.set_alpha(0)
        gameDisplay.blit(s, (165, 405))


def button_connect():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 90 + 395 > mouse[0] > 95 and 460 + 50 > mouse[1] > 460:
        s = pygame.Surface((395, 50))
        s.set_alpha(50)
        gameDisplay.blit(s, (90, 460))
        if click[0] == 1:
            action_connectgame()
            pygame.quit()
            quit()
    else:
        s = pygame.Surface((395, 50))
        s.set_alpha(0)
        gameDisplay.blit(s, (90, 460))


pygame.init()

display_width = 576
display_height = 960

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Terran Defenders')

black = (0, 0, 0)
white = (255, 255, 255)

clock = pygame.time.Clock()
crashed = False
img = pygame.image.load('multiplayer_menu.png')

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    gameDisplay.fill((white))
    gameDisplay.blit(img, (0, 0))
    pygame.display.flip()

    button_host()
    button_connect()

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()

