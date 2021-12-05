import numpy as np
import matplotlib.pyplot as plt


class Newtons_Divided_Differences:
    def __init__(self, differences):
        self.differences = differences

    def __call__(self, x):
        """
        this function is for calculating y from given x using all the difference coefficients
        x can be a single value or a numpy
        the formula being used:
        f(x) = f [x0] + (x-x0) f[x0,x1] + (x-x0) (x-x1) f[x0,x1,x2] + . . . + (x-x0) (x-x1) . . . (x-xk-1) f[x0, x1, . . ., xk]

        work on this after implementing 'calc_div_diff'. Then you should have
        f[x0], f[x0,x1]. . . . . ., f[x0, x1, . . ., xk] stored in self.differences

        'res' variable must return all the results (corresponding y for x)
        """

        # res = np.zeros(len(x)) #Initialization to avoid runtime error. You can change this line if you wish

        # place your code here!!!!!!!!!!!!!!!!!!!!!!!

        n = len(data_x) - 1  # degree
        res = self.differences[n]
        for k in range(1, n + 1):
            res = self.differences[n - k] + (x - data_x[n - k]) * res  # differnce f[x]

        return res
