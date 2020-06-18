"""
The pedestrian way would be to check if:
a + b >= c and a + c >= b and b + c >= a
(and that all lengths are positive)
and then conclude that it is a valid triangle.

The clever way is to realize that we only have to check
that the longest side length is less than the semiperimeter.
That is that if c is the longest side length, that we have c <= a + b
I may put a short demonstration in the README at some point but eh
"""


def check_triangle(a, b, c):
    a, b, c = sorted([a, b, c])
    return a >= 0 and c <= a + b


def is_triangle(a, b, c):
    print("Yes, it is a valid triangle." if check_triangle(a, b, c)
          else "No, it isn't a valid triangle.")


def is_triangle_prompt():
    print("\nInput the lengths of the sides of the triangle to verify:\n")

    a = float(input('a = '))
    b = float(input('b = '))
    c = float(input('c = '))
    print()

    is_triangle(a, b, c)


is_triangle_prompt()
