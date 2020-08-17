
'''
Nesse código, uma funcao que calcula o K1 do metodo
RungeKutta de 2 ordem para que o próximo y seja calculado:

yi+1 = y + K1
No final tem um comentário com um exemplo de aplicação 
com a equação =>

y' = sen(y)
y(0) = 1

Exemplo 7.3 livro Kiusalaas Numerical python

'''


import numpy as np
import math

def integrateRK2(F, xi, yi, h, xStop):

	def RK2(F, xi, yi, h):
		K0 = h*F(xi, yi)
		K1 = h*F(xi + h/2, yi + (1/2)*K0)
		return K1

	X = []
	Y = []
	K = []
	X.append(xi)
	Y.append(yi)

	while xi < xStop:
		h = min(h, xStop - xi)
		K.append(RK2(F, xi, yi, h))
		yi = yi + RK2(F, xi, yi, h)
		xi = xi + h
		X.append(xi)
		Y.append(yi)
	return np.array(X), np.array(Y), np.array(K)

'''
h = 0.1
x = 0
xStop = 0.5
y = 1

def F(x, y):
	return math.sin(y)

X,Y,K = integrateRK2(F, x, y, h, xStop)

print(X, Y, K)
'''
