import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial


def dh(f, h, x):
    '''
    Input:
        f: np.polynomial.Polynonimial type data.
        h: floating point data.
        x: np.array type data.
    Output:
        return np.array type data of slope at each point x.
    '''
    # return <write your code here>
    sss = (f(x + h) - f(x - h))
    ss = sss / (2 * h)
    return ss
def dh1(f, h, x):
    '''
    Input:
        f: np.polynomial.Polynonimial type data.
        h: floating point data.
        x: np.array type data.
    Output:
        return np.array type data of slope at each point x.
    '''
    # return <write your code here>
    aa =(4*dh(f , h/2 , x))
    bb =dh(f, h ,x)
    cc=aa-bb


    return cc/ 3


def error(f, hs, x_i):
    '''
    Input:
        f  : np.polynomial.Polynonimial type data.
        hs : np.array type data. list of h.
        x_i: floating point data. single value of x.
    Output:
        return two np.array type data of errors by two methods..
    '''
    d_eff = []
    d2_eff = []

    f_pp = f.deriv(1)
    Y_aa = f_pp(x_i)

    for h in hs:
        DE_hi = dh(f, h, x_i) - Y_aa
        d_eff.append(DE_hi)

        DE_hi1 = dh1(f, h, x_i) - Y_aa
        d2_eff.append(DE_hi1)

        # for each values of hs calculate the error using both methods
        # and append those values into d_eff and d2_eff list.

        # write your code here

        pass  # delete this line

    print(pd.DataFrame({"h": hs, "Diff": d_eff, "Diff2": d2_eff}))

    return d_eff, d2_eff

#function to draw the actual function
def draw_graph(f, ax, domain=[-10, 10], label=None):
    data = f.linspace(domain=domain)
    ax.plot(data[0], data[1], label='Function')

    fig, ax = plt.subplots()
    ax.axhline(y=0, color='k')

    p = Polynomial([2.0, 1.0, -6.0, -2.0, 2.5, 1.0])
    p_pp = p.deriv(1)
    draw_graph(p, ax, [-2.4, 1.5], 'Function')
    draw_graph(p_pp, ax, [-2.4, 1.5], 'Derivative')

    ax.legend()

#Draw the polynomial and it's aa derivative function
    fig, ax = plt.subplots()
    ax.axhline(y=0, color='k')

    p = Polynomial([2.0, 1.0, -6.0, -2.0, 2.5, 1.0])
    p_pp = p.deriv(1)
    draw_graph(p, ax, [-2.4, 1.5], 'Function')
    draw_graph(p_pp, ax, [-2.4, 1.5], 'Derivative')

    ax.legend()

#Draw the actual derivative and richardson derivative using h=1 and h=0.1 as step size.
fig, ax = plt.subplots()
ax.axhline(y=0, color='k')

draw_graph(p_pp, ax, [-2.4, 1.5], 'actual')

h = 1
x = np.linspace(-2.4, 1.5, 50, endpoint=True)
y = dh1(p, h, x)
ax.plot(x, y, label='Richardson; h=1')

h = 0.1
x = np.linspace(-2.4, 1.5, 50, endpoint=True)
y = dh1(p, h, x)
ax.plot(x, y, label='Richardson; h=0.1')

ax.legend()
#Draw error-vs-h cuve
fig, ax = plt.subplots()
ax.axhline(y=0, color='k')
hs = np.array([1., 0.55, 0.3, .17, 0.1, 0.055, 0.03, 0.017, 0.01])
e1, e2 = error(p, hs, 2.0)
ax.plot(hs, e1, label='e1')
ax.plot(hs, e2, label='e2')

ax.legend()
