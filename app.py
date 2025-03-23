"""
This is the main file that runs the program.
"""
from src.python.utils import validate
from src.python.utils import build_array
from src.python.utils import menu
from src.python.utils import sort_it


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
                sort_it.sort_array(arr)
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
