import numpy as np

def plane_from_points(p1, p2, p3, p4):
    # Convert points to numpy arrays
    p1, p2, p3, p4 = np.array(p1), np.array(p2), np.array(p3), np.array(p4)
    
    # Vectors spanning the plane
    v1 = p2 - p1
    v2 = p3 - p1
    
    # Calculate the normal vector to the plane
    normal = np.cross(v1, v2)
    
    # Equation of the plane: Ax + By + Cz + D = 0
    A, B, C = normal
    D = -np.dot(normal, p1)
    
    return A, B, C, D

# Example points
points = [(100, 100, 0), (200, 100, 0), (200, 200, 0), (100, 200, 0)]

# Extracting individual points
p1, p2, p3, p4 = points

# Calculate the plane equation
A, B, C, D = plane_from_points(p1, p2, p3, p4)
print(f"Equation of the plane: {A}x + {B}y + {C}z + {D} = 0")
