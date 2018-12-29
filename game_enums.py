from enum import Enum


class Factions(Enum):
    Player = 1
    Enemy = 2
    

class Direction(Enum):
    Left = 1
    Right = 2


class EnemyNames(Enum):
    Cruiser = 1
    Drone = 2
    Inteceptor1 = 3
    Inteceptor2 = 4
    Stalker = 5
