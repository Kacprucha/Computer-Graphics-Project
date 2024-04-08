import pygame
import numpy as np
from my_classes import Light

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
SPHERE_CENTER = (0,0,0)

class Phong_shading():
    def __init__(self, screen, ka, kd, ks, n, Ia, Ip, V, light, color):
        self.screen = screen
        self.ka = ka
        self.kd = kd
        self.ks = ks
        self.n = n
        self.Ia = Ia
        self.Ip = Ip
        self.V = V
        self.light = light
        self.color = color
        self.cashet_color = []
        
    def normalize(self, vector):
        norm = np.linalg.norm(vector)
        if norm == 0: 
            return vector
        return vector / norm
        
    def get_normal_of_point(self, point):
        vector_to_point = np.array(point) - np.array(SPHERE_CENTER)
        normal = self.normalize(vector_to_point)
        return normal
    
    def get_vector_R(self, normal, L):
        return 2 * np.dot(L, normal) * normal - L
    
    def phong_for_point(self, point):
        normal = self.get_normal_of_point(point)
        L = self.normalize(np.array(self.light.position) - np.array(point))
        R = self.get_vector_R(normal, L)
        V = self.normalize(np.array(self.V) - np.array(point))
        
        diffuseStrength = max(0.0, np.dot(L, normal))
        specularStrength = max(0.0, np.dot(R, V))
        
        I = self.Ia * self.ka + self.Ip * (self.kd * diffuseStrength + self.ks * specularStrength**self.n)
        return I
    
    def applay_phong_shading(self, points_list, rereander):
        if (rereander):
            self.cashet_color.clear()
        
        index = 0
        for point in points_list:
            if (rereander):
                I = self.phong_for_point(point)
                c = (min(255,self.color[0] * I), min(255,self.color[1] * I), min(255,self.color[2] * I))
                self.cashet_color.append(c)
            #I = self.phong_for_point(point)
            #c = (min(255,self.color[0] * I), min(255,self.color[1] * I), min(255,self.color[2] * I))
            pygame.draw.circle(self.screen, self.cashet_color[index], (SCREEN_WIDTH//2 + point[0], SCREEN_HEIGHT//2 - point[1]), 1)
            index += 1