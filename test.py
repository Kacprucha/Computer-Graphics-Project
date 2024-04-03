import numpy as np

# Example for N = 3
def plane_equation_3points(p1, p2, p3):
    v1 = p2 - p1
    v2 = p3 - p1
    cp = np.cross(v1, v2)
    A, B, C = cp
    D = -np.dot(cp, p1)
    return A, B, C, D

# Example usage with N = 3
p1 = np.array([40, 35, 10])
p2 = np.array([29, 25, 5])
p3 = np.array([35, 45, 7])
A, B, C, D = plane_equation_3points(p1, p2, p3)
print("Plane equation (N=3):", A, "x +", B, "y +", C, "z +", D, "= 0")

# Example for N > 3 using SVD
def plane_equation_n_points(points):
    # points is a Nx3 matrix
    centroid = np.mean(points, axis=0)
    normalized_points = points - centroid
    U, S, Vt = np.linalg.svd(normalized_points)
    normal_vector = Vt[2, :]
    A, B, C = normal_vector
    D = -np.dot(normal_vector, centroid)
    return A, B, C, D

# Example usage with N > 3
points = np.array([[30, 10, 2], [21, 4, 10], [16, 9, 10], [20, 20, 4]])
A, B, C, D = plane_equation_n_points(points)
print("Plane equation (N>3):", A, "x +", B, "y +", C, "z +", D, "= 0")
