def abs(value):
    # FIXME: Logic needs to be checked
    # FIXME: Complex numbers need to be handled too

    """ Return the absolute value of a number. The argument may be an integer, a floating point number, or an object
    implementing __abs__(). If the argument is a complex number, its magnitude is returned. """

    try:

        if value < 0:
            value *= -1
    except TypeError:
        raise

print(abs(-5j))

# TODO: Incomplete
