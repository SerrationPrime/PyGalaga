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


def initialize_game(multiplayer):
    p = Process(target=update_state, args=[multiplayer])
    p.start()
    p.join()


def update_state(multi):
    width = 600
    height = 800
    level = 1
    in_level = True
    level_delay = 180
    level_timer = 0

    multiplayer = multi

    init()
    screen = display.set_mode((width, height))
    display.flip()

    screen.fill([255, 255, 255])
    bground = Background('backgrounds/starfield.png', [0, 0])
    screen.blit(bground.image, bground.rect)

    myfont = font.SysFont("Miriad Pro Regular", 36)

    player1 = Player(1, [40, 600])
    label = myfont.render("Score: %s" % (player1.score), 1, (255, 255, 0))
    screen.blit(label, (420, 750))
    label2 = myfont.render("Lives: %s" % player1.lives, 1, (255, 255, 0))
    screen.blit(label2, (50, 750))
    label3 = myfont.render("Level: %s" % level, 1, (255, 255, 0))
    screen.blit(label3, (240, 750))

    if multiplayer:
        player2 = Player(2, [560, 600])
        labelp = myfont.render("Score: %s" % (player2.score), 1, (255, 255, 0))
        screen.blit(labelp, (420, 750))
        label2p = myfont.render("Lives: %s" % player2.lives, 1, (255, 255, 0))
        screen.blit(label2p, (50, 750))

    display.update()

    timekeeper = time.Clock()

    player_projectiles = sprite.Group()
    if multiplayer:
        player2_projectiles = sprite.Group()
    enemy_projectiles = sprite.Group()
    formation1 = EnemyGroup(4+level)

    game_active = True

    while game_active:
        event.pump()
        keys = key.get_pressed()

        if sprite.spritecollideany(player1, enemy_projectiles)is not None and player1.invuln_timer == 0:
            player1.lives -=1
            player1.invuln_timer = player1.invuln_len
            sprite.spritecollideany(player1, enemy_projectiles).kill()
            if player1.lives <=0:
                player1.alive=False
            if player1.lives <=0:
                if (multiplayer and player2.lives <=0) or (not multiplayer):
                    label = myfont.render("GAME OVER", 1, (255, 255, 0))
                    screen.blit(label, (230, 400))
                    game_active = False

        if multiplayer:
            if sprite.spritecollideany(player2, enemy_projectiles)is not None and player2.invuln_timer == 0:
                player2.lives -=1
                player2.invuln_timer = player2.invuln_len
                sprite.spritecollideany(player2, enemy_projectiles).kill()
                if player2.lives <= 0:
                    player2.alive = False
                if player1.lives <=0 and player2.lives <= 0:
                    label = myfont.render("GAME OVER", 1, (255, 255, 0))
                    screen.blit(label, (230, 400))
                    game_active=False

        if len(sprite.groupcollide(formation1.special_enemies, player_projectiles, True, True)) > 0:
            player1.score += 1000
        if multiplayer:
            if len(sprite.groupcollide(formation1.special_enemies, player2_projectiles, True, True)) > 0:
                player2.score += 1000

        play1_kills = len(sprite.groupcollide(formation1.enemies, player_projectiles, True, True))
        player1.score += play1_kills * 10
        formation1.enemy_count -= play1_kills
        if multiplayer:
            play2_kills = len(sprite.groupcollide(formation1.enemies, player2_projectiles, True, True))
            player2.score += play2_kills * 10
            formation1.enemy_count -= play2_kills
        if formation1.enemy_count <=0 and in_level:
            in_level = False
            player1.lives=3
            player1.alive=True
            if multiplayer:
                player2.lives=3
                player2.alive=True
            level_timer = level_delay
        elif not in_level:
            level_timer -=1
            if level_timer ==0:
                formation1.aggro_factor += 1
                formation1.get_enemies()
                level += 1
                in_level = True

        if player1.alive:
            if player1.update(keys, screen):
                player_projectiles.add(Projectile(Factions.Player, 0, -10, player1.rect.center))
        if multiplayer and player2.alive:
            if player2.update(keys, screen):
                player2_projectiles.add(Projectile(Factions.Player, 0, -10, player2.rect.center))
        formation1.update(screen, enemy_projectiles)

        player_projectiles.update(screen)
        enemy_projectiles.update(screen)
        label = myfont.render("Score: %s" % (player1.score), 1, (255, 255, 0))
        label2 = myfont.render("Lives: %s" % (player1.lives), 1, (255, 255, 0))
        label3 = myfont.render("Level: %s" % level, 1, (255, 255, 0))
        if multiplayer:
            player2_projectiles.update(screen)
            labelp = myfont.render("Score: %s" % (player2.score), 1, (255, 255, 0))
            label2p = myfont.render("Lives: %s" % (player2.lives), 1, (255, 255, 0))

        screen.blit(label, (420, 700))
        screen.blit(label2, (50, 700))
        screen.blit(label3, (240, 700))
        if multiplayer:
            screen.blit(labelp, (420, 750))
            screen.blit(label2p, (50, 750))
        display.update()
        screen.blit(bground.image, bground.rect)

        if game_active == False:
            time.wait(2000)
            quit()

        timekeeper.tick(60)


if __name__ == '__main__':
    initialize_game(False)
