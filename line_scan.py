import pygame
import numpy as np
from my_classes import Point, Figure, Line, Wall, WALL_COLOR, LINE_COLOR

class Skaner_liniowy:
    def __init__(self, screen, walls, lines):
        self.screen = screen
        self.walls = walls
        self.lines = []
        
        temp_lines = lines.copy()
        while len(temp_lines) > 0:
            lower_y_line = temp_lines[0]
            for line in temp_lines:
                if line.get_projected_y_start_point() < lower_y_line.get_projected_y_start_point():
                    lower_y_line = line
                elif line.get_projected_y_end_point() < lower_y_line.get_projected_y_end_point():
                    lower_y_line = line
            self.lines.append(lower_y_line)
            temp_lines.remove(lower_y_line)
        
        lowest = lambda x: self.lines[x].get_projected_y_start_point() if self.lines[x].get_projected_y_start_point() <= self.lines[x].get_projected_y_end_point() else self.lines[x].get_projected_y_end_point()
        highest_y = lambda x: self.lines[x].get_projected_y_start_point() if self.lines[x].get_projected_y_start_point() >= self.lines[x].get_projected_y_end_point() else self.lines[x].get_projected_y_end_point()
            
        self.lowest_y = int(lowest(0))
        self.highest_y = int(highest_y(-1))
        
        #print(self.lowest_y, self.highest_y)
        #for line in self.lines:
        #    print(line.walls_id, "|", line.get_projected_y_start_point(), line.get_projected_y_end_point())
            
    def scan(self):
        horizontal_lines = []
        for y in range(self.lowest_y, self.highest_y + 1):
            active_lines = []
            for line in self.lines:
                if y >= line.get_projected_y_start_point() and y <= line.get_projected_y_end_point():
                    active_lines.append(line)
                    if line.if_line_horizontal():
                        horizontal_lines.append(line)
                elif y >= line.get_projected_y_start_point() and line.if_line_horizontal():
                    if line not in horizontal_lines:
                        horizontal_lines.append(line)
                        active_lines.append(line)
            print("y:", y)
            for line in active_lines:
                print("\t", line.walls_id, "|", line.get_projected_y_start_point(), line.get_projected_y_end_point())
        
        