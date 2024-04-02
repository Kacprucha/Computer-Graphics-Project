import pygame
import numpy as np

LINE_COLOR = (255,255,255)
WALL_COLOR = (255,0,0)
D = 1000

projection_matrix = np.matrix([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
])

def get_projection_matrix():
    projection_m = np.matrix([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 1/D, 1]
    ])
    return projection_m

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def coordinates_as_matrix(self):
        matrix = np.matrix([self.x, self.y, self.z, 1])
        r_matrix = matrix.reshape((4,1))
        return r_matrix
    
    def matrix_operation(self, matrix):
        r_matrix = self.coordinates_as_matrix()
        operation = np.dot(matrix, r_matrix)
        self.x = int(operation[0][0])
        self.y = int(operation[1][0])
        self.z = int(operation[2][0])
        
class Line:
    def __init__(self, screen, s_point, e_point, walls_id, zoom=1):
        self.s_point = s_point
        self.e_point = e_point
        self.walls_id = walls_id
        self.zoom = zoom
        
        if self.get_projected_y_start_point() > self.get_projected_y_end_point():
            self.s_point, self.e_point = self.e_point, self.s_point
        
    def get_projected_point(self, point):
        p_x = (((point.x * self.zoom) * D) / ((point.z * self.zoom) + D)) 
        p_y = (((point.y * self.zoom) * D) / ((point.z * self.zoom) + D)) 
        
        return (p_x, p_y)
    
    def get_projected_y_start_point(self):
        y = 600 - self.s_point.y
        return (((y * self.zoom) * D) / ((self.s_point.z * self.zoom) + D))
    
    def get_projected_y_end_point(self):
        y = 600 - self.e_point.y
        return (((y * self.zoom) * D) / ((self.e_point.z * self.zoom) + D))
    
    def get_same_wall_id(self, walls_id):
        for wall_id in self.walls_id:
            if wall_id in walls_id:
                return wall_id
            
        return None
    
    def if_line_horizontal(self):
        return self.get_projected_y_start_point() == self.get_projected_y_end_point()
    
    def connect_points(self, screen):
        s_r_matrix = self.s_point.coordinates_as_matrix()
        projection2d = np.dot(get_projection_matrix(), s_r_matrix)
        s_x = (((self.s_point.x * self.zoom) * D) / ((self.s_point.z * self.zoom) + D)) 
        s_y = (((self.s_point.y * self.zoom) * D) / ((self.s_point.z * self.zoom) + D))
        
        e_r_matrix = self.e_point.coordinates_as_matrix()
        projection2d = np.dot(get_projection_matrix(), e_r_matrix)
        e_x = (((self.e_point.x * self.zoom) * D) / ((self.e_point.z * self.zoom) + D)) 
        e_y = (((self.e_point.y * self.zoom) * D) / ((self.e_point.z * self.zoom) + D)) 
        
        pygame.draw.line(screen, LINE_COLOR, (s_x, s_y), (e_x, e_y))
        
class Wall:
    def __init__(self, id, screen, line_list, points_list, color, if_in):
        self.id = id
        self.screen = screen
        self.line_list = line_list
        self.point_list = points_list
        self.color = color
        self.if_in = if_in
        
    def draw_wall_without_fill(self):
        for line in self.line_list:
            line.connect_points(self.screen)
            
    def applay_geometric_transformation(self, matrix):
        i = 0
        for point in self.point_list:
            point.matrix_operation(matrix)
            
    def change_zoom(self, zoom):
        self.zoom = zoom
        
class Figure:
    def __init__(self, screen, points_list, zoom):
        self.screen = screen
        self.points_list = points_list
        self.zoom = zoom
        
    def connect_points(self, screen, s_point, e_point):
        s_r_matrix = s_point.coordinates_as_matrix()
        projection2d = np.dot(get_projection_matrix(), s_r_matrix)
        s_x = (((s_point.x * self.zoom) * D) / ((s_point.z * self.zoom) + D)) 
        s_y = (((s_point.y * self.zoom) * D) / ((s_point.z * self.zoom) + D))
        
        e_r_matrix = e_point.coordinates_as_matrix()
        projection2d = np.dot(get_projection_matrix(), e_r_matrix)
        e_x = (((e_point.x * self.zoom) * D) / ((e_point.z * self.zoom) + D)) 
        e_y = (((e_point.y * self.zoom) * D) / ((e_point.z * self.zoom) + D)) 
        
        pygame.draw.line(screen, LINE_COLOR, (s_x, s_y), (e_x, e_y))
        
    def get_projected_point(self, point):
        p_x = ((point.x * D) / (point.z + D)) * self.zoom
        p_y = ((point.y * D) / (point.z + D)) * self.zoom
        
        return (p_x, p_y)

    def draw_figure_without_walls(self):            
        for p in range(4):
            line_d = self.connect_points(self.screen, self.points_list[p], self.points_list[(p+1) % 4])
            
            line_u = self.connect_points(self.screen, self.points_list[p + 4], self.points_list[((p+1) % 4) + 4])
            
            line_s = self.connect_points(self.screen, self.points_list[p], self.points_list[p + 4])
        
    def draw_figure_with_walls(self):            
        for p in range(4):
            line_d = self.connect_points(self.screen, self.points_list[p], self.points_list[(p+1) % 4])
            
            line_u = self.connect_points(self.screen, self.points_list[p + 4], self.points_list[((p+1) % 4) + 4])
            
            line_s = self.connect_points(self.screen, self.points_list[p], self.points_list[p + 4])
            
        front_points = [self.get_projected_point(self.points_list[0]), 
                        self.get_projected_point(self.points_list[1]), 
                        self.get_projected_point(self.points_list[2]), 
                        self.get_projected_point(self.points_list[3])]
        pygame.draw.polygon(self.screen, (255,0,0), front_points)
            
    def applay_geometric_transformation(self, matrix):
        i = 0
        for point in self.points_list:
            point.matrix_operation(matrix)
            
    def change_zoom(self, zoom):
        self.zoom = zoom