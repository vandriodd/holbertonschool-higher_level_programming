#!/usr/bin/python3
"""
    12-pascal_triangle module
"""


def pascal_triangle(n):
    """ Returns the Pascal's triangle up to depth n """
    if n <= 0:
        return []
    triangle = [[1]]
    for row_number in range(1, n):
        new_row = [1]
        for num in range(1, row_number):
            current_number = triangle[row_number - 1][num - 1]
            next_number = triangle[row_number - 1][num]
            sum = current_number + next_number
            new_row.append(sum)
        new_row.append(1)
        triangle.append(new_row)
    return triangle
