# Registro de prompts

Solicitudes relevantes hechas al asistente y su resultado.

## 2026-10-26 — Crear el grafo de conocimiento

**Prompt:** «En esta carpeta /context tienes el contexto del proyecto, casos de uso, base de conocimiento y tablas de Excel que contienen un análisis realizado (Patrones, Relaciones, Colecciones, Índices, Integridad, Validación); esa es la fuente de verdad sobre el proyecto. En esa carpeta /context es donde guardaremos los planes de implementación, documentación, registro de cambios, registro de prompts, todo lo que sea útil como contexto. Lo primero que quiero que hagamos es crear un KG (grafo de conocimiento) con base en la información del contexto; esto será para acceder a eso como única fuente de verdad y optimizar la consulta hacia el contexto.»

## 2026-10-26 — Confirmar precedencia de fuentes

**Prompt:** «Sí, la base de conocimiento es la principal, y los casos de uso son ya lo analizado y dan solución a los problemas con el Excel.»

**Resultado:** KG v1.1.0. CF-03, CF-05, CF-06 y CF-07 resueltos a favor de KB/CU (ver `registro-cambios.md`).

---

**Resultado (creación del KG):** KG v1.0.0 en `context/kg/` y skill `contexto-kg`. Ver la entrada del mismo día en `registro-cambios.md`.
