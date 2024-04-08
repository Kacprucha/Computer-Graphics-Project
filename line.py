import numpy as np
import pygame as pg

class Line:
    
    D = 1000
    BLACK = (0,0,0)
    
    def __init__(self, screen, start, end, wall_id, color = BLACK):
        self.screen = screen
        self.start = start
        self.end = end
        self.color = color
        self.wall_id = wall_id
        
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
            
    def if_line_horizontal(self):
        return self.start.y == self.end.y
    
    def find_x_for_y(self, y):
        if self.start.y == self.end.y:
            return self.start.x
        
        if self.start.x - self.end.x != 0:
            a = (self.start.y - self.end.y) / (self.start.x - self.end.x)
            b = self.start.y - a * self.start.x
            return (y - b) / a
        
    def check_if_in_line(self, x):
        if self.start.x > self.end.x:
            if self.start.x >= x and self.end.x <= x:
                return True
        else:
            if self.start.x <= x and self.end.x >= x:
                return True
            
        return False
    
    
        
        