import mysql.connector
from mysql.connector import Error

def insertar_cliente(apellido, nombre, dni, email):
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',           # Cambiá si usás otro usuario
            password='',           # Poné tu contraseña si tenés
            database='skyroute_db'
        )

        if conexion.is_connected():
            cursor = conexion.cursor()
            sql = "INSERT INTO Cliente (apellido, nombre, dni, email) VALUES (%s, %s, %s, %s)"
            valores = (apellido, nombre, dni, email)
            cursor.execute(sql, valores)
            conexion.commit()
            print("✅ Cliente insertado correctamente.")

    except Error as e:
        print(f"❌ Error al insertar: {e}")

    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

