import mysql.connector
from mysql.connector import Error
from faker import Faker
import random

# Inicializar Faker
fake = Faker()

# Conectar a la base de datos MySQL
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

        # Definir posiciones y equipos aleatorios
        posiciones = ['Delantero', 'Centrocampista', 'Defensa', 'Portero']
        equipos = ['Equipo A', 'Equipo B', 'Equipo C', 'Equipo D']

        # Insertar datos aleatorios
        for _ in range(1000):  # Cambia el número si necesitas más registros
            nombre = fake.name()
            posicion = random.choice(posiciones)
            equipo = random.choice(equipos)
            fecha_nacimiento = fake.date_of_birth(minimum_age=18, maximum_age=40)

            # Inserta el registro en la tabla jugadores
            query = """
            INSERT INTO jugadores (nombre, posicion, equipo, fecha_nacimiento)
            VALUES (%s, %s, %s, %s);
            """
            values = (nombre, posicion, equipo, fecha_nacimiento)
            cursor.execute(query, values)
        
        # Confirmar la inserción de los datos
        connection.commit()
        print("Datos aleatorios insertados correctamente en la tabla jugadores")

except Error as e:
    print("Error al conectar a MySQL:", e)

finally:
    # Cerrar la conexión
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Conexión MySQL cerrada")
