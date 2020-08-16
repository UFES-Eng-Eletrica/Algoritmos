import numpy as np

#função para integrar uma função F, com Xi e Yi sendo valores iniciais
#h é o valor do passo e X_Stop é o limite direito da integração
#função retorna dois numpy arrays contendo os pontos (x,y) da curva

def integrate(F, Xi, Yi, h, X_stop):
	X = []
	Y = []

	X.append(Xi)
	Y.append(Yi)

	while Xi < X_stop:
		h = min(h, X_stop - Xi)
		Yi = Yi + h*F(Xi, Yi)
		Xi = Xi + h
		X.append(Xi)
		Y.append(Yi)
	return np.array(X), np.array(Y)

'''
exemplo de uma função definida que pode ser modificada pelo usuário

def F(x, y):
	return x**2 - 4*y
'''


'''

Xplot, Yplot = integrate(F, 0, 1, 0.01, 0.03)

print(Xplot, Yplot)
''


