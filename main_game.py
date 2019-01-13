from multiprocessing import Process
from PyGalaga.entities import *
from PyGalaga.enemy_entities import *
from PyGalaga.networking.server import Server
from PyGalaga.networking.server_change_data import ServerChangeData

class Background(sprite.Sprite):
    def __init__(self, image_file, location):
        sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = image.load(image_file).convert_alpha()   #vazno je convert_alpha za performanse
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

def get_nb_players():
    return 1

class GameController():
    def __init__(self):
        self.nb_players = get_nb_players() # za pocetak
        self.players = []
        self.keys = []
        self.player_projectiles = sprite.Group()
        self.enemy_projectiles = sprite.Group()
        self.formation1 = EnemyGroup()
        self.screen = display.set_mode((600, 800))
        self.enemy_coordinates = []
        self.projectiles_coordinates = []
        self.player_projectile_coordinates = []
        self.player_coordinates = []
        self.player_lives = []

    def collect_changes(self):
        changes = ServerChangeData(self.enemy_coordinates, self.projectiles_coordinates, self.player_projectile_coordinates, self.player_coordinates, self.player_lives)
        return changes

    def initialize_players(self):
        for i in range(get_nb_players()):
            player = Player(i+1, [40+i*50, 600])
            self.players.append(player)


    # u sustini cu ga videti samo kada ga player pozove, tako da ce samo na njegov display uticati,
    # dok ce sam server ostati nepromenjen (simulira se po planu)
    def apply_changes(self, command):
        self.enemy_coordinates = command.enemy_coordinates
        self.projectiles_coordinates = command.projectile_coordinates
        self.player_projectile_coordinates = command.player_projectile_coordinates
        self.player_coordinates = command.player_coordinates
        self.player_lives = command.player_lives

    def update_player(self, keys):
        self.keys.append(keys)

    def update_state(self):
        self.initialize_players()
        init()
        display.flip()

        self.screen.fill([255, 255, 255])
        bground = Background('backgrounds/starfield.png', [0, 0])
        self.screen.blit(bground.image, bground.rect)

        display.update()
        timekeeper = time.Clock()
        done = False
        while not done:
            event.pump()
            # ovo treba da ostane zbog servera
            for i in range(len(self.players)):
                keys = list(self.keys[i])
                if self.players[i].update(keys, self.screen):
                    self.player_projectiles.add(Projectile(Factions.Player, 0, -10, self.players[i].rect.center))
                self.formation1.update(self.screen, self.enemy_projectiles)

                sprite.groupcollide(self.player_projectiles, self.formation1.enemies, True, True)
                if sprite.spritecollideany(self.players[i], self.enemy_projectiles) is not None:
                    self.players[i].lives -= 1
                    sprite.spritecollideany(self.players[i], self.enemy_projectiles).kill()
                    if self.players[i].lives <= 0:
                        exit()

            self.keys.remove(keys[:])

            self.player_projectiles.update(self.screen)
            self.enemy_projectiles.update(self.screen)

            display.update()
            self.screen.blit(bground.image, bground.rect)

            for event_ in event.get():  # User did something
                if event_.type == QUIT:  # If user clicked close
                    done = True

            if done:
                quit()

            timekeeper.tick(60)
    #add logic from main game

    def initialize_game(self):
        # initialize server
        server = Server('192.168.100.196', 5555, self.nb_players)
        server.start_server()

        p = Process(target=self.update_state())
        p.start()
        p.join()


if __name__ == '__main__':
    gc = GameController()
    gc.initialize_game()
