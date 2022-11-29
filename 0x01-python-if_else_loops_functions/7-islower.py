#!/usr/bin/python3

def islower(c):
    """Takes in one alphabetic character.
    Returns boolean True if lower case
    Returns boolean False if upper case"""
   
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
