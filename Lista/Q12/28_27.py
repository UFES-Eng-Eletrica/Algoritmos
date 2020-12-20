# -*- coding: utf-8 -*-
from Euler import integrate
import matplotlib.pyplot as plt
from RK4 import integrateRK4
import math

#de t = 0 a 0,5
#q=0,1 e i=−3,281515 em t = 0.

#para o valor de R = 50 temos que a funcao de q(t) fica:
def F(x, y):
	return -0.01*math.cos(1.87*x) + 0.034*math.exp(-0.08*x) + 0.0655*math.exp(-50*x)  - y

#utilizando o metodo de euler
Xplot, Yplot = integrate(F, 0, 0.1, 1, 10)
ax1 = plt.plot(Xplot,Yplot, '-')



#utilizando o metodo de RK4
X2plot, Y2plot = integrateRK4(F,0,0.1,0.1,10)
ax2 = plt.plot(X2plot,Y2plot, '-o')

plt.title("Euler e RK4 para R = 50 ohms")
plt.legend(["Euler -> h = 0.05", "RK4 -> h = 0.005"])
#plt.axis([0, 10, -5, 5])
plt.xlabel("time")
plt.ylabel("q(t)")
plt.show()



