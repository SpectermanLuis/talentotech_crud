####################################################
#                                                  #
# ingreso_datos.py - Funciones manejo de interfase #
#                    y comunicacion con el usuario #
#                distintos menus del sistema       #
#                                                  #
####################################################


from db_funciones import *
from utilidades import pausar,mostrar_listado_productos,mostrar_producto

def getNombre(mensaje="Ingrese el nombre del producto: "):
    '''
    Solicita ingresar nombre del producto ( ingreso / actualizacion x todos los campos)
    Validaciones basicas , que no este vacio y que tenga una longitud minima

    Parametro
    ---------

    mensaje - Texto - Mensaje a usar en el input del campo , teniendo un valor por defecto

    Retorna
    -------

    nombre - Nombre del producto 

    '''
    
    while True:
        nombre = input(mensaje).strip()

        if not nombre:
            print("❌ No se admite campo vacío.")
        elif len(nombre) < 3:
            print("❌ El nombre debe tener al menos 3 caracteres.")
        else:
            return nombre
        

def getNombreConVacio(mensaje="Ingrese nombre del producto: "):
    '''
    Solicita ingresar nombre del producto ( en caso de actualizacion por campo especifico)
    Validaciones basicas en caso que se ingrese un valor , que tenga una longitud minima

    Parametro
    ---------

    mensaje - Texto - Mensaje a usar en el input del campo , teniendo un valor por defecto

    Retorna
    -------

    nombre - Nombre del producto si es que se modifica el campo 
             Vacio si se va a mantener el mismo valor anterior
        
    '''

    while True:
        nombre = input(mensaje).strip()

        if nombre == "":
            return ""  # Devuelve vacío sin validar
        elif len(nombre) < 3:
            print("❌ El nombre debe tener al menos 3 caracteres.")
        else:
            return nombre


def getDescripcion(mensaje="Ingrese descripcion del producto: "):
    '''
    Solicita ingresar descripcion del producto ( ingreso / actualizacion x todos los campos)
    Validaciones basicas , que no este vacio y que tenga una longitud minima

    Parametro
    ---------

    mensaje - Texto - Mensaje a usar en el input del campo , teniendo un valor por defecto

    Retorna
    -------

    descripcion - descripcion del producto 

    '''

    while True:
        descripcion = input(mensaje).strip()

        if not descripcion:
            print("❌ No se admite campo vacío.")
        elif len(descripcion) < 3:
            print("❌ La descripcion debe tener al menos 3 caracteres.")
        else:
            return descripcion

def getDescripcionConVacio(mensaje="Ingrese descripcion del producto: "):
    '''
    Solicita ingresar descripcion del producto ( en caso de actualizacion por campo especifico)
    Validaciones basicas en caso que se ingrese un valor , que tenga una longitud minima

    Parametro
    ---------

    mensaje - Texto - Mensaje a usar en el input del campo , teniendo un valor por defecto

    Retorna
    -------

    descripcion - Descripcion del producto si es que se modifica el campo 
                  Vacio si se va a mantener el mismo valor anterior
        
    '''

    while True:
        descripcion = input(mensaje).strip()

        if descripcion == "":
            return ""  # Devuelve vacío sin validar
        elif len(descripcion) < 3:
            print("❌ La descripción debe tener al menos 3 caracteres.")
        else:
            return descripcion



def getCategoria(mensaje="Ingrese categoria del producto: "):
    '''
    Solicita ingresar categoria del producto ( ingreso / actualizacion x todos los campos)
    Validaciones basicas , que no este vacio y que tenga una longitud minima

    Parametro
    ---------

    mensaje - Texto - Mensaje a usar en el input del campo , teniendo un valor por defecto

    Retorna
    -------

    categoria - Categoria del producto 

    '''

    while True:
        categoria = input(mensaje).strip()

        if not categoria:
            print("❌ No se admite campo vacío.")
        elif len(categoria) < 3:
            print("❌ El nombre debe tener al menos 3 caracteres.")
        else:
            return categoria


def getCategoriaConVacio(mensaje="Ingrese categoria del producto: "):
    '''
    Solicita ingresar categoria del producto ( en caso de actualizacion por campo especifico)
    Validaciones basicas en caso que se ingrese un valor , que tenga una longitud minima

    Parametro
    ---------

    mensaje - Texto - Mensaje a usar en el input del campo , teniendo un valor por defecto

    Retorna
    -------

    categoria - Categoria del producto si es que se modifica el campo 
                Vacio si se va a mantener el mismo valor anterior
        
    '''

    while True:
        categoria = input(mensaje).strip()

        if categoria == "":
            return ""  # Devuelve vacío sin validar
        elif len(categoria) < 3:
            print("❌ El nombre debe tener al menos 3 caracteres.")
        else:
            return categoria


def getPrecio(mensaje="💲 Ingrese el *precio* del producto: "):
    '''
    Solicita ingresar precio del producto ( ingreso / actualizacion x todos los campos)
    Validaciones basicas , que sea un numero valido , no cero ni negativo

    Parametro
    ---------

    mensaje - Texto - Mensaje a usar en el input del campo , teniendo un valor por defecto

    Retorna
    -------

    precio - Float - Precio del producto

    '''

    while True:
        try:
            precio = float(input(mensaje))
            if precio >= 0:
                return precio
            print("⚠️ El precio no puede ser negativo.")
        except ValueError:
            print("❌ Ingrese un número válido.")


def getPrecioConVacio(mensaje="💲 Ingrese el *precio* del producto: "):
    '''
    Solicita ingresar precio del producto ( en caso de actualizacion por campo especifico)
    Validaciones basicas en caso que se ingrese un valor , que sea numero valido no cero ni negativo

    Parametro
    ---------

    mensaje - Texto - Mensaje a usar en el input del campo , teniendo un valor por defecto

    Retorna
    -------

    precio  - Precio del producto si es que se modifica el campo 
              Vacio si se va a mantener el mismo valor anterior
        
    '''

    while True:
        entrada = input(mensaje).strip()
        if entrada == "":
            return ""  # Retorna vacío si no ingresó nada
        try:
            precio = float(entrada)
            if precio >= 0:
                return precio
            print("⚠️ El precio no puede ser negativo.")
        except ValueError:
            print("❌ Ingrese un número válido.")


def getCantidad(mensaje="📦 Ingrese cantidad disponible: "):
    '''
    Solicita ingresar cantidad del producto ( ingreso / actualizacion x todos los campos)
    Validaciones basicas , que sea un numero valido , no cero ni negativo

    Parametro
    ---------

    mensaje - Texto - Mensaje a usar en el input del campo , teniendo un valor por defecto

    Retorna
    -------

    cantidad - Entero - Cantidad del producto

    '''

    while True:
        try:
            cantidad = int(input(mensaje))
            if cantidad >= 0:
                return cantidad
            print("⚠️ La cantidad no puede ser negativa")

        except ValueError:
            print("❌ Ingrese un número entero válido.")


def getCantidadConVacio(mensaje="📦 Ingrese cantidad disponible: "):
    '''
    Solicita ingresar cantidad del producto ( en caso de actualizacion por campo especifico)
    Validaciones basicas en caso que se ingrese un valor , que sea numero valido no cero ni negativo

    Parametro
    ---------

    mensaje - Texto - Mensaje a usar en el input del campo , teniendo un valor por defecto

    Retorna
    -------

    cantidad - Cantidad del producto si es que se modifica el campo 
               Vacio si se va a mantener el mismo valor anterior
        
    '''

    while True:
        entrada = input(mensaje).strip()
        if entrada == "":
            return ""  # Retorna vacío si no ingresó nada
        try:
            cantidad = int(entrada)
            if cantidad >= 0:
                return cantidad
            print("⚠️ La cantidad no puede ser negativa")
        except ValueError:
            print("❌ Ingrese un número entero válido.")



def getIdProductoBaseLista(mensaje):
   ''' 
   Seleccion un id de un producto para modificar , borrar o consultar a partir de 
   visualizar la lista de productos totales 
   
   Parametro
   ---------
   
   mensaje = identifica proceso que solicita codigo producto
             por ejemplo :  mensaje = 'Ingresar Id Producto a eliminar :"
                            mensaje = 'Ingresar Id Producto a modificar :"
   
   Retorna             
   -------
   Id - Entero - Identificacion del producto seleccionado 
                 Si en la tabla producto esta vacia , devuelve cero  
   '''

   lista_productos = bd_leer_productos()
   
   if not lista_productos:
        print(Fore.YELLOW + "⚠️ No hay articulos en la base de datos" + Style.RESET_ALL)
        pausar()
        return 0
   
   mostrar_listado_productos(lista_productos, "📦 TODOS LOS PRODUCTOS")
   pausar() 

   while True:
        try:
            id = int(input(mensaje))
            if id > 0:
                return id

            print("⚠️ Id no puede ser menor a 1")

        except ValueError:
            print("❌ Ingrese un Id valido.")



def getIdProducto():
   ''' 
   Solicitar el id de un producto para consultar en forma individual
   
   Parametro
   ---------
   
   Ninguno

   Retorna             
   -------
   Id - Entero - Identificacion del producto a consultar
   '''
   while True:
        try:
            id = int(input("Ingresar Id Producto a Buscar :"))
            if id > 0:
                return id

            print("⚠️ Id no puede ser menor a 1")

        except ValueError:
            print("❌ Ingrese un Id valido.")


