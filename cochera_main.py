from clase_cochera import Cochera



cochera1=Cochera(5,2500.00)
salir=False

while salir==False:
    #MENU
    print("Bienvenido:")
    print("""
          1) Ingresar un nuevo vehiculo
          2) Retirar vehículo
          3) Mostrar info
          4) Salir""")
    opcion=input("Opción: ")
    if opcion == "1":
        cochera1.ingresar_vehiculo()
    if opcion == "2":
        cochera1.retirar_vehiculo()
    if opcion == "3":
        cochera1.mostrar_vehiculos()
    if opcion == "4":
        break
    else:
        continue