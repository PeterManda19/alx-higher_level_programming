#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Takes two parameters, 
    a list and integer
    Returns counter"""

    counter = 0
    
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
        except IndexError:
            break
        else:
            counter += 1
    print()
    return counter
