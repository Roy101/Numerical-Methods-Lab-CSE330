class LagrangePolynomial:
    def __init__(self, data_x, data_y):
        '''
        First we need to check whether the input vectors (numpy arrays) are equal
        or not.
        assert (condition), "msg"
        this command checks if the condition is true or false. If true, the code
        runs normally. But if false, then the code returns an error message "msg"
        and stops execution
        '''
        assert len(data_x) == len(data_y), "length of data_x and data_y must be equal"

        '''
        Since lagrange polynomials do not use coefficeints a_i, rather the nodes 
        (x_i, y_i), we just need to store these inside the object
        '''

        self.x = data_x
        self.y = data_y

        self.degree = len(data_x) - 1
        # we assume that the inputs are numpy array, so we can perform
        # element wise operations

    def __repr__(self):
        # method for string representation
        # you don't need to worry about the following code if you don't understand
        strL = f"LagrangePolynomial of order {self.degree}\n"
        strL += "p(x) = "
        for i in range(len(self.y)):
            if self.y[i] == 0:
                continue
            elif self.y[i] >= 0:
                strL += f"+ {self.y[i]}*l_{i}(x) "
            else:
                strL += f"- {-self.y[i]}*l_{i}(x) "

        return strL

    def __call__(self, x):
        """
        The method to make the object callable (see the code of the matrix method).
        'x' is a set of given points (a numpy array). You have to use self.x and
        self.y to find the interpolated output of the polynomial for all elements
        of 'x'.

        Implement as you wish but your 'total' numpy array where the i'th element
        y[i] represents the interpolated value of p(x[i]).
        """
        # initialize with zero
        y_interp = np.zeros(len(x))
        # place your code here!!!!!!!!!!!!!!!!!!!!!!!!!

        for aa in range(len(x)):
            for a, b in zip(self.x, self.y):
                o = (x[aa] - self.x[self.x != a])
                p = (a - self.x[self.x != a])
                Y = b * np.prod(o / p)
                y_interp[aa] += Y
            Y = 0

        return y_interp
