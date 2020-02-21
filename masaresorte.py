import numpy as np 
from scipy.integrate import odeint
import math

#Para animaciones 
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.patches import ConnectionPatch

#Constantes por fuera for performance purposes
scale = 3 # 0 < scale < 6
lim = 5
#Masas
m1 = 10
m2 = 5
beta = 0.8 #Coeficiente de Friccioń
#Constantes de Elasticidad
k1 = 100
k2 = 100
#Tamaño de los resortes en reposo
l1 = 10
l2 = 10

def masaresorte(X, t):
    #Movimiento cosenoidal (Multiplico por una escala para hacerlo más 'amplio')
    offset = scale * math.cos(2*t)

    #Después de cierto tiempo, se deja de mover 
    if(t >= lim):
       offset = 0
       
    x1, dx1, x2, dx2 = X

    d1 = np.sqrt((x1-offset)**2)
    d2 = np.sqrt((x2-x1)*(x2-x1))
    
    dv1 = (-beta*dx1 - k1*(d1 - l1)*(offset-x1)/d1 + k2*(d2 - l2)*(x2-x1)/d2)/m1
    dv2 = (-beta*dx2 + k2*(d2 - l2)*(x1-x2)/d2)/m2

    return [dx1,dv1,dx2,dv2]

t = np.linspace(0,10,1800)

Y = odeint(masaresorte, [6, 0, 18, 0], t)

plt.xlabel('tiempo')
plt.ylabel('x')

plt.plot(t,Y[:,0])
plt.plot(t,Y[:,2])
plt.legend(['Carro 1','Carro 2'])

plt.show()

fig = plt.figure()
ax = plt.axes(xlim=(-60, 120), ylim=(0, 10))
carrito1 = plt.Rectangle((10,3), 2, 2, color="blue",fill=True)
carrito2 = plt.Rectangle((40,3), 2, 2, color="orange",fill=True)
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
    cx = math.cos((i+90)/180)*2
    circle.center = (cx,cy)

    line1 = plt.Arrow(cx, 4, x1 - cx, 0, width=0.2, color="green", hatch='o')
    ax.add_patch(line1)
   
    
    line2 = plt.Arrow(x1+3, 4, (x2 - (x1+3)), 0, width=0.2, color="green", hatch='o')
    ax.add_patch(line2)
    
    return [carrito1,carrito2, circle, line1, line2]

anim = animation.FuncAnimation(fig, animate, 
                               init_func=init, 
                               frames=  1799, 
                               interval=1,
                               blit=True)

plt.show()
