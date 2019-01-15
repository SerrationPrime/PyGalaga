from pygame import *
from game_enums import Factions

class Player(sprite.Sprite):
    def __init__(self, play_num, location):
        sprite.Sprite.__init__(self)
        self.play_num = play_num

        if play_num == 1:
            self.standard_image = 'sprites/m_play_char.png'
            self.invuln_image = 'sprites/m_play_charinvul.png'
        elif play_num == 2:
            self.standard_image = 'sprites/m_play_char2.png'
            self.invuln_image = 'sprites/m_play_char2invul.png'
        else:
            self.standard_image = 'sprites/m_play_char.png'
            self.invuln_image = 'sprites/m_play_charinvul.png'

        self.image = image.load(self.standard_image).convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

        self.lives = 3
        self.score = 0

        self.alive = True

        self.speed = 5
        self.fire_rate = 5
        self.reload = 0
        self.invuln_timer = 0
        self.invuln_len = 120

        # Vraca true ako treba da se kreira projektil
    def update(self, keys, screen, *args):
        retval = False
        if self.play_num == 1:
            if keys[K_a] and self.rect.x > 10:
                self.rect.x -= self.speed
            if keys[K_d] and self.rect.right < 590:
                self.rect.x += self.speed
            if keys[K_w] and self.rect.y > 10:
                self.rect.y -= self.speed
            if keys[K_s] and self.rect.bottom < 790:

                self.rect.y += self.speed
            if keys[K_SPACE] and self.reload <= 0:
                self.reload = 60/self.fire_rate
                retval = True
            else:
                if self.reload > 0:
                    self.reload -= 1
        elif self.play_num == 2:
            if keys[K_j] and self.rect.x > 10:
                self.rect.x -= self.speed
            if keys[K_l] and self.rect.right < 590:
                self.rect.x += self.speed
            if keys[K_i] and self.rect.y > 10:
                self.rect.y -= self.speed
            if keys[K_k] and self.rect.bottom < 790:
                self.rect.y += self.speed
            if keys[K_RETURN] and self.reload <= 0:
                self.reload = 60 / self.fire_rate
                retval = True
            else:
                if self.reload > 0:
                    self.reload -= 1

        if self.invuln_timer>0:
            self.invuln_timer-=1
            if self.invuln_timer == self.invuln_len-1:
                self.image = image.load(self.invuln_image).convert_alpha()
            elif self.invuln_timer == 20:
                self.image = image.load(self.standard_image).convert_alpha()
            elif self.invuln_timer == 15:
                self.image = image.load(self.invuln_image).convert_alpha()
            elif self.invuln_timer == 10:
                self.image = image.load(self.standard_image).convert_alpha()
            elif self.invuln_timer == 5:
                self.image = image.load(self.invuln_image).convert_alpha()
            elif self.invuln_timer == 0:
                self.image = image.load(self.standard_image).convert_alpha()


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


    def update(self, screen):
        # Moguci problemi sa negativnim koordinatama?
        self.rect.x += self.xspeed
        self.rect.y += self.yspeed

        screen.blit(self.image, self.rect)

        if self.rect.x <=0 or self.rect.x >= 600 or self.rect.y <=0 or self.rect.y >= 800:
            self.kill()
