# Proyecto Final coderhuse

Aplicación estilo blog con perfiles, registro, páginas y mensajeria

## Descripción del proyecto

Este proyecto es una aplicación web tipo blog desarrollada con Django.
Su objetivo es mostrar el funcionamiento completo de un sitio con usuarios, perfiles, páginas y mensajería interna.

La página permite que cada usuario pueda registrarse, iniciar sesión y crear sus propias publicaciones.
Cada publicación (o “página”) puede tener título, subtítulo, texto con formato, imágenes y fecha automática de creación.
Desde la lista principal se pueden leer los contenidos o, si el usuario está logueado, editarlos y borrarlos.

Además, cada usuario cuenta con un perfil personal donde puede subir una foto de avatar, escribir una breve biografía, agregar un enlace y su fecha de cumpleaños.
También puede modificar estos datos y cambiar su contraseña desde el mismo sitio.

Por otro lado, el proyecto incluye una sección de mensajería, donde los usuarios pueden enviarse mensajes privados entre sí.
Desde allí se pueden ver los mensajes recibidos, los enviados y abrir cada uno para leer su contenido.

La interfaz está hecha con Bootstrap, por lo que el diseño se adapta a pantallas grandes y celulares, con una navegación clara desde la barra superior.
El sitio cuenta con páginas de Inicio, Acerca de mí, Blog, Perfil, Login, Registro y Mensajes, cumpliendo con todos los requisitos pedidos en la consigna del proyecto final.

## Tecnologías
- Python 3.x
- Django
- django-ckeditor
- Pillow

## Instalación y ejecucin

```bash

# Crear y activar entorno
python -m venv venv
venv\Scripts\activate  # Windows

# Instalar dependencias
pip install -r requirements.txt

# Migrar base de datos
python manage.py migrate

# Crear superusuario (opcional)
python manage.py createsuperuser

# Ejecutar servidor
python manage.py runserver
