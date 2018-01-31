# This function takes a string of characters and returns a list of two numbers
# in which the first number is the number of capital letters per line
# and the second is the number of lowercase letters per line.


def rec(string):
    """

    :param string: str, wAt’rh7rJjoa
    :return: list, [2, 8]

    :param string: int, 57679
    :return: list, [0, 0]

    """
    if len(string) == 0:
        return [0, 0]
    res = rec(string[1:])
    if 96 < ord(string[0]) < 123:
        return [res[0], res[1] + 1]
    elif 64 < ord(string[0]) < 91:
        return [res[0] + 1, res[1]]
    return res


print(rec(input()))
