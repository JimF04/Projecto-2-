"""
Instituto TecnolÃ³gico de Costa Rica
Computer Engineering
Taller de ProgramaciÃ³n

Ejemplo Consola Cliente
Implementación del módulo NodeMCU
Proyecto 2, semestre 1
2019

Profesor: Milton Villegas Lemus
Autor: Santiago Gamboa RamÃ­rez

Restricciónes: Python3.7 
Ejemplo de como usar el módudo NodeMCU de wifiConnection

"""


#           _____________________________
#__________/BIBLIOTECAS
from tkinter import *               # Tk(), Label, Canvas, Photo
from threading import Thread        # p.start()
import threading                    # 
import os                           # ruta = os.path.join('')
import time                         # time.sleep(x)
from tkinter import messagebox      # AskYesNo ()
import tkinter.scrolledtext as tkscrolled
##### Biblioteca para el Carro
from WiFiClient import NodeMCU
from tkinter import ttk 


#           ____________________________
#__________/Ventana Principal
root=Tk()
root.title('Proyecto 3')
root.minsize(800,400)
root.resizable(width=NO,height=NO)

#           ______________________________
#__________/Se crea un lienzo para objetos
C_root=Canvas(root, width=800,height=600, bg='white')
C_root.place(x=0,y=0)

#           ______________________________
#__________/Variables 
lr_status = 0
ll_status = 0
lf_status = 0
lb_status = 0

#           _____________________________________
#__________/Se titulo de los Cuadros de texto


L_Titulo = Label(C_root,text="Respuesta Mensaje",font=('Agency FB',14),bg='white',fg='blue')
L_Titulo.place(x=340,y=10)


RevCarScrolledTxt = tkscrolled.ScrolledText(C_root, height=10, width=45)
RevCarScrolledTxt.place(x=250,y=50)


#           _____________________________________
#__________/Creando el cliente para NodeMCU
myCar = NodeMCU()
myCar.start()


def get_log():
    """
    Hilo que actualiza los Text cada vez que se agrega un nuevo mensaje al log de myCar
    """
    indice = 0
    # Variable del carro que mantiene el hilo de escribir.
    while(myCar.loop):
        while(indice < len(myCar.log)):
            mnsRecv = "[{0}] result: {1}\n".format(indice,myCar.log[indice][1])
            RevCarScrolledTxt.insert(END, mnsRecv)
            RevCarScrolledTxt.see('end')

            indice+=1
        time.sleep(0.200)
    
p = Thread(target=get_log)
p.start()

def send_delante(event=None):
    """
    Función para enviar al carro para que mueva hacia delante a una velocidad determinada.
    """
    myCar.send("dir:0;")
    myCar.send("pwm:-1000;")

def send_reset(event=None):
    """
    Función para resetear el carro para que esté al estado inicial.
    """
    myCar.send("dir:0;")
    myCar.send("pwm:0;")

def send_atras(event=None):
    """
    Función para enviar al carro para que mueva hacia atrás a una velocidad determinada.
    """
    myCar.send("dir:0;")
    myCar.send("pwm:1000;")

def send_izquierda(event=None):
    """
    Función para enviar al carro para que gire a la izquierda
    """
    myCar.send("dir:-1;")

def send_derecha(event=None):
    """
    Función para enviar al carro para que gire a la derecha
    """
    myCar.send("dir:1;")

def send_lr(event=None):
    """
    Función para enviar al carro para que encienda la luz direccional derecha
    """
    global lr_status
    if lr_status == 0:
        myCar.send("lr:1;")
        lr_status = 1
    else:
        myCar.send("lr:0;")
        lr_status = 0

def send_ll(event=None):
    """
    Función para enviar al carro para que encienda la luz direccional izquierda
    """
    global ll_status
    if ll_status == 0:
        myCar.send("ll:1;")
        ll_status = 1
    else:
        myCar.send("ll:0;")
        ll_status = 0

def send_lf(event=None):
    """
    Función para enviar al carro para que encienda las luces frontales
    """
    global lf_status
    if lf_status == 0:
        myCar.send("lf:1;")
        lf_status = 1
    else:
        myCar.send("lf:0;")
        lf_status = 0

def send_lb(event=None):
    """
    Función para enviar al carro para que encienda las luces traseras
    """
    global lb_status
    if lb_status == 0:
        myCar.send("lb:1;")
        lb_status = 1
    else:
        myCar.send("lb:0;")
        lb_status = 0

def send_sense(event=None):
    """
    Función para enviar al carro para que retorne el porcentaje de bateria restante y la luz
    """
    myCar.send("sense;")

def send_circle(event=None):
    """
    Función para enviar al carro para que se mueva de manera circular
    """
    myCar.send("circle;")

def send_infinite(event=None):
    """
    Función para enviar al carro para que se mueva en infito o en 8
    """
    myCar.send("infinite;")

def send_zigzag(event=None):
    """
    Función para enviar al carro para que se mueva en zigzag
    """
    myCar.send("zigzag;")

def send_special(event=None):
    """
    Función para enviar al carro para que se mueva su movimiento especial definida por el programador
    """
    myCar.send("special;")


#           ____________________________
#__________/Botones de ventana principal

delante = ttk.Button(C_root, text="UP", command=send_delante)
delante.place(x=365, y=200)

reset = ttk.Button(C_root, text="Reset", command=send_reset)
reset.place(x=365, y=240)

atras = ttk.Button(C_root, text="Down", command=send_atras)
atras.place(x=365, y=290)

izquierda = ttk.Button(C_root, text="Left", command=send_izquierda)
izquierda.place(x=290, y=240)

derecha = ttk.Button(C_root, text="Right", command=send_derecha)
derecha.place(x=440, y=240)

ll_button = ttk.Button(C_root, text="LL", command=send_ll)
ll_button.place(x=290, y=290)

lf_button = ttk.Button(C_root, text="LF", command=send_lf)
lf_button.place(x=290, y=200)

lb_button = ttk.Button(C_root, text="LB", command=send_lb)
lb_button.place(x=440, y=200)

lr_button = ttk.Button(C_root, text="LR", command=send_lr)
lr_button.place(x=440, y=290)

sense_button = ttk.Button(C_root, text="Sense", command=send_sense)
sense_button.place(x=365, y=335)

circle_button = ttk.Button(C_root, text="Circle", command=send_circle)
circle_button.place(x=515, y=200)

infinite_button = ttk.Button(C_root, text="Infinite", command=send_infinite)
infinite_button.place(x=515, y=240)

zigzag_button = ttk.Button(C_root, text="ZigZag", command=send_zigzag)
zigzag_button.place(x=215, y=200)

special_button = ttk.Button(C_root, text="Special", command=send_special)
special_button.place(x=215, y=240)


#           ____________________________
#__________/Teclas de ventana principal

root.bind("<w>", send_delante)
root.bind("<s>", send_reset)
root.bind("<x>", send_atras)
root.bind("<a>", send_izquierda)
root.bind("<d>", send_derecha)

root.bind("<q>", send_lf)
root.bind("<e>", send_lb)
root.bind("<z>", send_ll)
root.bind("<c>", send_lr)

root.bind("<v>", send_circle)
root.bind("<b>", send_zigzag)
root.bind("<n>", send_infinite)
root.bind("<m>", send_special)
root.bind("<f>", send_sense)

root.mainloop()
