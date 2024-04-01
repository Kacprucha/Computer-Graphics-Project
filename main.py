import pygame
import numpy as np
import sys
import ast
from math import *
from my_classes import Point, Figure

WHITE = (255,255,255)
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

def main ():

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    figure_paths = sys.argv[1:]
    
    figures = []
    for path in figure_paths:
        points = []
        with open(path, 'r') as file:
            for line in file:
                x,y,z = line.split()
                point = Point(int(x), int(SCREEN_HEIGHT - int(y)), int(z))
                points.append(point)
            
            figure = Figure(screen, points, 1)
            figures.append(figure)

    current_zoom = 1
    running = True
    while running:
        for fig in figures:
            fig.draw_figure_without_walls()
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                screen.fill(BLACK)
                if event.key == pygame.K_LEFT:
                    for fig in figures:
                        fig.applay_geometric_transformation(get_ratation_z_matrix(RADIOUS))
                if event.key == pygame.K_RIGHT:
                    for fig in figures:
                        fig.applay_geometric_transformation(get_ratation_z_matrix(-RADIOUS))
                if event.key == pygame.K_e:
                    for fig in figures:
                        fig.applay_geometric_transformation(get_ratation_y_matrix(-RADIOUS))
                if event.key == pygame.K_q:
                    for fig in figures:
                        fig.applay_geometric_transformation(get_ratation_y_matrix(RADIOUS))
                if event.key == pygame.K_z:
                    for fig in figures:
                        fig.applay_geometric_transformation(get_ratation_x_matrix(RADIOUS))
                if event.key == pygame.K_c:
                    for fig in figures:
                        fig.applay_geometric_transformation(get_ratation_x_matrix(-RADIOUS))
                if event.key == pygame.K_a:
                    for fig in figures:
                        fig.applay_geometric_transformation(get_translation_matrix(5, 0, 0))
                if event.key == pygame.K_d:
                    for fig in figures:
                        fig.applay_geometric_transformation(get_translation_matrix(-5, 0, 0))
                if event.key == pygame.K_w:
                    for fig in figures:
                        fig.applay_geometric_transformation(get_translation_matrix(0, 5, 0))
                if event.key == pygame.K_s:
                    for fig in figures:
                        fig.applay_geometric_transformation(get_translation_matrix(0, -5, 0))
                if event.key == pygame.K_UP:
                    for fig in figures:
                        fig.applay_geometric_transformation(get_translation_matrix(0, 0, -5))
                if event.key == pygame.K_DOWN:
                    for fig in figures:
                        fig.applay_geometric_transformation(get_translation_matrix(0, 0, 5))
                if event.key == pygame.K_m:
                    current_zoom = current_zoom / 2
                    for fig in figures:
                        fig.change_zoom(current_zoom)
                if event.key == pygame.K_p:
                    current_zoom = current_zoom * 2
                    for fig in figures:
                        fig.change_zoom(current_zoom)
            
        pygame.display.flip()
    
    pygame.quit()

if __name__ == '__main__':
    main()