
from math import atan, pi, sin

def circleish(n, center=None):
    center = center or (n//2, n//2)
    return [[distance_from_center(i, j, center) for j in range(n)]for i in range(n)]


def wheel_of_fortune(n, center=None, offset_multiplier=1):
    center = center or (n//2, n//2)
    return [[spiral_offset(i, j, center, 9)*offset_multiplier for j in range(n)]for i in range(n)]


def spiral(n, center=None, arms=1, offset_multiplier=1):
    center = center or (n//2, n//2)
    return [[distance_from_center(i, j, center) + spiral_offset(i, j, center, 9*arms)*offset_multiplier for j in range(n)]for i in range(n)]


def a():
    return [
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,5,6,1,1,1,1,1,1],
        [1,1,1,1,1,1,5,6,5,6,1,1,1,1,1],
        [1,1,1,1,1,5,6,1,1,5,6,1,1,1,1],
        [1,1,1,1,5,5,5,5,5,5,5,6,1,1,1],
        [1,1,1,5,1,1,1,1,1,1,1,5,6,1,1],
        [1,1,5,1,1,1,1,1,1,1,1,1,5,6,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    ]

    

def distance_from_center(a, b, center):
    return int(((a-center[1])**2 + (b-center[0])**2)**.5)


def spiral_offset(a, b, center, scale=9):
    angle = get_angle(a, b, center)
    return int(angle*scale/2/pi)


def get_angle(a, b, center):
    y = center[1] - a
    x = b - center[0]

    angle = pi/2 if x == 0 else atan(y/x)
    if angle < 0:
        angle += pi
    if y < 0 or (y == 0 and x < 0):
        angle += pi

    return angle


def print_matrix(matrix):
    for row in matrix:
        print(row)
