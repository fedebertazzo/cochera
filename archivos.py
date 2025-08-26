def escribir(nombre_archivo,registro):
    with open(nombre_archivo,"a",encoding="utf-8") as archivo:
        archivo.writelines(registro)
        print("Escritura exitosa!")

def leer(nombre_archivo):
    with open(nombre_archivo,"r",encoding="utf-8") as archivo:
        listado=archivo.readlines()
        cochera=[]
        for linea in listado:
            aux=linea.split(",")
            cochera.append(aux)
        # print(cochera)
        return cochera

def eliminar(nombre_archivo, dominio):
    listado=leer(nombre_archivo)
    # print(listado)
    for linea in listado:
        if linea[2] == dominio:
            print("Se encuentra el dominio en el registro")
            listado.remove(linea)
            print(f"Se quitó el registro con dominio {dominio}")
            # print(listado)
        else:
            print("No se encontró registro")
    with open(nombre_archivo,"w", encoding="utf-8") as archivo:
        for lista in listado:
            linea=",".join(lista).strip()
            # print(linea)
            archivo.write(linea+"\n")