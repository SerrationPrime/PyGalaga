
class ServerChangeData():
    def __init__(self, enemy_coords, projectile_coords, player_projectile_coords,
                 player_coords, players_lives, screen):
        self.enemy_coordinates = enemy_coords
        self.projectile_coordinates = projectile_coords
        self.player_projectile_coordinates = player_projectile_coords
        self.player_coordinates = player_coords
        self.player_lives = players_lives
        self.screen = screen

