import pygame


def image(pathname):
    pygame.init()

    display_width = 576
    display_height = 960

    gameDisplay = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption('Terran Defenders')

    black = (0, 0, 0)
    white = (255, 255, 255)

    clock = pygame.time.Clock()
    crashed = False
    img = pygame.image.load(pathname)

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

        gameDisplay.fill((white))
        gameDisplay.blit(img, (0, 0))
        pygame.display.flip()

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()

