from tkinter import *

import tkinter.font as font

import math


root=Tk()
root.title("Calculadora")

root.resizable(0,0)


frame=Frame(root)
frame.pack()
frame.config(bg="grey22")

TNR=font.Font(family="Times New Roman", size=20)


operacion=""

reset_pantalla=False

resultado=0


#--------------pantallla--------------

numeroPantalla=StringVar()

reset_pantalla=True

numeroPantalla.set(float(resultado))

pantalla=Entry(frame, width=25, font=TNR, textvariable=numeroPantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(bg="white", fg="black")

#--------------pulsaciones teclado--------------

def numeroPulsado(num):

	global reset_pantalla

	texto=numeroPantalla.get()

	if num==",":
		
		cant_comas=texto.count(",")

		cant_puntos=texto.count(".")

		if cant_comas >=1 or cant_puntos>=1 or len(texto)==0:
			return

	if reset_pantalla!=False:
		
		numeroPantalla.set("," if num=="," else num)
		
		reset_pantalla=False

	else:
		numeroPantalla.set(texto + ("." if num == "," else num))


#--------------funcion suma--------------

def suma(num):
	
	global operacion

	global resultado

	global reset_pantalla

	resultado+=float(num)

	operacion="suma"

	reset_pantalla=True

	numeroPantalla.set(resultado)

#--------------funcion resta--------------

num1=0

contador_resta=0

def resta(num):
	
	global operacion

	global resultado

	global num1

	global contador_resta

	global reset_pantalla

	if contador_resta==0:

		num1=float(num)

		resultado=num1

	else:

		if contador_resta==1:

			resultado=num1-float(num)

		else:

			resultado=float(resultado)-float(num)	

		numeroPantalla.set(resultado)

		resultado=numeroPantalla.get()


	contador_resta+=1

	operacion="resta"

	reset_pantalla=True

#-------------funcion multiplicacion---------------------
contador_multi=0

def multiplica(num):

	global operacion

	global resultado

	global num1

	global contador_multi

	global reset_pantalla
	
	if contador_multi==0:

		num1=float(num)
		
		resultado=num1

	else:

		if contador_multi==1:

			resultado=num1*float(num)

		else:

			resultado=float(resultado)*float(num)	

		numeroPantalla.set(resultado)
		
		resultado=numeroPantalla.get()


	contador_multi+=1

	operacion="multiplicacion"

	reset_pantalla=True

#-----------------funcion division---------------------

contador_divi=0

def divide(num):

	global operacion

	global resultado

	global num1

	global contador_divi

	global reset_pantalla
	
	if contador_divi==0:

		num1=float(num)
		
		resultado=num1

	else:

		if contador_divi==1:

			resultado=num1/float(num)

		else:

			resultado=float(resultado)/float(num)	

		numeroPantalla.set(resultado)
		
		resultado=numeroPantalla.get()


	contador_divi+=1

	operacion="division"

	reset_pantalla=True

#--------------funcion potencia al cuadrado--------------

contador_potencia=0

def potencia(num):

	global operacion

	global resultado

	global num1

	global contador_potencia

	global reset_pantalla
	
	if contador_potencia==0:

		num1=float(num)
		
		resultado=num1

	else:

		if contador_potencia==1:

			resultado=num1**2

		else:

			resultado=float(resultado)**2	

		numeroPantalla.set(resultado)
		
		resultado=numeroPantalla.get()


	contador_potencia+=1

	reset_pantalla=True

	numeroPantalla.set(float(resultado)**2)

	resultado=0

	contador_potencia=0

#--------------funcion raiz al cuadrado--------------

contador_raiz=0

def raiz(num):

	global operacion

	global resultado

	global num1

	global contador_raiz

	global reset_pantalla
	
	if contador_raiz==0:

		num1=float(num)
		
		resultado=num1

	else:

		if contador_raiz==1:

			resultado=math.sqrt(num1)

		else:

			resultado=float(math.sqrt(resultado))	

		numeroPantalla.set(resultado)
		
		resultado=numeroPantalla.get()


	contador_raiz+=1

	reset_pantalla=True

	numeroPantalla.set(float(math.sqrt(resultado)))

	resultado=0

	contador_raiz=0

#----------------funcion borrar----------------

def borrar():

	global resultado

	global reset_pantalla

	reset_pantalla=True

	resultado=0

	numeroPantalla.set(float(resultado))

#----------------funcion borrar ultimo digito----------------


def borrar_ultimo():

    texto = numeroPantalla.get()

    numeroPantalla.set(texto[:len(texto) - 1])

#----------------funcion el_resultado----------------

def el_resultado():

	global resultado

	global operacion

	global contador_resta

	global contador_multi

	global contador_divi
	

	if operacion=="suma":

		numeroPantalla.set(resultado+float(numeroPantalla.get()))

		resultado=0

	elif operacion=="resta":

		numeroPantalla.set(float(resultado)-float(numeroPantalla.get()))

		resultado=0

		contador_resta=0

	elif operacion=="multiplicacion":

		numeroPantalla.set(float(resultado)*float(numeroPantalla.get()))

		resultado=0

		contador_multi=0

	elif operacion=="division":

		numeroPantalla.set(float(resultado)/float(numeroPantalla.get()))

		resultado=0

		contador_divi=0


#--------------fila 1--------------

botonRaizCuadrada=Button(frame, text="X^(1/2)", width=5, font=TNR, command=lambda:raiz(numeroPantalla.get()))
botonRaizCuadrada.grid(row=2, column=1)

botonPotenciaCuadrado=Button(frame, text="X^2", width=5, font=TNR, command=lambda:potencia(numeroPantalla.get()))
botonPotenciaCuadrado.grid(row=2, column=2)

botonBorrarUltimoDigito = Button(frame, text="DEL", width=5, font=TNR, command=lambda: borrar_ultimo())
botonBorrarUltimoDigito.grid(row=2, column=3)

botonBorrarTodo = Button(frame, text="C", width=5, font=TNR,  command=lambda: borrar())
botonBorrarTodo.grid(row=2, column=4)
botonBorrarTodo.config(bg="grey22", fg="red")

#--------------fila 1--------------

boton7=Button(frame, text="7", width=5, font=TNR, command=lambda:numeroPulsado("7"))
boton7.grid(row=3, column=1)
boton7.config(fg="sandy brown")

boton8=Button(frame, text="8", width=5, font=TNR, command=lambda:numeroPulsado("8"))
boton8.grid(row=3, column=2)
boton8.config(fg="magenta2")

boton9=Button(frame, text="9", width=5, font=TNR, command=lambda:numeroPulsado("9"))
boton9.grid(row=3, column=3)
boton9.config(fg="saddle brown")

botonDividir=Button(frame, text="÷", width=5, font=TNR, command=lambda:divide(numeroPantalla.get()))
botonDividir.grid(row=3, column=4)

#--------------fila 2--------------

boton4=Button(frame, text="4", width=5, font=TNR, command=lambda:numeroPulsado("4"))
boton4.grid(row=4, column=1)
boton4.config(fg="cyan2")

boton5=Button(frame, text="5", width=5, font=TNR, command=lambda:numeroPulsado("5"))
boton5.grid(row=4, column=2)
boton5.config(fg="gold2")

boton6=Button(frame, text="6", width=5, font=TNR, command=lambda:numeroPulsado("6"))
boton6.grid(row=4, column=3)
boton6.config(fg="purple")

botonMultiplicar=Button(frame, text="X", width=5, font=TNR, command=lambda:multiplica(numeroPantalla.get()))
botonMultiplicar.grid(row=4, column=4)

#--------------fila 3--------------

boton1=Button(frame, text="1", width=5, font=TNR, command=lambda:numeroPulsado("1"))
boton1.grid(row=5, column=1)
boton1.config(fg="deep pink")

boton2=Button(frame, text="2", width=5, font=TNR, command=lambda:numeroPulsado("2"))
boton2.grid(row=5, column=2)
boton2.config(fg="blue")

boton3=Button(frame, text="3", width=5, font=TNR, command=lambda:numeroPulsado("3"))
boton3.grid(row=5, column=3)
boton3.config(fg="green")

botonRestar=Button(frame, text="-", width=5, font=TNR, command=lambda:resta(numeroPantalla.get()))
botonRestar.grid(row=5, column=4)

#--------------fila 4--------------

botonComa=Button(frame, text=",", width=5, font=TNR, command=lambda:numeroPulsado(","))
botonComa.grid(row=6, column=1)

boton0=Button(frame, text="0", width=5, font=TNR, command=lambda:numeroPulsado("0"))
boton0.grid(row=6, column=2)

botonIgual=Button(frame, text="=", width=5, font=TNR, command=lambda:el_resultado())
botonIgual.grid(row=6, column=3)
botonIgual.config(bg="grey22", fg="red")

botonSumar=Button(frame, text="+", width=5, font=TNR, command=lambda:suma(numeroPantalla.get()))
botonSumar.grid(row=6, column=4)


#--------------fin--------------

root.mainloop()


