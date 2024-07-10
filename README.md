1. Estructura del Proyecto:

manage.py: Es el script principal para interactuar con el proyecto Django.
inventariosistema/: Carpeta del proyecto que contiene la configuración principal.
inventario/: Aplicación principal que contiene los modelos, vistas, templates, etc.
templates/: Carpeta que contiene los archivos HTML.
static/: Carpeta para archivos estáticos como CSS y JavaScript.

2. Archivos y Directorios Clave:
manage.py: Archivo principal para ejecutar comandos Django.
inventariosistema/:
settings.py: Archivo de configuración del proyecto Django.
urls.py: Archivo que define las URL del proyecto.
inventario/:
models.py: Define los modelos de la base de datos.
views.py: Contiene las vistas que manejan la lógica del lado del servidor.
urls.py: Define las URL específicas de la aplicación.
admin.py: Configuración del panel de administración de Django.
templates/: Contiene las plantillas HTML utilizadas por la aplicación.

4. Instrucciones para Configuración y Ejecución:
Requisitos Previos
Python 3.x
pip (gestor de paquetes de Python)

Crear y Activar un Entorno Virtual:

Abre una terminal y navega hasta el directorio del proyecto.
Crea un entorno virtual con el siguiente comando:

python3 -m venv venv
Activa el entorno virtual:
source venv/bin/activate

Instalar Django y Otras Dependencias:

Con el entorno virtual activado, instala Django y otras dependencias necesarias:

pip install django==5.0.7
pip install django-crispy-forms==1.14.0
pip install crispy-bootstrap4

Realizar las Migraciones:

Ejecuta los siguientes comandos para aplicar las migraciones de la base de datos:

python manage.py makemigrations
python manage.py migrate

Crea un superusuario para poder acceder al panel de administración de Django:

python manage.py createsuperuser

Ejecutar el Servidor de Desarrollo:
python manage.py runserver
