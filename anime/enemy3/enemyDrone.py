import sys
import sprite
import pygame
from pygame.locals import Color, KEYUP, K_ESCAPE, K_RETURN
from sprite_strip_anim import SpriteStripAnim
from explosionSprite import exp


def enemyDrone1():
    surface = pygame.display.set_mode((50, 50))
    FPS = 60
    frames = FPS / 3
    strips1 = [
        SpriteStripAnim('enemy30001.png', (0, 0, 50, 50), 1, 1, True, frames),
        SpriteStripAnim('enemy30002.png', (0, 0, 50, 50), 1, 1, True, frames),
        SpriteStripAnim('enemy30003.png', (0, 0, 50, 50), 1, 1, True, frames)

    ]
    black = Color('black')
    clock = pygame.time.Clock()
    n = 0
    strips1[n].iter()
    image = strips1[n].next()
    while True:
        for e in pygame.event.get():
            if e.type == KEYUP:
                if e.key == K_ESCAPE:
                    exp()
                    sys.exit()

        n += 1
        if n >= len(strips1):
            n = 0
        strips1[n].iter()
        surface.fill(black)
        surface.blit(image, (0, 0))
        pygame.display.flip()
        image = strips1[n].next()
        clock.tick(FPS)
