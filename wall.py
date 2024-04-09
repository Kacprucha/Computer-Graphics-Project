import random

import numpy as np
import pygame as pg

from line import Line
from point import Point


class Wall:
    
    def __init__(self, wall_id, screen, path, if_in):
        self.id = wall_id
        self.screen = screen
        self.path = path
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        self.color = (r,g,b)
        self.if_in = if_in
        lines = []
        points = []
        self.read_wall_from_file()
        
        
    def read_wall_from_file(self):
        lines = []
        points = []
        sx, sy = self.screen.get_size()
        with open(self.path, 'r') as file:
            for line in file:
                x,y,z = line.split()
                point = Point(int(x), int(sy - int(y)), int(z))
                points.append(point)
            
            for i in range(len(points)-1):
                line = Line(self.screen, points[i], points[i+1], self.id)
                lines.append(line)
            line = Line(self.screen, points[len(points)-1], points[0], self.id)
            lines.append(line)
            
        self.points = points
        self. lines = lines

    
    def draw_wall_with_fill(self):
        points_to_fill = []
        for point in self.points:
            points_to_fill.append(point.cordinate_to_print())
            
        pg.draw.polygon(self.screen, self.color, points_to_fill)
            
    def points_transformation(self, tranfromation_matrix):
        for point in self.points:
            point.get_transformation(tranfromation_matrix)
            
    def zoom_transformation(self, value):
        for point in self.points:
            point.zoom_transformation(value)
            
    def print_polygon_structure(self):
        self.points_to_print = []
        self.line_to_print = []
        
        for point in self.points:
            self.points_to_print.append(point.cordinate_to_print())
        for i in range(len(self.points_to_print)-1):
            self.line_to_print.append((self.points_to_print[i], self.points_to_print[i+1]))
        self.line_to_print.append((self.points_to_print[0], self.points_to_print[len(self.points_to_print)-1]))
        
    def point_inside_polygon(self, x, y):
        crossings = 0
        for line in self.line_to_print:
            if (line[0][1] > y and line[1][1] <= y) or (line[0][1] <= y and line[1][1] > y):
                if line[0][0] + (y - line[0][1]) / (line[1][1] - line[0][1]) * (line[1][0] - line[0][0]) <= x:
                    crossings += 1
        return crossings % 2 == 1
        
            
            
            