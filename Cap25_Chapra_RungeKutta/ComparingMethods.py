from RungeKutta4order import integrateRK4
from RungeKutta2order import integrateRK2
from Integration_Euler import integrate
import numpy as np
import matplotlib.pyplot as plt

'''
comparando metodos e os resultados a partir da integração de uma eq =>

forma analítica:
y = 100x − 5x2 + 990(e−0.1x − 1)

y'' = -0.1y' - x

'''

def F(x,y):
	F = np.zeros(2)
	F[0] = y[1]
	F[1] = -0.1*y[1] - x
	return F

x = 0
xStop = 2
h = 0.05
y = np.array([0, 1])

X1,Y1 = integrate(F, x, y, h, xStop)
X2,Y2,K = integrateRK2(F, x, y, h, xStop)
X3,Y3 = integrateRK4(F, x, y, h, xStop)

yExact = 100*X1 - 5*X1**2 + 990*(np.exp(-0.1*X1) - 1)
plt.plot(X1,Y1[:,0],'o',X1,yExact,'-',X2,Y2[:,0], 's-', X3,Y3[:,0], '^-')
plt.grid(True)
plt.xlabel('x'); plt.ylabel('y')
plt.legend(('Euler','Exact', 'RK2', 'RK4'),loc=0)
plt.show()

