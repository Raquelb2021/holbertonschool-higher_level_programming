#!/usr/bin/python3
import sys
if __name__ == "__main__":
    args = sys.argv[1:]
    numbers = [int(arg) for arg in args]
    total = sum(numbers)
    print(total, end="\n")
