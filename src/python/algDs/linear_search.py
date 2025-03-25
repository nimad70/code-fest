"""
Linear search is a basic algorithm that checks each element in an array sequentially until it finds the target or reaches the end. 
Its time complexity is O(n).
"""
import time
import random
from src.python.utils.search_verify import verify


def linear_search(arr, key):
    """
    Perform a linear search on an array of integers. 
    Returns the index psoition of the target if found, otherwise returns None
    
    Args:
        arr: list of integers to search
        key: integer to search for in the array
        
    Return:
        index: index of the key in the array
    """
    if len(arr) == 0:
        return None
    elif len(arr) == 1:
        if arr[0] == key:
            return 0
    else:
        for i in range(len(arr)):
            if arr[i] == key:
                return i
    return None
        

def linear_search_exec_time(arr, key):
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
    index = linear_search(arr=arr, key=key)
    end = time.time()
    execution_time = end - start

    return index, execution_time


def display_linear_search(arr, key):
    """
    Display the result of the linear search operation
    
    Args:
        arr: list of integers to sort
        key: integer to search for in the arr
    """
    index, execution_time = linear_search_exec_time(arr=arr, key=key)
    verify(index)

    print(f"\n=> The array: {arr}")
    print(f"=> The target key: {key}")
    print(f"=> Execution time: {execution_time*10**3:.3f} seconds")


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