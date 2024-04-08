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
        
    def plane_equation_3points(self, p1, p2, p3):
        v1 = p2 - p1
        v2 = p3 - p1
        cp = np.cross(v1, v2)
        A, B, C = cp
        D = -np.dot(cp, p1)
        
        return A, B, C, D
    
    def plane_equation_n_points(self, points): # points is a Nx3 matrix
        centroid = np.mean(points, axis=0)
        normalized_points = points - centroid
        U, S, Vt = np.linalg.svd(normalized_points)
        normal_vector = Vt[2, :]
        A, B, C = normal_vector
        D = -np.dot(normal_vector, centroid)
        
        return A, B, C, D
    
    def find_z_of_plane(self, x, y):
        if len(self.points) == 3:
            point1 = np.array([self.points[0].x, self.points[0].y, self.points[0].z])
            point2 = np.array([self.points[1].x, self.points[1].y, self.points[1].z])
            point3 = np.array([self.points[2].x, self.points[2].y, self.points[2].z])
            A, B, C, D = self.plane_equation_3points(point1, point2, point3)
        else:
            points = np.zeros((len(self.point_list), 3))
            for i in range(len(self.point_list)):
                points[i] = [self.point_list[i].x, self.point_list[i].y, self.point_list[i].z]
            A, B, C, D = self.plane_equation_n_points(points)
            
        return (-A * x - B * y - D) / C
    
    def draw_wall_with_fill(self):
        points_to_fill = []
        for point in self.point_list:
            points_to_fill.append((point.x, point.y))
            
        pg.draw.polygon(self.screen, self.color, points_to_fill)
            
    def points_transformation(self, tranfromation_matrix):
        for point in self.points:
            point.get_transformation(tranfromation_matrix)
            
    def zoom_transformation(self, value):
        for point in self.points:
            point.zoom_transformation(value)
            
            
            