#!/usr/bin/python3

def no_c(my_string):
    """Remove all characters c and C from the string."""
    copy = [s for s in my_string if s != 'c' and s != 'C']
    return ("".join(copy))
