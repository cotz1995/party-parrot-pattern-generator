from random import randint
from math import atan, pi

def to_middle():
    for i in range(9):
        forward(i)
        forward(i)
        backward(i)
        backward(i)
        print('')

    for i in range(9, 0, -1):
        forward(i)
        forward(i)
        backward(i)
        backward(i)
        print('')

def big_to_middle_top():
    for i in range(9):
        forward(i)
        forward(i)
        backward(i)
        backward(i)
        print('')

    for i in range(9):
        forward(i)
        forward(i)
        backward(i)
        backward(i)
        print('')

def big_to_middle_bottom():
    for i in range(9, 0, -1):
        forward(i)
        forward(i)
        backward(i)
        backward(i)
        print('')

    for i in range(9, 0, -1):
        forward(i)
        forward(i)
        backward(i)
        backward(i)
        print('')

def chevron():
    for i in range(9, 0, -1):
        forward(i)
        forward(i)
        print('')

    for i in range(9):
        forward(i)
        forward(i)
        print('')

def diagonal_wave():
    for i in range(9, 0, -1):
        forward(i)
        forward(i)       
        forward(i)
        forward(i)
        print('')

def chaos():
    for i in range (0, 18):
        for j in range(0, 36):
            print_parrot(randint(1,9))
        print('')

def alternate():
        for i in range (0, 18):
            for j in range(0, 18):
                print_parrot(1)
            print('')
            for j in range(0, 18):
                print_parrot(5)
            print('')

def circleish(n, center=None):
    for row in generate_circleish_matrix(n, center):
        for num in row:
            print_parrot(num%9+1)
        print('')


def spiral(n, center=None, arms=1, reverse=False, clockwise=True):
    clockwise = not clockwise if reverse else clockwise
    for row in generate_spiral_matrix(n, center, arms, -1 if clockwise else 1):
        for num in row:
            if reverse:
                num *= -1
            print_parrot(num%9 + 1)
        print('')


def generate_circleish_matrix(n, center=None):
    center = center or (n//2, n//2)
    return [[distance_from_center(i, j, center) for j in range(n)]for i in range(n)]
    

def generate_spiral_matrix(n, center=None, arms=1, offset_multiplier=1):
    center = center or (n//2, n//2)
    return [[distance_from_center(i, j, center) + spiral_offset(i, j, center, 9*arms)*offset_multiplier for j in range(n)]for i in range(n)]


def distance_from_center(a, b, center):
    return int(((a-center[1])**2 + (b-center[0])**2)**.5)


def spiral_offset(a, b, center, scale=18):
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


def forward(i):
    for j in range(i, 9+i):
        print_parrot(j%9+1)

def backward(i):
    for k in range(9+i, i-1, -1):
        print_parrot(k%9+1)

def print_parrot(num):
    print(f':wave-{num}-parrot:', end="")
