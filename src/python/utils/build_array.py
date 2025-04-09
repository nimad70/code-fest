"""
This module contains the function to create an array to sort or search in.
"""

import random

from src.python.utils.menu import display_creat_array_options
import src.python.utils.validate as validate 
# import menu
# import validate


def create_array() -> list[int]:
    """
    Create an array to sort or search in.

    Returns:
        A list of integers based on user input or a default array.
    """
    default_array = [5, 2, 4, 6, 1, 3]

    while True:
        try:
            display_creat_array_options()
            array_option = int(input("\n# Enter your choice (1-3):~$ "))

            if array_option == 1:
                while True:
                    try:
                        num = int(input("\n# Enter the number of elements in the array (less than 100):~$ "))
                        if 0 < num <= 100 :
                            arr = []
                            for i in range(num):
                                while True:
                                    try:
                                        array_input = int(input(f"\n# Enter the element {i + 1} (<= 5 digits): "))
                                        if abs(array_input) < 100000:
                                            arr.append(array_input)
                                            break
                                        else:
                                            print("\n[ERROR] Invalid input. Please enter a valid number!")
                                    except ValueError:
                                        print("\n[ERROR] Invalid input. Please enter a valid number!")
                            print(f"\n[INFO] The array: {arr}")
                            return arr
                        else:
                            print("\n[WARNING] Really? more than <100> inputs?! Please enter a valid number!")
                    except ValueError:
                        print("\n[ERROR] Invalid input. Please enter a valid number.")
            
            elif array_option == 2:
                while True:
                    try:
                        num = int(input("\n# Enter the number of elements in the array (less than 100):~$ "))
                        if 0 < num < 100:
                            arr = random.choices(range(0, 99), k=num)
                            print(f"\n[INFO] The array: {arr}")
                            return arr
                        else:
                            print("\n[WARNING] Really? more than <100> inputs?! Please enter a valid number!")
                    except ValueError:
                        print("\n[ERROR] Invalid input. Please enter a valid number.")
                        
            elif array_option == 3:
                """
                Exits the build an array.
                """
                print("\n[INFO] Continue with the default array.")
                print(f"=> The default array: {default_array}")
                break
            
            else:
                validate.invalid_option(num_options=3)
        
        except ValueError:
            print("\n[ERROR] Invalid input. Please enter a valid number.")
    
    return default_array


if __name__ == "__main__":
    arr = create_array()