from src.python.algDs import insertionSort


def display_menu():
    """
    Display the menu for the user to select the type of sort to perform
    """
    option_text = "\n#Select the type of process to perform:\n"
    print(f"\n{'-' * len(option_text)}")
    print(option_text)
    print("1. Create an array")
    print("2. Sort an array")
    print("3. Search in an array")
    print("4. Exit")


def display_sort_options():
    """
    Display the menu for the user to select the type of sort to perform
    """
    option_text = "\n#Select the type of sort to perform:\n"
    print(f"\n{'-' * len(option_text)}")
    print(option_text)
    print("1. Insertion sort")
    # print("2. Selection sort")
    # print("3. Bubble sort")
    # print("4. Quick sort")
    # print("5. Merge sort")
    # print("6. Heap sort")
    print("7. Exit")

def display_search_options():
    """
    Display the menu for the user to select the type of search to perform
    """
    option_text = "\n#Select the type of search to perform:\n"
    print(f"\n{'-' * len(option_text)}")
    print(option_text)
    print("1. Linear search")
    print("2. Binary search")
    print("3. Exit")


def invalid_option(num_options):
    """
    Handles invalid menu selections.
    """
    invalid_option_text = f"Invalid choice. Please select a valid option between 1 to {num_options}."
    print()
    print(f"\n{'-' * len(invalid_option_text)}")
    print(f"{invalid_option_text}")
    print('-' * len(invalid_option_text))


def create_array():
    """
    Create an array to sort or search in
    """
    pass


def sort_array(arr):
    """
    Perform the sort operation based on the user's selection

    Args:
        arr: list of integers to sort
    """
    display_sort_options()
    sort_option = int(input("\n#Enter your choice (1-7):~$ "))

    while True:
        if sort_option == 1:
            insertionSort.insertionSort(arr=arr)
            break
        elif sort_option == 7:
            """
            Exits the application.
            """
            print("\nExiting the sort!")
            break
        else:
            invalid_option(num_options=7)


if __name__ == "__main__":
    """
    Main function to run the program 
    and display the menu for the user to select the type of sort or search to perform
    """
    arr = [5, 2, 4, 9, 1, 3]
    """""
    pre arry of a cutom array
    """
    soret_selected = False
    search_selected = False

    while True:
        display_menu()
        option = int(input("\n#Enter your choice (1-3):~$ "))

        if option == 1:
            # arr = create_array()
            break
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
            invalid_option(num_options=3)
