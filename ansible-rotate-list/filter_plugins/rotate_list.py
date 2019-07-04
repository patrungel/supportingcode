class FilterModule(object):
    """
    A jijna2 filter to right-rotate a list of values by a given number of positions.
    """

    def filters(self):
        return {
            'rotate_right': rotate_right
        }


def rotate_right(l, shifts_nr):
    return l[shifts_nr:] + l[:shifts_nr]
