# This function takes two positive integers n and m and returns the largest
# common divisor for these numbers based on the dependence
# F (n, m) = F (n-m, m)


def gcd(a, b):
    """

    :param a: int, 126
    :param b: int, 4
    :return: int, 2

    :param a: str, a
    :return: str, Enter only positive integers numbers, please!

    """
    if a < 0 or b < 0:
        return "Enter only positive numbers, please!"
    return gcd(b, a % b) if b else a


try:
    print(gcd(int(input()), int(input())))
except ValueError:
    print("Enter only positive integers numbers, please!")
