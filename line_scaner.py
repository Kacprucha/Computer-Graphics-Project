import pygame as pg
import numpy as np
from wall import Wall
from line import Line
from point import Point

class LineScaner:
    def __init__(self, screen, walls, lines):
        self.screen = screen
        self.sx, self.sy = screen.get_size()
        self.walls = walls
        self.lines = []
        
        temp_lines = lines.copy()
        while len(temp_lines) > 0:
            lower_y_line = temp_lines[0]
            for line in temp_lines:
                if line.start.y_for_alg() < lower_y_line.start.y_for_alg():
                    lower_y_line = line
                elif line.end.y_for_alg() < lower_y_line.end.y_for_alg():
                    lower_y_line = line
            self.lines.append(lower_y_line)
            temp_lines.remove(lower_y_line)
        
        lowest = lambda x: self.lines[x].start.y_for_alg() if self.lines[x].start.y_for_alg() <= self.lines[x].end.y_for_alg() else self.lines[x].end.y_for_alg()
        highest_y = lambda x: self.lines[x].start.y_for_alg() if self.lines[x].start.y_for_alg() >= self.lines[x].end.y_for_alg() else self.lines[x].end.y_for_alg()
            
        self.lowest_y = int(lowest(0))
        self.highest_y = int(highest_y(-1))
        
        
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
                if y >= line.start.y_for_alg() and y <= line.end.y_for_alg():
                    active_lines.append(line)
                    if line.if_line_horizontal():
                        horizontal_lines.append(line)
                elif y >= line.start.y_for_alg() and line.if_line_horizontal():
                    if line not in horizontal_lines:
                        horizontal_lines.append(line)
                        active_lines.append(line)
                        
            for line in active_lines:
                if line.if_line_horizontal():
                    active_lines.remove(line)
                        
            sorted_active_lines = []
            # get_lowest_x = lambda x: x.start.x if x.start.x <= x.end.x else x.end.x
            while len(active_lines) > 0:
                lowest_x_line = active_lines[0]
                for line in active_lines:
                    p_x_line = line.find_x_for_y(self.sy - y)
                    p_x_lowest = lowest_x_line.find_x_for_y(self.sy - y)
                    if p_x_line is not None and p_x_lowest is not None and p_x_line < p_x_lowest:
                        lowest_x_line = line
                sorted_active_lines.append(lowest_x_line)
                active_lines.remove(lowest_x_line)
            
            previous_line = None
            for line in sorted_active_lines:
                y_to_draw = self.sy - y
                l_x = line.find_x_for_y(y_to_draw)
                if line.start.x != l_x and line.start.y_for_alg() != y:
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
                                print("d1")
                                pg.draw.line(self.screen, color, (p_x, y_to_draw), (l_x, y_to_draw))
                        else:
                            p_x = previous_line.find_x_for_y(y_to_draw)
                            if p_x is not None:
                                closer_wall_id = None
                                closest_z = None
                                for id in a_id:
                                    wall = self.find_wall_of_id(id)
                                    z = wall.find_z_of_plane(p_x, y_to_draw)
                                    if closest_z is None or z < closest_z:
                                        closest_z = z
                                        closer_wall_id = id
                                c_wall = self.find_wall_of_id(closer_wall_id)
                                if c_wall is not None:
                                    color = c_wall.color
                                    if p_x is not None and l_x is not None:  #and p_x < l_x:
                                        print("d2")
                                        pg.draw.line(self.screen, color, (p_x, y_to_draw), (l_x, y_to_draw))
                        
                    w_id = line.wall_id
                    for wall in self.walls:
                        if wall.id == w_id:
                            wall.if_in = not wall.if_in
                    previous_line = line

    def scan_tk(self):
        pkt = []
        for wall in self.walls:
            tmp = None
            for point in wall.points:
                if tmp is None:
                   tmp = point.z
                elif point.z > tmp:
                    tmp = point.z
            pkt.append((tmp, wall.id))     
        pkt = sorted(pkt, key=lambda x: x[0])
        walls_order = []
        for id in pkt:
            self.find_wall_of_id(id[1])
            walls_order.append(self.find_wall_of_id(id[1]))
        return walls_order
    
    def scan_tk1(self):
        walls_order = []
        pkt = []
        for wall in self.walls:
            points = wall.points
            points = sorted(points, key=lambda point: point.z)
            pkt.append((points[1], wall.id))
        pkt = sorted(pkt, key=lambda x: x[0].z)
        for id in pkt:
            self.find_wall_of_id(id[1])
            walls_order.append(self.find_wall_of_id(id[1]))
        return walls_order
    
    def sizing_scan(self):
        min_x = None
        max_x = None
        min_y = None
        max_y = None
        for wall in self.walls:
            for point in wall.points:
                x, y = point.cordinate_to_print()
                x, y = int(x), int(y)
                if min_x == None or x < min_x:
                    min_x = x
                if min_y == None or y < min_y:
                    min_y = y
                if max_x == None or x > max_x:
                    max_x = x
                if max_y == None or y > max_y:
                    max_y = y
                if min_x < 0:
                    min_x = 0
                if min_y < 0:
                    min_y = 0
                if max_x > 800:
                    max_x = 800
                if max_y > 600:
                    maxy = 600
        return min_x, max_x, min_y, max_y
            
            
    def scren_scann(self):
        values_matrix = np.empty((800, 600), dtype=np.float64)
        values_matrix.fill(np.inf)
        colors_matrix = np.full((800, 600, 3), (255, 255, 255), dtype=np.uint8)
        min_x, max_x, min_y, max_y = self.sizing_scan()
        for wall in self.walls:
            wall.print_polygon_structure()
            for i in range(min_x, max_x):
                for j in range(min_y, max_y):
                    if wall.point_inside_polygon(i,j):
                        x, y, z = wall.points[0].print_to_coordinate(i, j)
                        if values_matrix[i][j] > z:
                            values_matrix[i][j] = z
                            colors_matrix[i][j] = wall.color
                            
        pg.surfarray.blit_array(self.screen, colors_matrix)
        
        # for i in range(800):
        #     for j in range(600): 
        #         pg.draw.circle(self.screen, macierz[i][j][1], (i, j), 1, 1)    
        