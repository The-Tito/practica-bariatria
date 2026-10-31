# Grafo de conocimiento (KG)

Punto de entrada único al contexto del proyecto. `graph.json` consolida en nodos y aristas tipados la base de conocimiento, los casos de uso y las seis tablas del análisis en Excel. Cada nodo indica su **estado** (`CONFIRMADO`, `PENDIENTE`, `POR_VALIDAR`…) y su **procedencia** (`src`).

| Archivo | Rol |
|---|---|
| `graph.json` | Fuente del grafo. Es el único archivo que se edita a mano. |
| `kg.py` | Consultas y validación (Python 3, solo biblioteca estándar). |
| `INDEX.md` | Índice generado (`kg.py render`). No se edita a mano. |

## Consultas

Ejecutar desde `backend/`:

```bash
python3 context/kg/kg.py brief CU-03      # ficha para implementar un caso de uso
python3 context/kg/kg.py get RN-06        # nodo completo + aristas
python3 context/kg/kg.py ctx COL-visitas -d 2
python3 context/kg/kg.py find idempotencia   # búsqueda sin acentos/mayúsculas
python3 context/kg/kg.py list Regla -s PARCIAL
python3 context/kg/kg.py inputs CALC-GET  # qué datos de captura necesita un cálculo
python3 context/kg/kg.py open             # todo lo no resuelto
python3 context/kg/kg.py check            # valida integridad
```

## Modelo

**Tipos de nodo:** Proyecto, Actor, CasoDeUso (CU-xx), Patron (Px), Regla (RN-xx), ReglaArquitectura (AR-xx), Seguridad (SEC-xx), Coleccion (COL-*), Indice (IDX-xx), Entidad (ENT-*), DecisionModelado (MD-xx), Modulo (MOD-*), Infraestructura (INFRA-*), Medicion (M-*), Atributo (ATTR-*), Calculo (CALC-*), Requisito, ADR (ADR-xx), Pendiente (PC-xx), Conflicto (CF-xx), Vacio (GAP-xx), CriterioAceptacion (AC-xx), EstrategiaPruebas, FueraDeAlcance (OOS-xx).

Los identificadores CU, P, RN, PC y ADR son los mismos que usan los documentos de origen.

**Aristas:** `[origen, relación, destino, {props opcionales}]`. El vocabulario de relaciones y estados está en `meta` de `graph.json`, y `kg.py check` rechaza cualquier valor fuera de él.

**Conflictos y vacíos:** donde el análisis del Excel contradice a la base de conocimiento o a los casos de uso, se crea un nodo `CF-xx` con lo vigente o la regla provisional. Lo que falta en todas las fuentes se registra como `GAP-xx`. Ninguno de los dos casos se resuelve en silencio.

## Protocolo de mantenimiento

1. Toda decisión nueva se anota primero en `context/registro-cambios.md`.
2. Después se edita `graph.json`: cambiar el `status`, añadir nodos o aristas y actualizar `meta.version` y `meta.actualizado`.
3. Si la decisión cierra un conflicto o un pendiente, su estado pasa a `RESUELTO`/`CONFIRMADO`, el nodo se conserva y se enlaza con lo que lo resolvió (`resuelto_por` y `sustituye`).
4. Ejecutar `kg.py check` y `kg.py render`.
5. Si la decisión modifica un documento de origen (KB o CU), actualizarlo también para que coincida.
