import numpy as np
from Integration_Euler import integrate
import matplotlib.pyplot as plt

def F(x,y):
	F = np.zeros(2)
	F[0] = y[1]
	F[1] = -0.1*y[1] - x
	return F

x = 0.0
x_stop = 2.0
y = np.array([0.0, 1.0])
h = 0.05

X,Y = integrate(F, x, y, h, x_stop)

print(Y)



yExact = 100*X - 5*X**2 + 990*(np.exp(-0.1*X) - 1)
plt.plot(X,Y[:,0],'o',X,yExact,'-')
plt.grid(True)
plt.xlabel('x'); plt.ylabel('y')
plt.legend(('Numerical','Exact'),loc=0)
plt.show()
