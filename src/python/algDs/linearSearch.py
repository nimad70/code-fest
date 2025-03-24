"""
Linear search is a simple search algorithm that searches for a target in an array of integers.
It compares the target with each element in the array until it finds the target or reaches the end of the array.
The time complexity of the linear search algorithm is O(n) where n is the number of elements in the array.
"""
import time
from src.python.utils.search_verify import verify


def linearSearch(arr, key):
    """
    Perform a linear search on an array of integers. 
    Returns the index psoition of the target if found, otherwise returns None
    
    Args:
        arr: list of integers to search
        key: integer to search for in the array
        
    return:
        index: index of the key in the array
    """
    if len(arr) == 0:
        return None
    elif len(arr) == 1:
        if arr[0] == key:
            return i
    else:
        for i in range(len(arr)):
            if arr[i] == key:
                return i
    return None
        

def linearSearchTimeCmpx(arr, key):
    """
    Perform a linear search on an array of integers and return the execution time.
    """
    start = time.time()
    index = linearSearch(arr=arr, key=key)
    end = time.time()
    execution_time = end - start

    return index, execution_time


def display_linearSearch(arr, key):
    """
    Display the result of the linear search operation
    """
    index, execution_time = linearSearchTimeCmpx(arr=arr, key=key)
    verify(index)
    print(f"=> Execution time: {execution_time*10**3:.3f} seconds")


if __name__ == "__main__":
    arr = [i for i in range(1, 11)]
    
    result = linearSearch(arr, key=5)
    verify(result)

    result = linearSearch(arr, key=12)
    verify(result)