#!/usr/bin/python3

if __name__ == "__main__":
    """prints the result of the addition of all arguments"""
    import sys

    args = len(sys.argv) - 1
    total = 0
    if args == 1:
        print("0")
    elif args > 1:
        # print("{} arguments:".format(args))
        for item in range(args):
            total = total + int(sys.argv[item + 1])

    print(total)
