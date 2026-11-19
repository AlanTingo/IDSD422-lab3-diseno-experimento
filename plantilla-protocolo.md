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

Sorteo de 20 tiendas a cada grupo (Paralelo).

- **Línea de código de la asignación (Python o R):** escribe el comando que asigna al azar tus N unidades a los dos grupos (tratamiento y control) y ejecútalo con semilla. Incluye el resultado de una corrida y explica por qué el sorteo reparte los factores desconocidos entre los grupos.

## 6. Respuesta y medición

- Variable respuesta: Ventas semanales en USD
- Período de medición: 4 semanas
- Quién registra y cómo (¿ciego?): Mediante el POS, ciego (vendedor no sabia si el producto esta en principal o en habitual)

## 7. Factores a controlar (mínimo 4)

| Factor a controlar | Cómo se controla o registra |
|---|---|
| 1. | clima |
| 2. | Evento local |
| 3. | Surtido / Stock |
| 4. | Cambios en el personal|

## 8. Limitaciones del diseño

- Perdida de potencia por promociones
- Canibalizacion de las tiendas

## 9. Comparación en código (Python/R)

*Escribe `scripts/comparacion_experimento.py` (o `.R`): debe cargar `plantillas/registro_experimento.csv` y calcular el promedio de `ventas_producto` por `ubicacion`. Incluye la salida y responde:*

- ¿Qué grupo muestra mayor venta promedio en la plantilla?
El pasillo muestra 1335 USD en venta frente a 1040 USD en habitual 

- ¿Por qué con 4 filas no se puede concluir nada sobre el efecto de la ubicación?
NO se puede concluir porque no hay ninguna asignacion real aleatoria, los datos son muy pocos (4) no tenemos control de temporada, ni promociones en el grupo pasillo  y no hay medida de variablilidad

- Si el experimento se ejecutara con tu protocolo, ¿qué le faltaría a este análisis para ser justo?
