from random import randint
import math

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

def parrots_from_matrix(matrix):
    for row in matrix:
        for num in row:
            print_parrot(num%9+1)
        print('')

def circleish(n):
    parrots_from_matrix(generate_circleish_matrix(n))

def spiral(n):
    parrots_from_matrix(generate_spiral_matrix(n))
    
def generate_circleish_matrix(n):
    return [[distance_from_center(i, j, n//2) for j in range(n)]for i in range(n)]

def generate_spiral_matrix(n):
    return [[distance_from_center(i, j, 0) + offset(i, j, 0) for j in range(-n//2, n//2)]for i in range(-n//2, n//2)]

def generate_coords_matrix(n):
    return [[(j,i*-1) for j in range(-n//2, n//2)]for i in range(-n//2, n//2)]

def offset(a, b, center):
    angle = determine_angle(a, b, center)
    return int(angle * 9 / 2 / math.pi ) + 1

def print_matrix(matrix):
    for row in matrix:
        print(row)

def determine_angle(a, b, center):
    y = (a - center)*-1
    x = b - center
    if x == 0:
        if y == 0:
            return 0
        return math.pi / 2 * (-1 if y < 0 else 1)
    angle = math.atan(y/x)
    if angle < 0:
        if y < 0:
            return angle + math.pi*2
        else:
            return angle + math.pi
    else:
        if x < 0:
            return angle + math.pi
        else:
            return angle
    #  - + | + +
    # ------------
    #  - - | + -
def distance_from_center(a, b, center):
    return int(((a-center)**2 + (b-center)**2)**.5)


def forward(i):
    for j in range(i, 9+i):
        print_parrot(j%9+1)

def backward(i):
    for k in range(9+i, i-1, -1):
        print_parrot(k%9+1)

def print_parrot(num):
    print(f':wave-{num}-parrot:', end="")
