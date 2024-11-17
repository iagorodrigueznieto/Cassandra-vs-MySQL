import json
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from uuid import uuid4
from datetime import datetime

# Configuración de conexión con Cassandra
def conectar_cassandra():
    # Aquí se asume que tienes acceso a Cassandra de manera local o en la red
    cluster = Cluster(['localhost'])  # Cambia esto si tu Cassandra está en otro servidor
    session = cluster.connect()
    session.set_keyspace('ejercicio')
    return session

# Función para insertar un jugador en la base de datos
def insertar_jugador(session, jugador):
    # Insertar los datos en la tabla 'jugadores'
    query = """
    INSERT INTO jugadores (id, nombre, posicion, equipo, fecha_nacimiento)
    VALUES (%s, %s, %s, %s, %s)
    """
    # Convertir la fecha de nacimiento de string a un objeto de fecha
    fecha_nacimiento = datetime.strptime(jugador['fecha_nacimiento'], '%Y-%m-%d').date()
    
    # Ejecutar la consulta con los valores
    session.execute(query, (uuid4(), jugador['nombre'], jugador['posicion'], jugador['equipo'], fecha_nacimiento))

# Función para leer el archivo JSON y procesar los jugadores
def procesar_json(json_data):
    session = conectar_cassandra()

    for jugador in json_data:
        insertar_jugador(session, jugador)

    print("Datos insertados correctamente.")

# Ejemplo de cómo podrías usar el script
if __name__ == "__main__":
    # Cargar el archivo JSON con la información de los jugadores
    with open('jugadores.json', 'r') as f:
        jugadores_json = json.load(f)

    # Procesar e insertar los jugadores
    procesar_json(jugadores_json)
