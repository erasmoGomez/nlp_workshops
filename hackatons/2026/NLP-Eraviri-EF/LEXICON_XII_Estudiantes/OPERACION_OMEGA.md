# LEXICON-X II — Operación Ω
**CONFIDENCIAL hasta el minuto 120 | By Erasmo Gomez Montoya**

## Transmisión de emergencia
La expedición ha recibido 120 nuevas preguntas sobre sitios no utilizados en entrenamiento ni validación. Los documentos pertinentes ya están en el corpus original. La misión es comprobar si el sistema generaliza sin ajustes adicionales.

## Instrucciones (120–140)
- Recibir `protocolo_omega.csv` (qid, question), sin respuestas.
- Usar exclusivamente la configuración guardada al minuto 120. No modificar modelos, reglas, prompts, umbrales ni corpus.
- Ejecutar el método seleccionado antes de la revelación. No responder manualmente ni consultar a otros equipos.
- Generar `omega_predictions.csv` con una fila por pregunta: qid, answer, citations. Respuesta numérica sin unidades o SIN_EVIDENCIA; citas separadas por |, vacías ante abstención.
- Reportar limitaciones observadas sin inventar métricas: las respuestas correctas permanecen reservadas al docente.

## Entrega (140–145)
Adjuntar las predicciones a los entregables originales. Incorporar a la defensa una breve reflexión sobre generalización y dificultades. La entrega cierra al minuto 145.

## Evaluación
Los 2 puntos de robustez y generalización corresponden a 2 × joint, proporción de preguntas con respuesta exacta y al menos una evidencia válida (o abstención correcta sin citas). Las citas incorrectas adicionales se revisan en el análisis de errores.

## Defensa
145–153 equipo 1; 153–161 equipo 2; 161–169 equipo 3; 169–177 equipo 4; 177–180 cierre. Cada equipo tiene 6 minutos de exposición y 2 de preguntas.
