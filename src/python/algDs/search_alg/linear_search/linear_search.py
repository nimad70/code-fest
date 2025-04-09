"""
Linear search is a basic algorithm that checks each element in an array sequentially until it finds the target or reaches the end. 
Its time complexity is O(n).
"""

import random
import time
from typing import Optional, Tuple

from src.python.utils.search_verify import verify


def linear_search(arr: list[int], key: int) -> Optional[int]:
    """
    Perform a linear search on a list of integers.

    Args:
        arr: List of integers to search.
        key: Integer to search for in the list.

    Returns:
        The index of the key in the list if found, otherwise None.
    """
    for i in range(0, len(arr)):
        if arr[i] == key:
            return i
    return None
        

def linear_search_exec_time(arr: list[int], key: int) -> Tuple[Optional[int], float]:
    """
    Perform a linear search on a list of integers and return the execution time.

    Args:
        arr: List of integers to search.
        key: Integer to search for in the list.

    Returns:
        A tuple containing:
        - The index of the key in the list if found, otherwise None.
        - The execution time in seconds.
    """
    start = time.time()
    index = linear_search(arr=arr, key=key)
    end = time.time()
    execution_time = end - start

    return index, execution_time


def display_linear_search(arr: list[int], key: int) -> None:
    """
    Display the result of the linear search operation.

    Args:
        arr: List of integers to search.
        key: Integer to search for in the list.
    """
    index, execution_time = linear_search_exec_time(arr=arr, key=key)
    verify(index)

    print(f"\n[INFO] The array: {arr}")
    print(f"[INFO] The target key: {key}")
    print(f"[INFO] Execution time: {execution_time*1000:.3f} milliseconds")


if __name__ == "__main__":
    # arr = [i for i in range(1, 11)]
    arr = random.choices(range(0, 99), k=7)
    print(arr)
    
    # result = linearSearch(arr, key=5)
    # verify(result)

    # result = linearSearch(arr, key=12)
    # verify(result)

    num = int(input("\n#Enter the number to search in the array:~$ "))
    index, execution_time = linear_search_exec_time(arr, key=num)
    if index is not None:
        print(f"\n=> The target key: {num} found at index: {index}")
        print(f"=> Execution time: {execution_time*10**3:.3f} seconds")
    else:
        print(f"\n=> The target key: {num} not found in the array")
        print(f"=> Execution time: {execution_time*10**3:.3f} seconds")