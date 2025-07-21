#  TALENTO TECH  - CURSO PYTHON 
#  AÑO 2025
#  DOCENTE  -  GRISELDA MEDINA 

## ALUMNO : SPECTERMAN LUIS OMAR     

## DNI :  14.620.696

### TP FINAL CRUD 

### Consigna
Crear un CRUD 

Funcionalidades de la aplicación
- La aplicación debe permitir:
- Registrar nuevos productos.
- Visualizar datos de los productos registrados.
- Actualizar datos de productos, mediante su ID.
- Eliminación de productos, mediante su ID.
- Búsqueda de productos, mediante su ID. De manera
  opcional, se puede implementar la búsqueda por los
  campos nombre o categoría.
- Reporte de productos que tengan una cantidad igual o
  inferior a un límite especificado por el usuario o usuaria


### 🔧 Tecnologías Usadas

- 🐍 Python 3.12.5 
- 🔹 Sqlite3         ( incluido en Python)
- 💻 Git & GitHub    ( control de versiones )
- 🖥️ Visual Studio Code ( editor de codigo)
---


#### Estructura de directorios
``` tree
    ├── inventario.db      ( base de datos Sqlite )
    │  
    ├── main.py            ( archivo principal del crud)
    ├── utilidades.py      ( funciones de utilidad varias usadas en el sistema)
    ├── def_menus.py       ( definicion del menu principal y los distintos submenues)
    ├── db_funciones.py    ( funciones que permiten la comunicacion y operaciones con la base de datos)
    ├── ingreso_datos.py   ( interfases para comunicarse con el usurio )
    │
    └── README.md          ( el presente archivo README.MD con la descripcion del sistema) 
```

## 🧱 Estructura de la base de datos 

```
        sql = """CREATE TABLE IF NOT EXISTS "productos" (
            "id" INTEGER,                      identificacion del producto 
            "nombre" TEXT NOT NULL,            nombre del producto 
            "descripcion" TEXT NOT NULL,       descripcion del producto
            "categoria" TEXT NOT NULL,         categoria del producto
            "precio" REAL NOT NULL,            precio del producto
            "cantidad" INTEGER NOT NULL,       cantidad del producto
            PRIMARY KEY("id" AUTOINCREMENT)

```



### 📂 Descripcion de Cada Modulo y sus funciones

- [`main.py`](#mainpy) — archivo principal del CRUD
- [`utilidades.py`](#utilidadespy) — funciones de utilidad general
- [`def_menus.py`](#def_menuspy) — definición del menú principal y submenús
- [`db_funciones.py`](#db_funcionespy) — funciones para la base de datos
- [`ingreso_datos.py`](#ingreso_datospy) — interfaz de usuario por consola
- [`operaciones_producto.py`](#operaciones_productopy) — procesos del crud


---
---
---

# main.py     

<a id="main.main"></a>

#### main

```python
def main()
```

Crear la base de datos y tabla productos si no existen
Invocar a los distintos menus y opciones del sistema


---
---
---

# utilidades.py


<a id="utilidades.limpiar_pantalla"></a>

#### limpiar\_pantalla

```python
def limpiar_pantalla()
```

Limpia la pantalla según el sistema operativo.

Parametro
---------

Ninguno

Retorna
-------

No tiene retorno

<a id="utilidades.pausar"></a>

#### pausar

```python
def pausar(mensaje="Presiona ENTER para continuar...")
```

Pausa la ejecución hasta que el usuario presione ENTER.

Parametro
---------

mensaje - Texto - Mensaje informativo , si no se ingresa nada , muestra un mensaje x defecto

Retorna
-------

No tiene retorno

<a id="utilidades.pedir_opcion"></a>

#### pedir\_opcion

```python
def pedir_opcion(mensaje, opciones_validas, mostrar_menu=None)
```

Solicita al usuario que ingrese una opción válida.
 Usada para las opciones de cada menu

Parametros
----------

- mensaje: el mensaje para el input.
- opciones_validas: una lista de opciones aceptadas (ej. [1, 2, 3]).
  Seran las opciones del menu especificado
- mostrar_menu: función opcional con las opciones del menu se vuelve a mostrar si hay error.


Retorna
-------

Devuelve el valor convertido a int.

<a id="utilidades.mostrar_listado_productos"></a>

#### mostrar\_listado\_productos

```python
def mostrar_listado_productos(lista_productos, titulo="Listado de productos")
```

Visualiza con formato una lista de productos

 Parametros
 ----------

 lista_productos - Lista -  Lista con productos seleccionados desde la tabla productos

 titulo          - Texto -  Titulo que encabeza la lista visualizada

Retorna
-------

No tiene retorno. Solo visualiza la lista

<a id="utilidades.mostrar_producto"></a>

#### mostrar\_producto

```python
def mostrar_producto(producto)
```

Visualiza con formato los datos de un producto determinado

 Parametros
 ----------

 producto - Diccionario -  Datos de un producto especifico obtenido de la tabla productos


Retorna
-------

No tiene retorno. Solo visualiza los datos del producto con formato




---
---
---
# def_menus.py

<a id="def_menus.mostrar_menu_principal"></a>

#### mostrar\_menu\_principal

```python
def mostrar_menu_principal()
```

Visualizar las opciones del menu principal del sistema

Parametros
----------

Ninguno


Retorno
-------
No retorna nada

<a id="def_menus.mostrar_menu_movimientos"></a>

#### mostrar\_menu\_movimientos

```python
def mostrar_menu_movimientos()
```

Visualizar las opciones del submenu de movimientos del sistema

Parametros
----------

Ninguno


Retorno
-------
No retorna nada

<a id="def_menus.mostrar_menu_consultas"></a>

#### mostrar\_menu\_consultas

```python
def mostrar_menu_consultas()
```

Visualizar las opciones del submenu de consultas del sistema

Parametros
----------

Ninguno


Retorno
-------
No retorna nada


---
---
---

# db_funciones.py


<a id="db_funciones.bd_crear_tabla_productos"></a>

#### bd\_crear\_tabla\_productos

```python
def bd_crear_tabla_productos()
```

Crear la tabla productos en la base de datos inventario
Verifica si no existe previamente sino la crea

Parametros
----------

Ninguno

Retorno
-------

True  = Creo la tabla correctamente

False = Hubo algun problema al crear la tabla

<a id="db_funciones.bd_leer_productos"></a>

#### bd\_leer\_productos

```python
def bd_leer_productos()
```

Obtener todos los productos de la base de datos

Parametros
----------

Ninguno

Retorno
-------

Lista con todos los productos de la tabla productos de la base de datos inventario

Si hubo algun problema la lista estara vacia

<a id="db_funciones.bd_leer_producto_por_id"></a>

#### bd\_leer\_producto\_por\_id

```python
def bd_leer_producto_por_id(id)
```

Obtener los datos de un producto especifico

Parametros
----------

id - numero identificacion del producto a buscar


Retorno
-------

Diccionario con los datos del producto indicado en el parametro ID

Si hubo algun problema retornara un diccionario vacio

<a id="db_funciones.bd_insertar_producto"></a>

#### bd\_insertar\_producto

```python
def bd_insertar_producto(nombre, descripcion, categoria, precio, cantidad)
```

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

<a id="db_funciones.bd_leer_producto_bajo_stock"></a>

#### bd\_leer\_producto\_bajo\_stock

```python
def bd_leer_producto_bajo_stock(limite)
```

Devuelve los productos de la tabla que se encuentren bajo el nivel de cantidad de stock
indicada en el parametro limite

Parametros
----------

limite      - Entero - Valor limite para control cantidades de producto que esten bajo ese valor        


Retorno
-------

Lista con los productos que cumplan con la condicion menor al parametro limite

En caso que ningun producto la cumpla , la lista estara vacia

<a id="db_funciones.bd_eliminar_producto"></a>

#### bd\_eliminar\_producto

```python
def bd_eliminar_producto(id)
```

Eliminar un producto de la tabla productos en base a un valor de id pasado por parametro

Parametros
----------

id    - Entero - Identificacion del producto a eliminar

Retorno
-------

True  - Se elimino correctamente el registro de la tabla productos

False - No se pudo eliminar el registro de la tabla productos

<a id="db_funciones.bd_modificar_producto"></a>

#### bd\_modificar\_producto

```python
def bd_modificar_producto(id, nombre, descripcion, categoria, precio,
                          cantidad)
```

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


---
---
---

# ingreso_datos.py


<a id="ingreso_datos.getNombre"></a>

#### getNombre

```python
def getNombre(mensaje="Ingrese el nombre del producto: ")
```

Solicita ingresar nombre del producto ( ingreso / actualizacion x todos los campos)
Validaciones basicas , que no este vacio y que tenga una longitud minima

Parametro
---------

mensaje - Texto - Mensaje a usar en el input del campo , teniendo un valor por defecto

Retorna
-------

nombre - Nombre del producto

<a id="ingreso_datos.getNombreConVacio"></a>

#### getNombreConVacio

```python
def getNombreConVacio(mensaje="Ingrese nombre del producto: ")
```

Solicita ingresar nombre del producto ( en caso de actualizacion por campo especifico)
Validaciones basicas en caso que se ingrese un valor , que tenga una longitud minima

Parametro
---------

mensaje - Texto - Mensaje a usar en el input del campo , teniendo un valor por defecto

Retorna
-------

nombre - Nombre del producto si es que se modifica el campo
         Vacio si se va a mantener el mismo valor anterior

<a id="ingreso_datos.getDescripcion"></a>

#### getDescripcion

```python
def getDescripcion(mensaje="Ingrese descripcion del producto: ")
```

Solicita ingresar descripcion del producto ( ingreso / actualizacion x todos los campos)
Validaciones basicas , que no este vacio y que tenga una longitud minima

Parametro
---------

mensaje - Texto - Mensaje a usar en el input del campo , teniendo un valor por defecto

Retorna
-------

descripcion - descripcion del producto

<a id="ingreso_datos.getDescripcionConVacio"></a>

#### getDescripcionConVacio

```python
def getDescripcionConVacio(mensaje="Ingrese descripcion del producto: ")
```

Solicita ingresar descripcion del producto ( en caso de actualizacion por campo especifico)
Validaciones basicas en caso que se ingrese un valor , que tenga una longitud minima

Parametro
---------

mensaje - Texto - Mensaje a usar en el input del campo , teniendo un valor por defecto

Retorna
-------

descripcion - Descripcion del producto si es que se modifica el campo
              Vacio si se va a mantener el mismo valor anterior

<a id="ingreso_datos.getCategoria"></a>

#### getCategoria

```python
def getCategoria(mensaje="Ingrese categoria del producto: ")
```

Solicita ingresar categoria del producto ( ingreso / actualizacion x todos los campos)
Validaciones basicas , que no este vacio y que tenga una longitud minima

Parametro
---------

mensaje - Texto - Mensaje a usar en el input del campo , teniendo un valor por defecto

Retorna
-------

categoria - Categoria del producto

<a id="ingreso_datos.getCategoriaConVacio"></a>

#### getCategoriaConVacio

```python
def getCategoriaConVacio(mensaje="Ingrese categoria del producto: ")
```

Solicita ingresar categoria del producto ( en caso de actualizacion por campo especifico)
Validaciones basicas en caso que se ingrese un valor , que tenga una longitud minima

Parametro
---------

mensaje - Texto - Mensaje a usar en el input del campo , teniendo un valor por defecto

Retorna
-------

categoria - Categoria del producto si es que se modifica el campo
            Vacio si se va a mantener el mismo valor anterior

<a id="ingreso_datos.getPrecio"></a>

#### getPrecio

```python
def getPrecio(mensaje="💲 Ingrese el *precio* del producto: ")
```

Solicita ingresar precio del producto ( ingreso / actualizacion x todos los campos)
Validaciones basicas , que sea un numero valido , no cero ni negativo

Parametro
---------

mensaje - Texto - Mensaje a usar en el input del campo , teniendo un valor por defecto

Retorna
-------

precio - Float - Precio del producto

<a id="ingreso_datos.getPrecioConVacio"></a>

#### getPrecioConVacio

```python
def getPrecioConVacio(mensaje="💲 Ingrese el *precio* del producto: ")
```

Solicita ingresar precio del producto ( en caso de actualizacion por campo especifico)
Validaciones basicas en caso que se ingrese un valor , que sea numero valido no cero ni negativo        

Parametro
---------

mensaje - Texto - Mensaje a usar en el input del campo , teniendo un valor por defecto

Retorna
-------

precio  - Precio del producto si es que se modifica el campo
          Vacio si se va a mantener el mismo valor anterior

<a id="ingreso_datos.getCantidad"></a>

#### getCantidad

```python
def getCantidad(mensaje="📦 Ingrese cantidad disponible: ")
```

Solicita ingresar cantidad del producto ( ingreso / actualizacion x todos los campos)
Validaciones basicas , que sea un numero valido , no cero ni negativo

Parametro
---------

mensaje - Texto - Mensaje a usar en el input del campo , teniendo un valor por defecto

Retorna
-------

cantidad - Entero - Cantidad del producto

<a id="ingreso_datos.getCantidadConVacio"></a>

#### getCantidadConVacio

```python
def getCantidadConVacio(mensaje="📦 Ingrese cantidad disponible: ")
```

Solicita ingresar cantidad del producto ( en caso de actualizacion por campo especifico)
Validaciones basicas en caso que se ingrese un valor , que sea numero valido no cero ni negativo        

Parametro
---------

mensaje - Texto - Mensaje a usar en el input del campo , teniendo un valor por defecto

Retorna
-------

cantidad - Cantidad del producto si es que se modifica el campo
           Vacio si se va a mantener el mismo valor anterior

<a id="ingreso_datos.getIdProductoBaseLista"></a>

#### getIdProductoBaseLista

```python
def getIdProductoBaseLista(mensaje)
```

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

<a id="ingreso_datos.getIdProducto"></a>

#### getIdProducto

```python
def getIdProducto()
```

Solicitar el id de un producto para consultar en forma individual

Parametro
---------

Ninguno

Retorna
-------
Id - Entero - Identificacion del producto a consultar



---
---
---

# operaciones_producto.py

<a id="operaciones_producto.altaProducto"></a>

#### altaProducto

```python
def altaProducto()
```

Procesos para el alta de un producto
Solicita ingresar los datos del producto
Insertarlos en la tabla productos

Parametro
---------

Ninguno

Retorna
-------

Mensaje de exito o error al insertar

<a id="operaciones_producto.eliminarProducto"></a>

#### eliminarProducto

```python
def eliminarProducto()
```

Proceso para la eliminacion de un producto
Solicita ingresar el id de un producto desde una lista de todos los productos
Eliminar producto de la tabla productos

Parametro
---------

Ninguno

Retorna
-------

Mensaje de exito o error al insertar

<a id="operaciones_producto.modificarProducto"></a>

#### modificarProducto

```python
def modificarProducto()
```

Modificar datos de un producto existente 
Solicita ingresar los datos del producto seleccionando el id desde una lista de todos los productos     
Solicata todos los campos para modificar

Parametro
---------

Ninguno

Retorna
-------

Mensaje de exito o error al actualizar

<a id="operaciones_producto.consultaProductoPorId"></a>

#### consultaProductoPorId

```python
def consultaProductoPorId()
```

Consultar los datos de un producto especifico
Solicita ingresar el id de un producto

Parametro
---------

Ninguno

Retorna
-------

En caso de existir el producto , muestra los datos del mismo en la consola

<a id="operaciones_producto.modificarProductoPorCampo"></a>

#### modificarProductoPorCampo

```python
def modificarProductoPorCampo()
```

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

---
---
---