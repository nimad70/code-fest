"""
Binary search is a search algorithm that finds the position of a target value within a sorted array.
It compares the target value to the middle element of the array. If they are not equal, the half in which the target cannot lie
is eliminated and the search continues on the remaining half, again taking the middle element to compare to the target value, and repeating this until the target value is found.
The time complexity of the binary search algorithm is O(log n) where n is the number of elements in the array.
"""
import time
import random
# from src.python.utils.search_verify import verify


def verify(index):
    """
    Verify the index position of the target in the array
    """
    if index is not None:
        print("\n$:) => Hooray! Target found at index position:", index)
    else:
        print("\n$:( => Traget not found in the array")


def binary_search_floor(arr, key):
    """
    Perform a linear search by taking the floor of ((l+r)/2) on an array of integers.
    """
    left = 0
    right = len(arr) - 1 
    
    while left <= right:
        midpoint = int((left+right) // 2) # floor of ((l+r)/2)
        if arr[midpoint] == key:
            return midpoint
        elif arr[midpoint] < key:
            left = midpoint + 1
        else:
            right = midpoint - 1
    
    return None


def binary_search_ceil(arr, key):
    """
    Perform a linear search by taking the ceiling of ((l+r)/2) on an array of integers.
    This implementation of binary search returns the index of the rightmost element in case of duplicates.
    """
    left = 0
    right = len(arr) - 1
    
    while left != right:
        midpoint = int(-1 * ((-1 * (left+right)) // 2)) # ceil of ((l+r)/2)
        if key < arr[midpoint]:
            right = midpoint - 1
        else:
            left = midpoint
    if arr[left] == key:
        return left
    
    return None


def binarySearch_Floor_TimeCmpx(arr, key):
    """
    Perform a linear search by taking the floor of ((l+r)/2) on an array of integers and return the execution time.
    """
    start = time.time()
    index = binary_search_floor(arr=arr, key=key)
    end = time.time()
    execution_time = end - start

    return index, execution_time


def binarySearch_Ceil_TimeCmpx(arr, key):
    """
    Perform a linear search by taking the ceiling of ((l+r)/2) on an array of integers and return the execution time.
    """
    start = time.time()
    index = binary_search_ceil(arr=arr, key=key)
    end = time.time()
    execution_time = end - start

    return index, execution_time


def display_binarySearch(arr, key):
    """
    Display the result of the binary search operation
    """
    print(f"\n=> The array: {arr}")
    print(f"=> The target key: {key}")

    index, execution_time_ceil = binarySearch_Floor_TimeCmpx(arr=arr, key=key)
    verify(index)
    print(f"=> Execution time by taking the ceiling of ((l+r)/2): {execution_time_ceil*10**3:.3f} seconds")

    index, execution_time_floor = binarySearch_Ceil_TimeCmpx(arr=arr, key=key)
    verify(index)
    print(f"=> Execution time by taking the floor of ((l+r)/2): {execution_time_floor*10**3:.3f} seconds")


if __name__ == "__main__":
    arr = random.choices(range(0, 99), k=10)
    arr.sort()
    print(arr)

    num = int(input("\n#Enter the number to search in the array:~$ "))
    index = binary_search_floor(arr, key=num)
    if index is not None:
        print(f"\n=> The target key: {num} found at index: {index}")
    else:
        print(f"\n=> The target key: {num} not found in the array")

    arr = [i for i in range(1, 11)]
    display_binarySearch(arr, key=5)
    display_binarySearch(arr, key=7)
    display_binarySearch(arr, key=12)

