import mysql.connector
from mysql.connector import Error
import json
import sys

# Cargar los datos generados desde el archivo JSON
with open('jugadores.json', 'r') as file:
    datos = json.load(file)

# Conectar a la base de datos MySQL e insertar datos
try:
    connection = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='root',
        database='ejercicio'
    )

    if connection.is_connected():
        print("Conexión exitosa a la base de datos MySQL")

        # Crear un cursor para ejecutar consultas SQL
        cursor = connection.cursor()

        # Insertar datos en la tabla jugadores
        for jugador in datos:
            query = """
            INSERT INTO jugadores (nombre, posicion, equipo, fecha_nacimiento)
            VALUES (%s, %s, %s, %s);
            """
            values = (jugador['nombre'], jugador['posicion'], jugador['equipo'], jugador['fecha_nacimiento'])
            cursor.execute(query, values)

        # Confirmar la inserción de los datos
        connection.commit()
        print(f"Datos insertados correctamente en la tabla jugadores")

except Error as e:
    print("Error al conectar a MySQL:", e)

finally:
    # Cerrar la conexión
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Conexión MySQL cerrada")

