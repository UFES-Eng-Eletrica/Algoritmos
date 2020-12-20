import numpy as np

def integrateRK4(F, xi, yi, h, xStop):

	def RK4(F, x, y, h):
		K0 = h*F(x,y)
		K1 = h*F(x + h/2.0, y + K0/2.0)
		K2 = h*F(x + h/2.0, y + K1/2.0)
		K3 = h*F(x + h, y + K2)
		return (K0 + 2.0*K1 + 2.0*K2 + K3)/6.0

	X = []
	Y = []
	X.append(xi)
	Y.append(yi)

	while xi < xStop:
		h = min(h, xStop - xi)
		yi = yi + RK4(F, xi, yi, h)
		xi = xi + h
		X.append(xi)
		Y.append(yi)
	return np.array(X), np.array(Y)