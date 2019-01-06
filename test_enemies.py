import pygame
from PyGalaga.enemy_entities import EnemyGroup

pygame.init()

#ZA SADA SE KRECU JAKO BRZO, PODESICU IH BOLJE, imam neki problem sa satom...

width = 800
height = 600
display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Invaders')
bg_img = pygame.image.load('backgrounds/sunrise.jpg').convert_alpha()
clock = pygame.time.Clock()
display.blit(bg_img, [0,0])

group = EnemyGroup()

print('{}'.format(len(group.enemy_list)))
for enemy in group.enemy_list:
    print('{} ({},{})'.format(enemy.name, enemy.x_coord, enemy.y_coord))

def show_enemies():
    for i in range(group.rows*group.columns):
            enemy = group.enemy_list[i]
            enemy_rect = pygame.Rect(enemy.x_coord, enemy.y_coord, enemy.image_width, enemy.image_height)
            display.blit(enemy.image, enemy_rect)
            #enemy.x_coord, enemy.y_coord)

def animation():
    i = 0
    while True:
        display.blit(bg_img, [0, 0])
        show_enemies()
        group.update()
        pygame.display.update()
        clock.tick(5000)
        if i >10:
            break

animation()

for enemy in group.enemy_list:
    print('{} ({},{})'.format(enemy.name, enemy.x_coord, enemy.y_coord))
