"""
Binary search is a fast search algorithm with run-time complexity of O(log n). 
This algorithm works on the principle of divide and conquer. 
It is used to find the position of a specific value in a sorted array.
In this implementation, we return the index of the leftmost element in case of duplicates.
"""
import time
from src.python.utils.search_verify import verify


def binary_search_leftmost(arr, key):
    """
    This implementation of binary search returns the index of the leftmost element in case of duplicates.
    
    Args:
        arr: list of integers to search
        key: integer to search for in the array
        
    Return:
        index: index of the key in the array
    """
    left = 0
    right = len(arr)
    
    while left < right:
        midpoint = int((left+right) // 2) # The floor value of ((l+r)/2)
        if key > arr[midpoint]:
            left = midpoint + 1
        else:
            right = midpoint
    
    if arr[left] == key:
        return left
    
    return None


def binary_search_leftmost_exec_time(arr, key):
    """
    Perform a linear search on an array of integers and return the execution time.
        
    Args:
        arr: list of integers to sort
        key: integer to search for in the array
    
    Returns:
        index: index of the key in the array
        exec_time: execution time in milliseconds
    """
    start = time.time()
    index = binary_search_leftmost(arr=arr, key=key)
    end = time.time()
    execution_time = end - start

    return index, execution_time


def display_binary_search_leftmost(arr, key):
    """
    Display the result of the binary search operation
        
    Args:
        arr: list of integers to sort
        key: integer to search for in the array
    """
    print(f"\n=> The array: {arr}")
    print(f"=> The target key: {key}")

    index, execution_time = binary_search_leftmost_exec_time(arr=arr, key=key)
    verify(index)
    print(f"=> Execution time by taking the floor value of ((l+r)/2): {execution_time*10**3:.3f} seconds")



if __name__ == "__main__":
    print("-" * 80)
    arr_dups = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5]
    print(arr_dups)

    display_binary_search_leftmost(arr=arr_dups, key=3)
    display_binary_search_leftmost(arr=arr_dups, key=4)
    display_binary_search_leftmost(arr=arr_dups, key=5)

