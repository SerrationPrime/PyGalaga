from pygame import *
from game_enums import Factions


class Player(sprite.Sprite):
    def __init__(self, play_num, location):
        sprite.Sprite.__init__(self)

        if play_num == 1:
            self.image = image.load('sprites/m_play_char.png').convert_alpha()
        elif play_num == 2:
            self.image = image.load('sprites/m_play_char2.png').convert_alpha()
        else:
            self.image = image.load('sprites/m_play_char.png').convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

        self.lives = 3
        self.score = 0

        self.speed = 5
        self.fire_rate = 5
        self.reload = 0

        # Vraca true ako treba da se kreira projektil
    def update(self, keys, screen, *args):
        retval = False
        if keys[K_a] and self.rect.x > 10:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.right < 590:
            self.rect.x += self.speed
        if keys[K_w] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.bottom < 990:
            self.rect.y += self.speed
        if keys[K_SPACE] and self.reload <= 0:
            self.reload = 60/self.fire_rate
            retval = True
        else:
            if self.reload > 0:
                self.reload -= 1
        screen.blit(self.image, self.rect)
        return retval


class Projectile(sprite.Sprite):
    def __init__(self, faction, xspeed, yspeed, location):
        sprite.Sprite.__init__(self)
        self.faction = faction

        if faction == Factions.Enemy:
            self.image = image.load('sprites/m_projectile_enemy1.png').convert_alpha()
        else:
            self.image = image.load('sprites/m_projectile_plasma1.png').convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.rect.x -= self.rect.width/2

        self.xspeed = xspeed
        self.yspeed = yspeed

        # Vraca true ako treba izbrisati projektil
    def update(self, screen):
        # Moguci problemi sa negativnim koordinatama?
        self.rect.x += self.xspeed
        self.rect.y += self.yspeed

        screen.blit(self.image, self.rect)

        if self.rect.x <=0 or self.rect.x>=600 or self.rect.y <=0 or self.rect.y >= 1000:
            self.kill()
