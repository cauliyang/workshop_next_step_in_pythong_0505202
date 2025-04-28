"""
This file will demonstrate Test-Driven Development with a statistics function.
The function will calculate basic statistics (min, max, average) for a list of numbers.
"""


def calculate_statistics(numbers):
    """Calculate statistics for a list of numbers.

    Args:
        numbers (list): A list of numbers

    Returns:
        dict: A dictionary containing min, max, and average values

    Raises:
        ValueError: If the input list is empty
    """
    if not numbers:
        raise ValueError("Cannot calculate statistics of an empty list")

    return {
        "min": min(numbers),
        "max": max(numbers),
        "average": sum(numbers) / len(numbers),
    }
