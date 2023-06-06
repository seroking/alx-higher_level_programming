#!/usr/bin/python3

def uppercase(str):
    for word in str:
        if (96 < ord(word) < 123):
            word = (ord(word) - 32)
        print("{:c}".format(word), end="")
    print("")
