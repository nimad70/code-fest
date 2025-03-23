import random
from src.python.utils import validate

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


def create_array():
    """
    Create an array to sort or search in
    """
    # is_valid = False
    # while not is_valid:
    #     num = int(input("\n#Enter the number of elements in the array:~$ "))
    #     if invalid_number.is_valid(num=num):
    #         arr = []
    #         for i in range(num):
    #             is_element_invalid = False
    #             while not is_element_invalid:
    #                 arr_inputs = int(input(f"\n#Enter the element {i+1}: "))
    #                 if invalid_number.is_valid(num=arr_inputs):
    #                     arr.append(arr_inputs)
    #                     is_element_invalid = False
    #                 else:
    #                     print("\nInvalid input. Please enter a valid number.")

    #         is_valid = False
    #         return arr
    #     else:
    #         print("\nInvalid input. Please enter a valid number.")
    display_creat_array_options()
    array_option = int(input("\n#Enter your choice (1-3):~$ "))

    while True:
        if array_option == 1:
            num = int(input("\n#Enter the number of elements in the array:~$ "))
            arr = []
            for i in range(num):
                arr_inputs = int(input(f" -> Enter the element {i+1}: "))
                arr.append(arr_inputs)
            print(f"\n The array: {arr}")
            return arr
        elif array_option == 2:
            num = int(input("\n#Enter the number of elements in the array:~$ "))
            arr = random.choices(range(0, 99), k=num)
            print(f"\n The array: {arr}")
            return arr
        elif array_option == 3:
            """
            Exits the application.
            """
            print("\nExiting the sort!")
            break
        else:
            validate.invalid_option(num_options=3)