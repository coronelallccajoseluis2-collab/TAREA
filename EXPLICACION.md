# Caso 02 — Explicación y conclusiones

**Explicación (10 líneas)**
1. Se leyó `datos.csv` (130 viajes simulados, sin valores ausentes ni duplicados).
2. Entradas X: `distancia_km`, `carga_kg`, `via_no_asfaltada`; salida y: `costo_transporte_soles`.
3. Se separó 80 % entrenamiento (104 filas) y 20 % prueba (26 filas), con `random_state=42`.
4. Se entrenó `LinearRegression`: costo = 21.52 + 2.774·km + 0.1073·kg + 26.44·vía_no_asfaltada.
5. Cada km extra suma ~S/ 2.77; cada 100 kg, ~S/ 10.7; la vía no asfaltada, ~S/ 26.
6. MAE = S/ 17.79: error promedio de unos S/ 18 por viaje.
7. R² = 0.977: explica ~98 % de la variación del costo.
8. Los coeficientes se guardan en `modelo.json`; `app.py` los lee y calcula la predicción.
9. La web (Flask + HTML + CSS, sin JavaScript) valida rangos y muestra el costo al pulsar «Calcular».
10. Pruebas: 25 km, 400 kg, asfaltada → S/ 133.79; 100 km, 1200 kg, no asfaltada → S/ 454.13.

**Límites del modelo**
- Datos simulados y pocos (130 filas); una sola partición train/test.
- No incluye combustible variable, peajes, clima, esperas ni retorno vacío.
- Supone relaciones lineales (sin interacción trocha × peso).
- Solo es válido en 3–165 km y 50–2050 kg.

**Cómo ejecutar**
```
pip install flask scikit-learn pandas
python entrenar_modelo.py   # genera modelo.json
python pruebas.py           # pruebas obligatorias
python app.py               # abrir http://127.0.0.1:5000
```
