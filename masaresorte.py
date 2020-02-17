import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.patches import ConnectionPatch

import numpy as np 
from scipy.integrate import odeint
import math

scale = 5

def masaresorte(X, t):
    #Masas
    m1 = 30
    m2 = 50
    beta = 0.4 #Coeficiente de Friccioń
    #Constantes de Elasticidad
    k1 = 100
    k2 = 100
    #Movimiento cosenoidal (Multiplico por una escala para hacerlo más 'amplio')
    cos = scale * math.cos(t)

    #Después de unas oscilaciones, Se deja de mover el resorte 1
    '''
    if(t >= 120):
        cos = 0
'''
    x1,dx1, x2, dx2 = X

    #Ecuaciones
    #Ecuación para la masa 1
    dv1dt = (-k1 * (x1 + cos) + k2*((x2+dx2) - (x1+dx1)) + beta*dx1)/m1
    #Ecuación para la masa 2
    dv2dt = (k2*(dx1 - dx2) + beta*dx2)/m2

    return [dx1, dv1dt, dx2, dv2dt]

#Simulo desde 90 para que el valor inicial de coseno sea 0
t = np.linspace(90,180,10000)

#Asumiendo que los resortes tienen su elongación natural acorde a la distancia entre un carrito y el otro
#El primer argumento es una elongación inicial del primer resorte, el segundo una velocidad incial para la primera masa
#el tercero una elongación inicial para el segundo resorte y el cuarto una velocidad inicial para la segunda masa

Y = odeint(masaresorte, [0, 0, 0, 0], t)

#y[1,3] -> Gráfica de la aceleración en función del tiempo
plt.plot(t,Y[:,1])
plt.plot(t,Y[:,3])

'''
#y[0,2] -> Grafica de la velocidad en función del tiempo
plt.plot(t,Y[:,0])
plt.plot(t,Y[:,2])
'''

plt.xlabel('tiempo')
plt.ylabel('aceleración')
plt.axis('equal')
plt.legend(['Carro 1','Carro 2'])

fig = plt.figure()
ax = plt.axes(xlim=(-30, 120), ylim=(0, 10))
carrito1 = plt.Rectangle((10,3), 3, 2, color="blue",fill=True)
carrito2 = plt.Rectangle((40,3), 3, 2, color="orange",fill=True)
circle = plt.Circle((0,3), 0.5,color='red')
line1 = plt.Arrow(0,4,10,0, width=0.2,color="black", hatch='o')
line2 = plt.Arrow(20,4,10,0, width=0.2,color="black", hatch='o')

def init():
    carrito1.xy = (10, 3)
    carrito2.xy = (30, 3)
    circle.center = (0,4)

    ax.add_patch(carrito1)
    ax.add_patch(carrito2)
    ax.add_patch(circle)
    ax.add_patch(line1)
    ax.add_patch(line2)
    return [carrito1, carrito2, circle, line1, line2]

def animate(i):
    x1, y = carrito1.xy
    x1 = Y[i][0] + 20
    carrito1.xy = (x1, y)
    
    x2, y = carrito2.xy
    x2 = Y[i][2] + 40
    carrito2.xy = (x2, y)

    cx, cy = circle.center
    cx = math.cos((i-45)/120)*scale
    circle.center = (cx,cy)

    line1 = plt.Arrow(cx, 4, x1 - cx, 0, width=0.2, color="green", hatch='o')
    ax.add_patch(line1)
   
    
    line2 = plt.Arrow(x1+3, 4, (x2 - (x1+3)), 0, width=0.2, color="green", hatch='o')
    ax.add_patch(line2)
    
    return [carrito1,carrito2, circle, line1, line2]

anim = animation.FuncAnimation(fig, animate, 
                               init_func=init, 
                               frames=  1500, 
                               interval=1,
                               blit=True)

plt.show()