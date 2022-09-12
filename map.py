import pygame as pg


_ = False
# 1 is object '_' is empty space

mini_map = [
    [1, 1, 3, 1, 3, 1, 1, 3, 5, 5, 2, 5, 2, 5, 2, 2],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 5],
    [3, _, _, _, 3, 3, 4, _, _, _, 5, 2, 2, _, _, 2],
    [1, _, _, _, _, _, 4, _, _, _, _, _, 2, _, _, 5],
    [3, _, _, _, _, _, 4, _, _, _, _, _, 5, _, _, 2],
    [1, _, _, _, 3, 3, 4, _, _, _, _, _, _, _, _, 5],         
    [1, _, _, _, _, _, _, _, _, _, _, _, 2, 5, 5, 2],
    [3, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 5],
    [1, _, _, _, 4, _, _, _, 4, _, _, 2, _, 2, _, 2],
    [1, 1, 1, 3, 1, 3, 1, 1, 1, 5, 5, 2, 5, 2, 5, 2]
]

# putting map into constactor, map and mini map becone attributes

class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.get_map()

# adding only numeric values to the dictionary

    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i, j)] = value

# drawing the 2d map

    def draw(self):
        [pg.draw.rect(self.game.screen, 'darkgray', (pos[0] * 100, pos[1] * 100, 100, 100), 2)
         for pos in self.world_map]