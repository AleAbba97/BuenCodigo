from clientes import agregar_cliente, modificar_cliente, eliminar_cliente, ver_clientes, clientes
from destinos import agregar_destino, modificar_destino, eliminar_destino, ver_destinos, destinos
from ventas import crear_venta, consultar_ventas, boton_arrepentimiento


def mostrar_menu_principal():
    """Muestra el menú principal del sistema."""
    menu = """
Bienvenidos a SkyRoute - Sistema de Gestión de Pasajes

1. Gestionar Clientes
2. Gestionar Destinos
3. Gestionar Ventas
4. Botón de Arrepentimiento
5. Salir

"""
    print(menu)

def mostrar_submenu_clientes():
    """Gestión de clientes."""
    submenu = """
--- Gestionar Clientes ---
1. Agregar Cliente
2. Modificar Cliente
3. Eliminar Cliente
4. Ver Clientes
5. Volver al Menú Principal
-----------------------------------
"""
    print(submenu)

def mostrar_submenu_destinos():
    """Gestión de destinos."""
    submenu = """
--- Gestionar Destinos ---
1. Agregar Destino
2. Modificar Destino
3. Eliminar Destino
4. Ver Destinos
5. Volver al Menú Principal
-----------------------------------
"""
    print (submenu)

def mostrar_submenu_ventas():
    """Gestión de ventas."""
    submenu = """
--- Gestionar ventas ---
1. Registrar venta
2. Consultar Venta
3. Volver al Menú Principal
-----------------------------------
"""
    print (submenu)

def Gestiones():
    while True:
        mostrar_menu_principal()
        opcion_principal = input("Ingrese una opción del menú principal: ")

        if opcion_principal == '1':
            while True:
                mostrar_submenu_clientes()
                opcion_clientes = input("Ingrese una opción del submenú de clientes: ")
                if opcion_clientes == '1':
                    agregar_cliente()
                elif opcion_clientes == '2':
                    modificar_cliente()
                elif opcion_clientes == '3':
                    eliminar_cliente()
                elif opcion_clientes == '4':
                    ver_clientes()
                elif opcion_clientes == '5':
                    print("Volviendo al menú principal...")
                    break  
                else:  
                    print("Opción inválida. Por favor, intente de nuevo.")

        elif opcion_principal == '2':
            while True:
                mostrar_submenu_destinos()
                opcion_destinos = input("Ingrese una opción del submenú de destinos: ")
                if opcion_destinos == '1':
                    agregar_destino()
                elif opcion_destinos == '2':
                    modificar_destino()
                elif opcion_destinos == '3':
                    eliminar_destino()
                elif opcion_destinos == '4':
                    ver_destinos()
                elif opcion_destinos == '5':
                    print("Volviendo al menú principal...")
                    break 
                else:
                    print("Opción inválida. Por favor, intente de nuevo.")
        elif opcion_principal == '3':
            while True:
                mostrar_submenu_ventas()
                opcion_ventas = input("Ingrese una opcion del submenu de ventas: ")
                if opcion_ventas == '1':
                    crear_venta(clientes, destinos)
                elif opcion_ventas == '2':
                    consultar_ventas()
                elif opcion_ventas == '3':
                    print("Volviendo al menú principal...")
                    break 
                else:
                    print("Opción inválida. Por favor, intente de nuevo.")
        elif opcion_principal == '4':
            boton_arrepentimiento()
        elif opcion_principal == '5':
            print("¡Gracias por usar SkyRoute! Saliendo del sistema.")
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")
 
        if opcion_principal != '6': 
            input("\nPresione Enter para continuar")
            print("\n" * 2) 
Gestiones()