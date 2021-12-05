def hermit(x, y, y_prime):
    assert (len(x) == len(y))
    assert (len(y) == len(y_prime))

    f = Polynomial([0.0])
    for i in range(len(x)):
        f += y[i] * h(i, x) + y_prime[i] * h_hat(i, x)
    return f