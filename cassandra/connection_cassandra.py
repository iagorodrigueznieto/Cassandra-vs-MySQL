import time
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from uuid import UUID

# Función para conectar a Cassandra
def conectar_cassandra():
    cluster = Cluster(['localhost'])  # Cambia esto si tu Cassandra está en otro servidor
    session = cluster.connect()
    session.set_keyspace('ejercicio')
    return session

# Función para consultar todos los jugadores
def consultar_jugadores(session):
    start_time = time.time()  # Iniciar el temporizador
    
    # Consulta para obtener todos los jugadores
    query = "SELECT * FROM jugadores ALLOW FILTERING"
    rows = session.execute(query)

    # Calcular el tiempo de ejecución
    elapsed_time = time.time() - start_time
    print(f"Tiempo de ejecución de la consulta (todos los jugadores): {elapsed_time:.4f} segundos")

    # Imprimir los resultados
    for row in rows:
        print(f"ID: {row.id}, Nombre: {row.nombre}, Posición: {row.posicion}, Equipo: {row.equipo}, Fecha Nacimiento: {row.fecha_nacimiento}")

# Función para consultar un jugador específico por nombre
def consultar_jugador_por_nombre(session, nombre):
    start_time = time.time()  # Iniciar el temporizador
    
    query = "SELECT * FROM jugadores WHERE nombre = %s ALLOW FILTERING"
    rows = session.execute(query, (nombre,))

    # Calcular el tiempo de ejecución
    elapsed_time = time.time() - start_time
    print(f"Tiempo de ejecución de la consulta (jugador {nombre}): {elapsed_time:.4f} segundos")

    # Imprimir los resultados
    for row in rows:
        print(f"ID: {row.id}, Nombre: {row.nombre}, Posición: {row.posicion}, Equipo: {row.equipo}, Fecha Nacimiento: {row.fecha_nacimiento}")

# Función principal
if __name__ == "__main__":
    # Conectar a Cassandra
    session = conectar_cassandra()

    # Consultar todos los jugadores
    print("Consultando todos los jugadores:")
    consultar_jugadores(session)

    # Consultar un jugador por nombre (ejemplo: 'Lionel Messi')
    print("\nConsultando jugador por nombre (Lionel Messi):")
    consultar_jugador_por_nombre(session, 'Lionel Messi')

