def input_info():
    """
    Input info aboat triangle
    """
    a, b, c, tch = map(float, input("Input info: ").split())
    # search for similar sides of triangle
    if a == b:
        return a, c, tch
    if a == c:
        return a, b, tch
    if c == b:
        return b, a, tch


def res(a, c, tch):
    """
    Search for side of square
    """
    return c * (a * a - c * c / 4) ** 0.5 / ((a * a - c * c / 4) ** 0.5 + c)


def write_file(res):
    """
    Write result to file
    """
    with open("result.txt", "w") as file:
        file.write(str(res))


def main_program():
    a, b, tch = input_info()
    result = res(a, b, tch)
    print(result)
    write_file(result)


main_program()
