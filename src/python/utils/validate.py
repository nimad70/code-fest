"""
Utility functions for validating user input.
This module contains functions to validate user input for menu options and numbers.
"""

import re


def invalid_option(num_options: int) -> None:
    """
    Handles invalid menu selections.

    Args:
        num_options: Total number of menu options available.
    """
    invalid_option_text = f"Invalid choice. Please select a valid option between 1 to {num_options}."
    print()
    print(f"\n{'-' * len(invalid_option_text)}")
    print(f"{invalid_option_text}")
    print('-' * len(invalid_option_text))


def validate_number(num: int) -> bool:
    """
    Check if the input is a valid number (1 to 5 digits).

    Args:
        is_list: If True, input is part of a list of numbers.
        num: The input string to validate.

    Returns:
        True if the input is a valid number, False otherwise.
    """
    num_pattern = re.compile('^\d{1,5}$')
    # # Uncomment for negative numbers patter
    # negative_num_pattern = re.compile('^-?\d{1,5}$')
    # float_patter = re.compile('^-?\d{1,5}(\.\d+)?$')

    return bool(num_pattern.fullmatch(num))


if __name__ == "__main__":
    num = input("\n# Enter the number of elements in the array:~$ ")
    is_valid = validate_number(num=num)
    if is_valid:
        print("\n# Valid input.")
    else:
        print("\n# Invalid input. Please enter a number with 1 to 5 digits.")
