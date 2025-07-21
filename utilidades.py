#####################################################
#                                                   #
# utilidades.py  -  funciones utilitarias generales #
#                                                   #
#####################################################

import os
from colorama import Fore, Style, init

def limpiar_pantalla():
    """
    Limpia la pantalla según el sistema operativo.
    
    Parametro
    ---------

    Ninguno

    Retorna
    -------

    No tiene retorno
    
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar(mensaje="Presiona ENTER para continuar..."):
    """
    Pausa la ejecución hasta que el usuario presione ENTER.

    Parametro
    ---------

    mensaje - Texto - Mensaje informativo , si no se ingresa nada , muestra un mensaje x defecto

    Retorna
    -------

    No tiene retorno
    
    """
    input(mensaje)

def pedir_opcion(mensaje, opciones_validas, mostrar_menu=None):
    """
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
    """
    while True:
        if mostrar_menu:
            limpiar_pantalla()
            mostrar_menu()
        opcion = input(mensaje).strip()
        if opcion.isdigit() and int(opcion) in opciones_validas:
            return int(opcion)
        print("❌ Opción inválida.")
        pausar()


def mostrar_listado_productos(lista_productos, titulo="Listado de productos"):
    '''
     Visualiza con formato una lista de productos 

     Parametros
     ----------

     lista_productos - Lista -  Lista con productos seleccionados desde la tabla productos

     titulo          - Texto -  Titulo que encabeza la lista visualizada                                   

    Retorna
    -------

    No tiene retorno. Solo visualiza la lista
     
    '''

    if not lista_productos:
        print(Fore.YELLOW + "⚠️  No hay productos para mostrar." + Style.RESET_ALL)
        return

    # Mostrar título centrado (opcional: rodeado de ===)
    ancho_total = 5 + 20 + 30 + 10 + 10 + 15
    print(Fore.MAGENTA + f"\n{titulo.center(ancho_total)}" + Style.RESET_ALL)
    print(Fore.MAGENTA + "=" * ancho_total + Style.RESET_ALL)

    # Títulos de las columnas
    titulos = ["ID", "Nombre", "Descripción", "Precio", "Cantidad", "Categoría"]
    anchos = [5, 20, 30, 10, 10, 15]

    encabezado = ""
    for titulo_col, ancho in zip(titulos, anchos):
        encabezado += Fore.CYAN + titulo_col.ljust(ancho)
    print(encabezado + Style.RESET_ALL)

    print("-" * ancho_total)

    for prod in lista_productos:
        id, nombre, desc, precio, cant, categ = prod
        fila = f"{str(id).ljust(5)}{nombre.ljust(20)}{desc.ljust(30)}"
        fila += f"{str(precio).rjust(10)}{str(cant).rjust(10)}{categ.ljust(15)}"
        print(Fore.GREEN + fila + Style.RESET_ALL)

def mostrar_producto(producto):
    '''
     Visualiza con formato los datos de un producto determinado 

     Parametros
     ----------

     producto - Diccionario -  Datos de un producto especifico obtenido de la tabla productos


    Retorna
    -------

    No tiene retorno. Solo visualiza los datos del producto con formato
     
    '''

    if not producto:
        print(Fore.YELLOW + "⚠️  No se encontró el producto." + Style.RESET_ALL)
        return

    print(Fore.MAGENTA + "\nInformación del producto".center(50, "=") + Style.RESET_ALL)
    
    print(Fore.CYAN + f"{'ID:':15}" + Style.RESET_ALL + f"{producto['id']}")
    print(Fore.CYAN + f"{'Nombre:':15}" + Style.RESET_ALL + f"{producto['nombre']}")
    print(Fore.CYAN + f"{'Descripción:':15}" + Style.RESET_ALL + f"{producto['descripcion']}")
    print(Fore.CYAN + f"{'Precio:':15}" + Style.RESET_ALL + f"${producto['precio']:.2f}")
    print(Fore.CYAN + f"{'Cantidad:':15}" + Style.RESET_ALL + f"{producto['cantidad']}")
    print(Fore.CYAN + f"{'Categoría:':15}" + Style.RESET_ALL + f"{producto['categoria']}")
    
    print(Fore.MAGENTA + "=" * 50 + Style.RESET_ALL)