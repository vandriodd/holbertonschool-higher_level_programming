#!/usr/bin/python3
def no_c(my_string):
    for i, letter in enumerate(my_string):
        if letter == "c" or letter == "C":
            return my_string[:i] + my_string[i+1:]
    return my_string
