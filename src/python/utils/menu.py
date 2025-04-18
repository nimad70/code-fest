"""
This module contains the functions to display the menu options for the user
"""

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


def display_search_options():
    """
    Display the menu for the user to select the type of search to perform
    """
    option_text = "\n#Select the type of search to perform:\n"
    print(f"\n{'-' * len(option_text)}")
    print(option_text)
    print("1. Linear search")
    print("2. Binary search")
    print("3. Binary search - finding the leftmost index in an array contains duplicates")
    print("4. Binary search - finding the rightmost index in an array contains duplicates")
    print("5. Exit")


def display_creat_array_options():
    """
    Display the menu for the user to select the type of array creation to perform
    """
    option_text = "\n#Select the type of process to perform:\n"
    print(f"\n{'-' * len(option_text)}")
    print(option_text)
    print("1. Build an customized array")
    print("2. Build a random array by the program")
    print("3. Exit")


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


