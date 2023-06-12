#!/usr/bin/python3

def multiple_returns(sentence):
    lenght = len(sentence)
    if lenght:
        char = sentence[0]
    else:
        char = 'None'
    tuple_info = (lenght, char)
    return tuple_info
