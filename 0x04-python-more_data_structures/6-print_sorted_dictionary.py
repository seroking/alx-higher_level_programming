#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dic = dict(sorted(a_dictionary.items()))

    for x, y in sorted_dic.items():
        print("{}: {}".format(x, y))
