#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    """Takes value as an argument
    Returns boolean True"""
    
    try:
        print("{:d}".format(value))
    except Exception as i:
        sys.stderr.write("Exception: {}\n".format(i))
        return (False)
    else:
        return (True)
