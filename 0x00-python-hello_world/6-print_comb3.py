#!/usr/bin/python3
for x in range(0, 9):
    for a in range(1, 10):
     if x >= a:
         continue
     elif x == 8 and a == 9:
       print("{}{}".format(x,a))
     else:
      print("{}{}".format(x,a), end=", ")
