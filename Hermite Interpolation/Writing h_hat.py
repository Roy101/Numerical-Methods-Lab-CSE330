def h_hat(k, x):
    l_k = l(k, x)
    l_k_sqr = l(k, x) * l(k, x)
    coeff = np.array([(-1) * x[k], 1])
    p = Polynomial(coeff)

    return p * l_k_sqr