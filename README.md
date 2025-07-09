# Proyecto de Gestión de Pacientes con Flask

Este es un proyecto para gestionar pacientes utilizando el framework **Flask** en Python. Permite registrar pacientes, buscar por ID, nombre o cédula, listar pacientes y manejar un error 404 en caso de URL no encontrada.

![Image](image.png)
---

## Descripción de Funcionalidades

El proyecto cuenta con las siguientes funcionalidades:

- **Registro de pacientes**: Permite registrar un nuevo paciente con su nombre, apellido, fecha de nacimiento, género y número de identificación.
- **Listado de pacientes**: Muestra una lista de todos los pacientes registrados.
- **Búsqueda de pacientes**: Permite buscar pacientes por **ID**, **nombre** o **cédula**.
- **Error 404**: Si el usuario intenta acceder a una página no existente, verá una página de error 404 personalizada.
- **Interfaz de usuario sencilla**: El frontend permite interactuar de manera fácil con los formularios para registrar y buscar pacientes.

---

## Requisitos

Antes de comenzar, asegúrate de tener lo siguiente instalado en tu sistema:

- **Python 3.7 o superior**
- **Pip** (para instalar dependencias)

---

## Instrucciones de Instalación

Sigue estos pasos para instalar el proyecto en tu máquina local:

### 1. Clona el repositorio

Primero, clona el repositorio a tu máquina local:

`` git clone https://github.com/tu-usuario/gestion-pacientes-flask.git ``

### 2. Navega al directorio del proyecto

En la terminal, navega al directorio del proyecto:

`` cd gestion-pacientes-flask ``

### 3. Crea un entorno virtual

Para evitar conflictos con otras dependencias, crea un entorno virtual:

`` python -m venv venv ``

### 4. Activa el entorno virtual

`` venv\Scripts\activate ``

### 5. Instala los requerimientos

Con el entorno virtual activado, instala las dependencias necesarias desde el archivo requirements.txt:

`` pip install -r requirements.txt ``

Este comando instalará todas las dependencias necesarias para ejecutar el proyecto, como Flask y otras bibliotecas necesarias.

---

## Instrucciones de Ejecución

Una vez instaladas las dependencias, puedes ejecutar la aplicación localmente

### 1. Inicia el servidor Flask

Para ejecutar la aplicación, usa el siguiente comando:

`` python app.py ``

### 2. Abre la aplicación en tu navegador

Accede a la siguiente URL en tu navegador para interactuar con la aplicación:

`` http://127.0.0.1:5000/ ``

