import pygame
import numpy as np
from my_classes import Point, Line, Wall, WALL_COLOR, LINE_COLOR

class Skaner_liniowy:
    def __init__(self, screen, walls, lines):
        self.screen = screen
        self.walls = walls
        self.lines = []
        
        temp_lines = lines.copy()
        while len(temp_lines) > 0:
            lower_y_line = temp_lines[0]
            for line in temp_lines:
                if line.s_point.y_for_alg() < lower_y_line.s_point.y_for_alg():
                    lower_y_line = line
                elif line.e_point.y_for_alg() < lower_y_line.e_point.y_for_alg():
                    lower_y_line = line
            self.lines.append(lower_y_line)
            temp_lines.remove(lower_y_line)
        
        lowest = lambda x: self.lines[x].s_point.y_for_alg() if self.lines[x].s_point.y_for_alg() <= self.lines[x].e_point.y_for_alg() else self.lines[x].e_point.y_for_alg()
        highest_y = lambda x: self.lines[x].s_point.y_for_alg() if self.lines[x].s_point.y_for_alg() >= self.lines[x].e_point.y_for_alg() else self.lines[x].e_point.y_for_alg()
            
        self.lowest_y = int(lowest(0))
        self.highest_y = int(highest_y(-1))
        
        # print(self.lowest_y, self.highest_y)
        # for line in self.lines:
        #     print(line.walls_id, "|", line.s_point.y_for_alg(), line.e_point.y_for_alg())
        
    def find_wall_of_id(self, wall_id):
        for wall in self.walls:
            if wall.id == wall_id:
                return wall
        return None
            
    def scan(self):
        horizontal_lines = []
        for y in range(self.lowest_y, self.highest_y + 1):
            active_lines = []
            for line in self.lines:
                if y >= line.s_point.y_for_alg() and y <= line.e_point.y_for_alg():
                    active_lines.append(line)
                    if line.if_line_horizontal():
                        horizontal_lines.append(line)
                elif y >= line.s_point.y_for_alg() and line.if_line_horizontal():
                    if line not in horizontal_lines:
                        horizontal_lines.append(line)
                        active_lines.append(line)
                        
            for line in active_lines:
                if line.if_line_horizontal():
                    active_lines.remove(line)
                        
            sorted_active_lines = []
            get_lowest_x = lambda x: x.s_point.x if x.s_point.x <= x.e_point.x else x.e_point.x
            while len(active_lines) > 0:
                lowest_x_line = active_lines[0]
                for line in active_lines:
                    # l_x = get_lowest_x(line)
                    # l_l_x = get_lowest_x(lowest_x_line)
                    # if lowest_x_line.s_point.x > line.s_point.x:
                    #     lowest_x_line = line
                    # elif lowest_x_line.e_point.x > line.e_point.x:
                    #     if l_x < l_l_x:
                    #         lowest_x_line = line
                    p_x_line = line.find_x_for_y(600 - y)
                    p_x_lowest = lowest_x_line.find_x_for_y(600 - y)
                    if p_x_line is not None and p_x_lowest is not None and p_x_line < p_x_lowest:
                        lowest_x_line = line
                sorted_active_lines.append(lowest_x_line)
                active_lines.remove(lowest_x_line)
            
            previous_line = None
            for line in sorted_active_lines:
                y_to_draw = 600 - y
                l_x = line.find_x_for_y(y_to_draw)
                if line.s_point.x != l_x and line.s_point.y_for_alg() != y:
                    if previous_line is not None:
                        active_planes = 0
                        a_id = []
                        for w in self.walls:
                            if w.if_in:
                                active_planes += 1
                                a_id.append(w.id)
                        if active_planes == 1:
                            a_wall = self.find_wall_of_id(a_id[0])
                            color = a_wall.color
                            p_x = previous_line.find_x_for_y(y_to_draw)
                            if p_x is not None and l_x is not None: #and p_x < l_x:
                                # if y in range(120,141):
                                #     print("\t\tp_x:", p_x, "l_x:", l_x)
                                #     print("\t\tp:", previous_line.wall_id, "|", previous_line.s_point.x, previous_line.e_point.x)
                                #     print("\t\tl:", line.wall_id, "|", line.s_point.x, line.e_point.x)
                                pygame.draw.line(self.screen, color, (p_x, y_to_draw), (l_x, y_to_draw))
                        else:
                            p_x = previous_line.find_x_for_y(y_to_draw)
                            if p_x is not None:
                                closer_wall_id = None
                                closest_z = None
                                for id in a_id:
                                    wall = self.find_wall_of_id(id)
                                    z = wall.find_z_of_plane(p_x, y_to_draw)
                                    #print("\t\t", id, z)
                                    if closest_z is None or z < closest_z:
                                        closest_z = z
                                        closer_wall_id = id
                                c_wall = self.find_wall_of_id(closer_wall_id)
                                if c_wall is not None:
                                    color = c_wall.color
                                    if p_x is not None and l_x is not None:  #and p_x < l_x:
                                        # if y in range(120,141):
                                        #     print("\t\tp_x:", p_x, "l_x:", l_x)
                                        #     print("\t\tp:", previous_line.wall_id, "|", previous_line.s_point.x, previous_line.e_point.x)
                                        #     print("\t\tl:", line.wall_id, "|", line.s_point.x, line.e_point.x)
                                        #     print("\t\tc:", c_wall.id)
                                        pygame.draw.line(self.screen, color, (p_x, y_to_draw), (l_x, y_to_draw))
                        
                    w_id = line.wall_id
                    for wall in self.walls:
                        if wall.id == w_id:
                            wall.if_in = not wall.if_in
                    previous_line = line
            # print("y:", y)
            # for wall in self.walls:
            #     print("\t|", wall.id, wall.if_in)
            # # print("y:", y)
            # for line in sorted_active_lines:
            #     print("\t", line.wall_id, "|", line.find_x_for_y(600 - y), "|", line.s_point.x, line.e_point.x)
        
        