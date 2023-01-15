#!/usr/bin/python3

"""Module containing the find_peak function."""


def find_peak(list_of_integers):
    """Find a peak in a list of unsorted integers.

    Args:
        list_of_integers: A list of unsorted integers.
    Returns:
        The first peak found in the list, or None if no peak is found.

    """
    if not list_of_integers:
        return None

    if len(list_of_integers) == 1:
        return list_of_integers[0]

    middle = len(list_of_integers) // 2
    if (list_of_integers[middle] > list_of_integers[middle - 1] and
            list_of_integers[middle] > list_of_integers[middle + 1]):
        return list_of_integers[middle]
    elif list_of_integers[middle] < list_of_integers[middle - 1]:
        return find_peak(list_of_integers[:middle])
    else:
        return find_peak(list_of_integers[middle + 1:])
