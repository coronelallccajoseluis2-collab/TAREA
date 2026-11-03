# -*- coding: utf-8 -*-
"""
CASO 02 - Aplicación Flask: estimación del costo de transporte agrícola.
Usa solo Python, Flask, HTML y CSS (sin JavaScript).

Ejecutar localmente:  python app.py   y abrir  http://127.0.0.1:5000
En PythonAnywhere:    importar como módulo WSGI (ver guía de despliegue).
"""
import os
import json
from flask import Flask, render_template, request

# --- Configuración de la app ---
app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "clave-desarrollo-caso02")

# --- Cargar modelo (ruta relativa al directorio del script) ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODELO_PATH = os.path.join(BASE_DIR, "modelo.json")

with open(MODELO_PATH, encoding="utf-8") as f:
    MODELO = json.load(f)

# --- Rangos válidos pedidos en el enunciado ---
LIMITES = {
    "distancia_km": (3, 165),
    "carga_kg": (50, 2050),
}
NOMBRES = {"distancia_km": "Distancia", "carga_kg": "Carga"}


def predecir(distancia, carga, no_asfaltada):
    """Ecuación: costo = b0 + b1·distancia + b2·carga + b3·vía_no_asfaltada"""
    c = MODELO["coeficientes"]
    costo = (MODELO["intercepto"]
             + c["distancia_km"] * distancia
             + c["carga_kg"] * carga
             + c["via_no_asfaltada"] * no_asfaltada)
    return max(costo, 0)


def validar(form):
    """Valida los campos del formulario. Devuelve (valores, errores)."""
    errores, valores = [], {}
    for campo, (minimo, maximo) in LIMITES.items():
        texto = form.get(campo, "").strip().replace(",", ".")
        try:
            v = float(texto)
        except ValueError:
            errores.append(f"{NOMBRES[campo]}: ingrese un número válido.")
            continue
        if not (minimo <= v <= maximo):
            errores.append(f"{NOMBRES[campo]}: debe estar entre {minimo} y {maximo}.")
        valores[campo] = v
    via = form.get("via_no_asfaltada", "")
    if via not in ("0", "1"):
        errores.append("Tipo de vía: elija asfaltada o no asfaltada.")
    else:
        valores["via_no_asfaltada"] = int(via)
    return valores, errores


@app.route("/", methods=["GET", "POST"])
def index():
    """Ruta principal: muestra el formulario y procesa la predicción."""
    resultado, errores, valores = None, [], {}
    if request.method == "POST":
        valores, errores = validar(request.form)
        if not errores:
            costo = predecir(valores["distancia_km"], valores["carga_kg"],
                             valores["via_no_asfaltada"])
            resultado = {
                "costo": round(costo, 2),
                "mae": round(MODELO["metricas"]["mae"], 2),
                "distancia": valores["distancia_km"],
                "carga": valores["carga_kg"],
                "via": "No asfaltada" if valores["via_no_asfaltada"] else "Asfaltada",
            }
    return render_template("index.html", resultado=resultado,
                           errores=errores, valores=valores, modelo=MODELO)


@app.route("/acerca")
def acerca():
    """Página informativa sobre el modelo y el proyecto."""
    return render_template("acerca.html", modelo=MODELO)


# --- Manejo de errores ---
@app.errorhandler(404)
def pagina_no_encontrada(e):
    return render_template("error.html", codigo=404,
                           mensaje="Página no encontrada"), 404


@app.errorhandler(500)
def error_interno(e):
    return render_template("error.html", codigo=500,
                           mensaje="Error interno del servidor"), 500


if __name__ == "__main__":
    app.run(debug=True)
