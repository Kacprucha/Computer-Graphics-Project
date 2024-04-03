import pygame
import numpy as np

LINE_COLOR = (255,255,255)
WALL_COLOR = (255,0,0)
D = 1000

projection_matrix = np.matrix([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 0],
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
        
    def y_for_alg(self):
        return 600 - self.y
        
class Line:
    def __init__(self, screen, s_point, e_point, wall_id, zoom=1):
        self.s_point = s_point
        self.e_point = e_point
        self.wall_id = wall_id
        self.zoom = zoom
        
        if self.s_point.y_for_alg() > self.e_point.y_for_alg():
            self.s_point, self.e_point = self.e_point, self.s_point
        
    def get_projected_point(self, point):
        r_matrix = point.coordinates_as_matrix()
        projection2d = np.dot(get_projection_matrix(), r_matrix)
        p_x = int(projection2d[0][0]) * self.zoom
        p_y = int(projection2d[1][0]) * self.zoom
        
        return (p_x, p_y)
    
    def if_line_horizontal(self):
        return self.s_point.y == self.e_point.y
    
    def find_x_for_y(self, y):
        if self.s_point.y == self.e_point.y:
            return self.s_point.x
        if self.s_point.x - self.e_point.x != 0:
            a = (self.s_point.y - self.e_point.y) / (self.s_point.x - self.e_point.x)
            b = self.s_point.y - a * self.s_point.x
            return (y - b) / a
    
    def check_if_in_line(self, x):
        if self.s_point.x > self.e_point.x:
            if self.s_point.x >= x and self.e_point.x <= x:
                return True
        else:
            if self.s_point.x <= x and self.e_point.x >= x:
                return True
            
        return False
    
    def connect_points(self, screen):
        s_r_matrix = self.s_point.coordinates_as_matrix()
        projection2d = np.dot(get_projection_matrix(), s_r_matrix)
        s_x = int(projection2d[0][0]) * self.zoom
        s_y = int(projection2d[1][0]) * self.zoom
            
        
        e_r_matrix = self.e_point.coordinates_as_matrix()
        projection2d = np.dot(get_projection_matrix(), e_r_matrix)
        e_x = int(projection2d[0][0]) * self.zoom
        e_y = int(projection2d[1][0]) * self.zoom
        
        pygame.draw.line(screen, LINE_COLOR, (s_x, s_y), (e_x, e_y))
        
class Wall:
    def __init__(self, w_id, screen, line_list, points_list, color, if_in):
        self.id = w_id
        self.screen = screen
        self.line_list = line_list
        self.point_list = points_list
        self.color = color
        self.if_in = if_in
        
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
        if len(self.point_list) == 3:
            point1 = np.array([self.point_list[0].x, self.point_list[0].y, self.point_list[0].z])
            point2 = np.array([self.point_list[1].x, self.point_list[1].y, self.point_list[1].z])
            point3 = np.array([self.point_list[2].x, self.point_list[2].y, self.point_list[2].z])
            A, B, C, D = self.plane_equation_3points(point1, point2, point3)
        else:
            points = np.zeros((len(self.point_list), 3))
            for i in range(len(self.point_list)):
                points[i] = [self.point_list[i].x, self.point_list[i].y, self.point_list[i].z]
            A, B, C, D = self.plane_equation_n_points(points)
            
        return (-A * x - B * y - D) / C
        
    def draw_wall_without_fill(self):
        for line in self.line_list:
            line.connect_points(self.screen)
            
    def draw_wall_with_fill(self):
        points_to_fill = []
        for point in self.point_list:
            points_to_fill.append((point.x, point.y))
            
        pygame.draw.polygon(self.screen, self.color, points_to_fill)
            
    def applay_geometric_transformation(self, matrix):
        i = 0
        for point in self.point_list:
            point.matrix_operation(matrix)
            
    def change_zoom(self, zoom):
        self.zoom = zoom