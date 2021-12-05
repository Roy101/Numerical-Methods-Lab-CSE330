data_x = np.array([-3.,-2.,-1.,0.,1.,3.,4.])
data_y = np.array([-60.,-80.,6.,1.,45.,30.,16.])
differences = calc_div_diff(list(data_x), list(data_y))
obj = Newtons_Divided_Differences(list(differences))

#generating 50 points from -3 to 4 in order to create a smooth line
X = np.linspace(-3, 4, 50, endpoint=True)
F = obj(X)
plt.plot(X,F)
plt.plot(data_x, data_y, 'ro')
plt.show()