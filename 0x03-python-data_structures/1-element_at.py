#!/usr/bin/python3

def element_at(my_list, idx):
    """
    gets an elment from a list at index idx
    Args:
        my_list - list to search
        idx - the position to access
    Return:
        None - if idx is out of range
        Data - element at idx
    """

    if idx < 0:
        return None
     elif idx > len(my_list):
         return None
     else:
          return my_list[idx]
