# This function takes two positive numbers n and m and returns the sum
# of the range 1 ^ m + 2 ^ m + ... + n ^ m.


def rec(n, m):
    """

    :param n: int, 5
    :param m: int, 6
    :return: int, 20515

    """
    if n == 0:
        return 0
    # check the input
    elif n < 0 or m < 0:
        return "Enter only positive numbers, please!"
    return n**m + rec(n - 1, m)


try:
    print('The sum of the range is:',
          rec(int(input('Enter a positive integer:',)),
              int(input('Enter another positive integer:',))))
except:
    print("Enter only positive integers numbers, please!")
