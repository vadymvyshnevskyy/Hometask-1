# The function takes the integer positive number n and returns the square of
# that number based on the dependence n2 = (n-1) 2 + 2 (n-1) +1.


def rec(n):
    """

    :param n: int, -98
    :return: str, Enter only positive numbers, please!

    :param n: int, 45
    :return: int, 2025
    """

    if n == 0:
        return 0
    elif n < 0:
        return "Enter only positive numbers, please!"
    else:
        return rec(n-1)+2*(n-1)+1


try:
    print(rec(int(input())))
except ValueError:
    print("Enter only positive integers numbers, please!")
