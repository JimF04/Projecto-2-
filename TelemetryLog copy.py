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
L_Titulo = Label(C_root,text="Mensajes Enviados",font=('Agency FB',14),bg='white',fg='blue')
L_Titulo.place(x=100,y=10)

L_Titulo = Label(C_root,text="Respuesta Mensaje",font=('Agency FB',14),bg='white',fg='blue')
L_Titulo.place(x=490,y=10)


SentCarScrolledTxt = tkscrolled.ScrolledText(C_root, height=10, width=45)
SentCarScrolledTxt.place(x=10,y=50)

RevCarScrolledTxt = tkscrolled.ScrolledText(C_root, height=10, width=45)
RevCarScrolledTxt.place(x=400,y=50)


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
            mnsSend = "[{0}] cmd: {1}\n".format(indice,myCar.log[indice][0])
            SentCarScrolledTxt.insert(END,mnsSend)
            SentCarScrolledTxt.see("end")

            mnsRecv = "[{0}] result: {1}\n".format(indice,myCar.log[indice][1])
            RevCarScrolledTxt.insert(END, mnsRecv)
            RevCarScrolledTxt.see('end')

            indice+=1
        time.sleep(0.200)
    
p = Thread(target=get_log)
p.start()

def send_delante():
    myCar.send("dir:0;")
    myCar.send("pwn:500;")

def send_reset():
    myCar.send("dir:0;")
    myCar.send("pwn:0;")

def send_atras():
    myCar.send("dir:0;")
    myCar.send("pwn:-500;")

def send_izquierda():
    myCar.send("dir:-1;")

def send_derecha():
    myCar.send("dir:1;")

def send_lr():
    global lr_status
    if lr_status == 0:
        myCar.send("lr:1;")
        lr_status = 1
    else:
        myCar.send("lr:0;")
        lr_status = 0

def send_ll():
    global ll_status
    if ll_status == 0:
        myCar.send("ll:1;")
        ll_status = 1
    else:
        myCar.send("ll:0;")
        ll_status = 0

def send_lf():
    global lf_status
    if lf_status == 0:
        myCar.send("lf:1;")
        lf_status = 1
    else:
        myCar.send("lf:0;")
        lf_status = 0

def send_lb():
    global lb_status
    if lb_status == 0:
        myCar.send("lb:1;")
        lb_status = 1
    else:
        myCar.send("lb:0;")
        lb_status = 0

def send_blvl():
    myCar.send("blvl;")

def send_ldr():
    myCar.send("ldr;")

def send_circle():
    myCar.send("circle;")

def send_infinite():
    myCar.send("infinite;")

def send_zigzag():
    myCar.send("zigzag;")

def send_special():
    myCar.send("especial;")


#           ____________________________
#__________/Botones de ventana principal

delante = Button(C_root, text="Delante", command=send_delante)
delante.place(x=200, y=200)

reset = Button(C_root, text="Reset", command=send_reset)
reset.place(x=200, y=250)

atras = Button(C_root, text="Atras", command=send_atras)
atras.place(x=200, y=300)

izquierda = Button(C_root, text="Izquierda", command=send_izquierda)
izquierda.place(x=100, y=250)

derecha = Button(C_root, text="Derecha", command=send_derecha)
derecha.place(x=300, y=250)

ll_button = Button(C_root, text="LL", command=send_ll)
ll_button.place(x=100, y=300)

lf_button = Button(C_root, text="LF", command=send_lf)
lf_button.place(x=100, y=200)

lb_button = Button(C_root, text="LB", command=send_lb)
lb_button.place(x=300, y=200)

lr_button = Button(C_root, text="LR", command=send_lr)
lr_button.place(x=300, y=300)

blvl_button = Button(C_root, text="Battery", command=send_blvl)
blvl_button.place(x=400, y=200)

ldr_button = Button(C_root, text="Light", command=send_ldr)
ldr_button.place(x=400, y=250)

circle_button = Button(C_root, text="Circle", command=send_circle)
circle_button.place(x=500, y=200)

infinite_button = Button(C_root, text="Infinite", command=send_infinite)
infinite_button.place(x=500, y=250)

zigzag_button = Button(C_root, text="ZigZag", command=send_zigzag)
zigzag_button.place(x=500, y=300)

special_button = Button(C_root, text="Special", command=send_special)
special_button.place(x=500, y=350)

root.mainloop()
