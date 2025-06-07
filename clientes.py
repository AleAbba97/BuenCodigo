clientes = {}
ultimo_id = 0

def generar_id():
    global ultimo_id
    ultimo_id += 1
    return ultimo_id

def agregar_cliente():
    nombre = input("Ingrese Nombre: ").strip()
    apellido = input("Ingrese Apellido: ").strip()
    dni = input("Ingrese DNI: ").strip()
    email = input("Ingrese Email: ").strip()

    if not nombre or not apellido or not dni or not email:
        print("❌ Todos los campos son obligatorios.")
        return

    # Verificamos que no haya otro cliente con ese DNI
    for cliente in clientes.values():
        if cliente["DNI"] == dni:
            print("❌ Ya existe un cliente con ese DNI.")
            return

    nuevo_id = generar_id()
    clientes[nuevo_id] = {
        "Nombre": nombre,
        "Apellido": apellido,
        "DNI": dni,
        "Email": email,
    }
    print(f"✅ Cliente agregado con ID: {nuevo_id}")
    insertar_cliente_bd(apellido, nombre, dni, email)

def modificar_cliente():
    print("=== Modificar cliente ===")
    id_cliente = int(input("Ingrese el ID del cliente a modificar: "))
    if id_cliente in clientes:
        cliente = clientes[id_cliente]
        print(f"Cliente actual: {cliente}")

        nuevo_nombre = input("Nuevo Nombre (dejar vacío para mantener): ").strip()
        nuevo_apellido = input("Nuevo Apellido (dejar vacío para mantener): ").strip()
        nuevo_email = input("Nuevo Email (dejar vacío para mantener): ").strip()

        if nuevo_nombre:
            cliente["Nombre"] = nuevo_nombre
        if nuevo_apellido:
            cliente["Apellido"] = nuevo_apellido
        if nuevo_email:
            cliente["Email"] = nuevo_email

        print("✅ Cliente modificado con éxito.")
    else:
        print("❌ No se encontró un cliente con ese ID.")

def eliminar_cliente():
    print("=== Eliminar cliente ===")
    id_cliente = int(input("Ingrese el ID del cliente a eliminar: "))
    if id_cliente in clientes:
        confirmacion = input(f"¿Está seguro de eliminar a {clientes[id_cliente]['Nombre']} {clientes[id_cliente]['Apellido']}? (s/n): ").lower()
        if confirmacion == 's':
            del clientes[id_cliente]
            print("✅ Cliente eliminado.")
        else:
            print("❎ Operación cancelada.")
    else:
        print("❌ No se encontró un cliente con ese ID.")

def ver_clientes():
    print("=== Lista de Clientes ===")
    if not clientes:
        print("No hay clientes registrados.")
    else:
        for id_cliente, datos in sorted(clientes.items()):
            print(f"ID: {id_cliente} | DNI: {datos['DNI']} | Nombre: {datos['Nombre']} {datos['Apellido']} | Email: {datos['Email']}")

import mysql.connector
from mysql.connector import Error

def insertar_cliente_bd(apellido, nombre, dni, email):
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',     
            password='1620',      
            database='skyroute_db'
        )
        cursor = conexion.cursor()
        sql = "INSERT INTO Cliente (apellido, nombre, dni, email) VALUES (%s, %s, %s, %s)"
        valores = (apellido, nombre, dni, email)
        cursor.execute(sql, valores)
        conexion.commit()
        print("✅ Cliente guardado en la base de datos.")
    except Error as e:
        print(f"❌ Error al insertar en la BD: {e}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()
