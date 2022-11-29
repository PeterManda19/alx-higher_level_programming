#!/usr/bin/python3

def remove_char_at(str, n):
    """Takes in string argument and number
    returns string if number n is less than 0
    returns copy of the string 
    without the character at position n if n > 0"""
   
    if n < 0:
        return (str)
    return (str[:n] + str[n+1:])
