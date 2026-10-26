# Laboratorio 3: Diseño de un experimento de ubicación de producto

**Caso empresarial:** RetailAndina S.A., cadena ecuatoriana de tiendas de consumo masivo.

## El contexto

RetailAndina sospecha que su producto estrella (el más rentable) vende más cuando se ubica en el pasillo principal, pero la gerencia no quiere mover todo el inventario sin evidencia. Tu equipo de Business Intelligence tiene que diseñar un experimento que responda a esta pregunta: ¿cambiar la ubicación del producto al pasillo principal aumenta sus ventas?

**Tu rol:** analista del equipo de BI. Diseñas el protocolo experimental completo: unidad experimental, factor, niveles, tratamiento, grupo de control, aleatorización, respuesta y factores a controlar. El experimento no se ejecuta en esta práctica; se evalúa la coherencia del diseño.

## Archivos del repositorio

- `README.md`: este documento, con el contexto del caso
- `plantilla-protocolo.md`: el entregable, el protocolo que debes completar
- `plantillas/registro_experimento.csv`: plantilla de registro, útil si el experimento se ejecutara
- `scripts/comparacion_experimento.py` y `.R`: archivos con pasos pendientes (TODOs) para que escribas el script de comparación
- `EVALUACION.md`: la rúbrica con la que se evalúa el laboratorio

## El componente de código (Python o R, tú eliges)

El diseño se completa con código en dos momentos:

1. **Asignación aleatoria (sección 5).** La línea que asigna tus unidades a los dos grupos al azar. Recuerda la regla del cap. 3: si el investigador asigna (con código), es un experimento; si solo observa lo que ya ocurrió, es un estudio observacional.
2. **Comparación en código (sección 9).** Escribes el script que calcularía las ventas promedio por grupo sobre la plantilla de registro, y explicas por qué con pocas filas no se puede concluir nada.

## Cómo trabajar

1. Clona el repositorio y crea tu rama (o haz un fork).
2. Completa la plantilla sección por sección: hipótesis, unidades, factor, control, aleatorización, respuesta, factores a controlar, limitaciones y comparación en código.
3. Haz un commit por cada sección completada.
4. Revisa tu diseño con la regla del curso: ¿quién asigna el tratamiento? Si el investigador asigna y controla, el diseño es un experimento válido.
5. Escribe el script de comparación (completa los TODOs de `scripts/`), córrelo sobre la plantilla y agrega la salida interpretada en la sección 9.

## Entregable

- **Protocolo completo (martes 27 de octubre).** La plantilla terminada: un diseño que la gerencia podría ejecutar tal cual, con su asignación en código y el script de comparación.

La evaluación está detallada en `EVALUACION.md`.

*Laboratorio 3, IDSD422, Estadística y Programación para Ciencia de Datos I, 2026-B.*
