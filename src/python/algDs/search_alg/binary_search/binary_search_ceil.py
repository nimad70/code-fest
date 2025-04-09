"""
Perform a binary search by taking the ceiling value of ((l+r)/2) on an array of integers.
"""

import time
import random
from typing import Optional, Tuple

from src.python.utils.search_verify import verify


def binary_search_ceil(arr: list[int], key: int) -> Optional[int]:
    """
    Perform a binary search using the ceiling value of (left + right) / 2.
    This implementation returns the index of the rightmost occurrence in case of duplicates.

    Args:
        arr: List of integers to search.
        key: Integer to search for in the list.

    Returns:
        The index of the key in the list if found (rightmost occurrence), otherwise None.
    """
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        midpoint = int(-1 * ((-1 * (left + right)) // 2))
        # midpoint = int((left + right + 1) // 2)
        if key < arr[midpoint]:
            right = midpoint - 1
        else:
            left = midpoint
    if 0 <= left < len(arr) and arr[left] == key:
        return left
    
    return None


def binary_search_ceil_exec_time(arr: list[int], key: int) -> Tuple[Optional[int], float]:
    """
    Perform a binary search using the ceiling of (left + right) / 2 and return the execution time.

    Args:
        arr: List of integers to search.
        key: Integer to search for in the list.

    Returns:
        A tuple containing:
        - The index of the key in the list (rightmost occurrence if duplicates exist), or None if not found.
        - The execution time in seconds.
    """
    start = time.time()
    index = binary_search_ceil(arr=arr, key=key)
    end = time.time()
    execution_time = end - start

    return index, execution_time


def display_binary_search(arr: list[int], key: int) -> None:
    """
    Display the result of the binary search operation using ceiling midpoint logic.

    Args:
        arr: List of integers to search.
        key: Integer to search for in the list.
    """
    print(f"\n[INFO] The array: {arr}")
    print(f"[INFO] The target key: {key}")

    index, execution_time = binary_search_ceil_exec_time(arr=arr, key=key)
    verify(index)
    print(f"[INFO] Execution time by taking the ceiling value of ((l+r)/2): {execution_time*1000:.3f} milliseconds")


if __name__ == "__main__":
    arr = random.choices(range(0, 99), k=10)
    arr.sort()
    print(arr)

    num = int(input("\n#Enter the number to search in the array:~$ "))
    index = binary_search_ceil(arr, key=num)
    if index is not None:
        print(f"\n=> The target key: {num} found at index: {index}")
    else:
        print(f"\n=> The target key: {num} not found in the array")

    arr = [i for i in range(1, 11)]
    display_binary_search(arr, key=5)
    display_binary_search(arr, key=7)
    display_binary_search(arr, key=12)

