#!/usr/bin/python3

def safe_print_integer(value):
    """Takes one argument value
    Returns boolean False"""

    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
        