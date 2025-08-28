import pymysql
import getpass

# Connect to the database
def conectar(ip,usuario,puerto):
    connection = pymysql.connect(host=ip,
                                user=usuario,
                                password=getpass.getpass("Ingrese la contraseña: "),
                                port=puerto,
                                database='cochera',
                                cursorclass=pymysql.cursors.DictCursor)
    print("Conectado a la DB!\n--------------------------------")
    return connection


def mostrar_dominios(conexion_db,nombre_tabla,dominio):
    with conexion_db:
        with conexion_db.cursor() as cursor:
            sql = "select "+ dominio+" from "+nombre_tabla+";"
            cursor.execute(sql)
            resultado = cursor.fetchall()
            print(resultado)
            return resultado
        
def crear_tabla(conexion_db):
    with conexion_db:
        with conexion_db.cursor() as cursor:
            sql = """CREATE TABLE Persons (
            ID int NOT NULL,
            LastName varchar(255) NOT NULL,
            FirstName varchar(255),
            Age int,
            PRIMARY KEY (ID)); """
            cursor.execute(sql)
            print("Tabla creada!")
        
def ejecutar_sql(conexion_db):
    with conexion_db:
        with conexion_db.cursor() as cursor:
            sql = input("Ingrese el query SQL: ")
            cursor.execute(sql)
            resultado = cursor.fetchall()
            print(resultado)
            return resultado

conexion=conectar('127.0.0.1','root',3306)
# info=ejecutar_sql(conexion)
# crear_tabla(conexion)