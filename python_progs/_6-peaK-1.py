#!/usr/bin/python3

"""Module containing the find_peak function."""

def find_peak(list_of_integers):
    """Find a peak in a list of unsorted integers.

    A peak is defined as an integer that is greater than or equal to its
    neighbors. If the list has less than three elements, the function returns
    None.

    Args:
        list_of_integers: A list of unsorted integers.

    Returns:
        The first peak found in the list, or None if no peak is found.

    """
    # Return None if the list has less than three elements
    if len(list_of_integers) < 3:
        return None

    # Check the first and last elements of the list
    if list_of_integers[0] >= list_of_integers[1]:
        return list_of_integers[0]
    elif list_of_integers[-1] >= list_of_integers[-2]:
        return list_of_integers[-1]

    # Check the remaining elements of the list
    for i in range(1, len(list_of_integers) - 1):
        if list_of_integers[i] >= list_of_integers[i - 1] and \
           list_of_integers[i] >= list_of_integers[i + 1]:
            return list_of_integers[i]

    # No peak was found
    return None

