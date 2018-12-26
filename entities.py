class Player:
    def __init__(self, label):
        self.label = label
        self.lives = 3
        self.score = 0

        self.fire_rate=5
        self.reload=0


class Projectile:
    def __init__(self, label, faction, xspeed, yspeed):
        self.label = label
        self.faction = faction
        self.xspeed = xspeed
        self.yspeed = yspeed

class Enemy:
    def __init__(self, label):
        self.label = label