from multiprocessing import Process
from entities import *
from pygame import *


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
    height = 1000

    init()
    screen = display.set_mode((width, height))
    display.flip()

    screen.fill([255, 255, 255])
    bground = Background('backgrounds/starfield.png', [0, 0])
    screen.blit(bground.image, bground.rect)

    player1 = Player(1, [40, 40])

    display.update()

    timekeeper = time.Clock()
    while True:
        event.pump()
        keys = key.get_pressed()

        player1.update(keys, screen)

        display.update()
        screen.blit(bground.image, bground.rect)

        timekeeper.tick(60)


if __name__ == '__main__':
    initialize_game()
