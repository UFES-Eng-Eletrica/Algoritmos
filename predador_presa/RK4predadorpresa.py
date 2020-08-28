import numpy as np
import matplotlib.pyplot as plt


def presa(x,y, a, b, c, d):  #retorna a eq diferencial da variação x(presa) em t (dx/dt)
	return a*x - b*x*y

def predador(x,y, a, b, c, d):  #retorna a eq diferencial da variação y(predador) em t (dy/dt)
	return -c*y + d*x*y

def RK4(F, xi, yi, h, a, b, c, d):  #retorna uma média ponderada dos valores de K de runge-kutta calculados
	K1 = F(xi,yi, a, b, c, d)
	K2 = F(xi + h/2, yi + (K1*h)/2, a, b, c, d)
	K3 = F(xi + h/2, yi + (K2*h)/2, a, b, c, d)
	K4 = F(xi + h, yi + K3*h, a, b, c, d)

	return (K1 + 2*K2 + 2*K3 + K4)*h/6

def integrationPredadorPresa(Predador, Presa, t, xi, yi, h, tStop, a, b, c, d):  #main function
	X = []
	Y = []
	T = []

	T.append(t)
	X.append(xi)
	Y.append(yi)

	while t < tStop:
		h = min(h, tStop - t)
		xi = xi + RK4(Presa, xi, yi, h, a, b, c, d)
		yi = yi + RK4(Predador, xi, yi, h, a, b, c, d)
		t = t + h
		T.append(t)
		X.append(xi)
		Y.append(yi)

	return np.array(T), np.array(X), np.array(Y)

