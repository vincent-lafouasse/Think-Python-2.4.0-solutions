"""
Note that this doesn't check for trivial solutions
any n with a = c and b = 0 satisfy the equation but do not disprove Fermat

Note also that this doesn't check for type. Fermat's Last Theorem requires
a, b and c to be positive integers.
"""


def check_fermat(a, b, c, n):
    if n > 2 and a**n + b**n == c**n:
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn’t work.")


def fermat_prompt():
    print("\nAlright, let's check if there are positive integers a, b, c " +
          "that satisfy the equation a**n + b**n = c**n with n > 2.\n")
    a = int(input('a = '))
    b = int(input('b = '))
    c = int(input('c = '))
    n = int(input('n = '))
    print()

    check_fermat(a, b, c, n)


fermat_prompt()
