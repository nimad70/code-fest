"""
This module is responsible for searching for the target in array based on the user's input.
"""
from src.python.algDs import linearSearch
from src.python.utils import menu
from src.python.utils import validate


def search_target(arr):
    """
    Perform the search operation based on the user's selection

    Args:
        arr: list of integers to sort
    """

    while True:
        try:
            menu.display_search_options()
            search_option = int(input("\n#Enter your choice (1-7):~$ "))

            if search_option == 1:
                linearSearch.linearSearch(arr=arr)
                break
            elif search_option == 7:
                """
                Exits the sort.
                """
                print("\nExiting the sort!")
                break
            else:
                validate.invalid_option(num_options=7)
        except:
            print("\n=> Invalid input. Please enter a valid number.")
