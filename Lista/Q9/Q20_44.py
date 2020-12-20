# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

T = np.array([0, 5, 10, 20, 30, 40])
mi = np.array([1.787, 1.519, 1.307, 1.002, 0.7975, 0.6529])

#calculo de interpolacao retirado de Kiusalaas
def coeffts(xData,yData):
    m = len(xData) 
    a = yData.copy()
    for k in range(1,m):
        a[k:m] = (a[k:m] - a[k-1])/(xData[k:m] - xData[k-1])
    return a

def evalPoly(a,xData,x):
    n = len(xData) - 1 
    p = a[n]
    for k in range(1,n+1):
        p = a[n-k] + (x -xData[n-k])*p
    return p
    
coeficientes = coeffts(T,mi)

#viscosidade para T = 7,5 graus
y_7_5 = evalPoly(coeficientes, T, 7.5)
print("temperatura de 7,5 celsius tem uma viscosidade de:\n")
print(y_7_5)

poly_reg = np.poly1d(np.polyfit(T, mi, 2))
poly_x = np.linspace(0, 40, 100)

y_interpolacao = []
for i in range(0,40):
    
    y = evalPoly(coeficientes, T, i)
    y_interpolacao.append(y)

ax1 = plt.plot(T, mi, 'o')
ax2 = plt.plot(y_interpolacao, '--')
ax3 = plt.plot(poly_x, poly_reg(poly_x), '-')

plt.legend(['dados','interpolacao','regressao'])
plt.xlabel('Temperatura')
plt.ylabel("viscosidade")
plt.axis([-10,50,0.5,2])

plt.show()
print(y_interpolacao)

