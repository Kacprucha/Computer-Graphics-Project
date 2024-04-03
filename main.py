import pygame
import numpy as np
import sys, ast, random
from math import *
from line_scan import Skaner_liniowy
from my_classes import Point, Line, Wall, WALL_COLOR, LINE_COLOR

WHITE = (255,255,255)
BLACK = (0,0,0)

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

RADIOUS = (5 * pi) / 180
STEP = 50

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
    
    # figures = []
    walss = []
    lines = []
    nr_wall = 1
    for path in figure_paths:
        lines_in_wall = []
        points = []
        with open(path, 'r') as file:
            for line in file:
                x,y,z = line.split()
                point = Point(int(x), int(SCREEN_HEIGHT - int(y)), int(z))
                points.append(point)
                
            # for p in range(4):
            #     line_b = Line(screen, points[p], points[(p+1) % 4], [nr_fig + ((p+1) * 0.1), nr_fig + (5 * 0.1)])
            #     lines.append(line_b)
            
            #     line_f = Line (screen, points[p + 4], points[((p+1) % 4) + 4], [nr_fig + ((p+1) * 0.1), nr_fig + (6 * 0.1)])
            #     lines.append(line_f)
            
            #     second_id = lambda x: nr_fig + (4 * 0.1) if x == 0 else nr_fig + (x * 0.1)
            #     line_s = Line (screen, points[p], points[p + 4], [nr_fig + ((p+1) * 0.1), second_id(p)])
            #     lines.append(line_s)
            
            for i in range(len(points)-1):
                line = Line(screen, points[i], points[i+1], nr_wall)
                lines.append(line)
            line = Line(screen, points[len(points)-1], points[0], nr_wall)
            lines_in_wall.append(line)
            lines.append(line)
                
            # for w in range(6):
            #     lines_in_wall = []
            #     wall_id = nr_fig + ((w+1) * 0.1)
                
            #     for line in lines:
            #         if wall_id in line.walls_id:
            #             lines_in_wall.append(line)
                
            #     wall_color = lambda x: WALL_COLOR if x == 0 else LINE_COLOR
                
            #     wall = Wall(wall_id, screen, lines_in_wall, wall_color, False)
            #     walss.append(wall)
            
            # figure = Figure(screen, points, 1)
            # figures.append(figure)
            
            r = random.randint(0,255)
            g = random.randint(0,255)
            b = random.randint(0,255)
            
            wall = Wall(nr_wall, screen, lines_in_wall, points, (r,g,b), False)
            walss.append(wall)
            nr_wall += 1
        
    # skaner = Skaner_liniowy(screen, walss, lines)
    # skaner.scan()

    current_zoom = 1
    running = True
    
    while running:
        # for wall in walss:
        #     wall.draw_wall_with_fill()
        skaner = Skaner_liniowy(screen, walss, lines)
        skaner.scan()
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                screen.fill(BLACK)
                if event.key == pygame.K_LEFT:
                    for fig in walss:
                        fig.applay_geometric_transformation(get_ratation_z_matrix(-RADIOUS))
                if event.key == pygame.K_RIGHT:
                    for fig in walss:
                        fig.applay_geometric_transformation(get_ratation_z_matrix(RADIOUS))
                if event.key == pygame.K_e:
                    for fig in walss:
                        fig.applay_geometric_transformation(get_ratation_y_matrix(RADIOUS))
                if event.key == pygame.K_q:
                    for fig in walss:
                        fig.applay_geometric_transformation(get_ratation_y_matrix(-RADIOUS))
                if event.key == pygame.K_z:
                    for fig in walss:
                        fig.applay_geometric_transformation(get_ratation_x_matrix(-RADIOUS))
                if event.key == pygame.K_c:
                    for fig in walss:
                        fig.applay_geometric_transformation(get_ratation_x_matrix(RADIOUS))
                if event.key == pygame.K_a:
                    for fig in walss:
                        fig.applay_geometric_transformation(get_translation_matrix(STEP, 0, 0))
                if event.key == pygame.K_d:
                    for fig in walss:
                        fig.applay_geometric_transformation(get_translation_matrix(-STEP, 0, 0))
                if event.key == pygame.K_w:
                    for fig in walss:
                        fig.applay_geometric_transformation(get_translation_matrix(0, STEP, 0))
                if event.key == pygame.K_s:
                    for fig in walss:
                        fig.applay_geometric_transformation(get_translation_matrix(0, -STEP, 0))
                if event.key == pygame.K_UP:
                    for fig in walss:
                        fig.applay_geometric_transformation(get_translation_matrix(0, 0, -STEP))
                if event.key == pygame.K_DOWN:
                    for fig in walss:
                        fig.applay_geometric_transformation(get_translation_matrix(0, 0, STEP))
                if event.key == pygame.K_m:
                    current_zoom = current_zoom / 2
                    for fig in walss:
                        fig.change_zoom(current_zoom)
                if event.key == pygame.K_p:
                    current_zoom = current_zoom * 2
                    for fig in walss:
                        fig.change_zoom(current_zoom)
            
        pygame.display.flip()
    
    pygame.quit()

if __name__ == '__main__':
    main()