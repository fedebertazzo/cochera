import tkinter

def abrir_ventana2():
    ventana2=tkinter.Tk()
    ventana2.title("Ventana 2")
    label2=tkinter.Label(ventana2,text="Nueva ventana")
    label2.pack()
    boton3=tkinter.Button(ventana2,text="salir",command=ventana2.destroy)
    boton3.pack()

color_fondo="#B84511"


principal=tkinter.Tk()
principal.title("Ventana principal")
principal.config(bg=color_fondo)
# principal.size('600x400')
###
#Elementos de la ventana#
titulo=tkinter.Label(principal,text="Hola Mundo",bg="#A3C50B")
titulo.pack()
# titulo.grid(row=0,column=1)

entrada1=tkinter.Entry(principal)
entrada1.pack()
# entrada1.grid(row=1,column=0)

entrada2=tkinter.Entry(principal)
entrada2.pack()
# entrada2.grid(row=1,column=3)

boton1=tkinter.Button(principal,text="Nueva ventana",command=abrir_ventana2)
boton1.pack()
boton2=tkinter.Button(principal,text="Cerrar",command=principal.quit)
boton2.pack()
# boton2.grid(row=2,column=1)
###
principal.mainloop()
print("Entrada 1: ",entrada1)
print("Entrada 2: ",entrada2)


# top = tkinter.Tk()
# Lb = tkinter.Listbox(top)
# Lb.insert(1, 'Python')
# Lb.insert(2, 'Java')
# Lb.insert(3, 'C++')
# Lb.insert(4, 'Any other')
# Lb.pack()
# top.mainloop()

# root = tkinter.Tk()
# menu = tkinter.Menu(root)
# root.config(menu=menu)
# filemenu = tkinter.Menu(menu)
# menu.add_cascade(label='File', menu=filemenu)
# filemenu.add_command(label='New')
# filemenu.add_command(label='Open...')
# filemenu.add_separator()
# filemenu.add_command(label='Exit', command=root.quit)
# helpmenu = tkinter.Menu(menu)
# menu.add_cascade(label='Help', menu=helpmenu)
# helpmenu.add_command(label='About')
# root.mainloop()