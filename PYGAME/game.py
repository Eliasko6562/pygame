import pygame as pg

from systems.spawner import Spawner
from entities.player import Player

from settings import WIDTH, HEIGHT, FPS

class Game:
    def __init__(self):
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption('Game Arena')
        self.clock = pg.time.Clock()
        
        # ToDo: Inicializace skupiny objektu
        self.all_sprites = pg.sprite.Group()
        
        # ToDo: Vytvoreni objektu hrace
        self.player = Player(game=self, pos=(WIDTH / 2, HEIGHT / 2), size=(50, 50), color=(0, 255, 0))
        self.all_sprites.add(self.player)
        
        # ToDo: Inicializace systemu vytvareni nepratel
        self.enemies = pg.sprite.Group()
        self.spawner = Spawner(self)
        
        #ToDo: Inicializace skupiny projektilu
        self.bullets = pg.sprite.Group()
        
        # Stav hry
        self.running = True
        self.score = 0
        
    def run(self):
        while self.running:
            dt = self.clock.tick(FPS) / 1000  # Delta time in seconds.
            self.handle_events()
            self.update(dt)
            self.draw()
    
    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    self.player.shoot()

    def update(self, dt):
        self.all_sprites.update(dt)
        self.spawner.update(dt)

    def draw(self):
        self.screen.fill((30, 30, 30))  # Clear screen with dark gray
        self.all_sprites.draw(self.screen)
        pg.display.flip()