# CASO PRÁCTICO INTERMEDIO 2 — SENATI

**Sistema de estimación de costo de transporte agrícola**

Un transportista quiere estimar el costo de un viaje a partir de distancia, peso y tipo de vía. Datos simulados inspirados en el transporte agrícola regional.

**Datos:** `datos.csv`. Son **simulados**, no registros reales.

## Trabajo que realizará el estudiante
1. Abrir el CSV e identificar las variables X: distancia_km, carga_kg, via_no_asfaltada; y: costo_transporte_soles.
2. Explorar datos, verificar ausentes y separar 80% entrenamiento / 20% prueba.
3. Entrenar `LinearRegression` y mostrar los coeficientes con explicación.
4. Calcular MAE y R² sobre prueba, y comentar qué significan en las unidades del problema.
5. Crear `app.py`, `templates/index.html` y `static/estilos.css` con **Python, Flask, HTML y CSS solamente**.
6. Guardar los coeficientes en `modelo.json`; mostrar la predicción en la página después de pulsar un botón.
7. Validar rangos: distancia de 3 a 165 km; carga 50 a 2050 kg; vía asfaltada/no asfaltada (0/1).
8. Hacer mínimo dos pruebas: Viaje 25 km, 400 kg, ruta asfaltada; Viaje 100 km, 1200 kg, ruta no asfaltada.
9. Entregar capturas, CSV, código comentado, una explicación de 10 líneas y conclusiones sobre límites del modelo.

## Rúbrica (20 puntos)
- Lectura y limpieza del CSV (3)
- Variables elegidas, ajuste y separación train/test (5)
- Interpretación de MAE y R² (4)
- Interfaz Flask usable sin JavaScript (5)
- Pruebas, comentarios y documentación (3)

**No se entrega una solución final de estos retos:** están diseñados para evaluar lo aprendido en los cuatro proyectos resueltos.
