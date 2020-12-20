from Euler import integrate
import matplotlib.pyplot as plt
from RK4 import integrateRK4
import math

#para o valor de R = 0,025 temos que a funcao de q(t) fica:
def F(x, y):
	return 2*math.sin(1.87*x) + 0.1*math.cos(1.87*x) - y
	

#utilizando o metodo de euler
Xplot, Yplot = integrate(F, 0, 0, 1, 10)
ax1 = plt.plot(Xplot,Yplot, '-')



#utilizando o metodo de RK4
X2plot, Y2plot = integrateRK4(F,0,0,0.1,10)
ax2 = plt.plot(X2plot,Y2plot, '-o')

plt.title("Euler e RK4 para R = 0,025 ohms")
plt.legend(["Euler -> h = 1", "RK4 -> h = 0,1"])
plt.axis([0, 10, -5, 5])
plt.xlabel("time")
plt.ylabel("q(t)")
plt.show()



