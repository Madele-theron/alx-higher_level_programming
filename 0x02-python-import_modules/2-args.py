#!/usr/bin/python3

if __name__ == "__main__":
    """prints the number of and the list of its arguments."""
    import sys

    args = len(sys.argv) - 1
    if args == 0:
        print("0 arguments.")
    elif args == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(args))
    for item in range(args):
        print("{}: {}".format(item + 1, sys.argv[item + 1]))
