#!/usr/bin/python3
if __name__ == "__main__":
    import sys
if len(sys.argv) == 1:
    print("0 arguments.")
else:
    print("{:d} argument".format(len(sys.argv) - 1), end="")
if len(sys.argv) > 2:
    print(":")
for a in range(1, len(sys.argv)):
    print("{:d}: {:s}".format(a, sys.argv[a]))
