# -*- coding: utf-8 -*-
"""
CASO 02 - Estimación del costo de transporte agrícola (SENATI)
Script de entrenamiento: lee datos.csv, entrena una regresión lineal múltiple,
evalúa con MAE y R² y guarda los coeficientes en modelo.json.

Ejecutar:  python entrenar_modelo.py
"""
import json
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# ---------------------------------------------------------------- 1. Lectura
datos = pd.read_csv("datos.csv", encoding="utf-8-sig")   # utf-8-sig quita el BOM
print("Filas y columnas:", datos.shape)
print(datos.head(), "\n")

# ---------------------------------------------------------------- 2. Limpieza
print("Valores ausentes por columna:")
print(datos.isna().sum(), "\n")
datos = datos.dropna().drop_duplicates()
print("Resumen estadístico:")
print(datos.describe().round(2), "\n")

# ---------------------------------------------------------------- 3. Variables
COLUMNAS = ["distancia_km", "carga_kg", "via_no_asfaltada"]
OBJETIVO = "costo_transporte_soles"
X = datos[COLUMNAS]
y = datos[OBJETIVO]

# 80 % entrenamiento / 20 % prueba
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42
)
print(f"Entrenamiento: {len(X_train)} filas | Prueba: {len(X_test)} filas\n")

# ---------------------------------------------------------------- 4. Modelo
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# ---------------------------------------------------------------- 5. Métricas (sobre PRUEBA)
pred = modelo.predict(X_test)
mae = mean_absolute_error(y_test, pred)
r2 = r2_score(y_test, pred)

print("COEFICIENTES")
print(f"  Intercepto (b0)          = {modelo.intercept_:.4f}")
for nombre, coef in zip(COLUMNAS, modelo.coef_):
    print(f"  {nombre:<22} = {coef:.4f}")
print(f"\nMAE (prueba) = S/ {mae:.2f}")
print(f"R²  (prueba) = {r2:.3f}")

# ---------------------------------------------------------------- 6. Guardar modelo.json
salida = {
    "intercepto": float(modelo.intercept_),
    "coeficientes": {n: float(c) for n, c in zip(COLUMNAS, modelo.coef_)},
    "metricas": {"mae": float(mae), "r2": float(r2)},
    "filas_entrenamiento": int(len(X_train)),
    "filas_prueba": int(len(X_test)),
}
with open("modelo.json", "w", encoding="utf-8") as f:
    json.dump(salida, f, indent=4, ensure_ascii=False)
print("\nmodelo.json guardado correctamente.")
