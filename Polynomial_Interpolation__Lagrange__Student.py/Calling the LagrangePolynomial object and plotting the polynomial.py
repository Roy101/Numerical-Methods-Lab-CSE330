data_x = np.array([-3.,-2.,-1.,0.,1.,3.,4.])
data_y = np.array([-60.,-80.,6.,1.,45.,30.,16.])

p = LagrangePolynomial(data_x, data_y)
print(p)
#generating 100 points from -3 to 4 in order to create a smooth line
x = np.linspace(-3, 4, 100)
print(x)
y_interp = p(x)

# plot to see if your implementation is correct
#google the functions to understand what each parameters mean, if not apparent
plt.plot(x, y_interp)
plt.plot(data_x, data_y, 'ro')
plt.legend(['interpolated', 'node points'], loc = 'upper left')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Lagrange Polynomial')

plt.show()