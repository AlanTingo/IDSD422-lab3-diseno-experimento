# comparacion_experimento.py — Comparación de grupos (Python)
# Ejecuta desde la raíz del repositorio:
#   python scripts/comparacion_experimento.py
import pandas as pd

# TODO 1: carga plantillas/registro_experimento.csv con pandas
df = pd.read_csv("plantillas/registro_experimento.csv")

# TODO 2: promedio de ventas_producto por ubicacion
print("Promedio de ventas_producto por ubicación:")
print(df.groupby("ubicacion")["ventas_producto"].mean())

# TODO 3: número de registros por grupo
print("\nRegistros por grupo:")
print(df["ubicacion"].value_counts())

# TODO 4: interpretación (sección 9 de la plantilla)
# Con solo 2 filas por grupo, el promedio no prueba nada: no se puede estimar
# la variabilidad y la diferencia puede ser puro azar. Además, una fila del
# pasillo principal (Guayaquil Centro) tuvo promoción simultánea, que confunde
# el efecto de la ubicación. Para concluir faltan más unidades, asignación
# aleatoria verificada, control de la promoción y una prueba estadística.
