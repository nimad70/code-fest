from src.python.algDs import insertionSort
from src.python.utils import validate
from src.python.utils import build_array
from src.python.utils import menu


def sort_array(arr):
    """
    Perform the sort operation based on the user's selection

    Args:
        arr: list of integers to sort
    """

    while True:
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


if __name__ == "__main__":
    """
    Main function to run the program 
    and display the menu for the user to select the type of sort or search to perform
    """
    arr = [5, 2, 4, 6, 1, 3] # The default array
    soret_selected = False
    search_selected = False

    while True:
        try:
            menu.display_menu()
            option = int(input("\n#Enter your choice (1-3):~$ "))

            if option == 1:
                arr = build_array.create_array()
            elif option == 2:
                sort_array(arr)
            elif option == 3:
                break
            elif option == 4:
                """
                Exits the application.
                """
                print("\nExiting the application!\n")
                break
            
            else:
                validate.invalid_option(num_options=3)
        
        except ValueError:
            print("\n=> Invalid input. Please enter a valid number.")
