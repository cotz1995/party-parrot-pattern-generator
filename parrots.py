from random import randint

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

def circleish(n):
    for row in generate_circleish_matrix(n):
        for num in row:
            print_parrot(num%9+1)
        print('')


def generate_circleish_matrix(n):
    return [[distance_from_center(i, j, n//2) for j in range(n)]for i in range(n)]

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
