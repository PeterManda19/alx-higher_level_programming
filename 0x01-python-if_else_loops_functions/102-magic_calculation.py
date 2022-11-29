#!/usr/bin/python3

def magic_calculation(a, b, c):
    """Takes in 3 numbers a, b, c 
    return c if a is less than b
    return sum of a and b if c i greater than b
    retun difference between the result of a to the power of b;
    and c """

    if a < b:
        return (c)
    if c > b:
        return (a + b)
    return (a*b - c)
