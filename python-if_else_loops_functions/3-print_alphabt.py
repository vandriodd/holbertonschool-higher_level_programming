#!/usr/bin/python3
for letter in range(97, 123):
    if letter == 'e' or letter == 'q':
        continue
    print("{}".format(chr(letter)), end="")
