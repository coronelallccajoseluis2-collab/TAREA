# -*- coding: utf-8 -*-
"""Pruebas obligatorias del Caso 02 (usa el cliente de prueba de Flask)."""
from app import app, predecir

casos = [
    ("Viaje 1: 25 km, 400 kg, ruta asfaltada", 25, 400, 0),
    ("Viaje 2: 100 km, 1200 kg, ruta no asfaltada", 100, 1200, 1),
]
print("=== Pruebas del modelo ===")
for nombre, d, c, v in casos:
    print(f"{nombre} -> S/ {predecir(d, c, v):.2f}")

cli = app.test_client()
print("\n=== Pruebas de la web ===")
for d, c, v in [("25", "400", "0"), ("100", "1200", "1")]:
    r = cli.post("/", data={"distancia_km": d, "carga_kg": c, "via_no_asfaltada": v})
    assert "Costo estimado" in r.get_data(as_text=True)
print("OK  2 pruebas por formulario")
for datos in [{"distancia_km": "2", "carga_kg": "400", "via_no_asfaltada": "0"},
              {"distancia_km": "166", "carga_kg": "400", "via_no_asfaltada": "0"},
              {"distancia_km": "50", "carga_kg": "49", "via_no_asfaltada": "0"},
              {"distancia_km": "50", "carga_kg": "2051", "via_no_asfaltada": "0"},
              {"distancia_km": "50", "carga_kg": "400", "via_no_asfaltada": "5"},
              {"distancia_km": "xx", "carga_kg": "400", "via_no_asfaltada": "0"}]:
    html = cli.post("/", data=datos).get_data(as_text=True)
    assert "Revise los datos" in html and "Costo estimado" not in html
print("OK  6 entradas inválidas rechazadas correctamente")
