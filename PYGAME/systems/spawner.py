import random
from entities.enemy import Enemy
from settings import WIDTH, HEIGHT, SPAWN_INTERVAL

class Spawner:
    def __init__(self, game):
        self.game = game
        self.timer = 0
    
    def update(self, dt):
        self.timer += dt
        
        if self.timer >= SPAWN_INTERVAL:
            self.timer = 0
            self.spawn_enemy()
    
    def spawn_enemy(self):
        side = random.choice(["top", "bottom", "left", "right"])
        
        if side == "top":
            pos = (random.randint(0, WIDTH), 0)
        if side == "bottom":
            pos = (random.randint(0, WIDTH), HEIGHT)
        if side == "left":
            pos = (0, random.randint(0, HEIGHT))
        if side == "right":
            pos = (WIDTH, random.randint(0, HEIGHT))

        enemy = Enemy(self.game, pos, size=(25, 25), color=(255, 0, 0))
        self.game.enemies.add(enemy)
        self.game.all_sprites.add(enemy)