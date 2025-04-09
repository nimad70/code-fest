"""
Binary search is an efficient algorithm for finding a target value in a sorted array. 
It repeatedly compares the target with the middle element, eliminating half of the search space each time until the target is found. 
Its time complexity is O(log n).
"""

import random
import time
from typing import Optional, Tuple

from src.python.utils.search_verify import verify


def binary_search(arr: list[int], key: int) -> Optional[int]:
    """
    Perform a binary search on a sorted list of integers.

    Args:
        arr: List of integers to search.
        key: Integer to search for in the list.

    Returns:
        The index of the key in the list if found, otherwise None.
    """
    left = 0
    right = len(arr) - 1 
    
    while left <= right:
        midpoint = int((left+right) // 2)
        if arr[midpoint] == key:
            return midpoint
        elif arr[midpoint] < key:
            left = midpoint + 1
        else:
            right = midpoint - 1
    
    return None


def binary_search_exec_time(arr: list[int], key: int) -> Tuple[Optional[int], float]:
    """
    Perform a binary search on a list of integers and return the index and execution time.
    
    Args:
        arr: List of integers to search.
        key: Integer to search for in the list.
    
    Returns:
        A tuple containing:
        - The index of the key in the list, or None if not found.
        - The execution time in seconds.
    """
    start = time.time()
    index = binary_search(arr=arr, key=key)
    end = time.time()
    execution_time = end - start

    return index, execution_time


def display_binary_search(arr: list[int], key: int) -> None:
    """
    Display the result of the binary search operation.

    Args:
        arr: List of integers to search.
        key: Integer to search for in the list.
    """
    print(f"\n[INFO] The array: {arr}")
    print(f"[INFO] The target key: {key}")

    index, execution_time = binary_search_exec_time(arr=arr, key=key)
    verify(index)

    print(f"[INFO] Execution time of finding an element using binary search: {execution_time*1000:.3f} milliseconds")


if __name__ == "__main__":
    arr = random.choices(range(0, 99), k=10)
    arr.sort()
    print(arr)

    num = int(input("\n#Enter the number to search in the array:~$ "))
    index = binary_search(arr, key=num)
    if index is not None:
        print(f"\n=> The target key: {num} found at index: {index}")
    else:
        print(f"\n=> The target key: {num} not found in the array")

    arr = [i for i in range(1, 11)]
    display_binary_search(arr, key=5)
    display_binary_search(arr, key=7)
    display_binary_search(arr, key=12)

