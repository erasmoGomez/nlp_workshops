# LEXICON-X II — Echoes of Eráviri
Examen final | Maestría en Informática | By Erasmo Gomez Montoya

## Misión
Seis meses después del primer contacto, una expedición descubre un archivo bilingüe. Los registros oficiales, históricos y rumores se contradicen. Construyan un asistente que responda preguntas en español con evidencia verificable. El universo y los datos son ficticios; Eráviri es una lengua artificial simplificada.

## Recursos
1,500 documentos, 500 preguntas de entrenamiento, 150 de validación y un léxico parcial. El corpus incluye registros de 250 sitios; los sitios de las preguntas de entrenamiento y validación son disjuntos. Los documentos de todos los sitios están disponibles para recuperación. Los metadatos incluyen año, fuente y confiabilidad (0–1). El año vigente es 2048. Los registros oficiales vigentes prevalecen para preguntas actuales; para preguntas históricas se usa el año solicitado. No inventen respuestas cuando falte evidencia.

## Requisitos
Implementar dos sistemas de recuperación y respuesta, uno baseline y otro alternativo. Se admite generación extractiva o neuronal; no se exige API ni GPU. Formular hipótesis falsable antes de experimentar. Comparar ambos con las mismas preguntas, reportar EM, evidence_hit, joint y resultados por tipo, además de latencia. Analizar al menos cinco errores o casos difíciles, incluyendo contradicción y ausencia de evidencia. No usar respuestas de validación como contexto de recuperación ni codificar respuestas por ID. Se permite utilizar entrenamiento para diseñar reglas.

## Formato de salida
CSV con qid, answer, citations. answer es un número sin unidades o SIN_EVIDENCIA. citations contiene IDs separados por |; vacío si no hay evidencia. EM compara respuesta exacta; evidence_hit verifica al menos una cita válida (o ninguna para ausencia); joint exige ambos. Una cita adicional incorrecta debe discutirse en análisis manual.

## Cronograma
0–10 misión; 10–30 exploración e hipótesis; 30–65 baseline; 65–105 alternativa; 105–120 evaluación; 120–145 consolidación y entrega; 145–180 defensa. Cuatro equipos de máximo cuatro integrantes. Cada equipo: 6 minutos de exposición y 2 de preguntas. Cierre 177–180.

## Entrega (minuto 145)
Notebook ejecutable, predicciones de validación de ambos métodos, tabla experimental, análisis de errores y presentación de máximo cinco diapositivas. Todos los integrantes deben poder defender decisiones. Guardar una copia del código y configuración al minuto 120. Registrar versiones y semillas. No compartir soluciones entre equipos.

## Rúbrica /20
Exploración 2; hipótesis 2; baseline 3; alternativa 3; diseño experimental y métricas 3; robustez y generalización 2; análisis de errores 2; reproducibilidad 1; defensa 2. La nota no depende exclusivamente del ranking.
