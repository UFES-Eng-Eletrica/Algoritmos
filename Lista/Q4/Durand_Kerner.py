import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def f(x):
    #polinomio a ser retornado
    return x**7 + 5*x**6 + 10*x**5 + x**4 + x**3 + x**2 + 4*x + 1

def durand_kerner(p, q, r, s, t, u, v, func):
    #procedimento durand-kerner
    pp = p - func(p) / ((p-q)*(p-r)*(p-s)*(p-t)*(p-u)*(p-v))
    qq = q - func(q) / ((q-p)*(q-r)*(q-s)*(q-t)*(q-u)*(q-v))
    rr = r - func(r) / ((r-p)*(r-q)*(r-s)*(r-t)*(r-u)*(r-v))
    ss = s - func(s) / ((s-p)*(s-q)*(s-r)*(s-t)*(s-u)*(s-v))
    tt = t - func(t) / ((t-p)*(t-q)*(t-r)*(t-s)*(t-u)*(t-v))
    uu = u - func(u) / ((u-p)*(u-q)*(u-r)*(u-s)*(u-t)*(u-v))
    vv = v - func(v) / ((v-p)*(v-q)*(v-r)*(v-s)*(v-t)*(v-u))
    return pp, qq, rr, ss, tt, uu, vv

#raizes chutes iniciais
p, q, r, s, t, u, v = 1 + 0*1j, 0.4 + 0.9j, -0.65 + 0.72j, -0.85 + 0.22j, -1 + 0.92j, 0.65 + 0.32j, -1.65 + 0.52j 

valores = [(p, q, r, s, t, u, v)]  
for _ in range(23):
    p, q, r, s, t, u, v = durand_kerner(p, q, r, s, t, u, v, f)
    valores.append((p, q, r, s, t, u, v))
    
print(pd.DataFrame(valores, columns=['p', 'q', 'r', 's', 't', 'u', 'v']))

