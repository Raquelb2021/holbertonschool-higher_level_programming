#!/usr/bin/python3
"""module that contem a function matrix_divided"""


def matrix_divided(matrix, div):
    """function that divides all elements of a matrix

    args: matrix must be a list of lists of integers or floats
    div: must be a number (integer or float)

    Return: a new matrix
    """
    if type(matrix) != list or matrix == []:
         raise TypeError("matrix must be a matrix\
 (list of lists) of integers/floats")


