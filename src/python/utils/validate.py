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


def is_valid_number(is_list, num):
    """
    Check if the input is a valid number
    """
    list_num_reg = re.compile('^[0-9]{1,5}$')
    num_reg = re.compile('^[0-9]{1,5}$')

    if is_list:
        matched = list_num_reg.fullmatch(num)
        return matched
    
    matched = bool(num_reg.fullmatch(num))
    return matched


if __name__ == "__main__":
    num = input("\n#Enter the number of elements in the array:~$ ")
    is_valid = is_valid_number(is_list=True, num=num)
    if is_valid:
        print("\n#is valid")
