#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is not None and isinstance(roman_string, str):
        roman_num = {"I": 1, "V": 5, "X": 10,
                     "L": 50, "C": 100, "D": 500, "M": 1000}

        size = len(roman_string)
        result = 0

        for idx, value in enumerate(roman_string):
            value = roman_num.get(value)
            if idx < size - 1 and roman_num.get(roman_string[idx + 1]) > value:
                result -= value
            else:
                result += value
        return result
    return 0
