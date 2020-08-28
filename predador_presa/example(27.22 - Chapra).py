'''
Exemplo de aplicação das fórmulas de predador-presa com o método de Runge-Kutta de 4 ordem
importando os métodos do módulo que está nessa mesma pasta.

Exemplo aplicado: 

problema 27.22 do livro Chapra Canale Métodos Numéricos para engenharia

'''

from RK4predadorpresa import * 

x = 2
y = 1
t = 0
tStop = 30
h = 0.1
a = 1.5
b = 0.7
c = 0.9
d = 0.4

t, x, y = integrationPredadorPresa(predador, presa, t, x, y, h, tStop, a, b, c, d)

plt.plot(t, x, '-', t, y, '--')
plt.grid(True)
plt.xlabel('tempo'); plt.ylabel('presador/presa');
plt.legend(('presa', 'predador'), loc=0)
plt.show()

