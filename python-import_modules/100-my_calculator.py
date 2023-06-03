#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    argc = len(sys.argv) - 1
    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a, operator, b = int(sys.argv[1]), sys.argv[2], int(sys.argv[3])

    available_ops = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div
    }
    if operator not in list(available_ops.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    result = available_ops[sys.argv[2]](a, b)
    print(f"{a} {operator} {b} = {result}")
