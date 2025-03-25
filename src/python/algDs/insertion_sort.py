"""
Insertion sort is a simple sorting algorithm that works the way we sort playing cards in our hands.
It is less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.
"""
import time


def insertion_sort(arr):
    """
    Sort an array using the insertion sort algorithm.

    Args:
        arr: list of integers to sort
    
    return:
        arr: sorted list of integers
    """
    i = 1
    n = len(arr)

    if n <= 1:
        return
    else:
        while i < n:
            j = i
            while j > 0 and arr[j-1] > arr[j]:
                temp = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = temp
                j -= 1
            i += 1
    return arr


def insertion_sort_exec_time(arr):
    """
    Sort an array using the insertion sort algorithm
    
    Args:
        arr: list of integers to sort
    
    Returns:
        sorted_array: list of sorted integers
        exec_time: execution time in milliseconds
    """
    start = time.time()
    sorted_array = insertion_sort(arr)
    end = time.time()
    exec_time = (end - start) * 10**3

    return sorted_array, exec_time



def display_insertion_sort(arr):
    """
    Display the sorted array using the insertion sort algorithm

    Args:
        arr: list of integers to sort
    
    Returns:
        sorted_array: list of sorted integers
    """
    print("\n=> Unsorted array: ", arr)
    sorted_arr, exec_time = insertion_sort_exec_time(arr)

    print(f"Sorted array using basic insertion sort: {sorted_arr}")
    print("Execution time: {:.3f}\n".format(exec_time))

    return sorted_arr


if __name__ == "__main__":
    arr = [3, 4, 1, 2, 5]
    sorted_arr = display_insertion_sort(arr=arr)