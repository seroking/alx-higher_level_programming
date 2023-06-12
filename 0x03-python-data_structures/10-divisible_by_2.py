#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list:
        for x in range(len(my_list)):
            if my_list[x] % 2 == 0:
                my_list[x] = True
            else:
                my_list[x] = False

        return(my_list)

