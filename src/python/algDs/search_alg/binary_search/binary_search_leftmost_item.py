"""
Binary search is a fast search algorithm with run-time complexity of O(log n). 
This algorithm works on the principle of divide and conquer. 
It is used to find the position of a specific value in a sorted array.
In this implementation, we return the index of the leftmost element in case of duplicates.
"""

import time
from typing import Optional, Tuple

from src.python.utils.search_verify import verify


def binary_search_leftmost(arr: list[int], key: int) -> Optional[int]:
    """
    Perform a binary search to find the leftmost index of a key in a sorted list.

    Args:
        arr: List of integers to search.
        key: Integer to search for in the list.

    Returns:
        The index of the leftmost occurrence of the key if found, otherwise None.
    """
    left = 0
    right = len(arr)
    
    while left < right:
        midpoint = int((left+right) // 2)
        if key > arr[midpoint]:
            left = midpoint + 1
        else:
            right = midpoint
    
    if arr[left] == key:
        return left
    
    return None


def binary_search_leftmost_exec_time(arr: list[int], key: int) -> Tuple[Optional[int], float]:
    """
    Perform a binary search to find the leftmost index of a key in a list and return the execution time.

    Args:
        arr: List of integers to search.
        key: Integer to search for in the list.

    Returns:
        A tuple containing:
        - The index of the leftmost occurrence of the key, or None if not found.
        - The execution time in seconds.
    """
    start = time.time()
    index = binary_search_leftmost(arr=arr, key=key)
    end = time.time()
    execution_time = end - start

    return index, execution_time


def display_binary_search_leftmost(arr: list[int], key: int) -> None:
    """
    Display the result of the leftmost binary search operation.

    Args:
        arr: List of integers to search.
        key: Integer to search for in the list.
    """
    print(f"\n[INFO] The array: {arr}")
    print(f"[INFO] The target key: {key}")

    index, execution_time = binary_search_leftmost_exec_time(arr=arr, key=key)
    verify(index)
    print(f"[INFO] Execution time of finding the leftmost element using binary search: {execution_time*1000:.3f} milliseconds")


if __name__ == "__main__":
    print("-" * 80)
    arr_dups = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5]
    print(arr_dups)

    display_binary_search_leftmost(arr=arr_dups, key=3)
    display_binary_search_leftmost(arr=arr_dups, key=4)
    display_binary_search_leftmost(arr=arr_dups, key=5)

