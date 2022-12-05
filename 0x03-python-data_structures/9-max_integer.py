#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list)-1
    if length == 0:
        return None
    Max = my_list[0]
    for i in my_list:
        if i > Max:
            max = i
    return Max
