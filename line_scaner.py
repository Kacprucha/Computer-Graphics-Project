import pygame as pg
import numpy as np
from wall import Wall
from line import Line
from point import Point

class LineScaner:
    def __init__(self, screen, walls, lines):
        self.screen = screen
        self.sx, self.sy = screen.get_size()
        self.walls = walls
        
    def find_wall_of_id(self, wall_id):
        for wall in self.walls:
            if wall.id == wall_id:
                return wall
        return None
            
    def sizing_scan(self):
        min_x = None
        max_x = None
        min_y = None
        max_y = None
        for wall in self.walls:
            for point in wall.points:
                x, y = point.cordinate_to_print()
                x, y = int(x), int(y)
                if min_x == None or x < min_x:
                    min_x = x
                if min_y == None or y < min_y:
                    min_y = y
                if max_x == None or x > max_x:
                    max_x = x
                if max_y == None or y > max_y:
                    max_y = y
                if min_x < 0:
                    min_x = 0
                if min_y < 0:
                    min_y = 0
                if max_x > 800:
                    max_x = 800
                if max_y > 600:
                    maxy = 600
        return min_x, max_x, min_y, max_y
            
            
    def scren_scann(self):
        values_matrix = np.empty((800, 600), dtype=np.float64)
        values_matrix.fill(np.inf)
        colors_matrix = np.full((800, 600, 3), (255, 255, 255), dtype=np.uint8)
        min_x, max_x, min_y, max_y = self.sizing_scan()
        for wall in self.walls:
            wall.print_polygon_structure()
            for i in range(min_x, max_x-1):
                for j in range(min_y, max_y-1):
                    if wall.point_inside_polygon(i,j):
                        x, y, z = wall.points[0].print_to_coordinate(i, j)
                        if values_matrix[i][j] > z:
                            values_matrix[i][j] = z
                            colors_matrix[i][j] = wall.color
                            
        pg.surfarray.blit_array(self.screen, colors_matrix)  
        