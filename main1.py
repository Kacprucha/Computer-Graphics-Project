import numpy as np
import pygame as pg
import sys
from cube import Cube
from trans_matrix import TransformationMatrix
from math import *

S_WIDTH = 800
S_HEIGHT = 600
WHITE = (255,255,255)
COLOR = (255,0,0)

RADIOUS = (15 * pi ) / 180
STEP = 50

tm = TransformationMatrix()

def main():
    
    pg.init()
    screen = pg.display.set_mode((S_WIDTH, S_HEIGHT))
    paths = sys.argv[1:]
    
    cubes = []
    for path in paths:
        cube = Cube(path, screen)
        cubes.append(cube)
    dispaly = True
    while dispaly:
        for cube in cubes:
            cube.draw_cube()
        pg.draw.line(screen, COLOR, (S_WIDTH/2-25, S_HEIGHT/2), (S_WIDTH/2+25, S_HEIGHT/2), 2)
        pg.draw.line(screen, COLOR, (S_WIDTH/2, S_HEIGHT/2-25), (S_WIDTH/2, S_HEIGHT/2+25), 2)
        
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                screen.fill(WHITE)
                if event.key == pg.K_a:
                    for cube in cubes:
                        cube.points_transformation(tm.translation_matrix(50, 0, 0))
                if event.key == pg.K_d:
                    for cube in cubes:
                        cube.points_transformation(tm.translation_matrix(-50, 0, 0))
                if event.key == pg.K_w:
                    for cube in cubes:
                        cube.points_transformation(tm.translation_matrix(0, 50, 0))
                if event.key == pg.K_s:
                    for cube in cubes:
                        cube.points_transformation(tm.translation_matrix(0, -50, 0))
                if event.key == pg.K_UP:
                    for cube in cubes:
                        cube.points_transformation(tm.translation_matrix(0, 0, -50))
                if event.key == pg.K_DOWN:
                    for cube in cubes:
                        cube.points_transformation(tm.translation_matrix(0, 0, 50))
                if event.key == pg.K_z:
                    for cube in cubes:
                        cube.points_transformation(tm.translation_matrix(0, -S_HEIGHT*1.5, 0))
                        cube.points_transformation(tm.x_rotation_matrix(RADIOUS))
                        cube.points_transformation(tm.translation_matrix(0, S_HEIGHT*1.5, 0))
                if event.key == pg.K_c:
                    for cube in cubes:
                        cube.points_transformation(tm.translation_matrix(0, -S_HEIGHT*1.5, 0))
                        cube.points_transformation(tm.x_rotation_matrix(-RADIOUS))
                        cube.points_transformation(tm.translation_matrix(0, S_HEIGHT*1.5, 0))
                if event.key == pg.K_e:
                    for cube in cubes:
                        cube.points_transformation(tm.translation_matrix(0, -S_HEIGHT*1.5, 0))
                        cube.points_transformation(tm.y_rotation_matrix(RADIOUS))
                        cube.points_transformation(tm.translation_matrix(0, S_HEIGHT*1.5, 0))
                if event.key == pg.K_q:
                    for cube in cubes:
                        cube.points_transformation(tm.translation_matrix(0, -S_HEIGHT*1.5, 0))
                        cube.points_transformation(tm.y_rotation_matrix(-RADIOUS))
                        cube.points_transformation(tm.translation_matrix(0, S_HEIGHT*1.5, 0))
                if event.key == pg.K_LEFT:
                    for cube in cubes:
                        cube.points_transformation(tm.translation_matrix(0, -S_HEIGHT*1.5, 0))
                        cube.points_transformation(tm.z_rotation_matrix(RADIOUS))
                        cube.points_transformation(tm.translation_matrix(0, S_HEIGHT*1.5, 0))
                if event.key == pg.K_RIGHT:
                    for cube in cubes:
                        cube.points_transformation(tm.translation_matrix(0, -S_HEIGHT*1.5, 0))
                        cube.points_transformation(tm.z_rotation_matrix(-RADIOUS))
                        cube.points_transformation(tm.translation_matrix(0, S_HEIGHT*1.5, 0))
                if event.key == pg.K_i:
                    for cube in cubes:
                        cube.points_transformation(tm.translation_matrix(0, -S_HEIGHT*1.5, 0))
                        cube.zoom_transformation(1.2)
                        cube.points_transformation(tm.translation_matrix(0, S_HEIGHT*1.5, 0))
                if event.key == pg.K_o:
                    for cube in cubes:
                        cube.points_transformation(tm.translation_matrix(0, -S_HEIGHT*1.5, 0))
                        cube.zoom_transformation(0.8)
                        cube.points_transformation(tm.translation_matrix(0, S_HEIGHT*1.5, 0))
                    
            elif event.type == pg.QUIT:
                dispaly = False
                
        pg.display.flip()
    pg.quit()
    
if __name__ == '__main__':
    main()
        
        
