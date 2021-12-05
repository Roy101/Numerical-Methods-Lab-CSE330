def h(k, x):
    # initialize with none
    l_k = l(k,x)
    l_k_sqr = l(k,x)*l(k,x)
    l_k_prime = l(k,x).deriv(1)
    coeff = np.array([1+2*x[k]*l_k_prime(x[k]),(-2)*l_k_prime(x[k])])
    p = Polynomial(coeff)

    # place your code here!!!!!!!!!!!!!!!!!!!!!!!
    return p * l_k_sqr