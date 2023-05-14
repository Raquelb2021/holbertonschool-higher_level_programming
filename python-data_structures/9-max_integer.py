#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return (0, None)
    myMax = my_list[0]
    for num in my_list:
        if myMax < num:
            myMax = num
            return myMax
