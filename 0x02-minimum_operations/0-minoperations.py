#!/usr/bin/python3
""" module containing a func to determine min ops"""


def minOperations(n: int) -> int:
    """func computing the min ops"""

    if type(n) is not int:
        return 0
    import math
    written = 1
    steps = 1
    clipboard = 1
    if math.isinf(n):
        return 0
    if n <= 0:
        return 0

    steps += 1
    written += clipboard
    rem = n - written
    to_copy = written

    while rem > 0:
        if rem % to_copy == 0:
            if (rem - to_copy) % (to_copy + clipboard) == 0:
                # paste
                steps += 1
                written += clipboard
                rem = n - written
            else:
                # copy
                steps += 1
                clipboard = 0
                clipboard = to_copy = written
                # paste
                steps += 1
                written += clipboard
                rem = n - written
        else:
            # paste
            steps += 1
            written += clipboard
            rem = n - written

    if rem % clipboard != 0:
        return 0
    if rem != 0:
        return 0
    return steps
