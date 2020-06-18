"4x4 grid"
def double_grid():
    double_beam()
    do_four(double_line)

"""
compound building blocks to make a four-square line
"""
def double_line():
    do_four(double_post)
    double_beam()

def double_beam():
    do_four(beam)
    print('+')

def double_post():
    do_four(post)
    print('|')


"2x2 grid"
def grid():
    full_beam()
    do_twice(line)

"""
compound building blocks to make a two-square line
"""
def line():
    do_four(full_post)
    full_beam()

def full_beam():
    do_twice(beam)
    print('+')

def full_post():
    do_twice(post)
    print('|')


"basic building blocks"
def beam():
    print('+ ' + '- '*4, end = '')

def post():
    print('|' + ' '*9, end = '')


"tools"
def do_twice(f, arg = None):
    if arg == None:
        f()
        f()
    else:
        f(arg)
        f(arg)

def do_four(f, arg = None):
    do_twice(f, arg)
    do_twice(f, arg)
