# This function takes a string of characters and returns a list of two numbers
# in which the first number is the number of capital letters per line
# and the second is the number of lowercase letters per line.
import sys


def recursion(string):
    """
    :param string: str, wAt’rh7rJjoa
    :return: list, [2, 8]
    :param string: int, 57679
    :return: list, [0, 0]
    """
    if len(string) == 0:
        return [0, 0]
    res = recursion(string[1:])
    # check by asci code
    if 96 < ord(string[0]) < 123:
        return [res[0], res[1] + 1]
    elif 64 < ord(string[0]) < 91:
        return [res[0] + 1, res[1]]
    return res

sys.setrecursionlimit(1000000)
capital, small = recursion(input("Enter some text: "))
print("The number of capital letters is %s; \
      The number of small letters is %s" % (capital, small))
