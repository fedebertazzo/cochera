from clase_vehiculos import Vehiculo
from datetime import datetime
from archivos import escribir, leer, eliminar

class Cochera:
    "Define la clase de cochera"
    def __init__(self,ubicaciones, precio_hora):
        self.precio_hora=precio_hora
        self.cant_ubicaciones=ubicaciones
        self.precio_dia=(precio_hora*24)*0.8 #Se bonifica un 20% de la hora
        txt=leer("cochera_registro.txt")
        print(txt)
        self.lugares={}
        # for i in range(1,self.cant_ubicaciones+1): #Arma la cochera vacía
        #     self.lugares[str(i)]=False
        for i in range(1,self.cant_ubicaciones+1):
            if len(txt) ==0:
                self.lugares[str(i)]=False
            else:
                for linea in txt:
                    linea_ubicacion=int(linea[1])
                    print(i, linea_ubicacion)
                    if i == linea_ubicacion:
                        print("match!")
                        self.lugares[str(i)]={"vehiculo":Vehiculo(linea[2],linea[3].strip()),
                                              "ingreso":datetime(int(linea[0].split("-")[0]),
                                                                 int(linea[0].split("-")[1]),
                                                                 int(linea[0].split("-")[2]),
                                                                 int(linea[0].split("-")[3]),
                                                                 int(linea[0].split("-")[4]))
                                            }
                        break
                    else:
                        self.lugares[str(i)]=False
        print(self.lugares)
        pass

    def ingresar_vehiculo(self):
        print("--------------------------------")
        print("Ingrese los datos del vehiculo:")
        dominio=input("Dominio: ").upper()
        tipo=input("Tipo: ").upper()
        vehiculo=Vehiculo(dominio,tipo) #Construir un objeto de la clase Vehiculo 
        print (f"Se ingreso el vehículo: {vehiculo.dominio}, tipo: {vehiculo.tipo}")
        ubicacion=input(f"Ingrese la ubicacion (1-{self.cant_ubicaciones}): ")
        if self.lugares[ubicacion] is False: # Si la ubicacion esta libre...
            # print(datetime.now())
            self.lugares[ubicacion]={"vehiculo":vehiculo,
                                     "ingreso":datetime.now()} #Guarda el objeto Vehiculo en la ubicacion
            registro=",".join([self.lugares[ubicacion]["ingreso"].strftime("%Y-%m-%d-%H-%M"), ubicacion,self.lugares[ubicacion]["vehiculo"].dominio, self.lugares[ubicacion]["vehiculo"].tipo])+"\n"
            # print(registro)
            escribir("cochera_registro.txt",registro)
            # print(self.lugares)
        else:
            print(f"La ubicación {ubicacion} esta ocupada")
        print("--------------------------------")

    def retirar_vehiculo(self):
        print("--------------------------------")
        dominio_buscado=input("Ingrese dominio del vehiculo:").upper()
        eliminar("cochera_registro.txt",dominio_buscado)
        for i in range(1,self.cant_ubicaciones+1):
            if self.lugares[str(i)] != False:
                if self.lugares[str(i)]["vehiculo"].dominio == dominio_buscado:
                    # print("Se encontró vehículo!")
                    ingreso=self.lugares[str(i)]["ingreso"]
                    # print(ingreso)
                    precio=self.calcular_precio(ingreso)                   
                    self.lugares[str(i)]=False
                # else:
                    # print(f"No se encuentra el dominio {dominio_buscado}")

    
    # def mostrar_vehiculo(self):
    #     lugar=input("Ingrese ubicacion: ")
    #     print(f"Dominio: {self.lugares[lugar].dominio}\nTipo: {self.lugares[lugar].tipo}")

    def mostrar_vehiculos(self):
        for i in range(1,self.cant_ubicaciones+1):
            if self.lugares[str(i)]== False:
                print(f"{str(i)} - LIBRE")
            else:
                print(f"{str(i)} - {self.lugares[str(i)]["vehiculo"].dominio} - {self.lugares[str(i)]["vehiculo"].tipo} - {self.lugares[str(i)]["ingreso"]}")

    def calcular_precio(self,ingreso):
        # salida=datetime(datetime.now().year,datetime.now().month,datetime.now().day,datetime.now().hour+2) #Agregamos manualmente 2 horas de diferencia
        salida=datetime.now()
        print("Hora de salida: ",salida)
        diferencia= (salida - ingreso).seconds/3600
        print("Horas: ",diferencia)
        if diferencia < 1:
            precio= self.precio_hora
        elif diferencia >24:
            precio= diferencia*self.precio_dia
        else:
            precio=diferencia * self.precio_hora
        print(f"Total a pagar: ${precio:.2f}")
        return precio