import re


def invalid_option(num_options):
    """
    Handles invalid menu selections.
    """
    invalid_option_text = f"Invalid choice. Please select a valid option between 1 to {num_options}."
    print()
    print(f"\n{'-' * len(invalid_option_text)}")
    print(f"{invalid_option_text}")
    print('-' * len(invalid_option_text))


def is_valid_number(num):
    """
    Check if the input is a valid single number
    """
    num_reg = re.compile('^[0-9]$')
    matched = bool(num_reg.fullmatch(num))

    return matched
