def insertionSort_basic(arr):
    """
    Sort an array using the insertion sort algorithm

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


def insertionSortWithoutSwap(arr):
    """
    Sort an array using the insertion sort algorithm without swapping 

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
            key = arr[i]
            j = i
            while j > 0 and arr[j-1] > key:
                arr[j] = arr[j-1]
                j -= 1
            arr[j] = key
            i += 1
    return arr


def insertionSortRecursive(arr, n):
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
        insertionSortRecursive(arr, n-1)
        key = arr[n]
        j = n-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr


def insertionSort(arr):
    """
    Sort an array using the insertion sort algorithm variations
        Args:
        arr: list of integers to sort
    """
    len_arr = len(arr) - 1
    
    sorted_arr = insertionSort_basic(arr)
    sorted_arr_ws = insertionSortWithoutSwap(arr)
    sorted_arr_r = insertionSortRecursive(arr, len_arr)

    print(f"Sorted array using basic insertion sort: {sorted_arr}")
    print(f"Sorted array using insertion sort without swapping: {sorted_arr_ws}")
    print(f"Sorted array using recursive insertion sort: {sorted_arr_r}")


if __name__ == "__main__":
    arr = [3, 4, 1, 2, 5]
    insertionSort(arr=arr)