#!/usr/bin/python3

def print_list_integers(my_list=[]):
    """
    prints integer in a list
    Args:
        my_list - list of integers default []
        """

    for i in my_list:
        print("{:d}".format(i))
