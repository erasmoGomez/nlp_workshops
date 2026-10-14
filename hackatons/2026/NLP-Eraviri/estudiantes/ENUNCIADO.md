# LEXICON-X — Expedición Náviri

**Hackatón de investigación | 180 minutos | 4 equipos de 3 | Nivel: maestría**

## Contexto
Una expedición encontró 3,000 mensajes monolingües en Náviri, una lengua artificial desconocida, y 420 traducciones verificadas al español. Se dispone además de 120 ejemplos bilingües para validación. Su equipo debe proponer un método reproducible para traducir mensajes inéditos, con un presupuesto de tiempo limitado.

## Pregunta de investigación
**¿Qué estrategia permite generalizar mejor a combinaciones nuevas cuando las traducciones paralelas son escasas?** Deben plantear una hipótesis falsable, implementar un baseline, comparar con al menos un segundo enfoque y analizar errores.

## Archivos
- `datos/train_parallel.csv`: 420 pares bilingües, entrenamiento.
- `datos/validation_parallel.csv`: 120 pares bilingües, validación.
- `datos/corpus_monolingual.csv`: 3,000 oraciones Náviri sin traducción.
- `datos/test_public_unlabeled.csv`: 40 mensajes para predicción final sin referencias.
- `LEXICON_X_Colab.ipynb`: notebook base ejecutable.

## Reglas
1. Trabajen en equipos de tres; todos deben comprender y poder defender la solución.
2. Se permite usar bibliotecas, modelos preentrenados, asistentes de IA e internet, siempre que se declaren. **No se permite buscar ni usar los archivos privados del docente**.
3. No utilicen las traducciones de validación para ajustar manualmente la salida frase por frase; utilicen el conjunto para comparar decisiones metodológicas.
4. No se exige entrenar un Transformer desde cero. Un experimento fallido bien explicado es valioso.
5. El corpus es sintético: los resultados no deben extrapolarse a lenguas indígenas reales.
6. La evaluación oficial se hará con datos que no reciben durante la sesión.

## Cronograma
- **0–15 min:** historia, equipos y pregunta de investigación.
- **15–40 min:** EDA, hipótesis sobre segmentación, orden de palabras y morfología.
- **40–95 min:** baseline y segundo método (reglas, n-gramas, seq2seq, embeddings, prompting, Transformer pequeño o híbrido).
- **95–130 min:** evaluación, ablación y análisis de errores.
- **130–155 min:** reto sorpresa: traducir 40 mensajes públicos, explicar incertidumbre y preparar defensa.
- **155–180 min:** 4 exposiciones de 5 minutos + 5 minutos de discusión.

## Entregables al minuto 155
1. Notebook reproducible con entrenamiento/inferencia, semilla y dependencias.
2. CSV `predicciones.csv` con columnas `id,prediccion` para los 40 mensajes públicos, en el mismo orden.
3. Miniinforme de máximo 2 páginas o 4 diapositivas: hipótesis, métodos, tabla de métricas, 3 errores y conclusión.
4. Registro de uso de modelos externos/IA y limitaciones.

## Preguntas para la defensa
- ¿Qué evidencia sostiene el orden de palabras propuesto?
- ¿Cómo separaron aprendizaje de vocabulario y aprendizaje de estructura?
- ¿Qué aporta el corpus monolingüe? Demuéstrenlo o expliquen por qué no fue útil.
- ¿Cómo evitaron la fuga de datos y el sobreajuste a validación?
- ¿Qué tipo de ejemplos falla más: negativos, tiempos verbales, lugares o combinaciones inéditas?
- ¿Qué experimento adicional harían con una semana más?

## Métricas sugeridas
- **Exact match normalizado**: proporción de traducciones idénticas a la referencia (minúsculas, sin puntuación final, espacios normalizados).
- **chrF** con sacrebleu si está disponible: similitud de caracteres útil como medida complementaria.
- **Análisis por fenómeno**: negativo, pasado, futuro, locativo y OOD (el docente hará esta evaluación).
- **No utilicen BLEU como único indicador**: las frases son cortas y la coincidencia exacta es exigente.

## Criterio central
No gana necesariamente quien obtenga el mayor puntaje, sino quien demuestre con evidencia una investigación rigurosa, reproducible y técnicamente defendible.
