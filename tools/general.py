from typing import List, Tuple
import os

# Declare constants
OUTPUT_FOLDER = "output"

def merge_strings(
        strings: List[str],
        separator: str = " "
    ) -> str:
    """
    Merge a list of strings into a single string.

    Args:
        strings (List[str]): A list of strings to merge.
        separator (str): The separator to use between the strings. Defaults to a space.

    Returns:
        str: A single string with all the strings merged.
    """
    return separator.join(strings)

def save_to_file(
        content: str,
        filename: str,
    ) -> Tuple[bool, str]:
    """
    Save a string to a file.

    Args:
        content (str): The content to save to the file.
        filename (str): The name of the file to save the content to.
    Returns:
        Tuple[bool, str]: A tuple containing a boolean indicating whether the file was saved successfully and the path to the file.
    """
    try:
        os.makedirs(OUTPUT_FOLDER, exist_ok=True)
        with open(f"{OUTPUT_FOLDER}/{filename}", "w") as file:
            file.write(content)

        return True, f"{OUTPUT_FOLDER}/{filename}"
    except OSError as e:
        print(f"Error creating output folder: {e}")
        return False, ""