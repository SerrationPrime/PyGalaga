import pygame
from PyGalaga.enemy_entities import EnemyGroup

pygame.init()


width = 800
height = 600
display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Invaders')
bg_img = pygame.image.load('backgrounds/sunrise.jpg')
clock = pygame.time.Clock()
display.blit(bg_img, [0,0])

group = EnemyGroup()

print('{}'.format(len(group.enemy_list)))
for enemy in group.enemy_list:
    print('{} ({},{})'.format(enemy.name, enemy.x_coord, enemy.y_coord))
def show_enemies():
    for i in range(group.rows*group.columns):
            enemy = group.enemy_list[i]
            display.blit(enemy.image, (enemy.x_coord, enemy.y_coord))

show_enemies()
pygame.display.update()
clock.tick(60)

"""" # za testiranje
crashed = False
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
"""
pygame.quit()