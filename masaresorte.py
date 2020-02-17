import numpy as np 
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import math

def masaresorte(X, t):
    #Masas
    m1 = 20
    m2 = 20
    beta = 1 #Coeficiente de Friccioń
    #Constantes de Elasticidad
    k1 = 20
    k2 = 20
    #Movimiento cosenoidal (Multiplico por 3 para hacerlo más 'amplio')
    scale = 3
    cos = scale * math.cos(t)

    #Después de unas oscilaciones, Se deja de mover el resorte 1
    
    if(t >= 120):
        cos = 0

    x1,dx1, dx2 = X

    #Ecuaciones
    #Ecuación para la masa 1
    dv1dt = (-k1 * (x1 + cos) + k2*(dx2 - dx1) + beta*dx1)/m1
    #Ecuación para la masa 2
    dv2dt = (k2*(dx1 - dx2) + beta*dx2)/m2

    return [dx1, dv1dt,dv2dt]

#Simulo desde 90 para que el valor inicial de coseno sea 0
t = np.linspace(90,180,10000)

#Asumiendo que los resortes tienen su elongación natural acorde a la distancia entre un carrito y el otro
#El primer argumento es una elongación inicial del primer resorte, el segundo una velocidad incial para la primera masa, el tercero una velocidad inicial para la segunda masa
y = odeint(masaresorte, [10, 0, 0], t)

#y[1,3] -> Gráfica de la aceleración en función del tiempo
plt.plot(t,y[:,0])
plt.plot(t,y[:,2])
#y[0,2] -> Grafica de la velocidad en función del tiempo
'''
plt.plot(t,y[:,0])
plt.plot(t,y[:,2])
'''

plt.xlabel('tiempo')
plt.ylabel('aceleración')
plt.axis('equal')
plt.legend(['Carro 1','Carro 2'])
plt.show()