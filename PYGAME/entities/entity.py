import pygame as pg

class Entity(pg.sprite.Sprite):
    def __init__(self, game, pos, size, color):
        super().__init__()
        self.game = game