# Cassandra vs MySQL: Comparación de Bases de Datos

Este repositorio contiene un análisis comparativo entre las bases de datos **Cassandra** y **MySQL**, incluyendo configuraciones prácticas con Docker Compose y un entorno de desarrollo gestionado por Conda.

---

## Contenido

- [Requisitos Previos](#requisitos-previos)
- [Configuración del Entorno Conda](#configuración-del-entorno-conda)
- [Ejecución de Docker Compose](#ejecución-de-docker-compose)
  - [Cassandra](#cassandra)
  - [MySQL](#mysql)

---

## Requisitos Previos

1. **Docker y Docker Compose**: Tener instalados [Docker](https://www.docker.com/) y [Docker Compose](https://docs.docker.com/compose/).
2. **Conda**: Instala [Miniconda](https://docs.conda.io/en/latest/miniconda.html) o [Anaconda](https://www.anaconda.com/).

---

## Configuración del Entorno Conda

El repositorio incluye un archivo `environment.yml` que define las dependencias necesarias para el entorno de trabajo. Para crear y activar el entorno:

1. **Crear el entorno**:
   ```bash
   conda env create -f environment.yml
2. **Activar el entonrno** :
     ```bash
     conda activate nombreDeTuEntorno
## Ejecución de Docker Compose
1. **Cassandra**: Para correr el contenedor de Cassandra primero te tendrás que situar donde esté situada el docker compose de cassandra y correrlo con el siguiente comando: 
    ```bash
   # Correr el contenedor
    docker-compose up --build 
    
    # Verificar que el contenedor esté en ejecución
    docker ps

  2.**MySQL**: Para correr el contenedor de Cassandra primero te tendrás que situar donde esté situada    el docker compose de mysql y correrlo con el siguiente comando: 
  ```bash 
     # Iniciar el contenedor de MySQL
     docker compose up --build

     # Verificar que el contenedor esté en ejecución
      docker ps



   
