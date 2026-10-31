# Índice del grafo de conocimiento

> Generado por `python3 context/kg/kg.py render` desde `graph.json`. No editar a mano.
> Versión 1.2.0 · actualizado 2026-10-30 · 194 nodos · 395 aristas.

## Precedencia de fuentes

- 1. Decisiones registradas en context/registro-cambios.md posteriores a esta versión.
- 2. KB: fuente principal (CONFIRMADO por el equipo, 2026-10-26).
- 3. CU: casos de uso ya analizados; resuelven los problemas detectados en el Excel.
- 4. Análisis del Excel (XP, XR, XC, XI, XN, XV): insumo previo. Ante contradicción con KB/CU prevalecen KB/CU; el Excel solo aporta detalle donde KB/CU no se pronuncian.

## Fuentes (`src`)

- **KB**: context/base_conocimiento_grafo_proyecto_bariatria.md (v1.0, 2026-10-26)
- **CU**: context/casos-de-uso.md
- **XP**: context/excel/Patrones.csv
- **XR**: context/excel/Relaciones.csv
- **XC**: context/excel/Colecciones.csv
- **XI**: context/excel/Indices.csv
- **XN**: context/excel/Integridad.csv
- **XV**: context/excel/Validacion.csv

## Proyecto (1)

| ID | Título | Estado | Grado |
|---|---|---|---|
| PROY | Sistema de gestión clínica bariátrica | CONFIRMADO | 9 |

## Actor (3)

| ID | Título | Estado | Grado |
|---|---|---|---|
| ACT-MED | Médico | CONFIRMADO | 11 |
| ACT-AYU | Ayudante médico | CONFIRMADO | 1 |
| ACT-PAC | Paciente (destinatario del expediente) | CONFIRMADO | 2 |

## CasoDeUso (12)

| ID | Título | Estado | Grado |
|---|---|---|---|
| CU-01 | Registrar paciente | CONFIRMADO | 7 |
| CU-02 | Adjuntar expediente externo | CONFIRMADO | 8 |
| CU-03 | Registrar mediciones clínicas | CONFIRMADO | 22 |
| CU-04 | Consultar historial clínico | CONFIRMADO | 6 |
| CU-05 | Registrar seguimiento clínico | CONFIRMADO | 16 |
| CU-06 | Consultar cálculos antropométricos y calóricos | CONFIRMADO | 33 |
| CU-07 | Registrar dieta y medicamentos | CONFIRMADO | 9 |
| CU-08 | Clasificar paciente por padecimiento | CONFIRMADO | 7 |
| CU-09 | Vincular pacientes familiares | CONFIRMADO | 6 |
| CU-10 | Consultar antecedentes heredofamiliares | CONFIRMADO | 9 |
| CU-11 | Entregar expediente clínico (PDF) | PARCIAL | 8 |
| CU-12 | Consultar pacientes por padecimiento | CONFIRMADO | 7 |

## Patron (14)

| ID | Título | Estado | Grado |
|---|---|---|---|
| P1 | Registrar paciente nuevo | CONFIRMADO | 4 |
| P2 | Registrar expediente/antecedentes externos | CONFIRMADO | 3 |
| P3 | Registrar mediciones | CONFIRMADO | 5 |
| P4 | Consultar historial completo | CONFIRMADO | 6 |
| P5 | Registrar seguimiento | CONFIRMADO | 4 |
| P6 | Realizar cálculos | CONFIRMADO | 4 |
| P7 | Registrar dietas y medicamentos | CONFIRMADO | 2 |
| P8 | Clasificar paciente por padecimiento | CONFIRMADO | 4 |
| P9 | Conectar paciente con familiares | CONFIRMADO | 4 |
| P10 | Consultar antecedentes de familiares | CONFIRMADO | 4 |
| P11 | Entregar expediente al paciente | CONFIRMADO | 5 |
| P12 | Listar pacientes por padecimiento | CONFIRMADO | 4 |
| P13 | Reporte: frecuencia de glucosa en ayuno elevada por año y sexo | PROPUESTA | 1 |
| P14 | Auditoría de captura: visitas cerradas con IMC más alto | PROPUESTA | 2 |

## Regla (14)

| ID | Título | Estado | Grado |
|---|---|---|---|
| RN-01 | Campos obligatorios y tipos | PARCIAL | 5 |
| RN-02 | Valores permitidos | PARCIAL | 3 |
| RN-03 | Rangos de mediciones | POR_VALIDAR | 7 |
| RN-04 | Una sola visita inicial por paciente | PENDIENTE | 2 |
| RN-05 | Toda visita pertenece a un paciente existente | CONFIRMADO | 3 |
| RN-06 | Relaciones familiares bidireccionales y atómicas | CONFIRMADO | 4 |
| RN-07 | Padecimientos del catálogo y sin duplicados | CONFIRMADO | 2 |
| RN-08 | Expediente externo siempre con su archivo | CONFIRMADO | 4 |
| RN-09 | Escrituras autorizadas por responsabilidad | PARCIAL | 4 |
| RN-10 | Cálculos consistentes con sus datos de origen | CONFIRMADO | 5 |
| RN-11 | Retención mínima de 15 años | CONFIRMADO | 5 |
| RN-12 | Inmutabilidad del historial | CONFIRMADO | 12 |
| RN-13 | Prevención de duplicados por reintentos (idempotencia) | CONFIRMADO | 6 |
| RN-14 | Autenticación y autorización por rol | PARCIAL | 13 |

## ReglaArquitectura (8)

| ID | Título | Estado | Grado |
|---|---|---|---|
| AR-01 | Controladores HTTP no consultan MongoDB directamente | CONFIRMADO | 1 |
| AR-02 | Módulos no importan archivos internos de otros módulos | CONFIRMADO | 1 |
| AR-03 | La lógica de cálculo no depende de HTTP ni MongoDB | CONFIRMADO | 2 |
| AR-04 | Toda escritura pasa por servicios que aplican reglas de negocio | CONFIRMADO | 1 |
| AR-05 | Sin dependencias circulares | CONFIRMADO | 1 |
| AR-06 | No crear capas, interfaces o archivos vacíos sin necesidad concreta | CONFIRMADO | 1 |
| AR-07 | Probar cada módulo de forma aislada cuando sea posible | CONFIRMADO | 1 |
| AR-08 | Features acceden a MongoDB/GridFS solo a través de infrastructure | CONFIRMADO | 2 |

## Seguridad (9)

| ID | Título | Estado | Grado |
|---|---|---|---|
| SEC-01 | Mínimo privilegio en cuentas de BD (sin borrado físico ni drop) | CONFIRMADO | 1 |
| SEC-02 | Validar entradas en API y BD | CONFIRMADO | 1 |
| SEC-03 | Validar PDF por contenido, no solo por extensión | CONFIRMADO | 2 |
| SEC-04 | Errores sin exponer credenciales, internos ni datos clínicos | CONFIRMADO | 1 |
| SEC-05 | No registrar información clínica completa en logs | CONFIRMADO | 1 |
| SEC-06 | Secretos en variables de entorno, nunca en el repositorio | CONFIRMADO | 1 |
| SEC-07 | Generación del expediente solo para usuarios autorizados | CONFIRMADO | 2 |
| SEC-08 | El vínculo familiar no da acceso al expediente del familiar | CONFIRMADO | 3 |
| SEC-09 | Respaldo, DR, cifrado, auditoría y regulación por definir antes de producción | PENDIENTE | 1 |

## Coleccion (4)

| ID | Título | Estado | Grado |
|---|---|---|---|
| COL-pacientes | pacientes | PROPUESTA | 17 |
| COL-visitas | visitas (Excel: consultas) | PROPUESTA | 18 |
| COL-expedientes | expedientes.files / expedientes.chunks (GridFS) | PROPUESTA | 5 |
| COL-catalogo-padecimientos | catálogo de padecimientos | PROPUESTA | 5 |

## Indice (6)

| ID | Título | Estado | Grado |
|---|---|---|---|
| IDX-01 | visitas { paciente_id: 1, fecha: -1 } | PROPUESTA | 5 |
| IDX-02 | pacientes { apellido_paterno: 1, apellido_materno: 1, nombre: 1, fecha_nacimiento: 1 } collation es strength 1 | PROPUESTA | 6 |
| IDX-02-OLD | pacientes { nombre_completo: 1, fecha_nacimiento: 1 } collation es strength 1 | SUPERADO | 3 |
| IDX-03 | pacientes { padecimientos.codigo: 1 } (multikey) | PENDIENTE | 3 |
| IDX-04 | visitas { paciente_id: 1 } único parcial { tipo: 'inicial' } | PENDIENTE | 5 |
| IDX-05 | visitas { fecha: 1 } | PROPUESTA | 2 |

## Entidad (11)

| ID | Título | Estado | Grado |
|---|---|---|---|
| ENT-Paciente | Paciente | CONFIRMADO | 11 |
| ENT-Antecedentes | Antecedentes y alergias | CONFIRMADO | 3 |
| ENT-Visita | Visita | CONFIRMADO | 8 |
| ENT-Estudio | Estudio | CONFIRMADO | 8 |
| ENT-Medicion | Medición | CONFIRMADO | 17 |
| ENT-ResultadoCalculado | Resultado calculado | CONFIRMADO | 4 |
| ENT-Dieta | Dieta indicada | CONFIRMADO | 3 |
| ENT-Medicamento | Medicamento indicado | CONFIRMADO | 3 |
| ENT-DocumentoExterno | Documento externo (PDF) | PARCIAL | 5 |
| ENT-Padecimiento | Padecimiento | PARCIAL | 4 |
| ENT-RelacionFamiliar | Relación familiar | CONFIRMADO | 4 |

## DecisionModelado (9)

| ID | Título | Estado | Grado |
|---|---|---|---|
| MD-01 | Paciente → antecedentes y alergias: EMBEBIDO | PROPUESTA | 1 |
| MD-02 | Paciente → padecimientos: EMBEBIDO (arreglo) | PROPUESTA | 1 |
| MD-03 | Paciente → visitas: REFERENCIA (colección aparte con paciente_id) | PROPUESTA | 1 |
| MD-04 | Visita → mediciones: EMBEBIDO | PROPUESTA | 1 |
| MD-05 | Visita → resultados de cálculos: EMBEBIDO | PROPUESTA | 2 |
| MD-06 | Visita → dieta: EMBEBIDO (copia) | PROPUESTA | 1 |
| MD-07 | Visita → medicamentos: EMBEBIDO (copia) | PROPUESTA | 1 |
| MD-08 | Paciente → familiares: REFERENCIA ({paciente_id, parentesco}) | PROPUESTA | 1 |
| MD-09 | Paciente → expediente externo: REFERENCIA (metadatos embebidos, binario en GridFS) | PROPUESTA | 1 |

## Modulo (9)

| ID | Título | Estado | Grado |
|---|---|---|---|
| MOD-auth | features/auth | CONFIRMADO | 2 |
| MOD-patients | features/patients | CONFIRMADO | 7 |
| MOD-visits | features/visits | CONFIRMADO | 12 |
| MOD-calculations | features/calculations (+ formulas/) | CONFIRMADO | 7 |
| MOD-documents | features/documents | CONFIRMADO | 7 |
| MOD-family-history | features/family-history | CONFIRMADO | 4 |
| MOD-conditions | features/conditions | CONFIRMADO | 5 |
| MOD-shared | shared (errors, logging, validation) | CONFIRMADO | 3 |
| MOD-config | config | CONFIRMADO | 3 |

## Infraestructura (3)

| ID | Título | Estado | Grado |
|---|---|---|---|
| INFRA-mongodb | infrastructure/database/mongodb | CONFIRMADO | 9 |
| INFRA-gridfs | infrastructure/storage/gridfs | PROPUESTA | 3 |
| INFRA-pdf | infrastructure/pdf | CONFIRMADO | 1 |

## Medicion (13)

| ID | Título | Estado | Grado |
|---|---|---|---|
| M-PESO | Peso (kg) | CONFIRMADO | 7 |
| M-ESTATURA | Estatura (cm) | CONFIRMADO | 7 |
| M-PLIEGUE-BICEPS | Pliegue bicipital (mm) | CONFIRMADO | 2 |
| M-PLIEGUE-TRICEPS | Pliegue tricipital (mm) | CONFIRMADO | 3 |
| M-PLIEGUE-SUBESCAPULAR | Pliegue subescapular (mm) | CONFIRMADO | 2 |
| M-PLIEGUE-SUPRAILIACO | Pliegue suprailiaco (mm) | CONFIRMADO | 2 |
| M-CIRC-MUNECA | Circunferencia de muñeca (cm) | CONFIRMADO | 2 |
| M-CIRC-CINTURA | Circunferencia de cintura (cm) | CONFIRMADO | 2 |
| M-CIRC-CADERA | Circunferencia de cadera (cm) | CONFIRMADO | 2 |
| M-CIRC-BRAZO | Circunferencia de brazo (cm) | CONFIRMADO | 2 |
| M-GLUCOSA | Glucosa (mg/dL) | CONFIRMADO | 1 |
| M-PRESION | Presión arterial (sistólica/diastólica) | CONFIRMADO | 2 |
| M-BIOIMPEDANCIA | Bioimpedancia (datos reportados por la báscula) | POR_VALIDAR | 2 |

## Atributo (1)

| ID | Título | Estado | Grado |
|---|---|---|---|
| ATTR-SEXO | Sexo del paciente | CONFIRMADO | 7 |

## Calculo (21)

| ID | Título | Estado | Grado |
|---|---|---|---|
| CALC-LORENTZ-H | Peso ideal Lorentz (hombre) | POR_VALIDAR | 4 |
| CALC-LORENTZ-M | Peso ideal Lorentz (mujer) | POR_VALIDAR | 4 |
| CALC-BROCCA | Peso ideal Brocca | POR_VALIDAR | 3 |
| CALC-PI-PROM | Promedio de peso ideal | POR_VALIDAR | 6 |
| CALC-PCT-PI | Porcentaje de peso ideal (%PI) | POR_VALIDAR | 3 |
| CALC-IMC | IMC | POR_VALIDAR | 4 |
| CALC-COMPLEXION | Complexión | POR_VALIDAR | 3 |
| CALC-ICC | Índice cintura-cadera | POR_VALIDAR | 3 |
| CALC-SUMA-PLIEGUES | Sumatoria de pliegues | POR_VALIDAR | 6 |
| CALC-LOG-PLIEGUES | Logaritmo de la sumatoria de pliegues | POR_VALIDAR | 3 |
| CALC-DENSIDAD | Densidad corporal | POR_VALIDAR | 4 |
| CALC-MASA-GRASA | Masa grasa | POR_VALIDAR | 4 |
| CALC-MLG | Masa libre de grasa | POR_VALIDAR | 3 |
| CALC-PCT-GRASA-SIRI | % grasa corporal (Siri) | POR_VALIDAR | 2 |
| CALC-AMB | Área muscular del brazo (AMB) | POR_VALIDAR | 3 |
| CALC-GEB | Gasto energético basal (GEB) | POR_VALIDAR | 6 |
| CALC-ETA | Efecto térmico de los alimentos (ETA) | POR_VALIDAR | 3 |
| CALC-EF | Factor de actividad (EF) | POR_VALIDAR | 3 |
| CALC-GET | Gasto energético total (GET) | POR_VALIDAR | 5 |
| CALC-RESTRICCION | Restricción calórica | POR_VALIDAR | 2 |
| CALC-PCT-PESO-PERDIDO | % de peso perdido vs. visita inicial | SUPERADO | 4 |

## Requisito (1)

| ID | Título | Estado | Grado |
|---|---|---|---|
| CALC-REQS | Ficha obligatoria antes de programar una fórmula | CONFIRMADO | 2 |

## ADR (14)

| ID | Título | Estado | Grado |
|---|---|---|---|
| ADR-01 | NoSQL con MongoDB como diseño base | CONFIRMADO | 1 |
| ADR-02 | Arquitectura modular por funcionalidades (monolito modular) | CONFIRMADO | 8 |
| ADR-03 | Separar nombre, apellido paterno, apellido materno y fecha de nacimiento | CONFIRMADO | 3 |
| ADR-04 | Una visita puede contener varios estudios | CONFIRMADO | 4 |
| ADR-05 | No modificar visitas ni estudios anteriores | CONFIRMADO | 3 |
| ADR-06 | Cálculos aislados de infraestructura | PROPUESTA | 2 |
| ADR-07 | Documentos PDF en GridFS | PROPUESTA | 2 |
| ADR-08 | Relaciones familiares bidireccionales y consistentes | CONFIRMADO | 1 |
| ADR-09 | Historial resumido y detalle bajo demanda | PROPUESTA | 1 |
| ADR-10 | Conservar información clínica ≥ 15 años | CONFIRMADO | 1 |
| ADR-11 | Evitar duplicados con identidad estable e idempotencia | CONFIRMADO | 1 |
| ADR-12 | Visita con estudios[] embebidos y mediciones tipadas | CONFIRMADO | 3 |
| ADR-13 | Ciclo de vida de la visita: estado abierta/cerrada | CONFIRMADO | 3 |
| ADR-14 | _id de la visita: UUID generado por el cliente | CONFIRMADO | 2 |

## Pendiente (12)

| ID | Título | Estado | Grado |
|---|---|---|---|
| PC-01 | Fórmulas clínicas | POR_VALIDAR | 5 |
| PC-02 | Ciclo de vida de visitas y estudios | CONFIRMADO | 7 |
| PC-03 | PDF externos: tamaño máximo y metadatos | PARCIAL | 3 |
| PC-04 | Contenido del expediente de entrega | PARCIAL | 1 |
| PC-05 | Alcance de familiares | CONFIRMADO | 3 |
| PC-06 | Administración del catálogo de padecimientos | PARCIAL | 3 |
| PC-07 | Tecnología backend | PENDIENTE | 1 |
| PC-08 | Modelo físico de visitas/estudios | CONFIRMADO | 5 |
| PC-09 | Matriz de roles y permisos | PENDIENTE | 2 |
| PC-10 | Correcciones posteriores | PENDIENTE | 3 |
| PC-11 | Retención: evento de inicio y respaldo | PENDIENTE | 1 |
| PC-12 | Catálogo de estudios y mediciones | PARCIAL | 4 |

## Conflicto (9)

| ID | Título | Estado | Grado |
|---|---|---|---|
| CF-01 | nombre_completo (Excel) vs nombre y apellidos separados | RESUELTO | 4 |
| CF-02 | Campo 'estudio' único en consultas vs varios estudios por visita | RESUELTO | 4 |
| CF-03 | Editar 'la consulta del día' con $set vs inmutabilidad | RESUELTO | 10 |
| CF-04 | P5 seguimiento = $set de notas (Excel) vs nueva visita (CU-05) | RESUELTO | 3 |
| CF-05 | Momento del cálculo: al guardar mediciones (Excel) vs al consultar (CU-06) | RESUELTO | 5 |
| CF-06 | Correcciones posteriores registradas en notas (Excel) vs procedimiento pendiente | RESUELTO | 3 |
| CF-07 | % de peso perdido y visita inicial no figuran en la lista de cálculos de KB | RESUELTO | 4 |
| CF-08 | P10 'historial de familiares' (Excel) vs solo heredofamiliares | RESUELTO | 3 |
| CF-09 | Índice multikey de padecimientos: listado (XI) vs sin índice por ahora (XV) | RESUELTO | 1 |

## Vacio (4)

| ID | Título | Estado | Grado |
|---|---|---|---|
| GAP-01 | El modelo de Paciente no incluye 'sexo' | RESUELTO | 5 |
| GAP-02 | Clave de idempotencia de visitas sin definir | RESUELTO | 5 |
| GAP-03 | KB§4 cita 'casos_de_uso.md' pero el archivo es 'casos-de-uso.md' | ABIERTO | 1 |
| GAP-04 | Entradas exactas del GEB (¿edad?) no documentadas | ABIERTO | 1 |

## CriterioAceptacion (7)

| ID | Título | Estado | Grado |
|---|---|---|---|
| AC-01 | Ningún reintento crea visitas duplicadas | CONFIRMADO | 2 |
| AC-02 | Ningún estudio asociado a un paciente inexistente | CONFIRMADO | 1 |
| AC-03 | Una visita histórica no se modifica por endpoints ordinarios | CONFIRMADO | 2 |
| AC-04 | Cálculos no se presentan como válidos si faltan entradas | CONFIRMADO | 1 |
| AC-05 | Una relación familiar nunca queda en un solo extremo | CONFIRMADO | 1 |
| AC-06 | Un documento no aparece vinculado si su archivo no se almacenó | CONFIRMADO | 1 |
| AC-07 | Los permisos se comprueban en el servidor | CONFIRMADO | 1 |

## EstrategiaPruebas (1)

| ID | Título | Estado | Grado |
|---|---|---|---|
| TST | Estrategia de pruebas | CONFIRMADO | 3 |

## FueraDeAlcance (8)

| ID | Título | Estado | Grado |
|---|---|---|---|
| OOS-01 | Portal o cuenta para pacientes | CONFIRMADO | 1 |
| OOS-02 | Integración con sistemas externos, laboratorios o aseguradoras | CONFIRMADO | 1 |
| OOS-03 | Aplicación móvil nativa | CONFIRMADO | 1 |
| OOS-04 | Firma electrónica | CONFIRMADO | 1 |
| OOS-05 | Mensajería, recordatorios y agenda de citas | CONFIRMADO | 1 |
| OOS-06 | Diagnóstico automatizado o recomendaciones clínicas autónomas | CONFIRMADO | 1 |
| OOS-07 | Corrección o eliminación de visitas y estudios históricos | CONFIRMADO | 3 |
| OOS-08 | Acceso automático a expedientes completos de familiares | CONFIRMADO | 1 |
