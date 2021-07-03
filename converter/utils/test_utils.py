import random


def get_random_number(greater_than=0, less_than=100, round_to=3):
    """Function that generates a random floating point number between two
    numbers.

    Args:
        greater_than (int, optional): Low limit. Defaults to 0.
        less_than (int, optional): High limit. Defaults to 100.
        round_to (int, optional): Number to round the result to. Defaults to 3.

    Returns:
        [float]: Random number generated.
    """
    return round(random.uniform(greater_than, less_than), round_to or 3)
