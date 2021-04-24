from tkinter import *
from tkinter import scrolledtext as st
import tkinter.font as font
from tkinter import messagebox as mb
from tkinter import filedialog as fd
import sqlite3



#--------------Funciones--------------

def conexionBBDD():


    conn = sqlite3.connect("Usuarios.sqlite")
    cur = conn.cursor()
    
    
    try:
        cur.execute("DROP TABLE IF EXISTS Usuarios")

        cur.execute('''
        CREATE TABLE Usuarios (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name VARCHAR(50),Lastname VARCHAR(50),
            Password VARCHAR(16),
            Address VARCAHR(30),
            Comments VARCHAR(100))
            ''')
        mb.showinfo("DDBB", "BBDD correctly created.")

    except:
        mb.showwarning("Warning", "The BBDD already exists.")


def salirAplicacion():

    valor=mb.askquestion("Exit", "Are you sure you want to exit?")

    if valor =="yes":
        root.destroy()

def limpiarCampos():

    miID.set("")
    miNombre.set("")
    miApellido.set("")
    miPass.set("")
    miDirec.set("")
    cuadroComent.delete(1.0, END)

def crear():
    try:

        conn = sqlite3.connect("Usuarios.sqlite")
        cur = conn.cursor()
        

        varUsuarios = (miNombre.get(), miApellido.get(), miPass.get(), miDirec.get(), cuadroComent.get("1.0", END))
                
        cur.execute("INSERT INTO Usuarios VALUES (NULL, ?, ?, ?, ?, ?)", varUsuarios)
        
        conn.commit()
        
        mb.showinfo("BBDD", "Record inserted successfully")
    
    except:
        mb.showwarning("Error")

def leer():

    conn = sqlite3.connect("Usuarios.sqlite")
    cur = conn.cursor()

    cur.execute("SELECT * FROM Usuarios WHERE ID=" + miID.get())

    elUsuario=cur.fetchall()

    for i in elUsuario:

        miID.set(i[0])
        miNombre.set(i[1])
        miApellido.set(i[2])
        miPass.set(i[3])
        miDirec.set(i[4])
        cuadroComent.insert(1.0, i[5])
    
    conn.commit()

def actualizar():

    conn = sqlite3.connect("Usuarios.sqlite")
    cur = conn.cursor()
    
    varUsuarios = (miNombre.get(), miApellido.get(), miPass.get(),
                   miDirec.get(), cuadroComent.get("1.0", END))
    
    cur.execute("UPDATE Usuarios SET Name=?, Lastname=?, Password=?, Address=?, Comments=?" +
                 "WHERE ID=" + miID.get(), (varUsuarios))
    
    #cur.execute("UPDATE Usuarios SET Name='" + miNombre.get() + 
    #            "', Lastname='" + miApellido.get() + 
    #            "', Password='" + miPass.get() + 
    #            "', Address='" + miDirec.get() + 
    #            "', Comments='" + cuadroComent.get("1.0", END) + 
    #            "'WHERE ID=" + miID.get())
    
    conn.commit()
    
    mb.showinfo("BBDD", "Record updated successfully")

def eliminar():

    conn = sqlite3.connect("Usuarios.sqlite")
    cur = conn.cursor()

    cur.execute("DELETE FROM Usuarios WHERE ID=" + miID.get())

    conn.commit()

    mb.showinfo("BBDD", "Record deleted successfully")


#--------------Root--------------

root=Tk()
root.title("Practice")

barraMenu = Menu()

root.config(menu=barraMenu, width=300, height=300)

TNR = font.Font(family="Times New Roman", size=11)

#--------------Menu--------------

bbdd = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="BBDD", menu=bbdd)
bbdd.add_command(label="Connect", command=conexionBBDD)
bbdd.add_separator()
bbdd.add_command(label="Exit", command=salirAplicacion)


edit = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Edit", menu=edit)
edit.add_command(label="Erase Fields", command=limpiarCampos)

crud = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="CRUD", menu=crud)
crud.add_command(label="Create", command=crear)
crud.add_command(label="Read", command=leer)
crud.add_command(label="Update", command=actualizar)
crud.add_command(label="Delete", command=eliminar)

helps = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Help", menu=helps)
helps.add_command(label="Welcome")
helps.add_command(label="Documentation")
helps.add_separator()
helps.add_command(label="Report Issue")
helps.add_separator()
helps.add_command(label="View License")
helps.add_command(label="Privacy Statement")
helps.add_separator()
helps.add_command(label="Chek for Updates")
helps.add_separator()
helps.add_command(label="About")


#--------------Frame 1--------------
frame = Frame()
frame.pack()

miID=StringVar()
miNombre=StringVar()
miApellido=StringVar()
miPass = StringVar()
miDirec = StringVar()


cuadroID = Entry(frame, font=TNR, textvariable=miID)
cuadroID.grid(row=0, column=1, padx=10, pady=10)
cuadroID.config(fg="magenta2")

cuadroNombre = Entry(frame, font=TNR, textvariable=miNombre)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)
cuadroNombre.config(fg="red")

cuadroApellido = Entry(frame, font=TNR, textvariable=miApellido)
cuadroApellido.grid(row=2, column=1, padx=10, pady=10)
cuadroApellido.config(fg="green")

cuadroPass = Entry(frame, font=TNR, textvariable=miPass)
cuadroPass.grid(row=3, column=1, padx=10, pady=10)
cuadroPass.config(fg="blue")
cuadroPass.config(show="*")

cuadroDirec = Entry(frame, font=TNR, textvariable=miDirec)
cuadroDirec.grid(row=4, column=1, padx=10, pady=10)

cuadroComent = st.ScrolledText(frame, width=19, height=8, font=TNR)
cuadroComent.grid(row=5, column=1, padx=10, pady=10)
cuadroComent.config(fg="cyan2")




IDLabel = Label(frame, text="ID: ", font=TNR)
IDLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)
IDLabel.config(fg="magenta2")

nombreLabel = Label(frame, text="Name: ", font=TNR)
nombreLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)
nombreLabel.config(fg="red")

apellidoLabel = Label(frame, text="Lastname: ", font=TNR)
apellidoLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)
apellidoLabel.config(fg="green")

PassLabel = Label(frame, text="Password: ", font=TNR)
PassLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)
PassLabel.config(fg="blue")

direcLabel = Label(frame, text="Address: ", font=TNR)
direcLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

comentLabel = Label(frame, text="Comments: ", font=TNR)
comentLabel.grid(row=5, column=0, sticky="e", padx=10, pady=10)
comentLabel.config(fg="cyan2")


#--------------Frame 2--------------


frame2 = Frame()
frame2.pack()


botonCrear=Button(frame2, text="Create", font=TNR, command=crear)
botonCrear.grid(row=0, column=0, padx=10, pady=10)

botonLeer = Button(frame2, text="Read", font=TNR, command=leer)
botonLeer.grid(row=0, column=1, padx=10, pady=10)

botonUpdate = Button(frame2, text="Update", font=TNR, command=actualizar)
botonUpdate.grid(row=0, column=2, padx=10, pady=10)

botonBorrar = Button(frame2, text="Delete", font=TNR, command=eliminar)
botonBorrar.grid(row=0, column=3, padx=10, pady=10)


#--------------Fin--------------


root.mainloop()
