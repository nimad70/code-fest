"""
Linear search is a simple search algorithm that searches for a target in an array of integers.
It compares the target with each element in the array until it finds the target or reaches the end of the array.
The time complexity of the linear search algorithm is O(n) where n is the number of elements in the array.
"""
import time


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
    i = 0
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return None
        

def linearSearchTimeCmpx(arr, key):
    start = time.time()
    index = linearSearch(arr=arr, key=key)
    end = time.time()
    execution_time = end - start

    return index, execution_time


def verify(index):
    """
    Verify the index position of the target in the array
    """
    if index is not None:
        print("Target found at index position:", index)
    else:
        print("Traget not found in the array")


if __name__ == "__main__":
    arr = [i for i in range(1, 11)]
    
    result = linearSearch(arr, key=5)
    verify(result)

    result = linearSearch(arr, key=12)
    verify(result)