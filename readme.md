# Piedra Papel Tijera

Piedra Papel Tijera es un juego web basado en el clásico juego de Rock-Paper-Scissors, implementado en Django. Los usuarios pueden jugar el juego, ver estadísticas de su desempeño y gestionar su perfil.

## Características

- **Registro de Usuarios**: Permite a los usuarios registrarse en el sistema.
- **Inicio de Sesión**: Los usuarios pueden iniciar sesión en el sistema.
- **Perfil de Usuario**: Los usuarios pueden ver su perfil con estadísticas de juegos jugados, ganados y perdidos, así como su porcentaje de victorias.
- **Juego**: Los usuarios pueden jugar al juego de Piedra Papel Tijera contra la computadora.
- **Panel de Administración**: Los superusuarios tienen acceso al panel de administración de Django para gestionar usuarios y perfiles.

## Tecnologías Utilizadas

- Django 5.0.5
- Python 3.12.2
- HTML/CSS
- Bootstrap (opcional para el diseño)

## Instalación

Sigue estos pasos para configurar el proyecto en tu entorno local:

1. **Clona el repositorio**:

    ```bash
    git clone https://github.com/tuusuario/tuproyecto.git
    cd tuproyecto
    ```

2. **Crea un entorno virtual e instálalo**:

    ```bash
    python -m venv env
    source env/bin/activate  # En Windows usa `env\Scripts\activate`
    pip install -r requirements.txt
    ```

3. **Configura la base de datos**:

    Ejecuta las migraciones para crear las tablas necesarias en la base de datos:

    ```bash
    python manage.py migrate
    ```

4. **Crea un superusuario**:

    ```bash
    python manage.py createsuperuser
    ```

    Sigue las instrucciones para crear el superusuario.

5. **Inicia el servidor**:

    ```bash
    python manage.py runserver
    ```

6. **Accede a la aplicación**:

    Abre tu navegador web y ve a `http://127.0.0.1:8000/` para ver la aplicación en funcionamiento.

## Uso

- **Registro**: Los nuevos usuarios pueden registrarse desde la página de registro.
- **Inicio de Sesión**: Los usuarios existentes pueden iniciar sesión desde la página de inicio de sesión.
- **Perfil**: Los usuarios pueden ver su perfil con estadísticas de su desempeño en el juego.
- **Jugar**: Los usuarios pueden jugar al juego desde la página principal.

## Personalización

Para personalizar el proyecto, puedes modificar los siguientes archivos:

- **`game/views.py`**: Lógica del juego.
- **`user/views.py`**: Lógica del perfil y gestión de usuarios.
- **`templates/`**: Plantillas HTML para las páginas.
- **`static/`**: Archivos estáticos como CSS y JavaScript.

## Contribución

Si deseas contribuir al proyecto, por favor sigue estos pasos:

1. **Haz un fork del repositorio**.
2. **Crea una rama nueva**:

    ```bash
    git checkout -b nombre-de-la-rama
    ```

3. **Haz tus cambios y confirma**:

    ```bash
    git add .
    git commit -m "Descripción de los cambios"
    ```

4. **Sube tus cambios**:

    ```bash
    git push origin nombre-de-la-rama
    ```

5. **Crea un pull request** en GitHub.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.


