"""
I added a bit so that do_twice and do_four could call function which take
no argument, such as print_spam
"""


def do_twice(f, arg=None):
    if arg is None:
        f()
        f()
    else:
        f(arg)
        f(arg)


def do_four(f, arg=None):
    do_twice(f, arg)
    do_twice(f, arg)


def print_spam():
    print('spam')


def print_twice(bruce):
    print(bruce)
    print(bruce)
