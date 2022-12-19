#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    """Takes fct annd args pointers as arguments
    Returns the result of the function"""
    
    try:
        result = fct(*args)
    except Exception as i:
        sys.stderr.write("Exception: {}\n".format(i))
        result = None
    return (result)
