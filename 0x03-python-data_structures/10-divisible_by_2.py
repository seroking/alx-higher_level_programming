#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list:
        boleen_list = []
        for slot in my_list:
            boleen_list.append(slot % 2 == 0)
        return boleen_list
