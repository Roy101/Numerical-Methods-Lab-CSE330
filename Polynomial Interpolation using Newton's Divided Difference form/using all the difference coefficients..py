# basic rule for calculating the difference, implanted in the lambda function.
# You may use it if you wish
difference = lambda y2, y1, x2, x1: (y2 - y1) / (x2 - x1)


def calc_div_diff(x, y):
    assert (len(x) == len(y))
    # write this function to calculate all the divided differences in the list 'b'
    lng = len(x)

    x = np.copy(x)
    b = np.copy(y)

    for k in range(1, lng):
        b[k:lng] = (b[k:lng] - b[k - 1]) / (x[k:lng] - x[k - 1])

    return b

    # place your code here!!!!!!!!!!!!!!!!!!!!!!!!!

