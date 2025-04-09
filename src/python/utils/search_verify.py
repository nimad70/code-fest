"""
Verify whether the target is in the array
"""

from typing import Optional

def verify(index: Optional[int]) -> None:
    """
    Verify the index position of the target in the array.
    """
    if index is not None:
        print(f"\n[SUCCESS] Hooray! Target found at index position: {index}.")
    else:
        print("\n[WARNING] Target not found in the array.")

