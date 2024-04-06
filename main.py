import pygame
import numpy as np
import sys, ast
from math import *
from my_classes import Light
from phong_shading import Phong_shading

WHITE = (255,255,255)
METALIC = (187,187,187)
BRICK = (188, 74, 60)
PLASTIC = (0,0,255)
WOOD = (139,69,19)
BLACK = (0,0,0)

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

RADIOUS = (5 * pi) / 180

def get_ratation_z_matrix(angle):
    rotation_z = np.matrix([
        [cos(angle), -sin(angle), 0, 0],
        [sin(angle), cos(angle), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])
    return rotation_z

def get_ratation_y_matrix(angle):
    rotation_y = np.matrix([
        [cos(angle), 0, sin(angle), 0],
        [0, 1, 0, 0],
        [-sin(angle), 0, cos(angle), 0],
        [0, 0, 0, 1]
    ])
    return rotation_y

def get_ratation_x_matrix(angle):
    rotation_x = np.matrix([
        [1, 0, 0, 0],
        [0, cos(angle), -sin(angle), 0],
        [0, sin(angle), cos(angle), 0],
        [0, 0, 0, 1]
    ])
    return rotation_x

def get_translation_matrix(t_x, t_y, t_z):
    rotation_x = np.matrix([
        [1, 0, 0, t_x],
        [0, 1, 0, t_y],
        [0, 0, 1, t_z],
        [0, 0, 0, 1]
    ])
    return rotation_x

def get_z_for_sphere(x, y, r):
    return sqrt(r**2 - x**2 - y**2)

def main ():

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    points_list = []
    
    for x in range(-100, 100+1):
        y_values = sqrt(100**2 - x**2)
        for y in range(int(-y_values), int(y_values+1)):
            z = get_z_for_sphere(x, y, 100)
            points_list.append([x, y, -z])
            
    light = Light([-120, 120, -120])
    camera = [0, 0, -200]
    
    #phong = Phong_shading(screen, 0.3, 0.8, 0.2, 20, 0.6, 1, camera, light, WOOD)
    phong = Phong_shading(screen, 0.1, 0.4, 0.9, 150, 0.6, 1, camera, light, METALIC)
    #phong = Phong_shading(screen, 0.3, 0.8, 0.1, 10, 0.6, 1, camera, light, BRICK)
    #phong = Phong_shading(screen, 0.2, 0.8, 0.6, 50, 0.6, 1, camera, light, PLASTIC)
    
    running = True
    while running:
        phong.applay_phong_shading(points_list)
        pygame.draw.circle(screen, (255,255,0), (SCREEN_WIDTH//2 + light.position[0], SCREEN_HEIGHT//2 - light.position[1]), 5)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                screen.fill(BLACK)
                if event.key == pygame.K_a:
                    light.position[0] -= 20
                if event.key == pygame.K_d:
                    light.position[0] += 20
                if event.key == pygame.K_w:
                    light.position[1] += 20
                if event.key == pygame.K_s:
                    light.position[1] -= 20
                if event.key == pygame.K_UP:
                    light.position[2] += 20
                if event.key == pygame.K_DOWN:
                    light.position[2] -= 20
                if event.key == pygame.K_1:
                    phong.ka = 0.1
                    phong.kd = 0.4
                    phong.ks = 0.9
                    phong.n = 150
                    phong.color = METALIC
                if event.key == pygame.K_2:
                    phong.ka = 0.2
                    phong.kd = 0.8
                    phong.ks = 0.6
                    phong.n = 50
                    phong.color = PLASTIC
                if event.key == pygame.K_3:
                    phong.ka = 0.3
                    phong.kd = 0.8
                    phong.ks = 0.2
                    phong.n = 20
                    phong.color = WOOD
                if event.key == pygame.K_4:
                    phong.ka = 0.3
                    phong.kd = 0.8
                    phong.ks = 0.1
                    phong.n = 10
                    phong.color = BRICK
            
        pygame.display.flip()
    
    pygame.quit()

if __name__ == '__main__':
    main()