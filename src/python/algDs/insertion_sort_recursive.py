"""
Insertion sort algorithm using recursive version
"""
import time


def insertion_sort_recursive(arr, n):
    """
    Sort an array using the insertion sort algorithm recursively
    
    Args:
        arr: list of integers to sort
    
    return:
        arr: sorted list of integers
    """
    if n <= 1:
        return
    elif n > 0:
        insertion_sort_recursive(arr, n-1)
        key = arr[n]
        j = n-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr


def insertion_sort_recursive_exec_time(arr):
    """
    Sort an array using the insertion sort algorithm recursive version
        Args:
        arr: list of integers to sort
    """
    len_arr = len(arr) - 1
    
    start = time.time()
    sorted_array = insertion_sort_recursive(arr, len_arr)
    end = time.time()
    exec_time = (end - start) * 10**3

    return sorted_array, exec_time


def display_insertion_sort(arr):
    """
    Display the sorted array using the insertion sort algorithm recursive version
    Args:
        arr: list of integers to sort
        Returns:
        sorted_array: list of sorted integers
    """
    print("\n=> Unsorted array: ", arr)
    sorted_array, exec_time = insertion_sort_recursive_exec_time(arr)
    
    print(f"Sorted array using recursive insertion sort: {sorted_array}")
    print("Execution time: {:.3f}\n".format(exec_time))
    
    return sorted_array


if __name__ == "__main__":
    arr = [3, 4, 1, 2, 5]
    sorted_arr = display_insertion_sort(arr=arr)