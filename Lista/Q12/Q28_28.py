# -*- coding: utf-8 -*-
from Euler import integrate
import matplotlib.pyplot as plt
from RK4 import integrateRK4
import math
import numpy as np

'''
R = 1,5
L = 1
i(0) = 0,5

'''

# podemos escolher usar o F ou F1 abaixo nos métodos

#resolvendo a EDO 1 ordem:
def F(x, y):
	return 0.5*math.exp(-1.5*x) - y

def F1(x,y):
	F = np.zeros(2)
	F[0] = -1.5*y[0]
	return F

#utilizando o metodo de euler
Xplot, Yplot = integrate(F, 0, 0.5, 1, 10)
ax1 = plt.plot(Xplot,Yplot, '-')



#utilizando o metodo de RK4
X2plot, Y2plot = integrateRK4(F,0,0.5,0.1,10)
ax2 = plt.plot(X2plot,Y2plot, '-o')

plt.title("Euler e RK4 para circuto RL")
plt.legend(["Euler -> h = 1", "RK4 -> h = 0.1"])
#plt.axis([0, 10, -5, 5])
plt.xlabel("time")
plt.ylabel("i(t)")
plt.show()



