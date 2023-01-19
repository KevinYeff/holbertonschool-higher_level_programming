#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    total = 0
    for args in range(len(sys.argv) - 1):
        total = total + int(sys.argv[args + 1])
    print("{}".format(total))
