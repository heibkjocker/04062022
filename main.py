#Importar la libreria para GUI
from tkinter import *

#importar la libreria para VENTANA DE MENSAJES
from tkinter import messagebox

#importar la libreria para FUNCIONES MATEMATICAS
import math

#importar la libreria para LISTAS DESPLEGABLES
from tkinter.ttk import Combobox

#importar libreria de UTILIDADES
import Util

#importar la libreria para EXPRESIONES REGULARES
import re

ventana = Tk()
ventana.title("Grafica Funcion")

ancho = 400
alto = 300

ventana.minsize(width=ancho, height=alto+50)

#definir el area de la grafica
c = Canvas(ventana, width=ancho, height=alto, bg='black')
c.grid(row=1)

#definir contenedor de los elementos para datos de entrada
frm=Frame(ventana)
frm.grid(row=0)

Util.agregarEtiqueta(frm, "Limite Inferior", 0, 0)
txtLI=Util.agregarTexto(frm, 10, 0, 1)
txtLI.insert(0, "-10")

Util.agregarEtiqueta(frm, "Limite Superior", 0, 2)
txtLS=Util.agregarTexto(frm, 10, 0, 3)
txtLS.insert(0, "10")

cmbF=Util.agregarLista(frm,("Cuadratica", "Cubica", "Seno", "Coseno", "Tangente", "Logaritmo Natural"), 1, 1)

def f(x, tipo):
    if tipo==0:
        y=x**2
    elif tipo==1:
        y=x**3
    elif tipo==2:
        y=math.sin(x)
    elif tipo==3:
        y=math.cos(x)
    elif tipo==3:
        y=math.tan(x)
    elif tipo==3:
        y=math.log(x)
    return y


def graficar():
    #validar datos de entrada
    if len(txtLI.get())>0 and len(txtLS.get())>0 and \
        re.match("^[-]?[0-9]*[.]?[0-9]*$", txtLI.get()) and \
        re.match("^[-]?[0-9]*[.]?[0-9]*$", txtLS.get()) and \
        cmbF.current()>=0:
        #Limpiar area de despliegue
        c.delete("all")
        
        #parametros
        xI=float(txtLI.get())
        xF=float(txtLS.get())

        #Calcula incremento de X
        dX = (xF - xI)/ancho

        #Hallar valores maximos y minimos de Y
        x = xI
        yI = f(x, cmbF.current())
        yF = yI
        for xP in range(1, ancho):
            fX = f(x, cmbF.current())

            if fX > yI:
                yI = fX
            if fX < yF:
                yF = fX

            x += dX

        #Incremento de Y
        dY = (yI - yF)/alto

        #Mostrar eje y
        if xI <= 0 and 0 <= xF:
            xP = int(abs(xI)/dX)
            c.create_line(xP, 0, xP, alto, fill="green")
        #Mostrar eje x
        if yI >= 0 and 0 >= yF:
            yP = int(yI/dY)
            c.create_line(0, yP, ancho, yP, fill="green")

    else:
        messagebox.showerror("", "Datos no validos para la grafica")


btnG=Button(frm, text='Graficar' , command=graficar)
btnG.grid(row=1)
mainloop()