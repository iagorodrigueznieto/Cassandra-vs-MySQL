import json
import uuid
from cassandra.cluster import Cluster


with open('jugadores.json', 'r') as file:
    datos = json.load(file)


CASSANDRA_HOSTS = ['127.0.0.1']  # Cambia esto a la IP o el dominio de tu clúster
KEYSPACE = 'ejercicio'          # Cambia esto por tu keyspace

a = Cluster(CASSANDRA_HOSTS)
session = a.connect()

session.set_keyspace(KEYSPACE)

for jugador in datos:
    id_jugador = uuid.uuid4()  # Crea un UUID único
    query = """
            INSERT INTO jugadores (id,nombre, posicion, equipo, fecha_nacimiento)
            VALUES (%s,%s, %s, %s, %s);
            """
    values = (id_jugador,jugador['nombre'], jugador['posicion'], jugador['equipo'], jugador['fecha_nacimiento'])
    session.execute(query, values)