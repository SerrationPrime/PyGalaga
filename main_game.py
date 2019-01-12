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
    score = 0
    display.flip()

    screen.fill([255, 255, 255])
    bground = Background('backgrounds/starfield.png', [0, 0])
    screen.blit(bground.image, bground.rect)

    myfont = font.SysFont("Miriad Pro Regular", 36)

    label = myfont.render("Score: %s" % (score), 1, (255, 255, 0))
    screen.blit(label, (420, 750))

    player1 = Player(1, [40, 600])

    display.update()

    timekeeper = time.Clock()

    player_projectiles = sprite.Group()
    enemy_projectiles = sprite.Group()
    formation1 = EnemyGroup()

    player1.lives = 3
    player1.image.set_alpha(100)
    label2 = myfont.render("Lives: %s" % (player1.lives), 1, (255, 255, 0))
    screen.blit(label2, (50, 750))

    invuln_timer = 0
    while True:
        event.pump()
        keys = key.get_pressed()

        if player1.update(keys, screen):
            player_projectiles.add(Projectile(Factions.Player,0,-10,player1.rect.center))
        formation1.update(screen, enemy_projectiles)

        score += len(sprite.groupcollide(formation1.enemies, player_projectiles, True, True))*10
        if sprite.spritecollideany(player1, enemy_projectiles)is not None and invuln_timer == 0:
            player1.lives -= 1
            invuln_timer = 120
            player1.image = image.load('sprites/m_play_charinvul.png').convert_alpha()
            sprite.spritecollideany(player1, enemy_projectiles).kill()
            if player1.lives <= 0:
                exit()

        player_projectiles.update(screen)
        enemy_projectiles.update(screen)
        label = myfont.render("Score: %s" % (score), 1, (255, 255, 0))
        label2 = myfont.render("Lives: %s" % (player1.lives), 1, (255, 255, 0))

        display.update()
        screen.blit(bground.image, bground.rect)
        screen.blit(label, (420, 750))
        screen.blit(label2, (50, 750))

        if invuln_timer>0:
            invuln_timer-=1
            if invuln_timer <= 20:
                if invuln_timer == 20:
                    player1.image = image.load('sprites/m_play_char.png').convert_alpha()
                if invuln_timer == 15:
                    player1.image = image.load('sprites/m_play_charinvul.png').convert_alpha()
                if invuln_timer == 10:
                        player1.image = image.load('sprites/m_play_char.png').convert_alpha()
                if invuln_timer == 5:
                        player1.image = image.load('sprites/m_play_charinvul.png').convert_alpha()
                if invuln_timer == 0:
                    player1.image = image.load('sprites/m_play_char.png').convert_alpha()
        timekeeper.tick(60)


if __name__ == '__main__':
    initialize_game()
