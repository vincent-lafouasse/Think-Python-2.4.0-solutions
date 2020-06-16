def do_twice(f, arg):
    f(arg)
    f(arg)

def print_spam():
    print('spam')

def print_twice(bruce):
    print(bruce)
    print(bruce)

do_twice(print_twice, "lmao")
