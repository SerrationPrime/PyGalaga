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
    level = 1
    in_level = True
    level_delay = 180
    level_timer = 0

    init()
    screen = display.set_mode((width, height))
    display.flip()

    screen.fill([255, 255, 255])
    bground = Background('backgrounds/starfield.png', [0, 0])
    screen.blit(bground.image, bground.rect)

    myfont = font.SysFont("Miriad Pro Regular", 36)

    player1 = Player(1, [40, 600])
    label = myfont.render("Score: %s" % player1.score, 1, (255, 255, 0))
    screen.blit(label, (420, 750))
    label2 = myfont.render("Lives: %s" % player1.lives, 1, (255, 255, 0))
    screen.blit(label2, (50, 750))
    label3 = myfont.render("Level: %s" % level, 1, (255, 255, 0))
    screen.blit(label3, (240, 750))

    display.update()

    timekeeper = time.Clock()

    player_projectiles = sprite.Group()
    enemy_projectiles = sprite.Group()
    formation1 = EnemyGroup(4+level)

    while True:
        event.pump()
        keys = key.get_pressed()

        if sprite.spritecollideany(player1, enemy_projectiles)is not None and player1.invuln_timer == 0:
            player1.lives -=1
            player1.invuln_timer = player1.invuln_len
            sprite.spritecollideany(player1, enemy_projectiles).kill()
            if player1.lives <= 0:
                label1 = myfont.render("GAME OVER", 1, (255, 255, 0))
                label2 = myfont.render("SCORE: %s" % player1.score, 1, (255, 255, 0))
                screen.blit(label1, (230, 400))
                screen.blit(label2, (230, 450))
                display.update()
                time.wait(2000)
                exit()

        if len(sprite.groupcollide(formation1.special_enemies, player_projectiles, True, True)) > 0:
            player1.score += 1000

        play1_kills = len(sprite.groupcollide(formation1.enemies, player_projectiles, True, True))
        player1.score += play1_kills * 10
        formation1.enemy_count -= play1_kills
        if formation1.enemy_count <=0 and in_level:
            in_level = False
            level_timer = level_delay
        elif not in_level:
            level_timer -=1
            if level_timer ==0:
                formation1.aggro_factor += 1
                formation1.get_enemies()
                level += 1
                in_level = True

        if player1.update(keys, screen):
            player_projectiles.add(Projectile(Factions.Player, 0, -10, player1.rect.center))
        formation1.update(screen, enemy_projectiles)

        player_projectiles.update(screen)
        enemy_projectiles.update(screen)
        label = myfont.render("Score: %s" % (player1.score), 1, (255, 255, 0))
        label2 = myfont.render("Lives: %s" % (player1.lives), 1, (255, 255, 0))
        label3 = myfont.render("Level: %s" % level, 1, (255, 255, 0))

        display.update()
        screen.blit(bground.image, bground.rect)
        screen.blit(label, (420, 750))
        screen.blit(label2, (50, 750))
        screen.blit(label3, (240, 750))


        timekeeper.tick(60)


if __name__ == '__main__':
    initialize_game()
