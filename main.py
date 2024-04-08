import numpy as np
import pygame as pg
import sys
from wall import Wall
from line_scaner import LineScaner
from trans_matrix import TransformationMatrix
from math import *

S_WIDTH = 800
S_HEIGHT = 600
GRAY = (200,200,200)
COLOR = (255,0,0)

RADIOUS = (15 * pi ) / 180
STEP = 50

tm = TransformationMatrix()

def main():
    
    pg.init()
    screen = pg.display.set_mode((S_WIDTH, S_HEIGHT))
    paths = sys.argv[1:]
    
    walls = []
    lines = []
    wall_id = 1
    for path in paths:
        wall = Wall(wall_id, screen, path, False)
        lines.extend(wall.lines)
        walls.append(wall)
        wall_id += 1
        
    scaner = LineScaner(screen, walls, lines)
    dispaly = True
    while dispaly:
        scaner.scan()
        screen.fill(GRAY)
        
        pg.draw.line(screen, COLOR, (S_WIDTH/2-25, S_HEIGHT/2), (S_WIDTH/2+25, S_HEIGHT/2), 2)
        pg.draw.line(screen, COLOR, (S_WIDTH/2, S_HEIGHT/2-25), (S_WIDTH/2, S_HEIGHT/2+25), 2)
        
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                # screen.fill(GRAY)
                if event.key == pg.K_a:
                    for wall in walls:
                        wall.points_transformation(tm.translation_matrix(50, 0, 0))
                if event.key == pg.K_d:
                    for wall in walls:
                        wall.points_transformation(tm.translation_matrix(-50, 0, 0))
                if event.key == pg.K_w:
                    for wall in walls:
                        wall.points_transformation(tm.translation_matrix(0, 50, 0))
                if event.key == pg.K_s:
                    for wall in walls:
                        wall.points_transformation(tm.translation_matrix(0, -50, 0))
                if event.key == pg.K_UP:
                    for wall in walls:
                        wall.points_transformation(tm.translation_matrix(0, 0, -50))
                if event.key == pg.K_DOWN:
                    for wall in walls:
                        wall.points_transformation(tm.translation_matrix(0, 0, 50))
                if event.key == pg.K_z:
                    for wall in walls:
                        wall.points_transformation(tm.translation_matrix(0, -S_HEIGHT*1, 0))
                        wall.points_transformation(tm.x_rotation_matrix(RADIOUS))
                        wall.points_transformation(tm.translation_matrix(0, S_HEIGHT*1, 0))
                if event.key == pg.K_c:
                    for wall in walls:
                        wall.points_transformation(tm.translation_matrix(0, -S_HEIGHT*1, 0))
                        wall.points_transformation(tm.x_rotation_matrix(-RADIOUS))
                        wall.points_transformation(tm.translation_matrix(0, S_HEIGHT*1, 0))
                if event.key == pg.K_e:
                    for wall in walls:
                        wall.points_transformation(tm.translation_matrix(0, -S_HEIGHT*1, 0))
                        wall.points_transformation(tm.y_rotation_matrix(RADIOUS))
                        wall.points_transformation(tm.translation_matrix(0, S_HEIGHT*1, 0))
                if event.key == pg.K_q:
                    for wall in walls:
                        wall.points_transformation(tm.translation_matrix(0, -S_HEIGHT*1, 0))
                        wall.points_transformation(tm.y_rotation_matrix(-RADIOUS))
                        wall.points_transformation(tm.translation_matrix(0, S_HEIGHT*1, 0))
                if event.key == pg.K_LEFT:
                    for wall in walls:
                        wall.points_transformation(tm.translation_matrix(0, -S_HEIGHT*1, 0))
                        wall.points_transformation(tm.z_rotation_matrix(RADIOUS))
                        wall.points_transformation(tm.translation_matrix(0, S_HEIGHT*1, 0))
                if event.key == pg.K_RIGHT:
                    for wall in walls:
                        wall.points_transformation(tm.translation_matrix(0, -S_HEIGHT*1, 0))
                        wall.points_transformation(tm.z_rotation_matrix(-RADIOUS))
                        wall.points_transformation(tm.translation_matrix(0, S_HEIGHT*1, 0))
                if event.key == pg.K_i:
                    for wall in walls:
                        wall.points_transformation(tm.translation_matrix(0, -S_HEIGHT*1, 0))
                        wall.zoom_transformation(1.2)
                        wall.points_transformation(tm.translation_matrix(0, S_HEIGHT*1, 0))
                if event.key == pg.K_o:
                    for wall in walls:
                        wall.points_transformation(tm.translation_matrix(0, -S_HEIGHT*1, 0))
                        wall.zoom_transformation(0.8)
                        wall.points_transformation(tm.translation_matrix(0, S_HEIGHT*1, 0))
                    
            elif event.type == pg.QUIT:
                dispaly = False
                
        pg.display.flip()
    pg.quit()
    
if __name__ == '__main__':
    main()
        
        
