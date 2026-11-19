# Plantilla de protocolo — Experimento de ubicación de producto

**Estudiante:** Alan Tingo· **Fecha:** 27/10/2026

Completa cada sección. Usa commits por sección; la historia del repositorio se revisa.

## 1. Pregunta e hipótesis

**Pregunta:** ¿cambiar la ubicación del producto estrella al pasillo principal aumenta sus ventas?

**Hipótesis:** durante 4 semanas, las ventas semanales del producto estrella (en USD) serán mayores, en promedio, en las tienda-semana en que el producto está en el pasillo principal (tratamiento) que en las tienda-semana en que permanece en su ubicación habitual (control).

**Hipótesis nula:** no hay diferencia entre las ventas semanales promedio de las dos ubicaciones.

## 2. Unidad experimental
- Unidad: la tienda-semana (una tienda durante una semana). Cada una recibe una sola ubicación del producto.
- Número de unidades y justificación: 10 tiendas × 4 semanas = 40 unidades, 20 por grupo. Es un piloto manejable en logística. Como cada tienda pasa por ambos niveles, se compara consigo misma y se reduce el efecto de las diferencias entre tiendas. No se calculó el tamaño necesario para detectar un efecto; se declara como limitación (sección 8).

## 3. Factor, niveles y tratamiento

- **Factor** (variable manipulada): ubicación del producto estrella dentro de la tienda.
- **Niveles** (valores del factor): pasillo principal y ubicación habitual.
- **Tratamiento** (combinación asignada): colocar el producto en el pasillo principal durante la semana asignada, con el mismo precio y sin promociones propias. El pasillo principal es un nivel del factor; el tratamiento es la acción de mover el producto a ese nivel.
- 
## 4. Grupo de control

Las tienda-semana en que el producto permanece en su ubicación habitual. Son la referencia sin tratamiento: muestran cuánto se vende sin el cambio y absorben los efectos que afectan a todas las unidades por igual (temporada, tendencia general). Sin control no se podría saber si un aumento se debe al pasillo o a algo que habría pasado igual.

## 5. Aleatorización

Las 40 tienda-semana se asignan a los grupos con un sorteo en código, no a criterio de una persona. Dentro de cada tienda se sortean 2 de las 4 semanas para el tratamiento, así cada tienda aporta 2 semanas por grupo. El sorteo es necesario por dos razones:

- Reparte entre los dos grupos, por azar, los factores que no se pueden medir (clientela, clima, ánimo de compra de la semana), de modo que no favorezcan sistemáticamente a un grupo.
- Evita el sesgo de selección: nadie puede poner el tratamiento en las semanas que prevé buenas. Por eso es un experimento y no un estudio observacional: el investigador asigna.

```python
import numpy as np, pandas as pd

np.random.seed(42)                      # semilla: la asignación es reproducible
filas = []
for t in range(1, 11):                  # 10 tiendas
    trat = np.random.choice([1, 2, 3, 4], size=2, replace=False)   # 2 semanas con tratamiento
    for s in [1, 2, 3, 4]:
        filas.append({"tienda": f"T{t:02d}", "semana": s,
                      "ubicacion": "pasillo_principal" if s in trat else "habitual"})
asignacion = pd.DataFrame(filas)
print(asignacion.head(8).to_string(index=False))
print(asignacion["ubicacion"].value_counts())
```

Resultado de una corrida (semilla 42):

```
tienda  semana         ubicacion
   T01       1          habitual
   T01       2 pasillo_principal
   T01       3          habitual
   T01       4 pasillo_principal
   T02       1          habitual
   T02       2 pasillo_principal
   T02       3          habitual
   T02       4 pasillo_principal

ubicacion
habitual             20
pasillo_principal    20
Name: count, dtype: int64
```

La semilla fija el sorteo para que cualquiera pueda reproducirlo y auditarlo.

## 6. Respuesta y medición

- Variable respuesta: `ventas_producto`, ventas del producto estrella por tienda-semana, en USD.
- Período de medición: las mismas 4 semanas consecutivas para todas las tiendas.
- Quién registra y cómo (¿ciego?): el sistema de punto de venta (POS), no el personal de la tienda. El personal no puede ser ciego, porque mueve el producto. Quien analiza los datos recibe los grupos con etiquetas neutras (A y B) y no sabe cuál es el tratamiento hasta terminar la comparación.

## 7. Factores a controlar (mínimo 4)

| Factor a controlar | Cómo se controla o registra |
|---|---|
| 1. Clima | Se registra por semana; como cada tienda pasa por ambos niveles en las mismas 4 semanas, el clima afecta a los dos grupos. |
| 2. Evento local | Se anota por tienda-semana y se marcan las semanas afectadas para analizarlas aparte. |
| 3. Surtido / stock | Reposición igual en ambos grupos; se registran los quiebres de stock, porque sin producto no hay ventas. |
| 4. Cambios en el personal | Se registra el personal por semana y se evitan cambios durante el experimento. |
| 5. Precio y promociones | Mismo precio en todas las tiendas y semanas; sin promociones del producto ni de sustitutos; si ocurre una, se registra en `promocion_simultanea`. |

## 8. Limitaciones del diseño

- **Promociones y canibalización:** una promoción simultánea resta potencia al análisis, y mover el producto al pasillo principal puede quitar ventas a otros productos de la tienda; este diseño mide solo el producto estrella, no las ventas totales.
- **Efecto residual:** lo que ocurre en una semana puede influir en la siguiente (hábitos de compra, stock). Aleatorizar el orden lo reparte, pero no lo elimina.
- **Independencia:** las 40 unidades no son independientes, porque cada tienda aporta 4. El análisis debe tener en cuenta la tienda y no tratar las filas como 40 tiendas distintas.
- **Tamaño pequeño:** con 10 tiendas el azar pesa mucho, y no se calculó el tamaño necesario para detectar un efecto.
- **Sin ciego completo:** el personal sabe cuándo está el tratamiento y podría influir (por ejemplo, recomendando el producto).
- **No se podrá concluir** que el efecto valga para otros productos, otras tiendas ni otras épocas del año.

## 9. Comparación en código (Python/R)

*Escribe `scripts/comparacion_experimento.py` (o `.R`): debe cargar `plantillas/registro_experimento.csv` y calcular el promedio de `ventas_producto` por `ubicacion`. Incluye la salida y responde:*

- ¿Qué grupo muestra mayor venta promedio en la plantilla?
El pasillo muestra 1335 USD en venta frente a 1040 USD en habitual 

- ¿Por qué con 4 filas no se puede concluir nada sobre el efecto de la ubicación?
NO se puede concluir porque no hay ninguna asignacion real aleatoria, los datos son muy pocos (4) no tenemos control de temporada, ni promociones en el grupo pasillo  y no hay medida de variablilidad

- Si el experimento se ejecutara con tu protocolo, ¿qué le faltaría a este análisis para ser justo?
