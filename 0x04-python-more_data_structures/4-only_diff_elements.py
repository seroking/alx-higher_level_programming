#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    empty = set()
    for elem in set_1:
        if elem not in set_2:
            empty.add(elem)
    for elem in set_2:
        if elem not in set_1:
            empty.add(elem)
    return(empty)
