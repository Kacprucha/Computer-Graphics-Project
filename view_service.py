import pygame as pg

class ViewService:
    
    def __init__(self, screen_width, screen_height, step, radious):
        self.screan_height = screen_height
        self.screan_width = screen_width
        self.step = step
        self.radious = radious
        
    def window_start(self):
        pg.init()
        screen = pg.display.set_mode((self.screan_width, self.screan_height))