"""
Binary search is a search algorithm that finds the position of a target value within a sorted array.
It compares the target value to the middle element of the array. If they are not equal, the half in which the target cannot lie
is eliminated and the search continues on the remaining half, again taking the middle element to compare to the target value, and repeating this until the target value is found.
The time complexity of the binary search algorithm is O(log n) where n is the number of elements in the array.
"""
import time
from src.python.utils.search_verify import verify


def binarySearch(arr, key):
    pass


def binarySearchTimeCmpx(arr, key):
    """
    Perform a linear search on an array of integers and return the execution time.
    """
    start = time.time()
    index = binarySearch(arr=arr, key=key)
    end = time.time()
    execution_time = end - start

    return index, execution_time


def display_binarySearch(arr, key):
    """
    Display the result of the binary search operation
    """
    index, execution_time = binarySearchTimeCmpx(arr=arr, key=key)
    verify(index)
    print(f"=> Execution time: {execution_time*10**3:.3f} seconds")


if __name__ == "__main__":
    arr = [i for i in range(1, 11)]
    
    result = binarySearch(arr, key=5)
    verify(result)

    result = binarySearch(arr, key=12)
    verify(result)