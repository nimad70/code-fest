"""
This module contains the sort_array function which performs the sort operation based on the user's selection.
"""
from src.python.algDs import insertionSort
from src.python.utils import menu
from src.python.utils import validate


def sort_array(arr):
    """
    Perform the sort operation based on the user's selection

    Args:
        arr: list of integers to sort
    """

    while True:
        try:
            menu.display_sort_options()
            sort_option = int(input("\n#Enter your choice (1-7):~$ "))

            if sort_option == 1:
                insertionSort.insertionSort(arr=arr)
                break
            elif sort_option == 7:
                """
                Exits the sort.
                """
                print("\nExiting the sort!")
                break
            else:
                validate.invalid_option(num_options=7)
        except:
            print("\n=> Invalid input. Please enter a valid number.")
