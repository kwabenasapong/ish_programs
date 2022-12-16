def find_peak(list_of_integers):
    """
    This function takes a list of unsorted integers as input and returns
    the peak element in the list. A peak element is defined as an element
    that is greater than or equal to its neighbors.
    
    The function uses a divide and conquer approach to find the peak element
    in the list. It first checks the middle element of the list and compares
    it to its neighbors. If the middle element is greater than or equal to
    both of its neighbors, it is a peak element and the function returns it.
    If the middle element is less than its left neighbor, the peak element
    must be in the left half of the list, so the function recursively calls
    itself on the left half of the list. Similarly, if the middle element is
    less than its right neighbor, the peak element must be in the right half
    of the list and the function recursively calls itself on the right half
    of the list.
    
    This approach has a time complexity of O(log n), as each recursive call
    reduces the size of the input list by half.
    """
    # handle edge cases where the input list is empty or has only one element
    if not list_of_integers:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    
    # get the middle index of the list
    mid = len(list_of_integers) // 2
    
    # if the middle element is greater than or equal to its neighbors,
    # it is a peak element and we return it
    if (mid == 0 or list_of_integers[mid] >= list_of_integers[mid - 1]) and (mid == len(list_of_integers) - 1 or list_of_integers[mid] >= list_of_integers[mid + 1]):
        return list_of_integers[mid]
    
    # if the middle element is less than its left neighbor, the peak element
    # must be in the left half of the list, so we recursively call the function
    # on the left half of the list
    elif (mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]):
        return

