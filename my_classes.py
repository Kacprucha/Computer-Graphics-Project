import pygame
import numpy as np

HALF_WIDTH = 400
HALF_HIGH = 300

LINE_COLOR = (255,255,255)
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
        
class Figure:
    def __init__(self, screen, points_list, zoom):
        self.screen = screen
        self.points_list = points_list
        self.zoom = zoom
        
    def connect_points(self, screen, s_point, e_point):
        s_r_matrix = s_point.coordinates_as_matrix()
        projection2d = np.dot(get_projection_matrix(), s_r_matrix)
        # s_x = (((s_point.x * self.zoom) * D) / ((s_point.z * self.zoom) + D)) 
        # s_y = (((s_point.y * self.zoom) * D) / ((s_point.z * self.zoom) + D))
        s_x = (((s_point.x ) * D) / ((s_point.z ) + D)) 
        s_y = (((s_point.y ) * D) / ((s_point.z ) + D))
        
        e_r_matrix = e_point.coordinates_as_matrix()
        projection2d = np.dot(get_projection_matrix(), e_r_matrix)
        # e_x = (((e_point.x * self.zoom) * D) / ((e_point.z * self.zoom) + D)) 
        # e_y = (((e_point.y * self.zoom) * D) / ((e_point.z * self.zoom) + D))
        e_x = (((e_point.x ) * D) / ((e_point.z ) + D)) 
        e_y = (((e_point.y ) * D) / ((e_point.z ) + D)) 
        
        pygame.draw.line(screen, LINE_COLOR, (s_x + HALF_WIDTH, s_y - HALF_HIGH), (e_x+ HALF_WIDTH, e_y - HALF_HIGH),2)
        
    def get_projected_point(self, point):
        p_x = ((point.x * D) / (point.z + D)) * self.zoom
        p_y = ((point.y * D) / (point.z + D)) * self.zoom
        
        return (p_x, p_y)

    def draw_figure_without_walls(self):            
        for p in range(4):
            if not (self.points_list[p].z < 0 or self.points_list[(p+1) % 4].z < 0):
                line_d = self.connect_points(self.screen, self.points_list[p], self.points_list[(p+1) % 4])
            if not (self.points_list[p + 4].z < 0 or self.points_list[((p+1) % 4) + 4].z < 0):
                line_u = self.connect_points(self.screen, self.points_list[p + 4], self.points_list[((p+1) % 4) + 4])
            if not (self.points_list[p].z < 0 or self.points_list[p + 4].z < 0):
                line_s = self.connect_points(self.screen, self.points_list[p], self.points_list[p + 4])
            
    def applay_geometric_transformation(self, matrix):
        i = 0
        for point in self.points_list:
            point.matrix_operation(matrix)
            
    def applay_zoom(self, n_zoom):
        for point in self.points_list:
            point.x = point.x / self.zoom
            point.y = point.y / self.zoom
            point.z = point.z / self.zoom
            
            point.x = point.x * n_zoom
            point.y = point.y * n_zoom
            point.z = point.z * n_zoom
            
    def change_zoom(self, zoom):
        self.zoom = zoom