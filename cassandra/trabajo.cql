CREATE KEYSPACE IF NOT EXISTS ejercicio
WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};

USE ejercicio;

CREATE TABLE jugadores (
    id UUID PRIMARY KEY,
    nombre TEXT,
    posicion TEXT,
    equipo TEXT,
    fecha_nacimiento DATE
);
