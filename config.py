import mysql.connector
from mysql.connector import Error

conexion = mysql.connector.connect(
            host='localhost',      
            user='root',     
            password='1620', 
            database='skyroute_db' 
)

if conexion.is_connected():
    print("✅ Conexión exitosa a skyroute_db")