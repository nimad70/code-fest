"""
This module is responsible for searching for the target in array based on the user's input.
"""
from src.python.utils import menu
from src.python.utils import validate
from src.python.algDs import linear_search
from src.python.algDs import binary_search
from src.python.algDs import binary_search_leftmost_item
from src.python.algDs import binary_search_rightmost_item


def search_target(arr):
    """
    Perform the search operation based on the user's selection

    Args:
        arr: list of integers to sort
    """

    while True:
        try:
            menu.display_search_options()
            search_option = int(input("\n#Enter your choice (1-3):~$ "))
            
            # Linear search
            if search_option == 1:
                while True:
                    try:
                        key = int(input("\n#Enter a number to search in the array (<= 5 digits):~$ "))
                        if len(str(key)) <= 5:
                            linear_search.display_linear_search(arr=arr, key=key)
                            break                       
                        else:
                            print("\n=> Really? more than 5 digits?! Please enter a valid number.")
                    except ValueError:
                        print("\n=> Invalid input. Please enter a valid number.")
                    break
            
            # binary search
            elif search_option == 2:
                while True:
                    try:
                        key = int(input("\n#Enter a number to search in the array (<= 5 digits):~$ "))
                        if len(str(key)) <= 5:
                            binary_search.display_binary_search(arr=arr, key=key)
                            break                       
                        else:
                            print("\n=> Really? more than 5 digits?! Please enter a valid number.")
                    except ValueError:
                        print("\n=> Invalid input. Please enter a valid number.")
                    break
            
            # binary search in an array contains duplicates to find the leftmost index
            elif search_option == 3:
                while True:
                    try:
                        key = int(input("\n#Enter a number to search in the array (<= 5 digits):~$ "))
                        if len(str(key)) <= 5:
                            binary_search_leftmost_item.display_binary_search_leftmost(arr=arr, key=key)
                            break                       
                        else:
                            print("\n=> Really? more than 5 digits?! Please enter a valid number.")
                    except ValueError:
                        print("\n=> Invalid input. Please enter a valid number.")
                    break
            
            # binary search in an array contains duplicates to find the rightmost index
            elif search_option == 4:
                while True:
                    try:
                        key = int(input("\n#Enter a number to search in the array (<= 5 digits):~$ "))
                        if len(str(key)) <= 5:
                            binary_search_rightmost_item.display_binary_search_rightmost(arr=arr, key=key)
                            break                       
                        else:
                            print("\n=> Really? more than 5 digits?! Please enter a valid number.")
                    except ValueError:
                        print("\n=> Invalid input. Please enter a valid number.")
                    break
            
            elif search_option == 5:
                """
                Exits the search.
                """
                print("\nExiting the search!")
                break
            else:
                validate.invalid_option(num_options=7)
        except:
            print("\n=> Invalid input. Please enter a valid number.")
