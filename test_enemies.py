from pygame import *
from PyGalaga.game_enums import *
from PyGalaga.entities import *
from random import Random
from PyGalaga.enemy_entities import EnemyGroup
from multiprocessing import Process

class Background(sprite.Sprite):
    def __init__(self, image_file, location):
        sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = image.load(image_file).convert_alpha()   #vazno je convert_alpha za performanse
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


def initialize_game():
    p = Process(target=update_state)
    p.start()
    p.join()


def update_state():
    width = 800
    height = 600

    init()
    screen = display.set_mode((width, height))
    display.flip()

    screen.fill([255, 255, 255])
    bground = Background('backgrounds/sunrise.jpg', [0, 0])
    screen.blit(bground.image, bground.rect)

    group = EnemyGroup()

    display.update()

    timekeeper = time.Clock()

    projectiles = sprite.Group()
    done = False
    while not done:
        event.pump()

        show_enemies(group, screen)
        group.update()

        r = Random()
        index = r.randint(0, group.enemy_list.__len__())

        projectiles.add(Projectile(Factions.Enemy,0,10,group.enemy_list[3].rect.center))
        projectiles.update(screen)

        display.update()
        screen.blit(bground.image, bground.rect)

        for enemy in group.enemy_list:
            print('[{}, {}]'.format(enemy.row, enemy.column))

        #if group.enemy_list.__len__() == 30:
         #   group.enemy_list.remove(group.enemy_list[29])
         #   group.enemy_list.remove(group.enemy_list[19])
         #   group.enemy_list.remove(group.enemy_list[9])

        timekeeper.tick(60)

        for sevent in event.get():  # User did something
            if sevent.type == QUIT:  # If user clicked close
                done = True

        if done:
            quit()

def show_enemies(group, screen):
    for i in range(group.enemy_list.__len__()):
            enemy = group.enemy_list[i]
            enemy_rect = Rect(enemy.x_coord, enemy.y_coord, enemy.image_width, enemy.image_height)
            screen.blit(enemy.image, enemy_rect)


if __name__ == '__main__':
    initialize_game()




