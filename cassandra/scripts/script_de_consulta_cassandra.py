import time
from cassandra.cluster import Cluster


# Configura los detalles de conexión
CASSANDRA_HOSTS = ['127.0.0.1']  # Cambia esto a la IP o el dominio de tu clúster
KEYSPACE = 'ejercicio'          # Cambia esto por tu keyspace

# Conectar al clúster de Cassandra sin autenticación
a = Cluster(CASSANDRA_HOSTS)
session = a.connect()

# Establecer el keyspace
session.set_keyspace(KEYSPACE)

start_time = time.time()  # Marca el tiempo de inicio

# Ejecutar la consulta
query = "SELECT * FROM jugadores LIMIT 5;"
rows = session.execute(query)

end_time = time.time()


execution_time = end_time - start_time

print("La consulta ha tardado: ",execution_time)


# Mostrar resultados
for row in rows:
    print(row)

# Cerrar la conexión
a.shutdown()