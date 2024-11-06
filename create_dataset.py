import json
from faker import Faker
import random
import sys

# Inicializar Faker
fake = Faker()

# Comprobar si se pasa el número de inserciones por parámetro
if len(sys.argv) < 2:
    print('Debes pasar un número por parámetro')
    exit()

num_inserciones = int(sys.argv[1])

# Definir posiciones y equipos aleatorios
posiciones = ['Delantero', 'Centrocampista', 'Defensa', 'Portero']
equipos = ['Equipo A', 'Equipo B', 'Equipo C', 'Equipo D']

# Crear una lista para almacenar los datos generados
datos = []

# Generar datos aleatorios
for _ in range(num_inserciones):
    jugador = {
        "nombre": fake.name(),
        "posicion": random.choice(posiciones),
        "equipo": random.choice(equipos),
        "fecha_nacimiento": fake.date_of_birth(minimum_age=18, maximum_age=40).isoformat()
    }
    datos.append(jugador)

# Guardar los datos en un archivo JSON
with open('jugadores.json', 'w') as file:
    json.dump(datos, file, indent=4)

print(f"Datos generados y guardados en jugadores.json")
