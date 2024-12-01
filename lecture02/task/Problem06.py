def sol():
    # swap variables
    x = 5
    y = 10
    print("x = ", x, " y = ", y, sep="")
    x, y = y, x
    print("x = ", x," y = ", y, sep="")


if __name__ == '__main__':
    sol()

