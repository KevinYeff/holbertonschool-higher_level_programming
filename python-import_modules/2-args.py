#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arglen = len(sys.argv) - 1
    if arglen == 0:
        print("{} arguments.".format(arglen))
    elif arglen == 1:
        print("{} argument:".format(arglen))
    else:
        print("{} arguments:".format(arglen))
    for i in range(1, arglen + 1):
        print("{}: {}".format(i, sys.argv[i]))
