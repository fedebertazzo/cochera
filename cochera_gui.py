import tkinter

class CocheraGUI():
    def __init__(self,cochera):
        self.cochera =cochera #Objeto cochera con sus atributos y métodos
        self.top=tkinter.Tk() #Crea la ventana principal
        self.top.title("Mi cochera") #Define el título de la ventana

        #ELEMENTOS DE LA VENTANA#

        self.boton1=tkinter.Button(self.top,text="Ingresar vehiculo") 
        self.boton1.pack()
        self.boton2=tkinter.Button(self.top,text="Retirar vehiculo")
        self.boton2.pack()
        self.boton3=tkinter.Button(self.top,text="Mostrar vehiculos")
        self.boton3.pack()
        self.boton4=tkinter.Button(self.top,text="Salir",command=self.top.destroy)
        self.boton4.pack()
        # FIN DE ELEMENTOS DE LA VENTANA #

        self.top.mainloop()