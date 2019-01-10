import pygame
from PyGalaga.game_enums import Direction, EnemyNames
from random import Random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, image, name, x_coord, y_coord, row, column):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.left = x_coord
        self.rect.top = y_coord
        self.name = name
        self.image_width = 50
        self.image_height = 50
        self.lives = 1
        self.speed = 10
        self.fire_rate = 5
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.row = row
        self.column = column
        self.go_back = False

class EnemyGroup(pygame.sprite.Sprite):
    def __init__(self,):    # neka se u listu pakuju enemies po redovima
        self.direction = Direction.Right
        self.rows = 3
        self.columns = 10
        self.distance = 60  # razmak izmedju pocetka jednog avatara i pocetka dugog avatara
        self.speed = 2
        self.enemy_images = self.get_enemy_images()
        self.enemy_list = self.get_enemies()
        self.drifters_list = []
        self.screen_width = 800
        self.screen_height = 600

    def get_enemy_images(self):
        images = []
        for i in range(self.rows):
            for j in range(self.columns):
                if i == 0:
                    images.append(pygame.image.load('sprites/m_cruiser_enemy1.png').convert_alpha())
                elif i == 1:
                    images.append(pygame.image.load('sprites/m_drone_enemy1.png').convert_alpha())
                elif i == 2:
                    images.append(pygame.image.load('sprites/m_inteceptor_enemy1.png').convert_alpha())
        return images

    def get_enemies(self):  # za postavljanje neprijatelja na pocetne pozicije
        enemies = []
        x_begin = 105
        nx_coord = 105
        ny_coord = 10
        enemy = Enemy(self.enemy_images[0], EnemyNames.Cruiser, 0, 0, 0, 0)

        for i in range(self.rows):
            for j in range(self.columns):
                index = i*self.columns+j
                if i == 0:
                    enemy = Enemy(self.enemy_images[index], EnemyNames.Cruiser, nx_coord, ny_coord, i, j)
                    if j == 9:
                        ny_coord = ny_coord + self.distance
                        nx_coord = x_begin
                    else:
                        nx_coord = nx_coord + self.distance
                elif i == 1:
                    enemy = Enemy(self.enemy_images[index], EnemyNames.Drone, nx_coord, ny_coord, i, j)
                    if j == 9:
                        ny_coord = ny_coord + self.distance
                        nx_coord = x_begin
                    else:
                        nx_coord = nx_coord + self.distance
                elif i == 2:
                    enemy = Enemy(self.enemy_images[index], EnemyNames.Inteceptor1, nx_coord, ny_coord, i, j)
                    if j == 9:
                        ny_coord = ny_coord + self.distance
                        nx_coord = x_begin
                    else:
                        nx_coord = nx_coord + self.distance

                enemies.append(enemy)

        return enemies

    def boundary_reached(self):
        ret  = False
        if self.direction == Direction.Right:
            for i in range(self.enemy_list.__len__()):
                if self.enemy_list[i].x_coord+self.distance >= self.screen_width:
                    ret =  True
        else:
            for i in range(self.enemy_list.__len__()):
                if self.enemy_list[i].x_coord-self.distance <= 0:
                    ret =  True
        return ret

    def update(self):
        #if self.enemy_list.__len__()<30:
         #   pass
        #else:
        if self.direction == Direction.Right:
            for index in range(self.enemy_list.__len__()):
                enemy = self.enemy_list[index]
                # samo kretanje svih avatara u desno
                if self.enemy_list[index].x_coord + self.distance < self.screen_width:
                    self.enemy_list[index].x_coord = self.enemy_list[index].x_coord + self.speed
                else:
                    self.enemy_list[index].x_coord = self.enemy_list[index].x_coord
                if self.boundary_reached():
                    self.direction = Direction.Left
        else:
            for index in range(self.enemy_list.__len__()):
                enemy = self.enemy_list[index]
                # samo kretanje svih avatara na levo
                self.enemy_list[index].x_coord = self.enemy_list[index].x_coord - self.speed
                if self.boundary_reached():
                    self.direction = Direction.Right


    def refresh(self):
        #stara se o brisanju neprijatelja iz odgovarajuce liste
        for enemy in self.enemy_list:
            if enemy.lives < 1:
                self.enemy_list.remove(enemy)
        for drifter in self.drifters_list:
            if drifter.lives < 1:
                self.drifters_list.remove(drifter)

    def choose_drifters(self):
    #pazi na indexe datih avatara (izabere 29, a imam 7 avatara...)
    #ovim se biraju indeksi 5 aviona koji ce poceti da se spustaju na zemlju i ti avioncici se ppostavljaju u listu driftera u grupi, a brisu se iz liste neprijatelja
    #to znaci da ce i o  njima morati da se vodi racuna u posebnoj lisdti, pri gubljenju zivota
        indexes = []
        r = Random()
        if self.enemy_list.__len__() >= 5:
            for i in range(5):
                idx = r.randint(0, self.enemy_list.__len__())
                if not indexes.__contains__(idx):
                    indexes.append(idx)
                else:
                    idx = r.randint(0, self.enemy_list.__len__())
                    indexes.append(idx)
        else:
            for i in range(self.enemy_list.__len__()):
                indexes.append(i)

        indexes.sort()
        indexes.reverse()

        for idx in indexes:
            self.drifters_list.append(self.enemy_list[idx])
            self.enemy_list.remove(self.enemy_list[idx])
        #sada avioni koji se obrusavaju treba da postoje samo u listi driftera


    def drifting(self):
        #svakog od neprijateljskih aviona iz odabrane grupe se spusta jedan po jedan, do samog dna ekrana
        #potom se dizu do svoje pozicije (v, k) i vracaju se u listu neprijatelja
        #hide t

        self.choose_drifters()

        for drifter in self.drifters_list:
            if not drifter.go_back:
                drifter.y_coord = drifter.y_coord + drifter.speed
                if drifter.y_coord >= self.screen_height:
                    drifter.go_back = True
            else:
                drifter.y_coord = drifter.y_coord - drifter.speed
        #kada da se zaustavi?

        self.refresh()

