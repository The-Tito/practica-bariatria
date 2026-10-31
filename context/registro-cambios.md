# Registro de cambios

Decisiones y cambios del contexto del proyecto, del más reciente al más antiguo. Cada entrada indica los nodos del KG afectados.

## 2026-10-30 — Modelo físico de visitas y reportes de población (KG v1.2.0)

Contexto: práctica de medición MongoDB vs PostgreSQL JSONB, que se adapta a este proyecto. El detalle y la justificación de cada punto están en el repositorio del experimento (`experimento/docs/decisiones.md`). Decidió el equipo; los puntos clínicos quedan por validar con el médico.

- **ADR-12 (cierra PC-08):** la visita embebe `estudios[]`; cada estudio tiene `tipo_estudio`, mediciones tipadas según su tipo y `resultados_calculados`. Motivo: CU-03 guarda visita y estudios en una sola operación (atómica sin transacción), no cambian después (RN-12), su número está acotado y ningún patrón consulta un estudio suelto.
- **ADR-13 (cierra PC-02 y lo que CF-03 dejaba pendiente):** la visita tiene `estado` abierta/cerrada. El médico la cierra al terminar; si lo olvida, se cierra automáticamente al final del día. CU-07 escribe con `updateOne({_id, estado: "abierta"}, {$set})`, así que el motor rechaza los cambios a visitas cerradas.
- **ADR-14 (cierra GAP-02):** el `_id` de la visita es un UUID que genera el cliente al abrir la captura. Un reintento choca con la llave `_id` y devuelve la visita existente (RN-13), sin índice adicional.
- **GAP-01 resuelto:** se agrega `sexo` (F/M) al paciente. Se deriva de cálculos ya identificados (Lorentz, GEB) y del parentesco inverso (RN-06). La visita congela `datos_paciente {sexo, edad_anios}` para cumplir la procedencia de RN-10.
- **ADR-09 concretado:** la visita guarda `resumen {peso_kg, imc}` en el mismo insert, para la gráfica de evolución de CU-04.
- **PC-12 parcial:** catálogo propuesto de 4 tipos de estudio, uno por instrumento: `antropometria` (peso, estatura, circunferencias), `pliegues_cutaneos`, `signos_vitales` (glucosa en ayuno, presión) y `bioimpedancia`. Supuesto del experimento; lo valida el médico.
- **P13 y P14 (PROPUESTA):** reportes de población que no pidió el cliente y se adoptan como supuestos para el experimento. P13: frecuencia de mediciones de glucosa en ayuno ≥ 100 mg/dL por año y sexo (umbral ADA; la glucosa se toma en ayuno, confirmado). P14: auditoría de captura, visitas cerradas de un periodo con el IMC más alto, para detectar errores plausibles que RN-03 no rechaza.
- **IDX-05 (PROPUESTA):** `visitas { fecha: 1 }` para P14. `resumen.imc` se deja sin índice a propósito.
- Nodos afectados: PC-02, PC-08, PC-12, GAP-01, GAP-02, CF-03, ATTR-SEXO, ENT-Paciente, ENT-Visita, COL-visitas, RN-13, ADR-09; nuevos ADR-12, ADR-13, ADR-14, P13, P14, IDX-05.

## 2026-10-26 — Precedencia de fuentes confirmada (KG v1.1.0)

- **Decisión (equipo):** la base de conocimiento es la fuente principal. Los casos de uso son el resultado del análisis y resuelven los problemas detectados en el Excel. Ante una contradicción prevalecen KB y CU; el Excel solo aporta detalle donde KB y CU no dicen nada.
- Conflictos resueltos con esta regla:
  - CF-03: no se adopta la edición de la "consulta del día". Solo CU-07 actualiza campos autorizados de una visita.
  - CF-05: el cálculo se hace como describe CU-06.
  - CF-06: se descarta registrar las correcciones en notas.
  - CF-07: el % de peso perdido queda fuera del alcance de cálculos (CALC-PCT-PESO-PERDIDO → SUPERADO).
- Se reescriben RN-09 y RN-10 conforme a KB y CU; el mecanismo del Excel queda en el campo `superado`.
- Siguen abiertos porque KB y CU no los resuelven: PC-01…PC-12 (salvo PC-05), RN-04 y GAP-01…GAP-04.

## 2026-10-26 — Creación del grafo de conocimiento (KG v1.0.0)

- Se crea `context/kg/` (`graph.json`, `kg.py`, `INDEX.md`, `README.md`) a partir de la base de conocimiento v1.0, los casos de uso CU-01…CU-12 y las tablas del Excel (Patrones, Relaciones, Colecciones, Índices, Integridad, Validación).
- Precedencia propuesta: registro de cambios > KB/CU > análisis del Excel (confirmada en v1.1.0).
- Se modelan como conflictos las diferencias entre el Excel y la KB/CU:
  - Resueltos por decisiones ya confirmadas: CF-01 (nombre_completo), CF-02 (un solo estudio), CF-04 (seguimiento = nueva visita), CF-08 (familiares) y CF-09 (índice de padecimientos).
  - Abiertos: CF-03 (edición de la visita del día), CF-05 (momento del cálculo), CF-06 (correcciones posteriores) y CF-07 (% de peso perdido y visita inicial).
- Vacíos detectados: GAP-01 (falta `sexo` en Paciente), GAP-02 (clave de idempotencia), GAP-03 (nombre de archivo citado en KB§4) y GAP-04 (entradas del GEB).
- Se añade el skill del proyecto `.claude/skills/contexto-kg` para consultar el KG antes de implementar.
