import pygame
from PyGalaga.game_enums import Direction, EnemyNames

class Enemy(pygame.sprite.Sprite):
    def __init__(self, image, name, x_coord, y_coord):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.image_width = 50
        self.image_height = 50
        self.name = name        # ime je dodato da ne bi morala da predjem na dictionary sa liste, posto mi dictionary ne garantuje da je redosled dodavanja isti kao redosled prolazenja
        self.lives = 1
        self.speed = 5
        self.fire_rate = 5
        self.x_coord = x_coord
        self.y_coord = y_coord

class EnemyGroup(pygame.sprite.Sprite):
    def __init__(self,):    # neka se u listu pakuju enemies po redovima
        self.direction = Direction.Left
        self.rows = 3
        self.columns = 10
        self.speed = 60  # razmak izmedju pocetka jednog avatara i pocetka dugog avatara
        self.enemy_images = self.get_enemy_images()
        self.enemy_list = self.get_enemies()

    def get_enemy_images(self):
        images = []
        for i in range(self.rows):
            for j in range(self.columns):
                if i == 0:
                    images.append(pygame.image.load('sprites/m_cruiser_enemy1.png'))
                elif i == 1:
                    images.append(pygame.image.load('sprites/m_drone_enemy1.png'))
                elif i == 2:
                    images.append(pygame.image.load('sprites/m_inteceptor_enemy1.png'))
        return images

    def get_enemies(self):  # za postavljanje neprijatelja na pocetne pozicije
        enemies = []
        x_begin = 105
        nx_coord = 105
        ny_coord = 10
        enemy = Enemy(self.enemy_images[0], EnemyNames.Cruiser, 0, 0)

        for i in range(self.rows):
            for j in range(self.columns):
                index = i*self.columns+j
                if i == 0:
                    enemy = Enemy(self.enemy_images[index], EnemyNames.Cruiser, nx_coord, ny_coord)
                    if j == 9:
                        ny_coord = ny_coord + self.speed
                        nx_coord = x_begin
                    else:
                        nx_coord = nx_coord + self.speed
                elif i == 1:
                    enemy = Enemy(self.enemy_images[index], EnemyNames.Drone, nx_coord, ny_coord)
                    if j == 9:
                        ny_coord = ny_coord + self.speed
                        nx_coord = x_begin
                    else:
                        nx_coord = nx_coord + self.speed
                elif i == 2:
                    enemy = Enemy(self.enemy_images[index], EnemyNames.Inteceptor1, nx_coord, ny_coord)
                    if j == 9:
                        ny_coord = ny_coord + self.speed
                        nx_coord = x_begin
                    else:
                        nx_coord = nx_coord + self.speed

                enemies.append(enemy)

        return enemies



    def update(self):
        '''
        for i in range(self.rows):
            for j in range(self.columns):
                index = i * self.columns + j
                enemy = self.enemy_list[index]
                if self.direction == Direction.Right & enemy.x_coord + enemy.speed > self.screen.width :   # ako izlazi iz granica ekrana, nek promeni pravac kretanja
                    self.direction = Direction.Left
                #ovde koristim name za kretanje
                # za kretanje ulevo -
                # za kretanje udesno +


                elif self.direction == Direction.Left & enemy.x_coord - enemy.speed < 0:
                    #ako bi iskocio iz rama sa leve strane
                    self.direction = Direction.Right

        self.show_enemies()

        '''