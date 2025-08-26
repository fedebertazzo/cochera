import pymysql
import getpass

# Connect to the database
def conectar(ip,usuario,puerto):
    connection = pymysql.connect(host=ip,
                                user=usuario,
                                password=getpass.getpass("Ingrese la contraseña: "),
                                port=puerto,
                                database='demo_vehiculos',
                                cursorclass=pymysql.cursors.DictCursor)
    print("Conectado a la DB!\n--------------------------------")
    return connection


def mostrar_tabla(conexion_db,nombre_tabla):
    with conexion_db:
        with conexion_db.cursor() as cursor:
            sql = "select * from "+nombre_tabla+";"
            cursor.execute(sql)
            resultado = cursor.fetchall()
            print(resultado)
            return resultado
        

conexion=conectar('127.0.0.1','root',3306)
info=mostrar_tabla(conexion,"Vehiculos")