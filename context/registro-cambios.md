# Registro de cambios

Decisiones y cambios del contexto del proyecto, del más reciente al más antiguo. Cada entrada indica los nodos del KG afectados.

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
