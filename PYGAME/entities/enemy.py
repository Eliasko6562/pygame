import pygame as pg
from entities.entity import Entity
from settings import ENEMY_SPEED

class Enemy(Entity):
    def __init__(self, game, pos, size, color):
        super().__init__(game, pos, size, color)
        
    def update(self, dt):
        direction = self.game.player.pos - self.pos
        
        if direction.length() > 0:
            direction = direction.normalize()
            
        self.pos += direction * ENEMY_SPEED * dt
        self.rect.center = self.pos