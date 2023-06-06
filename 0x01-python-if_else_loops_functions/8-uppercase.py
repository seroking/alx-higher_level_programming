#!/usr/bin/python3

def uppercase(str):
    for word in str:
        if (96 < ord(word) < 123):
            print("{:c}".format(ord(word) - 32), end="")
        else:
            print(f"{word}",end="")
