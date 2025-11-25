import pygame as pg

from settings import WIDTH, HEIGHT, FPS

class Game:
    def __init__(self):
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption('Game Arena')
        self.clock = pg.time.Clock()
        
        # ToDo: Inicializace skupiny objektu
        
        # ToDo: Vytvoreni objektu hrace
        
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

    def update(self, dt):
        pass

    def draw(self):
        pass