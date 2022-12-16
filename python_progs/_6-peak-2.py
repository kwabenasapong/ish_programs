#!/usr/bin/python3
"""
Module that finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    Function that finds a peak in a list of unsorted integers
    using a divide and conquer approach with a complexity of O(log(n))
    """
    if not list_of_integers:
        return None
    # set the initial low and high indices
    low = 0
    high = len(list_of_integers) - 1

    # keep dividing the list in half until the peak is found
    while low < high:
        # find the middle index of the current range
        mid = low + (high - low) // 2

        # if the current value is greater than the value on the right,
        # the peak is on the left side of the list
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            high = mid

        # if the current value is less than the value on the right,
        # the peak is on the right side of the list
        else:
            low = mid + 1

    # return the peak value
    return list_of_integers[low]
