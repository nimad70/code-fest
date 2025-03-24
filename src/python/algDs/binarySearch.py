"""
Binary search is a search algorithm that finds the position of a target value within a sorted array.
It compares the target value to the middle element of the array. If they are not equal, the half in which the target cannot lie
is eliminated and the search continues on the remaining half, again taking the middle element to compare to the target value, and repeating this until the target value is found.
The time complexity of the binary search algorithm is O(log n) where n is the number of elements in the array.
"""
import time
# from src.python.utils.search_verify import verify

"""
Verify whether the target is in the array
"""

def verify(index):
    """
    Verify the index position of the target in the array
    """
    if index is not None:
        print("\n$:) => Hooray! Target found at index position:", index)
    else:
        print("\n$:( => Traget not found in the array")

def ceil(l, r, divident=2):
    """
    Return the ceiling value of a number
    """
    return int(-1 * ((-1 * (l+r)) // divident))


def floor(l, r, divident=2):
    """
    Return the floor value of a number
    """
    return int((l+r) // divident)


def binarySearchFloor(arr, key):
    """
    Perform a linear search by taking the floor of ((l+r)/2) on an array of integers.
    """
    l = 0
    r = len(arr) - 1 
    
    while l <= r:
        mid = floor(l, r)
        if key == arr[mid]:
            return mid
        elif key < arr[mid]:
            r = mid - 1
        else:
            l = mid + 1
    
    return None


def binarySearchCeil(arr, key):
    """
    Perform a linear search by taking the ceiling of ((l+r)/2) on an array of integers.
    This implementation of binary search returns the index of the rightmost element in case of duplicates.
    """
    l = 0
    r = len(arr) - 1
    
    while l != r:
        mid = ceil(l, r)
        if key < arr[mid]:
            r = mid - 1
        else:
            l = mid
    if arr[l] == key:
        return l
    
    return None


def binary_search_leftmost(arr, key):
    """
    This implementation of binary search returns the index of the leftmost element in case of duplicates.
    """
    l = 0
    r = len(arr)
    
    while l < r:
        mid = floor(l, r)
        if key > arr[mid]:
            l = mid + 1
        else:
            r = mid
    
    if arr[l] == key:
        return l
    
    return None



def binary_search_rightmost(arr, key):
    """
    This implementation of binary search returns the index of the rightmost element in case of duplicates.
    """
    l = 0
    r = len(arr)
    
    while l < r:
        mid = floor(l, r)
        if key < arr[mid]:
            r = mid
        else:
            l = mid + 1
    
    if arr[r-1] == key:
        return r-1
    
    return None


def binarySearchFloorTimeCmpx(arr, key):
    """
    Perform a linear search by taking the floor of ((l+r)/2) on an array of integers and return the execution time.
    """
    start = time.time()
    index = binarySearchFloor(arr=arr, key=key)
    end = time.time()
    execution_time = end - start

    return index, execution_time


def binarySearchCeilTimeCmpx(arr, key):
    """
    Perform a linear search by taking the ceiling of ((l+r)/2) on an array of integers and return the execution time.
    """
    start = time.time()
    index = binarySearchCeil(arr=arr, key=key)
    end = time.time()
    execution_time = end - start

    return index, execution_time


def display_binarySearch(arr, key):
    """
    Display the result of the binary search operation
    """
    print(f"\n=> The array: {arr}")
    print(f"=> The target key: {key}")

    index, execution_time_floor = binarySearchFloorTimeCmpx(arr=arr, key=key)
    verify(index)
    print(f"=> Execution time by taking the floor of ((l+r)/2): {execution_time_floor*10**3:.3f} seconds")

    index, execution_time_ceil = binarySearchFloorTimeCmpx(arr=arr, key=key)
    verify(index)
    print(f"=> Execution time by taking the ceiling of ((l+r)/2): {execution_time_ceil*10**3:.3f} seconds")


if __name__ == "__main__":
    arr = [i for i in range(1, 11)]
    print(arr)

    display_binarySearch(arr, key=3)
    display_binarySearch(arr, key=5)
    display_binarySearch(arr, key=7)
    display_binarySearch(arr, key=12)