#!/usr/bin/python3
def print_last_digit(number):
    number = abs(int(number))
    last_digit = number % 10
    print((last_digit), end="")
    return last_digit
