"""
Insertion sort is a simple sorting algorithm that works the way we sort playing cards in our hands.
It is less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.
"""

import time
from typing import Tuple


def insertion_sort_tuple_packing(arr: list[int]) -> list[int]:
    """
    Sort an array using the insertion sort algorithm (using tuple packing instead of temp method).

    Args:
        arr: List of integers to sort.

    Returns:
        The sorted list of integers.
    """
    n = len(arr)

    if n <= 1:
        return arr

    for i in range(1, n):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
    return arr


def insertion_sort_exec_time(arr: list[int]) -> Tuple[list[int], float]:
    """
    Sort an array using the insertion sort algorithm and return the execution time.

    Args:
        arr: List of integers to sort.

    Returns:
        A tuple containing:
        - The sorted list of integers.
        - The execution time in milliseconds.
    """
    start = time.time()
    ## Uncomment to not mutate the original array
    # arr_copy = arr.copy
    # sorted_array = insertion_sort_tuple_packing(arr_copy)
    sorted_array = insertion_sort_tuple_packing(arr)
    end = time.time()
    exec_time = (end - start) * 1000

    return sorted_array, exec_time


def display_insertion_sort(arr: list[int]) -> list[int]:
    """
    Display the sorted array using the insertion sort algorithm.

    Args:
        arr: List of integers to sort.

    Returns:
        The sorted list of integers.
    """
    print("\n[INFO] Unsorted array: ", arr)
    sorted_arr, exec_time = insertion_sort_exec_time(arr)

    print(f"[INFO] Sorted array using basic insertion sort: {sorted_arr}")
    print(f"[INFO] Execution time: {exec_time:.3f} milliseconds\n")

    return sorted_arr


if __name__ == "__main__":
    arr = [3, 4, 1, 2, 5]
    sorted_arr = display_insertion_sort(arr=arr)