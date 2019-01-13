from pygame import *
from .game_enums import *
from .entities import Projectile
import random

class Enemy(sprite.Sprite):
    def __init__(self, image, name, x_coord, y_coord):
        sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.left = 800
        self.formation_x = x_coord
        self.rect.top = y_coord
        self.formation_y = y_coord

        self.name = name
        self.speed = 1

        self.go_back = True
        self.drifting = False
        self.drifting_speed=10
        self.drifting_barrage=0

    def update(self, screen, projectiles):
        if not ((self.formation_x+self.rect.width+self.speed < 590 and self.speed>0) or (self.formation_x+self.speed>10 and self.speed<0)):
            self.speed *= -1
        self.formation_x += self.speed
        if not (self.drifting or self.go_back):
            self.rect.x += self.speed
        elif self.drifting:
            if self.rect.bottom<500:
                self.rect.y += self.drifting_speed
                if self.drifting_barrage>0:
                    self.drifting_barrage-=1
                else:
                    projectiles.add(Projectile(Factions.Enemy, 0, 30, self.rect.center))
                    self.drifting_barrage = 5
            else:
                self.drifting_barrage = 0
                self.drifting = False
                self.go_back = True
        else:
            self.move_to_position()

        if random.randint(1, 1000)<=2:
            projectiles.add(Projectile(Factions.Enemy, 0, 10, self.rect.center))
        if random.randint(1, 10000)<=2 and not self.drifting:
            self.drifting = True

        screen.blit(self.image,self.rect)

    def move_to_position(self):
        if self.rect.y != self.formation_y:
            distance_to_go = self.formation_y - self.rect.y
            if -5  < distance_to_go < 5:
                self.rect.y = self.formation_y
            else:
                if distance_to_go > 0:
                    self.rect.y += 5
                else:
                    self.rect.y -= 5
            if self.rect.y - self.formation_y < 5:
                self.rect.y = self.formation_y
            else:
                self.rect.y -= 5
        else:
            if self.rect.x != self.formation_x:
                distance_to_go = self.formation_x - self.rect.x
                if -5 < distance_to_go < 5:
                    self.rect.x = self.formation_x
                    go_back = False
                else:
                    if distance_to_go > 0:
                        self.rect.x += 5
                    else:
                        self.rect.x -= 5


class EnemyGroup():
    def __init__(self,):    # neka se u listu pakuju enemies po redovima
        self.rows = 3
        self.columns = 10
        self.distance = 55  # razmak izmedju pocetka jednog avatara i pocetka dugog avatara
        self.enemy_images = self.get_enemy_images()
        self.enemies = self.get_enemies()
        self.screen_width = 600
        self.screen_height = 800

    def get_enemy_images(self):
        images = []
        for i in range(self.rows):
            for j in range(self.columns):
                if i == 0:
                    images.append(image.load('sprites/m_cruiser_enemy1.png').convert_alpha())
                elif i == 1:
                    images.append(image.load('sprites/m_drone_enemy1.png').convert_alpha())
                elif i == 2:
                    images.append(image.load('sprites/m_interceptor_enemy1.png').convert_alpha())
        return images

    def get_enemies(self):  # za postavljanje neprijatelja na pocetne pozicije
        enemies = sprite.Group()
        nx_coord = 10
        ny_coord = 10

        for i in range(self.rows):
            for j in range(self.columns):
                index = i * self.columns + j
                if i==0:
                    enemy_name=EnemyNames.Cruiser
                elif i==1:
                    enemy_name=EnemyNames.Drone
                else:
                    enemy_name=EnemyNames.Interceptor1
                enemy = Enemy(self.enemy_images[index], enemy_name, nx_coord, ny_coord)
                nx_coord += self.distance
                enemies.add(enemy)
            ny_coord += self.distance
            nx_coord = 10
        return enemies

    def update(self,screen,projectiles):
        self.enemies.update(screen,projectiles)

