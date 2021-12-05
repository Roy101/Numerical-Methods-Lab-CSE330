import math
import itertools
import matplotlib.pyplot as plt


class Float8():

    def __init__(self, bitstring):
        '''Constructor
        takes a 8-bit string of 0's and 1's as input and stores the sub-strings
        accordingly.
        Usage: Float8('00011110')
        '''

        # Make sure the input consists of exactly 8-bits.
        assert (len(bitstring) == 8)

        # Assign the sign bit

        self.sign = bitstring[0]

        # Assign the exponent part

        self.exponent = bitstring[1:4]

        # Assign the mantissa

        self.mantissa = bitstring[4:]

        self.val = self.calculate_value()

    def __str__(self):
        return f'Sign bit value: {self.sign}\n' + \
               f'Exponent value: {self.exponent}\n' + \
               f'Mantissa value: {self.mantissa}\n' + \
               f'Floating value: {self.val}\n'

    def tobitstring(self):
        return self.sign + self.exponent + self.mantissa

    def toformattedstring(self):
        return ' '.join([self.sign, self.exponent, self.mantissa])

    def calculate_value(self):
        '''Calculate the value of the number from bits'''

        # Initialize with zero
        val = 0.0

        # Handle the case of inf and nan
        if self.exponent == '111':
            count = 0
            for exp, bit in enumerate(self.mantissa, 1):
                if (bit == '1'):
                    count += 1
                if count == 0:
                    val = math.inf
                else:
                    val = math.nan


        # Handle the case of subnormals
        elif self.exponent == '000':
            val = 0.0

            for exp, bit in enumerate(self.mantissa, 1):
                if (bit == '1'):
                    val += pow(2, -exp)
            val *= pow(2, -2)


        # Handle the case of normals
        else:
            val = 1.0
            for exp, bit in enumerate(self.mantissa, 1):
                if (bit == '1'):
                    val += pow(2, -exp)

            # use a loop like this to calculate exponent value
            exp = 0
            for e, bit in enumerate(reversed(self.exponent)):
                if (bit == '1'):
                    exp += pow(2, e)

            # calculate final value
            val *= pow(2, (exp - 3))

        # Handle the sign bit
        if self.sign == '1':
            val = -val
        else:
            val = val

        return val

