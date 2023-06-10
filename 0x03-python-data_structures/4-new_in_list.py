#!/usr/bin/python3
def new_in_list(my_list, idx, element):

    list_cp = my_list.copy()

    if idx < 0 or idx >= len(my_list):
        return(list_cp)
    else:
        list_cp.pop(idx)
        list_cp.insert(idx, element)
        return(list_cp)
