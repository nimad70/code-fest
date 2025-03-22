import time
from src.python.algDs import insertionSort


def timeIt(func):
    """
    Compute and display the time of execution in milliseconds of a function
    
    Args:
        func: function to time
    """
    start = time.time()
    func()
    end = time.time()
    exe_time = (end - start) * 10**3
    print(f"The time of execution is: {exe_time} ms")


def display_menu():
    """
    Display the menu for the user to select the type of sort to perform
    """
    print("\nSelect the type of sort to perform:")
    print("1. Sort an array")
    print("2. Search in an array")
    print("3. Exit")


def display_sort():
    """
    Display the menu for the user to select the type of sort to perform
    """
    print("\nSelect the type of sort to perform:")
    print("1. Insertion sort")
    # print("2. Selection sort")
    # print("3. Bubble sort")
    # print("4. Quick sort")
    # print("5. Merge sort")
    # print("6. Heap sort")
    print("7. Exit")

def display_search():
    """
    Display the menu for the user to select the type of search to perform
    """
    print("\nSelect the type of search to perform:")
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


def array_sort(arr):
    """
    Perform the sort operation based on the user's selection

    Args:
        arr: list of integers to sort
    """
    display_sort()
    sort_option = int(input("Enter your choice (1-7): "))

    while True:
        if sort_option == 1:
            timeIt(insertionSort.insertionSort())
        elif sort_option == 7:
            """
            Exits the application.
            """
            print("Exiting the application!")
            break
        else:
            invalid_option(num_options=7)


if __name__ == "__main__":
    """
    Main function to run the program 
    and display the menu for the user to select the type of sort or search to perform
    """
    arr = [5, 2, 4, 6, 1, 3]
    soret_selected = False
    search_selected = False

    while True:
        display_menu()
        option = int(input("Enter your choice (1-3): "))

        if option == 1:
            # array_sort(arr)
            break
        elif option == 2:
            break

        elif option == 3:
            """
            Exits the application.
            """
            print("\nExiting the application!\n")
            break
        
        else:
            invalid_option(num_options=3)
