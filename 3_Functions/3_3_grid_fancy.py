def grid(height, width, size=4):
    beam = ' -'*size + ' +'
    post = ' '*(2*size + 1) + '|'

    print('+' + beam*width)

    for _ in range(height):
        for _ in range(size):
            print('|' + post*width)
        print('+' + beam*width)


grid(4, 4)
