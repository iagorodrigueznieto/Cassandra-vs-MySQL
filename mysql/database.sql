CREATE DATABASE IF NOT EXISTS ejercicio;

USE ejercicio;

CREATE TABLE jugadores (
id INT AUTO_INCREMENT PRIMARY KEY,
nombre VARCHAR(100) NOT NULL,
posicion VARCHAR(50),
equipo VARCHAR(100),
fecha_nacimiento DATE
);
