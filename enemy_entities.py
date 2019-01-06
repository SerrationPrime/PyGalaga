import pygame
from PyGalaga.game_enums import Direction, EnemyNames

class Enemy(pygame.sprite.Sprite):
    def __init__(self, image, name, x_coord, y_coord, row, column):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.image_width = 50
        self.image_height = 50
        self.name = name
        self.lives = 1
        self.speed = 10
        self.fire_rate = 5
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.row = row
        self.column = column

class EnemyGroup(pygame.sprite.Sprite):
    def __init__(self,):    # neka se u listu pakuju enemies po redovima
        self.direction = Direction.Right
        self.rows = 3
        self.columns = 10
        self.speed = 60  # razmak izmedju pocetka jednog avatara i pocetka dugog avatara
        self.enemy_images = self.get_enemy_images()
        self.enemy_list = self.get_enemies()
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
                        ny_coord = ny_coord + self.speed
                        nx_coord = x_begin
                    else:
                        nx_coord = nx_coord + self.speed
                elif i == 1:
                    enemy = Enemy(self.enemy_images[index], EnemyNames.Drone, nx_coord, ny_coord, i, j)
                    if j == 9:
                        ny_coord = ny_coord + self.speed
                        nx_coord = x_begin
                    else:
                        nx_coord = nx_coord + self.speed
                elif i == 2:
                    enemy = Enemy(self.enemy_images[index], EnemyNames.Inteceptor1, nx_coord, ny_coord, i, j)
                    if j == 9:
                        ny_coord = ny_coord + self.speed
                        nx_coord = x_begin
                    else:
                        nx_coord = nx_coord + self.speed

                enemies.append(enemy)

        return enemies

    def boundary_reached(self):
        ret  = False
        if self.direction == Direction.Right:
            for i in range(self.enemy_list.__len__()):
                if self.enemy_list[i].x_coord+self.speed >= self.screen_width:
                    ret =  True
        else:
            for i in range(self.enemy_list.__len__()):
                if self.enemy_list[i].x_coord-self.speed <= 0:
                    ret =  True
        return ret

    def update(self):
        screen_width  = 800
        screen_height = 600

        if len(self.enemy_list)<self.rows*self.columns: # kretanje ako je neki avatar unuisten
            for i in range(self.rows):
                for j in range(self.columns):
                    index = i * self.columns + j
                    enemy = self.enemy_list[index]


        else:   # kretanje kada su svi avatari na broju
            if self.direction == Direction.Right:
                for i in range(self.rows):
                    for j in range(self.columns):
                        index = i * self.columns + j
                        enemy = self.enemy_list[index]
                        # samo kretanje svih avatara u desno
                        self.enemy_list[index].x_coord = self.enemy_list[index].x_coord + self.speed
                        if self.boundary_reached():
                            self.direction = Direction.Left
            else:
                for i in range(self.rows):
                    for j in range(self.columns):
                        index = i * self.columns + j
                        enemy = self.enemy_list[index]
                        # samo kretanje svih avatara na levo
                        self.enemy_list[index].x_coord = self.enemy_list[index].x_coord - self.speed
                        if self.boundary_reached():
                            self.direction = Direction.Right

