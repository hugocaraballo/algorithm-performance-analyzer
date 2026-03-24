"""Classic sorting algorithm implementations."""


def bubble_sort(arr: list) -> list:
    """Sorts a list using bubble sort.

    Repeatedly steps through the list, compares adjacent elements, and swaps
    them if they are in the wrong order.

    Args:
        arr: Input list to sort.

    Returns:
        A new sorted list; ``arr`` is not modified.
    """
    # Work on a copy to avoid mutating the original list
    result = list(arr)

    # Outer loop: each pass moves the largest unsorted element to its final position
    for i in range(len(result) - 1, 0, -1):
        # Inner loop: compare adjacent pairs and swap if needed
        for j in range(i):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]

    return result


def selection_sort(arr: list) -> list:
    """Sorts a list using selection sort.

    Maintains sorted and unsorted regions; repeatedly picks the smallest
    element in the unsorted part and moves it to the end of the sorted part.

    Args:
        arr: Input list to sort.

    Returns:
        A new sorted list; ``arr`` is not modified.
    """
    # Work on a copy to avoid mutating the original list
    result = list(arr)

    # Iterate over each position (except the last, which will be sorted by default)
    for i in range(len(result) - 1):
        # Find the index of the minimum element in the unsorted portion
        min_idx = i
        for j in range(i + 1, len(result)):
            if result[j] < result[min_idx]:
                min_idx = j

        # Swap the minimum with the current position using multiple assignment
        if min_idx != i:
            result[i], result[min_idx] = result[min_idx], result[i]

    return result


def merge_sort(arr: list) -> list:
    """Sorts a list using merge sort (divide and conquer).

    Recursively splits the list in half, sorts each half, then merges the two
    sorted halves.

    Args:
        arr: Input list to sort.

    Returns:
        A new sorted list; ``arr`` is not modified.
    """
    # Base case: lists of length 0 or 1 are already sorted
    if len(arr) <= 1:
        return list(arr)

    # Divide: split the list into two halves
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Conquer: merge the two sorted halves
    return _merge(left, right)


def _merge(left: list, right: list) -> list:
    """Merges two sorted lists into one sorted list.

    Walks both lists from the start, repeatedly taking the smaller front
    element until one list is exhausted, then appends the remainder.

    Args:
        left: First sorted sequence.
        right: Second sorted sequence.

    Returns:
        A new list containing all elements of ``left`` and ``right`` in order.
    """
    result = []
    i, j = 0, 0

    # Compare elements from both lists and append the smaller one
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append any remaining elements from the unfinished list
    result.extend(left[i:])
    result.extend(right[j:])

    return result
