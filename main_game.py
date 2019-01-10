from multiprocessing import Process
from entities import *
from pygame import *
from enemy_entities import *


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
    width = 600
    height = 800

    init()
    screen = display.set_mode((width, height))
    display.flip()

    screen.fill([255, 255, 255])
    bground = Background('backgrounds/starfield.png', [0, 0])
    screen.blit(bground.image, bground.rect)

    player1 = Player(1, [40, 600])

    display.update()

    timekeeper = time.Clock()

    player_projectiles = sprite.Group()
    enemy_projectiles = sprite.Group()
    formation1 = EnemyGroup()

    while True:
        event.pump()
        keys = key.get_pressed()

        if player1.update(keys, screen):
            player_projectiles.add(Projectile(Factions.Player,0,-10,player1.rect.center))
        formation1.update(screen, enemy_projectiles)

        sprite.groupcollide(player_projectiles,formation1.enemies,True,True)
        if sprite.spritecollideany(player1, enemy_projectiles)is not None:
            player1.lives -= 1
            sprite.spritecollideany(player1, enemy_projectiles).kill()
            if player1.lives <= 0:
                exit()

        player_projectiles.update(screen)
        enemy_projectiles.update(screen)

        display.update()
        screen.blit(bground.image, bground.rect)

        timekeeper.tick(60)

if __name__ == '__main__':
    initialize_game()
