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


def forward(i):
    for j in range(i, 9+i):
        print_parrot(j%9+1)

def backward(i):
    for k in range(9+i, i-1, -1):
        print_parrot(k%9+1)

def print_parrot(num):
    print(f':wave-{num}-parrot:', end="")