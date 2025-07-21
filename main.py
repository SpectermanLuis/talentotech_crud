#############################################
# CURSO - PROGRAMACION INICIAL CON PYTHON   #
# COMISION 25009                            #
# TP FINAL INTEGRADOR                       #
# ALUMNO : SPECTERMAN LUIS OMAR             #
#############################################

'''
MAIN.PY 

Modulo principal del sistema CRUD

'''

'''
Importar los distintos modulos
que se usaran en los procesos 
'''

from def_menus import *
from db_funciones import *
from utilidades import *
from ingreso_datos import *
from operaciones_producto import *

def main():

   '''
   Crear la base de datos y tabla productos si no existen

   '''
   if not bd_crear_tabla_productos():
       print("No se pudo iniciar correctamente la base de datos.")
       pausar()
       exit()  # 🛑 Sale del programa sin ejecutar los menús

   '''
   ciclo principal del programa 
   se van invocando los distintos menues 
   que se encuentran en def_menus.py
   '''   

   while True:

       '''
       Invocar al menu principal
       '''
       opcion_principal = pedir_opcion(
           "Selecciona una opción (1-3): ",
           [1, 2, 3],mostrar_menu_principal)

       opcion_principal = int(opcion_principal)

       match opcion_principal:
           case 1:

               while True:
                     '''
                     Invocal al menu movimientos
                     ''' 
                     opcion_movim = pedir_opcion(
                       "Selecciona una opción (1-5): ",
                       [1, 2, 3, 4, 5],mostrar_menu_movimientos)
                     opcion_movim = int(opcion_movim)
                     match opcion_movim:
                           case 1:
                              # ingresar producto nuevo
                              altaProducto()
                       
                           case 2:
                              # eliminar producto
                              eliminarProducto()

                           case 3:
                              # modificar producto todos los campos 
                              modificarProducto()


                           case 4:
                              # modificar producto campo especifico
                              modificarProductoPorCampo()

                           case 5:
                              # volver al menu principal
                              break


           case 2:

               while True:
                     '''
                     Invocar al menu consultas
                     ''' 
                     opcion_consulta = pedir_opcion(
                       "Selecciona una opción (1-4): ",
                       [1, 2, 3, 4],mostrar_menu_consultas)
                  
                     opcion_consulta = int(opcion_consulta)
                     match opcion_consulta:
                           case 1:
                              # visualizar todos los productos de la base de datos
                              lista_productos = bd_leer_productos()
                              mostrar_listado_productos(lista_productos, "📦 TODOS LOS PRODUCTOS")
                              pausar() 

                           case 2:
                              # Reporte de bajo stock
                              # capturamos el limite para la consulta
                              limite = int(input("Ingrese el límite para el reporte de bajo stock: "))
                              # la funcion bd_leer_prodcucto_bajo_stock(limite) nos retorna una lista con todos los productos cuyo campo cantidad es menor o igual a límite
                              lista_productos = bd_leer_producto_bajo_stock(limite)
                              # evaluamos e informamos
                              mostrar_listado_productos(lista_productos, f"PRODUCTOS CON STOCK MENOR O IGUAL A: {limite}")
                              pausar()


                           case 3:
                              # consulta y visualizacion de datos de un producto en particular
                              consultaProductoPorId()

                           case 4:
                              # volver al menu principal
                              break


           case 3:
               print("👋  Saliendo del programa. ¡Hasta luego!")
               break


# ✅ Punto de entrada
if __name__ == "__main__":
    main()