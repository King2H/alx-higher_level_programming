#!/usr/bin/python3
# Range for Lowercase alphabet in reverse
for i in range(122, 96, -1):
    if i % 2 == 0:
        print("{:c}".format(i), end="")
    else:
        print("{:c}".format(i - 32), end="")
