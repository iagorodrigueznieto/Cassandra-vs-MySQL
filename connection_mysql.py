import mysql.connector
import time
from mysql.connector import Error

try:
    # Establece la conexión con la base de datos
    connection = mysql.connector.connect(
        host='127.0.0.1',     # O usa 'localhost'
        port=3306,            # Puerto expuesto por Docker
        user='root',          # Usuario de MySQL (cambia si usaste otro)
        password='root',  # Contraseña del usuario (ajusta a la tuya)
        database='ejercicio' # Nombre de la base de datos
    )
    
    if connection.is_connected():
        print("Conexión exitosa a la base de datos MySQL")

        # Crear un cursor para ejecutar consultas SQL
        cursor = connection.cursor()
        
        start_time = time.time()
        # Ejemplo de consulta: Selecciona todos los jugadores
        cursor.execute("SELECT * FROM jugadores;")
        rows = cursor.fetchall()

        end_time = time.time()


        execution_time = end_time - start_time
        print("El tiempo de consulta ha sido: ",execution_time)
        print("Datos en la tabla jugadores:")
        for row in rows:
            print(row)

except Error as e:
    print("Error al conectar a MySQL:", e)

finally:
    # Cierra la conexión
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("Conexión MySQL cerrada")
