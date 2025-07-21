###################################################
#                                                 #
# db_funciones.py - Funciones para conexion y     #
#                   manejo de las distintas       #
#                   opciones en la base de  datos #
#                   Insert , update , delete      #  
###################################################

# importamos el módulo Sqlite3
import sqlite3

# importamos el módulo os
import os

# importamos modulo colorama
from colorama import Fore, Style, init

# Carpeta donde está el script actual
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Ruta completa a la base de datos
bd_ruta = os.path.join(BASE_DIR, "inventario.db")


# Función para crear la tabla productos
def bd_crear_tabla_productos():
    '''
    Crear la tabla productos en la base de datos inventario  
    Verifica si no existe previamente sino la crea 

    Parametros
    ----------

    Ninguno

    Retorno
    -------

    True  = Creo la tabla correctamente 

    False = Hubo algun problema al crear la tabla

    '''

    try:
        conexion = sqlite3.connect(bd_ruta)
        cursor = conexion.cursor()
        sql = """CREATE TABLE IF NOT EXISTS "productos" (
            "id" INTEGER,
            "nombre" TEXT NOT NULL,
            "descripcion" TEXT NOT NULL,
            "categoria" TEXT NOT NULL,
            "precio" REAL NOT NULL,
            "cantidad" INTEGER NOT NULL,
            PRIMARY KEY("id" AUTOINCREMENT)
        );"""
        cursor.execute(sql)
        conexion.commit()
        return True  # ✔️ Todo bien
    except Exception as error:
        print(Fore.RED + f"❌ Error al crear la tabla: {error}" + Style.RESET_ALL)
        return False  # ❌ Hubo error
    finally:
        conexion.close()




# Funcion para leer TODOS los datos de la tabla productos
def bd_leer_productos():
    '''
    Obtener todos los productos de la base de datos

    Parametros
    ----------

    Ninguno

    Retorno
    -------

    Lista con todos los productos de la tabla productos de la base de datos inventario

    Si hubo algun problema la lista estara vacia

    '''


    # declaramos una lista local para retornar el resultado de la consulta en la tabla
    lista_productos = []
    try:
        # establecemos la conexión a la base inventario.db con ruta relativa
        conexion = sqlite3.connect(bd_ruta)
        # creamos el cursor para ejecutar la consulta
        cursor = conexion.cursor()
        # declaramos la variable sql con la consulta en texto plano
        sql = """SELECT * FROM productos"""
        # ejecutamos la consulta
        cursor.execute(sql)
        # volcamos en una variable local los datos que vienen de la base
        lista_productos = cursor.fetchall()
    except Exception as error:
        print(
            f"Error encontrado al crear la tabla: {error}"
        )  # muestramos en pantalla si hubo error
    finally:
        conexion.close()  # cerramos la conexión
    return lista_productos


def bd_leer_producto_por_id(id):
    '''
    Obtener los datos de un producto especifico

    Parametros
    ----------

    id - numero identificacion del producto a buscar

    
    Retorno
    -------

    Diccionario con los datos del producto indicado en el parametro ID

    Si hubo algun problema retornara un diccionario vacio

    '''

    producto = None  # Solo debería devolver un producto (no una lista)
    try:
        conexion = sqlite3.connect(bd_ruta)
        conexion.row_factory = sqlite3.Row
        cursor = conexion.cursor()
        sql = "SELECT * FROM productos WHERE id = ?"
        cursor.execute(sql, (id,))  # el segundo parámetro debe ser una tupla
        fila = cursor.fetchone()  # como solo debería haber uno, usamos fetchone()
        if fila:
            producto = dict(fila)  # Convierte el resultado a un diccionario 
    except Exception as error:
        print(f"Error encontrado al leer el producto: {error}")
    finally:
        conexion.close()
    return producto


# Funcion para insertar datos en la tabla productos
def bd_insertar_producto(nombre,descripcion,categoria, precio, cantidad):
    '''
    Insertar un registro en la tabla productos con los datos de un nuevo producto

    Parametros
    ----------

    nombre      - Texto - Nombre del producto

    descripcion - Texto - Descripcion del producto

    categoria   - Texto - Categoria del producto

    precio      - float - Precio del producto 

    cantidad    - Entero - Cantidad de existencia del producto

    
    Retorno
    -------

    True  - Se inserto correctamente el registro en la tabla productos

    False - No se pudo insertar el nuevo registro en la tabla productos

    '''

    status = False
    try:
        # establece la conexión a la base inventario.db con ruta relativa
        conexion = sqlite3.connect(bd_ruta)
        # cursor para ejecutar las consultas
        cursor = conexion.cursor()
        # variable sql con la consulta en texto plano - los valores estan parametrizados
        sql = """INSERT INTO productos 
		("nombre", "descripcion","categoria","precio", "cantidad") 
		VALUES 
		(?,?,?,?,?)"""
        # ejecuta la consulta con los parametros en la lista
        cursor.execute(sql, (nombre,descripcion, categoria, precio,  cantidad))
        # validamos que se haya actualizado el registro y actualizamos el estado para informar
        if cursor.rowcount == 1:
            status = True
        # confirma los cambios
        conexion.commit()
    except Exception as error:
        # muestra en pantalla si hubo error
        print(f"Error encontrado al crear la tabla: {error}")
    finally:
        # cierra la conexión
        conexion.close()
        # retorna el estado de la transaccion
        return status
    

# Funcion para buscar los producto con bajo stock
def bd_leer_producto_bajo_stock(limite):
    '''
    Devuelve los productos de la tabla que se encuentren bajo el nivel de cantidad de stock
    indicada en el parametro limite

    Parametros
    ----------

    limite      - Entero - Valor limite para control cantidades de producto que esten bajo ese valor

    
    Retorno
    -------

    Lista con los productos que cumplan con la condicion menor al parametro limite

    En caso que ningun producto la cumpla , la lista estara vacia

    '''

    # declaramos una variable local para retornar el resultado de la consulta en la tabla
    lista_productos = []
    try:
        # establecemos la conexión a la base inventario.db con ruta relativa
        conexion = sqlite3.connect(bd_ruta)
        # creamos el cursor para ejecutar la consulta
        cursor = conexion.cursor()
        # preparamos la consulta SQL parametrizada
        sql = """SELECT * FROM productos WHERE cantidad < ?"""
        
        # ejecutamos la consulta con el parámetro cantidad
        cursor.execute(sql, (limite,))
        # volcamos en una variable local el dato que vienen de la base
        lista_productos = cursor.fetchall()

    except Exception as error:
        # muestramos en pantalla si hubo error
        print(f"Error encontrado al leer el registro por id: {error}")
    finally:
        # cerramos la conexión
        conexion.close()
        # retornamos el resultado
        return lista_productos


def bd_eliminar_producto(id):
    '''
    Eliminar un producto de la tabla productos en base a un valor de id pasado por parametro

    Parametros
    ----------

    id    - Entero - Identificacion del producto a eliminar
    
    Retorno
    -------

    True  - Se elimino correctamente el registro de la tabla productos

    False - No se pudo eliminar el registro de la tabla productos

    '''

    # declaramos una variable local con el estado de la operacion
    status = False
    try:
        # establecemos la conexión a la base inventario.db con ruta relativa
        conexion = sqlite3.connect(bd_ruta)
        # creamos el cursor para ejecutar la consulta
        cursor = conexion.cursor()
        # preparamos la consulta SQL parametrizada
        sql = """DELETE FROM productos WHERE id = ?"""
        # ejecutamos la consulta y pasamos como argumento la tupla con el id del registro a eliminar
        cursor.execute(sql, (id,))
        # confirmamos el cambio
        conexion.commit()
        # validamos que se haya actualizado el registro y actualizamos el estado para informar
        if cursor.rowcount > 0:
            status = True
    except Exception as error:
        print(
            f"Error encontrado al eliminar el registro: {error}"
        )  # muestramos en pantalla si hubo error
    finally:
        # cerramos la conexión
        conexion.close()
        # retornamos el estado de la operación
        return status        
    

def bd_modificar_producto(id, nombre, descripcion, categoria, precio, cantidad):
    '''
    Modificar un registro en la tabla productos con los datos de un nuevo producto

    Parametros
    ----------

    id          - Entero - identificacion del producto a modificar

    nombre      - Texto - Nombre del producto

    descripcion - Texto - Descripcion del producto

    categoria   - Texto - Categoria del producto

    precio      - float - Precio del producto 

    cantidad    - Entero - Cantidad de existencia del producto

    
    Retorno
    -------

    True  - Se actualizo correctamente el registro en la tabla productos

    False - No se pudo actualizar el registro en la tabla productos

    '''

    status = False
    try:
        # establecer conexión
        conexion = sqlite3.connect(bd_ruta)
        cursor = conexion.cursor()
        
        # sentencia SQL UPDATE con WHERE
        sql = """
        UPDATE productos SET 
            nombre = ?, 
            descripcion = ?, 
            categoria = ?, 
            precio = ?, 
            cantidad = ?
        WHERE id = ?
        """
        # ejecutar con los parámetros (¡el id va último!)
        cursor.execute(sql, (nombre, descripcion, categoria, precio, cantidad, id))
        
        if cursor.rowcount == 1:
            status = True
        
        conexion.commit()
    except Exception as error:
        print(f"Error al modificar el producto: {error}")
    finally:
        conexion.close()
        return status
    