# -*- coding: utf-8 -*-
"""
Punto de entrada para Vercel (Serverless Python).
Importa la app Flask del módulo principal.
"""
import sys
import os

# Agregar la raíz del proyecto al path de Python
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from app import app
