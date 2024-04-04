import numpy as np
from math import *

class TransformationMatrix:
        
    def translation_matrix(self, tx, ty, tz):
        m = np.matrix([
            [1,0,0,tx],
            [0,1,0,ty],
            [0,0,1,tz],
            [0,0,0,1]
        ])
        return m
    
    def x_rotation_matrix(self, radious):
        m  = np.matrix([
            [1,0,0,0],
            [0,cos(radious),-sin(radious),0],
            [0,sin(radious),cos(radious),0],
            [0,0,0,1]
        ])
        return m

    def y_rotation_matrix(self, radious):
        m  = np.matrix([
            [cos(radious),0,sin(radious),0],
            [0,1,0,0],
            [-sin(radious),0,cos(radious),0],
            [0,0,0,1]
        ])
        return m
    
    def z_rotation_matrix(self, radious):
        m  = np.matrix([
            [cos(radious),-sin(radious),0,0],
            [sin(radious),cos(radious),0,0],
            [0,0,1,0],
            [0,0,0,1]
        ])
        return m
    
    
        