from random import randint
from math import pi, sin

import matrix_generator

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
    for i in range (18):
        for j in range(36):
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

def sine_wave(n):
    for i in range(n):
        forward_sine(n, i)
        print('')


def parrots_from_matrix(matrix, reverse=False):
    for row in matrix:
        for num in row:
            if reverse:
                num *= -1
            print_parrot(num%9 + 1)
        print('')

def circleish(n):
    parrots_from_matrix(matrix_generator.circleish(n))

def spiral(n):
    parrots_from_matrix(matrix_generator.spiral(n))
    
def spiral(n, center=None, arms=1, reverse=False, clockwise=True):
    clockwise = not clockwise if reverse else clockwise
    matrix = matrix_generator.spiral(n, center, arms, -1 if clockwise else 1)
    parrots_from_matrix(matrix, reverse)

def wheel_of_fortune(n, center=None, clockwise=True):
    matrix = matrix_generator.wheel_of_fortune(n, center, -1 if clockwise else 1)
    parrots_from_matrix(matrix)

def a():
    parrots_from_matrix(a())


def forward_sine(n, i):
    for j in range(n):
        num = int(sin(j * 2*pi/n) * n + i)
        print_parrot(num%9+1)

def forward(i):
    for j in range(i, 9+i):
        print_parrot(j%9+1)
def backward(i):
    for k in range(9+i, i-1, -1):
        print_parrot(k%9+1)

def print_parrot(num):
    print(f':wave-{num}-parrot:', end="")

def print_parrot_hax(num):
    if(num == 2):
        print(f':twins_parrot:', end='')
        return
    if(num==6):
        print(':monkey_face:', end='')
        return
    print(':palm_tree:', end='')
