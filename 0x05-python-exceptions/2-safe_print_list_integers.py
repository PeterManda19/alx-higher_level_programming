#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Takes two parameters, 
    a list and integer
    Returns tuple with counter"""

    counter = 0

    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
        except (ValueError, TypeError):
            pass
        else:
            counter += 1
    print()
    return (counter)
