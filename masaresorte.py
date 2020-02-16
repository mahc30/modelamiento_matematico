import numpy as np 
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import math

def masaresorte(X, t):
    #Masas
    m1 = 20
    m2 = 10
    beta = 0.4 #Coeficiente de Friccioń
    #Constantes de Elasticidad
    k1 = 100
    k2 = 100
    #Movimiento cosenoidal
    cos = math.cos(t)
    x1,dx1, x2, dx2 = X

    dv1dt = (-k1 * cos - k2*x1 + k2*x2 + beta*dx1)/m1
    dv2dt = (-k2*x2 + k2*x1 + beta*dx2)/m2

    return [dx1, dv1dt, dx2, dv2dt]

t = np.linspace(0,30,1000)
y = odeint(masaresorte, [3,0,5,0], t)


plt.plot(t,y[:,1])
plt.plot(t,y[:,3])
plt.axis('equal')
plt.show()