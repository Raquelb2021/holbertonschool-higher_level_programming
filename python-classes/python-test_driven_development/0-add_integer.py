#!/usr/bin/python3
def add_integer(a, b=98):
    """Adds two integers or floats and returns an integer.

    Args:
        a (int or float): The first operand.
        b (int or float): The second operand.


    Returns:
        int: The sum of a and b as an integer.


    Raises:
        TypeError: If a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
