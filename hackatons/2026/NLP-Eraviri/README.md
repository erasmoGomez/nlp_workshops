# LEXICON-X — paquete completo

**Entregar únicamente la carpeta `estudiantes/` a los equipos.** No compartir `docente/`, que contiene referencias, gramática y pruebas privadas.

## Uso
1. Extraer ZIP.
2. Compartir la carpeta `estudiantes/` (enunciado, datos, notebook).
3. En Colab, subir la subcarpeta `datos` a `/content/datos` o abrir Jupyter desde `estudiantes/`.
4. El notebook funciona con Python estándar, sin instalar paquetes.
5. Al minuto 155, recoger notebook, CSV y miniinforme.
6. Ejecutar `python docente/evaluador_y_oraculo.py` para verificar el oráculo.
7. Ejecutar `python docente/evaluador_y_oraculo.py predicciones.csv --gold test_public_gold.csv` desde cualquier ubicación para puntuar el reto público.

**Aviso:** IDs son únicos dentro de cada archivo, pero no globalmente entre archivos. Emparejar siempre las predicciones con el archivo gold correspondiente.
