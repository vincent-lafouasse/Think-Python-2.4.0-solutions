"""
We want to print N whitespaces then the argument string s such that the last
character of the input is in the 70th column.
i.e. such that N + len(s) = 70

Note that for that to work, s has to have a length lesser than 70.
"""


def right_justify(s):
    if len(s) > 70:
        raise ValueError('input is too long')

    N = 70 - len(s)
    print(' '*N + s)
