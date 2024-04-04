import numpy as np
import pygame as pg

class Line:
    
    D = 1000
    BLACK = (0,0,0)
    
    def __init__(self, screen, start, end, color = BLACK):
        self.screen = screen
        self.start = start
        self.end = end
        self.color = color
        
    def get_projection_matrix(self):
        m = np.matrix([
            [1,0,0,0],
            [0,1,0,0],
            [0,0,0,0],
            [0,0,1/self.D,1]
        ])
        return m
        
    def draw_line(self):
        if not (self.start.z < 0 or self.end.z < 0):
            s_width, s_height = self.screen.get_size()
            start_vertical_matrix = self.start.xyz_to_matrix()
            
            projection = np.dot(self.get_projection_matrix(), start_vertical_matrix)
            start_x = ((self.start.x * self.D) / (self.start.z + self.D)) + s_width/2
            start_y = ((self.start.y * self.D) / (self.start.z + self.D)) - s_height/2
            end_vertical_matrix = self.end.xyz_to_matrix()
            projection = np.dot(self.get_projection_matrix(), end_vertical_matrix)
            end_x = ((self.end.x * self.D) / (self.end.z + self.D)) + s_width/2
            end_y = ((self.end.y * self.D) / (self.end.z + self.D)) - s_height/2
            pg.draw.circle(self.screen, self.BLACK,(start_x, start_y), 2, 2)
            pg.draw.circle(self.screen, self.BLACK,(end_x, end_y), 2, 2)
            pg.draw.line(self.screen, self.color, (start_x, start_y), (end_x, end_y))
        
        