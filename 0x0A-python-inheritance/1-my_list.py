#!/usr/bin/python3
"""
module : 1-my_list.py

functions :
    print_sorted(self)
classes :
    Mylist
"""


class MyList(list):
    """
     class MyList inherits from list
    """

    def print_sorted(self):
        """
        function print the list in ascending sort
        """
        print(sorted(self))
