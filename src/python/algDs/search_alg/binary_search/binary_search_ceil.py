"""
Perform a binary search by taking the ceiling value of ((l+r)/2) on an array of integers.
"""
import time
import random
from src.python.utils.search_verify import verify


def binary_search_ceil(arr, key):
    """
    Perform a binary search by taking the ceiling value of ((l+r)/2) on an array of integers.
    This implementation of binary search returns the index of the rightmost element in case of duplicates.

    Args:
        arr: list of integers to search
        key: integer to search for in the array
        
    Return:
        index: index of the key in the array
    """
    left = 0
    right = len(arr) - 1
    
    while left != right:
        midpoint = int(-1 * ((-1 * (left+right)) // 2)) # the ceiling value of ((l+r)/2)
        if key < arr[midpoint]:
            right = midpoint - 1
        else:
            left = midpoint
    if arr[left] == key:
        return left
    
    return None


def binary_search_ceil_exec_time(arr, key):
    """
    Perform a binary search by taking the ceiling of ((l+r)/2) on an array of integers and return the execution time.
        
    Args:
        arr: list of integers to sort
        key: integer to search for in the array
    
    Returns:
        index: index of the key in the array
        exec_time: execution time in milliseconds
    """
    start = time.time()
    index = binary_search_ceil(arr=arr, key=key)
    end = time.time()
    execution_time = end - start

    return index, execution_time


def display_binary_search(arr, key):
    """
    Display the result of the binary search operation
        
    Args:
        arr: list of integers to sort
        key: integer to search for in the array
    """
    print(f"\n=> The array: {arr}")
    print(f"=> The target key: {key}")

    index, execution_time = binary_search_ceil_exec_time(arr=arr, key=key)
    verify(index)
    print(f"=> Execution time by taking the ceiling value of ((l+r)/2): {execution_time*10**3:.3f} seconds")


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

