"""
Binary search is an efficient algorithm for finding a target value in a sorted array. 
It repeatedly compares the target with the middle element, eliminating half of the search space each time until the target is found. 
Its time complexity is O(log n).
"""
import time
import random
from src.python.utils.search_verify import verify


def binary_search(arr, key):
    """
    Perform a binary search by taking the floor of ((l+r)/2) on an array of integers.
    
    Args:
        arr: list of integers to search
        key: integer to search for in the array
        
    Return:
        index: index of the key in the array
    """
    left = 0
    right = len(arr) - 1 
    
    while left <= right:
        midpoint = int((left+right) // 2) # The floor value of ((l+r)/2)
        if arr[midpoint] == key:
            return midpoint
        elif arr[midpoint] < key:
            left = midpoint + 1
        else:
            right = midpoint - 1
    
    return None


def binary_search_exec_time(arr, key):
    """
    Perform a linear search by taking the floor of ((l+r)/2) on an array of integers and return the execution time.
    
    Args:
        arr: list of integers to sort
        key: integer to search for in the array
    
    Returns:
        index: index of the key in the array
        exec_time: execution time in milliseconds
    """
    start = time.time()
    index = binary_search(arr=arr, key=key)
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

    index, execution_time = binary_search_exec_time(arr=arr, key=key)
    verify(index)

    print(f"=> Execution time by taking the floor value of ((l+r)/2): {execution_time*10**3:.3f} seconds")


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

