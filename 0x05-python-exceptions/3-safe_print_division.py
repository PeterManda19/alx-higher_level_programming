#!/usr/bin/python3

def safe_print_division(a, b):
    """Takes 2 parameters a and b
    Returns tuple with result"""

    try:
        result = a/b
    except:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return (result)
