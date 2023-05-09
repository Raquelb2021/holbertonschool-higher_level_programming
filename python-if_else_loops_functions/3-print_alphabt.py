#!/usr/bin/python3
for ch in range(ord('a'), ord('z')+1):
    if ch not in [ord ('q'), ord ('e')]:
        print("{:c}".format(ch), end='')
