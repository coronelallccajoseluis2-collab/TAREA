# -*- coding: utf-8 -*-
"""
Archivo WSGI para PythonAnywhere.
Este archivo NO se usa directamente; su contenido se pega en la
configuración WSGI de PythonAnywhere (ver guía de despliegue).
"""
import sys
import os

# Ruta del proyecto en PythonAnywhere (ajustar con tu usuario)
# Ejemplo: /home/TU_USUARIO/CASO_02_TRANSPORTE_AGRICOLA
project_home = '/home/TU_USUARIO/CASO_02_TRANSPORTE_AGRICOLA'

if project_home not in sys.path:
    sys.path.insert(0, project_home)

os.chdir(project_home)

from app import app as application
