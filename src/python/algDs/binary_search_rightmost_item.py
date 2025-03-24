"""
Binary search is a fast search algorithm with run-time complexity of O(log n). 
This algorithm works on the principle of divide and conquer. 
It is used to find the position of a specific value in a sorted array.
In this implementation, we return the index of the rightmost element in case of duplicates.
"""
import time
from src.python.utils.search_verify import verify


def binary_search_rightmost(arr, key):
    """
    This implementation of binary search returns the index of the rightmost element in case of duplicates.
    """
    left = 0
    right = len(arr)
    
    while left < right:
        midpoint = int((left+right) // 2) # floor of ((l+r)/2)
        if key < arr[midpoint]:
            right = midpoint
        else:
            left = midpoint + 1
    
    if arr[right-1] == key:
        return right-1
    
    return None


def binarySearch_rightmost_TimeCmpx(arr, key):
    """
    Perform a linear search by taking the ceiling value of ((l+r)/2) on an array of integers and return the execution time.
    """
    start = time.time()
    index = binary_search_rightmost(arr=arr, key=key)
    end = time.time()
    execution_time = end - start

    return index, execution_time


def display_binarySearch_rightmost(arr, key):
    """
    Display the result of the binary search operation
    """
    print(f"\n=> The array: {arr}")
    print(f"=> The target key: {key}")

    index, execution_time_ceil = binarySearch_rightmost_TimeCmpx(arr=arr, key=key)
    verify(index)
    print(f"=> Execution time by taking the ceiling value of ((l+r)/2): {execution_time_ceil*10**3:.3f} seconds")


if __name__ == "__main__":
    print("-" * 80)
    arr_dups = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5]
    print(arr_dups)

    display_binarySearch_rightmost(arr=arr_dups, key=3)
    display_binarySearch_rightmost(arr=arr_dups, key=4)
    display_binarySearch_rightmost(arr=arr_dups, key=5)
