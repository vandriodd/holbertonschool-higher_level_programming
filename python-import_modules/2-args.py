#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num_elements = len(sys.argv) - 1
    msg = "arguments"
    if num_elements == 1:
        print("{} {}:".format(num_elements, msg[:8]))
    else:
        print("{} {}{}".format(num_elements, msg,
              "." if num_elements == 0 else ":"))
    for ac, name in enumerate(sys.argv[1:], start=1):
        print(f"{ac}: {name}")
