import numpy as np
from math import *


s_width = 800
s_height = 600

class Point:
    D = 1000
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def get_projection_matrix(self):
        m = np.matrix([
            [1,0,0,0],
            [0,1,0,0],
            [0,0,0,0],
            [0,0,1/self.D,1]
        ])
        return m
    
    def cordinate_to_print(self):
        start_x = ((self.x * self.D) / (self.z + self.D)) + s_width/2
        start_y = ((self.y * self.D) / (self.z + self.D)) - s_height/2
        return (start_x, start_y)
    
    def xyz_to_matrix(self):
        horizontal_m = np.matrix([self.x, self.y, self.z, 1])
        vertical_m = horizontal_m.reshape((4,1))
        return vertical_m
    
    def get_transformation(self, transtormation_matrix):
        vertical_m = self.xyz_to_matrix()
        new_positon = np.dot(transtormation_matrix, vertical_m)
        self.x = int(new_positon[0][0])
        self.y = int(new_positon[1][0])
        self.z = int(new_positon[2][0])
        
    def zoom_transformation(self, value):
        self.x = self.x*value
        self.y = self.y*value
        self.z = self.z*value
        
    def y_for_alg(self):
        return 600 - self.y
        
    def print_to_coordinate(self, start_x, start_y):
        epsilon = 1e-6
        max_iterations = 1000
        z = 1.0
        for _ in range(max_iterations):
            prev_z = z
            x = (start_x - s_width/2) * (z + self.D) / self.D
            y = (start_y + s_height/2) * (z + self.D) / self.D
            z = ((x**2 + y**2) / (2 * self.D)) - self.D
            if abs(z - prev_z) < epsilon:
                break
        else:
            print("MAX ITERATION!!!")
        return x, y, z