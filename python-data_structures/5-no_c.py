#!/usr/bin/python3
def no_c(my_string):
    my_string_cpy = ""
    for letter in my_string:
        if letter == "c" or letter == "C":
            continue
        my_string_cpy += letter
    return my_string_cpy
