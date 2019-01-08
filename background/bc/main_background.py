import pygame
from main_menu_btnfunc import action_open_multi, action_signal_single


def button_single():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 135 + 310 > mouse[0] > 135 and 415 + 50 > mouse[1] > 415:
        s = pygame.Surface((310, 50))
        s.set_alpha(50)
        gameDisplay.blit(s, (135, 415))
        if click[0] == 1:
            action_signal_single()
            pygame.quit()
            quit()
    else:
        s = pygame.Surface((310, 50))
        s.set_alpha(0)
        gameDisplay.blit(s, (135, 415))


def button_multi():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 145 + 285 > mouse[0] > 145 and 470 + 50 > mouse[1] > 470:
        s = pygame.Surface((285, 50))
        s.set_alpha(50)
        gameDisplay.blit(s, (145, 470))
        if click[0] == 1:
            action_open_multi()
            pygame.quit()
            quit()
    else:
        s = pygame.Surface((285, 50))
        s.set_alpha(0)
        gameDisplay.blit(s, (145, 470))


def button_exit():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 240 + 95 > mouse[0] > 240 and 525 + 50 > mouse[1] > 525:
        s = pygame.Surface((95, 50))
        s.set_alpha(50)
        gameDisplay.blit(s, (240, 525))
        if click[0] == 1:
            pygame.quit()
            quit()
    else:
        s = pygame.Surface((95, 50))
        s.set_alpha(0)
        gameDisplay.blit(s, (240, 525))


pygame.init()

display_width = 576
display_height = 960

gameDisplay = pygame.display.set_mode((display_width, display_height))
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

