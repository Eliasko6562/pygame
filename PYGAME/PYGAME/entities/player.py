import pygame as pg
from entities.entity import Entity
from settings import PLAYER_SPEED, WIDTH, HEIGHT
from entities.bullet import Bullet

class Player(Entity):
    def __init__(self, game, pos, size, color):
        super().__init__(game, pos, size=(50, 50), color=(0, 255, 0))
        
    def update(self, dt):
        keys = pg.key.get_pressed()
        vel = pg.Vector2(0, 0)
        
        if keys[pg.K_LEFT]:
            vel.x = -1
        if keys[pg.K_RIGHT]:
            vel.x = 1
        if keys[pg.K_UP]:
            vel.y = -1
        if keys[pg.K_DOWN]:
            vel.y = 1
            
        if vel.length() > 0:
            vel = vel.normalize()
        
        self.pos += vel * PLAYER_SPEED * dt
        self.rect.center = self.pos
        
        # Keep player within screen bounds
        self.rect.clamp_ip(pg.Rect(0, 0, WIDTH, HEIGHT))
        self.pos = pg.Vector2(self.rect.center)
        
        # Teachers way of doing it
        # half_width = self.rect.width / 2
        # half_height = self.rect.height / 2
        # self.pos.x = max(half_width, min(WIDTH - half_width, self.pos.x))
        # self.pos.y = max(half_height, min(HEIGHT - half_height, self.pos.y))
        
    def shoot(self):
        mouse_ps = pg.Vector2(pg.mouse.get_pos())
        
        direction = (mouse_ps - self.pos)
        
        if 0 < direction.length() < 100:
            direction = direction.normalize()
        
        bullet = Bullet(self.game, self.pos, direction)
        self.game.bullets.add(bullet)
        self.game.all_sprites.add(bullet)