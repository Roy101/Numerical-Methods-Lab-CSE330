import numpy as np
import matplotlib.pyplot as plt
from itertools import combinations
from numpy.polynomial import Polynomial


def l(k, x):
    n = len(x)
    assert (k < len(x))

    x_k = x[k]
    x_copy = np.delete(x, k)

    denominator = np.prod(x_copy - x_k)

    coeff = []

    for i in range(n):
        coeff.append(sum([np.prod(x) for x in combinations(x_copy, i)]) * (-1) ** (i) / denominator)

    coeff.reverse()

    return Polynomial(coeff)