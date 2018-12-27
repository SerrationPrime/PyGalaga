import sys
import sprite
import pygame
from pygame.locals import Color, KEYUP, K_ESCAPE, K_RETURN
from sprite_strip_anim import SpriteStripAnim

surface = pygame.display.set_mode((100, 100))
FPS = 120
frames = FPS / 24
strips = [
    SpriteStripAnim('Exp0001.png', (0, 0, 48, 48), 1, 1, True, frames),
    SpriteStripAnim('Exp0002.png', (0, 0, 48, 48), 1, 1, True, frames),
    SpriteStripAnim('Exp0003.png', (0, 0, 48, 48), 1, 1, True, frames),
    SpriteStripAnim('Exp0004.png', (0, 0, 48, 48), 1, 1, True, frames),
    SpriteStripAnim('Exp0005.png', (0, 0, 48, 48), 1, 1, True, frames),
    SpriteStripAnim('Exp0006.png', (0, 0, 48, 48), 1, 1, True, frames),
    SpriteStripAnim('Exp0007.png', (0, 0, 48, 48), 1, 1, True, frames),
    SpriteStripAnim('Exp0008.png', (0, 0, 48, 48), 1, 1, True, frames),
    SpriteStripAnim('Exp0009.png', (0, 0, 48, 48), 1, 1, True, frames)

]
black = Color('black')
clock = pygame.time.Clock()
n = 0
strips[n].iter()
image = strips[n].next()
while True:
    for e in pygame.event.get():
        if e.type == KEYUP:
            if e.key == K_ESCAPE:
                sys.exit()

    n += 1
    if n >= len(strips):
        n = 0
    strips[n].iter()
    surface.fill(black)
    surface.blit(image, (0, 0))
    pygame.display.flip()
    image = strips[n].next()
    clock.tick(FPS)
