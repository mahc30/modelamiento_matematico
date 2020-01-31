import turtle
pen = turtle.Turtle()
screen = turtle.Screen()
screen.screensize(400,400)

pen.shape("classic")

screen.bgcolor("#000000")
color_palette_1= ['#fffb96','#b967ff']
color_palette_3 =['#fffb96','#b967ff','#f47835','#d41243','#d41243','#8ec127']

pen.width(3)
pen.speed(1000)
pen.setposition(0,0)
#lado del cuadrado
l = 40

for i in range (0,40):
    pen.pencolor(color_palette_1[i% len(color_palette_1)])
    pen.forward(1000)

    pen.penup()
    pen.setposition(0,0)
    pen.pendown()
    pen.left(9)

pen.goto(-10,-15)
pen.pendown()
pen.pencolor("#ffffff")
pen.width(4)
l=40
#Recomiendo un Limite entre 420 - infinito
lim = 3600

for i in range(0,lim):
    pen.pencolor(color_palette_1[i % len(color_palette_1)])
    pen.forward(l+i)
    pen.left(120)
    pen.forward(l+i)
    pen.left(130)
    pen.forward(l+i)
    pen.left(125)
input()