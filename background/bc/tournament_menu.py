import pygame
from tournament_menu_btnfunc import action_create_tournament, action_join_tournament


def button_create():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 65 + 445 > mouse[0] > 65 and 405 + 50 > mouse[1] > 405:
        s = pygame.Surface((445, 50))
        s.set_alpha(50)
        gameDisplay.blit(s, (65, 405))
        if click[0] == 1:
            action_create_tournament()
            pygame.quit()
            quit()
    else:
        s = pygame.Surface((445, 50))
        s.set_alpha(0)
        gameDisplay.blit(s, (65, 405))


def button_join():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 95 + 395 > mouse[0] > 95 and 460 + 50 > mouse[1] > 460:
        s = pygame.Surface((395, 50))
        s.set_alpha(50)
        gameDisplay.blit(s, (90, 460))
        if click[0] == 1:
            action_join_tournament()
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
img = pygame.image.load('tournament_menu.png')

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    gameDisplay.fill((white))
    gameDisplay.blit(img, (0, 0))
    pygame.display.flip()

    button_create()
    button_join()

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()

