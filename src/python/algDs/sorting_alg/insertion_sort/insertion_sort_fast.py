"""
Insertion sort algorithm faster version
"""
import time


def insertion_sort_faster(arr):
    """
    Sort an array using the insertion sort algorithm with moving A[i] to its position in one go and 
    only performs one assignment in the inner loop body.

    Args:
    arr: list of integers to sort

    Return:
        arr: sorted list of integers
    """
    i = 1
    n = len(arr)

    if n <= 1:
        return
    else:
        while i < n:
            key = arr[i]
            j = i
            while j > 0 and arr[j-1] > key:
                arr[j] = arr[j-1]
                j -= 1
            arr[j] = key
            i += 1
    return arr


def insertion_sort_faster_exec_time(arr):
    """
    Sort an array using the insertion sort algorithm faster version
    
    Args:
        arr: list of integers to sort
    
    Returns:
        sorted_array: list of sorted integers
        exec_time: execution time in milliseconds
    """
    start = time.time()
    sorted_array = insertion_sort_faster(arr)
    end = time.time()
    exec_time = (end - start) * 10**3

    return sorted_array, exec_time


def display_insertion_sort(arr):
    """
    Display the sorted array using the insertion sort algorithm faster version
    
    Args:
        arr: list of integers to sort
    
    Returns:
        sorted_array: list of sorted integers
    """
    print("\n=> Unsorted array: ", arr)
    sorted_array, exec_time_insertion_sort = insertion_sort_faster_exec_time(arr)

    print(f"Sorted array using insertion sort without swapping: {sorted_array}")
    print("Execution time: {:.3f}\n".format(exec_time_insertion_sort))

    return sorted_array


if __name__ == "__main__":
    arr = [3, 4, 1, 2, 5]
    sorted_arr = display_insertion_sort(arr=arr)