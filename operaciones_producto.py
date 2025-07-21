#############################################################################################
#                                                                                           #
#  operaciones_producto.py  - Operaciones basicas del CRUD contectando el ingreso de datos  #
#                              desde ingreso_datos.py  y la conexcion a la base de datos    #
#                              desde db_funciones.py                                        #
#                                                                                           #
#############################################################################################                   


from ingreso_datos import *

# Función local que maneja el proceso de alta de producto
def altaProducto():
    '''
    Procesos para el alta de un producto  
    Solicita ingresar los datos del producto
    Insertarlos en la tabla productos

    Parametro
    ---------

    Ninguno

    Retorna
    -------
    
    Mensaje de exito o error al insertar
        
    '''

    nombre      = getNombre()
    descripcion = getDescripcion()
    categoria   = getCategoria()
    precio      = getPrecio()
    cantidad    = getCantidad()
    resultado   = bd_insertar_producto(nombre,descripcion, categoria, precio,  cantidad)
    if resultado:
        print("✅ Registro insertado exitosamente!")
        pausar()
    else:
        print("❌Error : Algo fallo al insertar")


# Eliminar un producto específico
def eliminarProducto():
    '''
    Proceso para la eliminacion de un producto
    Solicita ingresar el id de un producto desde una lista de todos los productos
    Eliminar producto de la tabla productos

    Parametro
    ---------

    Ninguno

    Retorna
    -------
    
    Mensaje de exito o error al insertar
        
    '''


    # El usuario ingresa el id del producto a eliminar
    id = getIdProductoBaseLista("Ingresar Id Producto a Eliminar :")

    # verificar si existe el id en la base
    producto = bd_leer_producto_por_id(id)
    
    if producto is None:
        print("❌Error: No existe un producto con ese ID.")
        pausar()
        return  

    # eliminamos el producto con ese id
    resultado  = bd_eliminar_producto(id)

    # evaluamos el retorno e informamos
    if resultado:
        print("✅ Registro eliminado.")
        pausar()
    else:
        print("❌Error: algo fallo al eliminar.")

def modificarProducto():
    '''
    Modificar datos de un producto existente 
    Solicita ingresar los datos del producto seleccionando el id desde una lista de todos los productos
    Solicata todos los campos para modificar 

    Parametro
    ---------

    Ninguno

    Retorna
    -------
    
    Mensaje de exito o error al actualizar
        
    '''


    # El usuario ingresa el id del producto a eliminar
    id = getIdProductoBaseLista("Ingresar Id Producto a Modificar :")

    # verificar si existe el id en la base
    producto = bd_leer_producto_por_id(id)
    
    if producto is None:
        print("❌Error: No existe un producto con ese ID.")
        pausar()
        return  

    
    nombre      = getNombre()
    descripcion = getDescripcion()
    categoria   = getCategoria()
    precio      = getPrecio()
    cantidad    = getCantidad()
    resultado   = bd_modificar_producto(id,nombre,descripcion, categoria, precio,  cantidad)

    # evaluamos el retorno e informamos
    if resultado:
        print("✅ Registro Actualizado OK.")
        pausar()
    else:
        print("❌Error: algo fallo al modificar.")


def consultaProductoPorId():
    '''
    Consultar los datos de un producto especifico
    Solicita ingresar el id de un producto

    Parametro
    ---------

    Ninguno

    Retorna
    -------
    
    En caso de existir el producto , muestra los datos del mismo en la consola
        
    '''

    # El usuario ingresa el id del producto a eliminar
    id = getIdProducto()

    # verificar si existe el id en la base
    producto = bd_leer_producto_por_id(id)
    
    if producto is None:
        print("❌Error: No existe un producto con ese ID.")
        pausar()
        return  
   
    mostrar_producto(producto)
    pausar() 

def modificarProductoPorCampo():
    '''
    Moficar los datos de un producto seleccionado solo de los campos necesarios , no siendo 
    necesario volver a ingresar los mismos como sucede en modificarProducto()
    Solicita ingresar el id de un producto previa visualizacion de una lista de todos los productos
    Solicita campo por campo el valor a modificar , en caso de no modicar se pasa la solicitud 
    con enter dejando el campo vacio , indicando que se mantiene el valor anterior

    Parametro
    ---------

    Ninguno

    Retorna
    -------
    
    Mensaje de actualizacion Ok o en caso de error , mensaje indicando esa situacion

        
    '''
    id = getIdProductoBaseLista("Ingresar Id Producto a Modificar :")

    producto = bd_leer_producto_por_id(id)
    if producto is None:
        print("Error: No existe un producto con ese ID.")
        pausar()
        return

    print("\n--- Datos actuales del producto ---")
    print(f"Nombre: {producto['nombre']}")
    print(f"Descripción: {producto['descripcion']}")
    print(f"Categoría: {producto['categoria']}")
    print(f"Precio: {producto['precio']}")
    print(f"Cantidad: {producto['cantidad']}")
    print("-----------------------------------\n")

    # Pedimos al usuario si quiere modificar cada campo
    nombre = getNombreConVacio("Nuevo nombre (Enter para mantener '{producto['nombre']}'): ")
    if nombre == "":
        nombre = producto['nombre']

    descripcion = getDescripcionConVacio("Nueva descripcion (Enter para mantener '{producto['descripcion']}'): ")
    if descripcion == "":
        descripcion = producto['descripcion']

    categoria = getCategoriaConVacio("Nueva Categoria (Enter para mantener '{producto['categoria']}'): ")
    if categoria == "":
        categoria = producto['categoria']

    precio_txt = getPrecioConVacio("Nuevo precio (Enter para mantener '{producto['precio']}'): ")
    if precio_txt == "":
        precio = producto['precio']
    else:
        precio = float(precio_txt)

    cantidad_txt = getCantidadConVacio("Nueva cantidad (Enter para mantener '{producto['cantidad']}'): ")
    if cantidad_txt == "":
        cantidad = producto['cantidad']
    else:
        cantidad = int(cantidad_txt)

    # Llamamos a la función que actualiza
    resultado = bd_modificar_producto(id, nombre, descripcion, categoria, precio, cantidad)

    if resultado:
        print("✅ Registro actualizado correctamente.")
    else:
        print("❌ Error: algo falló al modificar.")
    pausar()
