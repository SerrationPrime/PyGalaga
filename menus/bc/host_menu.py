import pygame
from host_menu_btnfunc import action_start_multi


def button_start():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 370 + 130 > mouse[0] > 370 and 585 + 50 > mouse[1] > 585:
        s = pygame.Surface((130, 50))
        s.set_alpha(50)
        gameDisplay.blit(s, (370, 585))
        if click[0] == 1:
            action_start_multi()
            pygame.quit()
            quit()
    else:
        s = pygame.Surface((130, 50))
        s.set_alpha(0)
        gameDisplay.blit(s, (370, 585))


pygame.init()

display_width = 576
display_height = 960

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Terran Defenders')

black = (0, 0, 0)
white = (255, 255, 255)

clock = pygame.time.Clock()
crashed = False
img = pygame.image.load('host_game_menu.png')

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    gameDisplay.fill((white))
    gameDisplay.blit(img, (0, 0))
    pygame.display.flip()

    button_start()

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()

