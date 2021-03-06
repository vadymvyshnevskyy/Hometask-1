# The function takes the integer positive number n and returns the square of
# that number based on the dependence n2 = (n-1) 2 + 2 (n-1) +1.
import sys


def rec(n):
    """

    :param n: int, -98
    :return: str, Enter only positive numbers, please!

    :param n: int, 45
    :return: int, 2025
    """

    if n == 0:
        return 0
    else:
        return rec(n - 1) + 2 * (n - 1) + 1


try:
    sys.setrecursionlimit(1000000)
    n = int(input("Please enter positive number: "))
    if n < 0:
        print("Enter only positive numbers, please!")
    else:
        print("The square of {} is {}".format(n, rec(n)))
except:
    print("Wrong input")
