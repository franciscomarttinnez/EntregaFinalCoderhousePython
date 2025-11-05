# Proyecto Final coderhuse

Aplicación estilo blog con perfiles, registro, páginas y mensajeria

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
