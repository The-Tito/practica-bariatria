# Registro de prompts

Solicitudes relevantes hechas al asistente y su resultado.

## 2026-10-26 — Crear el grafo de conocimiento

**Prompt:** «En esta carpeta /context tienes el contexto del proyecto, casos de uso, base de conocimiento y tablas de Excel que contienen un análisis realizado (Patrones, Relaciones, Colecciones, Índices, Integridad, Validación); esa es la fuente de verdad sobre el proyecto. En esa carpeta /context es donde guardaremos los planes de implementación, documentación, registro de cambios, registro de prompts, todo lo que sea útil como contexto. Lo primero que quiero que hagamos es crear un KG (grafo de conocimiento) con base en la información del contexto; esto será para acceder a eso como única fuente de verdad y optimizar la consulta hacia el contexto.»

## 2026-10-26 — Confirmar precedencia de fuentes

**Prompt:** «Sí, la base de conocimiento es la principal, y los casos de uso son ya lo analizado y dan solución a los problemas con el Excel.»

**Resultado:** KG v1.1.0. CF-03, CF-05, CF-06 y CF-07 resueltos a favor de KB/CU (ver `registro-cambios.md`).

---

**Resultado (creación del KG):** KG v1.0.0 en `context/kg/` y skill `contexto-kg`. Ver la entrada del mismo día en `registro-cambios.md`.

## 2026-10-30 — Adaptar el proyecto a la práctica MongoDB vs PostgreSQL JSONB

**Prompt:** «Antes de avanzar finalicemos y dejemos listo la parte NoSQL, resolvamos lo faltante y los problemas ya que esta es la base, y sobre todo que cumpla con los requisitos y si estamos simulando un caso real, lo que hagamos debe tener un por qué, no solo para cumplir los requisitos.»

**Resultado:** KG v1.2.0. Se cierran PC-08 (ADR-12), PC-02 (ADR-13), GAP-01 y GAP-02 (ADR-14); se agregan los reportes P13 y P14 y el índice IDX-05 (ver `registro-cambios.md`). El análisis completo de Q1 y Q2 está en el repositorio del experimento (`docs/decisiones.md`).

## 2026-10-30 — Elementos homogéneos en el arreglo de Q1

**Prompt:** «No es posible preguntarle al profesor, lo decidamos acá, desglósame el punto 3 y si conviene hacerlo.» Después: «Sí, avanza con C.»

**Resultado:** KG v1.3.0. ADR-15 (medicación vigente estructurada) y P15 como nueva Q1 del experimento; P13 deja de ser Q1 (ver `registro-cambios.md`). Se acepta y se reporta la compresión TOAST de ~14 % de las filas JSONB, en vez de recortar los datos.

