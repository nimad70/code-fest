"""
Linear search is a simple search algorithm that searches for a target in an array of integers.
It compares the target with each element in the array until it finds the target or reaches the end of the array.
The time complexity of the linear search algorithm is O(n) where n is the number of elements in the array.
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
        
    return:
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
    """
    start = time.time()
    index = linear_search(arr=arr, key=key)
    end = time.time()
    execution_time = end - start

    return index, execution_time


def display_linear_search(arr, key):
    """
    Display the result of the linear search operation
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