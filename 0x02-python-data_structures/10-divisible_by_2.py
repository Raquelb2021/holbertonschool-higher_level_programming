#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_ = []
    for num in my_list:
        if (num % 2) == 0:
            list_.append(True)
        else:
            list_.append(False)
    return(list_)
