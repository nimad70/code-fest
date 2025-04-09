"""
Insertion sort algorithm faster version
"""

import time
from typing import Tuple


def insertion_sort_optimized(arr: list[int]) -> list[int]:
    """
    Sort an array using an optimized insertion sort algorithm.
    This version shifts elements and inserts the key once, reducing assignments.

    Args:
        arr: List of integers to sort.

    Returns:
        The sorted list of integers.
    """
    i = 1
    n = len(arr)

    if n <= 1:
        return arr
    else:
        while i < n:
            key = arr[i]
            j = i
            while j > 0 and arr[j-1] > key:
                arr[j] = arr[j-1]
                j -= 1
            arr[j] = key
            i += 1
    return arr


def insertion_sort_faster_exec_time(arr: list[int]) -> Tuple[list[int], float]:
    """
    Sort an array using the faster insertion sort algorithm and return the execution time.

    Args:
        arr: List of integers to sort.

    Returns:
        A tuple containing:
        - The sorted list of integers.
        - The execution time in milliseconds.
    """
    start = time.time()

    # Uncomment the following lines to avoid mutating the original array
    # arr_copy =arr.copy()
    # sorted_array = insertion_sort_optimized(arr_copy)
    
    sorted_array = insertion_sort_optimized(arr)
    end = time.time()
    exec_time = (end - start) * 1000

    return sorted_array, exec_time


def display_insertion_sort(arr: list[int]) -> list[int]:
    """
    Display the sorted array using the insertion sort algorithm faster version
    
    Args:
        arr: list of integers to sort
    
    Returns:
        sorted_array: list of sorted integers
    """
    print(f"\n[INFO] Unsorted array: {arr}")
    sorted_array, exec_time_insertion_sort = insertion_sort_faster_exec_time(arr)

    print(f"[INFO] Sorted array using insertion sort without swapping: {sorted_array}")
    print(f"[INFO] Execution time: {exec_time_insertion_sort:.3f} milliseconds\n")

    return sorted_array


if __name__ == "__main__":
    arr = [3, 4, 1, 2, 5]
    sorted_arr = display_insertion_sort(arr=arr)