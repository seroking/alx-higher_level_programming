#!/usr/bin/python3
if __name__ == "__main__":
    """Print arguments"""
    import sys

    n = len(sys.argv) - 1
    if n == 0:
        print("0 arguments.")
    elif n == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(n))

    for x in range(n):
        print("{}: {}".format(x + 1, sys.argv[x + 1]))
