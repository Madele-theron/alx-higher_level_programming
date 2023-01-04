# !/usr/bin/python3

if __name__ == "__main__":
    """prints the number of and the list of its arguments."""
    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b> ")
        exit(1)

    if sys.argv[2] == "+":
        add(sys.argv[1], sys.argv[3])
    elif sys.argv[2] == "-":
        sub(sys.argv[1], sys.argv[3])
    elif sys.argv[2] == "/":
        div(sys.argv[1], sys.argv[3])
    elif sys.argv[2] == "*":
        mul(sys.argv[1], sys.argv[3])
    else:
        print("Unknown operator. Available operators: +, -, * and / ")
        exit(1)
