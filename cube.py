import numpy as np
from line import Line
from point import Point

class Cube:
    
    def __init__(self, path, screen):
        self.points = []
        self.read_cube_from_file(path)
        self.screen = screen
        self.lines = []
        self.create_lines()
        
    def create_lines(self):
        for i in range(4):
            self.lines.append(Line(self.screen, self.points[i], self.points[(i+1) % 4]))
            self.lines.append(Line(self.screen, self.points[i + 4], self.points[((i+1) % 4) + 4]))
            self.lines.append(Line(self.screen, self.points[i], self.points[i + 4]))
            
    def draw_cube(self):
        for line in self.lines:
            line.draw_line()
            
    def points_transformation(self, tranfromation_matrix):
        for point in self.points:
            point.get_transformation(tranfromation_matrix)
            
    def zoom_transformation(self, value):
        for point in self.points:
            point.zoom_transformation(value)
            
    def read_cube_from_file(self, path):
        with open(path, 'r') as file:
            for line in file:
                x, y, z = line.split()
                point = Point(int(x), int(int(y)), int(z))
                self.points.append(point)