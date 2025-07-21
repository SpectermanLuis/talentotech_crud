##################################################
#                                                #
# def_menus.py - Funciones para visualizar los   #
#                distintos menus del sistema     #
#                                                #
##################################################

def mostrar_menu_principal():
    '''
    Visualizar las opciones del menu principal del sistema

    Parametros
    ----------
    
    Ninguno

    
    Retorno
    -------
    No retorna nada
    
    '''
    
    print("\n" * 2)
    print("\n=== 📦 MENÚ PRINCIPAL 📦 ===")
    print("1. Movimientos")
    print("2. Consultas")
    print("3. Salir")


def mostrar_menu_movimientos():
    '''
    Visualizar las opciones del submenu de movimientos del sistema

    Parametros
    ----------
    
    Ninguno

    
    Retorno
    -------
    No retorna nada
    
    '''

    print("\n" * 2)
    print("\n=== 📦 SUBMENU MOVIMIENTOS 📦 ===")
    print("1. Ingresar  Producto")
    print("2. Eliminar  Producto")
    print("3. Modificar Producto ( Version reingreso todos los campos) ")
    print("4. Modificar Producto ( Version campo x campo) ")
    print("5. Volver al Menu Principal")


def mostrar_menu_consultas():
    '''
    Visualizar las opciones del submenu de consultas del sistema

    Parametros
    ----------
    
    Ninguno

    
    Retorno
    -------
    No retorna nada
    
    '''

    print("\n" * 2)
    print("\n=== 📦 SUBMENU CONSULTAS 📦 ===")
    print("1. Consulta Todos los Productos")
    print("2. Consulta Productos Bajo Stock")
    print("3. Consulta Producto x Codigo")
    print("4. Volver al Menu Principal")
