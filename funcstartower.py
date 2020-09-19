# pyramid(3): print the star tower, height = 3

def pyramid(height):
    start = 1
    while height > 0:
        print(' ' * (height-1) + '*' * start)
        start += 2
        height -= 1

pyramid(5)
