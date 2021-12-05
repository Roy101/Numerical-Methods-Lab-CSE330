class Float16():

    def __init__(self, bitstring):
        '''Constructor
        takes a 16-bit string of 0's and 1's as input and stores the sub-strings
        accordingly.
        Usage: Float16('0001111000011110')
        '''

        # Make sure the input consists of exactly 16-bits.
        assert (len(bitstring) == 16)

        # Assign the sign bit

        self.sign = bitstring[0]

        # Assign the exponent part

        self.exponent = bitstring[1:5]

        # Assign the mantissa

        self.mantissa = bitstring[5:]

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

        if self.exponent == '1111':
            on1 = 0
            for exp, bit in enumerate(self.mantissa, 1):
                if (bit == '1'):
                    on1 += 1
                if on1 == 0:
                    val = math.inf
                else:
                    val = math.nan

        #    Write you code here

        elif self.exponent == '0000':
            val = 0.0

            for exp, bit in enumerate(self.mantissa, 1):
                if (bit == '1'):
                    val += pow(2, -exp)
            val *= pow(2, -6)

        else:
            val = 1.0

            # use a loop like this to calculate mantissa value

            for exp, bit in enumerate(self.mantissa, 1):
                if (bit == '1'):
                    val += pow(2, -exp)

            # use a loop like this to calculate exponent value

            exp = 0
            for e, bit in enumerate(reversed(self.exponent)):
                if (bit == '1'):
                    exp += pow(2, e)

            # calculate final value
            val *= pow(2, (exp - 7))

        # Handle the sign bit
        if self.sign == '1':
            val = -val

        return val