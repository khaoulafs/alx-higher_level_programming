#!/usr/bin/python3
# 8-uppercase.py

def uppercase(str):
    """Print a string in uppercase."""
    for y in str:
        if ord(y) >= 97 and ord(y) <= 122:
            y = chr(ord(y) - 32)
        print("{}".format(y), end="")
    print("")

