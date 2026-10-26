# Casos de uso del sistema de gestión clínica bariátrica

## CU-01. Registrar paciente

**Actor principal:** Médico.

**Objetivo:** Registrar a un paciente nuevo en el sistema para iniciar su expediente clínico.

**Precondiciones:**

- El médico ha iniciado sesión.
- El paciente no se ha registrado previamente, según la búsqueda de coincidencias.

**Flujo principal:**

1. El médico selecciona la opción para registrar un paciente.
2. El sistema solicita los datos personales del paciente.
3. El médico captura el nombre, apellido paterno, apellido materno y fecha de nacimiento, además de los demás datos requeridos que estén definidos.
4. El sistema valida los campos y sus formatos.
5. El sistema busca posibles coincidencias para detectar pacientes que ya estén registrados.
6. El médico confirma el registro.
7. El sistema crea el expediente del paciente y guarda la fecha de registro.

**Flujos alternativos:**

- Si faltan datos obligatorios o alguno tiene un formato inválido, el sistema informa el error y solicita corregirlo.
- Si existen coincidencias con otro paciente, el sistema las muestra para que el médico verifique si se trata de un registro existente.

**Postcondiciones:**

- El paciente queda registrado con un identificador único.
- El expediente queda disponible para registrar visitas y consultar su historial.

---

## CU-02. Adjuntar expediente externo

**Actor principal:** Médico.

**Objetivo:** Asociar un expediente o documento clínico externo al expediente de un paciente.

**Precondiciones:**

- El médico ha iniciado sesión.
- El paciente ya está registrado.
- El archivo que se desea adjuntar está disponible en formato PDF.

**Flujo principal:**

1. El médico busca y selecciona al paciente.
2. El médico elige la opción para adjuntar un expediente externo.
3. El sistema permite seleccionar un archivo PDF.
4. El sistema valida que el archivo tenga el formato permitido.
5. El sistema almacena el archivo.
6. El sistema registra los metadatos necesarios y vincula el documento con el paciente.
7. El sistema confirma que el expediente externo quedó asociado.

**Flujos alternativos:**

- Si el archivo no es PDF, el sistema rechaza la carga.
- Si ocurre un error al guardar el archivo o sus metadatos, el sistema informa que la operación no se completó y permite gestionar la recuperación sin dejar referencias inválidas.

**Postcondiciones:**

- El PDF queda almacenado y vinculado al paciente.
- El archivo puede recuperarse posteriormente para su consulta o inclusión en la entrega del expediente.

**Restricción:** El tamaño máximo permitido para los archivos está pendiente de definición.

---

## CU-03. Registrar mediciones clínicas

**Actor principal:** Ayudante médico.

**Objetivo:** Registrar las mediciones clínicas de un paciente durante una visita.

**Precondiciones:**

- El ayudante médico ha iniciado sesión.
- El paciente está registrado.
- No existe una visita equivalente ya registrada para la misma operación.

**Flujo principal:**

1. El ayudante médico busca y selecciona al paciente.
2. El sistema muestra la información necesaria para identificar al paciente.
3. El ayudante médico inicia el registro de una visita.
4. El sistema permite registrar uno o varios estudios de distintos tipos dentro de la visita.
5. El ayudante médico captura las mediciones correspondientes a cada estudio.
6. El sistema valida los campos, tipos de datos y rangos configurados.
7. El sistema guarda la visita, los estudios y sus mediciones.
8. El sistema confirma el registro.

**Flujos alternativos:**

- Si faltan datos obligatorios o existen valores inválidos, el sistema informa los errores y solicita corregirlos antes de guardar.
- Si se reintenta una operación ya procesada, el sistema evita crear registros duplicados.
- Si la visita o sus estudios ya fueron guardados, no se permite modificarlos posteriormente.

**Postcondiciones:**

- La visita y sus estudios quedan vinculados al paciente.
- Las mediciones quedan disponibles para los cálculos clínicos y las consultas del historial.

**Restricciones:**

- Una visita puede incluir uno o varios estudios de diferentes tipos.
- Las visitas y los estudios anteriores son inmutables: no se pueden corregir ni modificar una vez registrados.
- Los cálculos se guardan asociados a la visita y a los datos que los originaron.

---

## CU-04. Consultar historial clínico

**Actor principal:** Médico.

**Objetivo:** Consultar la evolución clínica de un paciente a partir de sus visitas registradas.

**Precondiciones:**

- El médico ha iniciado sesión.
- El paciente está registrado.

**Flujo principal:**

1. El médico busca al paciente mediante sus datos de identificación.
2. El sistema muestra las coincidencias disponibles, si existen.
3. El médico selecciona al paciente.
4. El sistema presenta un resumen cronológico de sus visitas, incluyendo las fechas y los datos de evolución relevantes, como peso e IMC cuando estén disponibles.
5. El sistema muestra el detalle de las tres visitas más recientes.
6. El médico selecciona una visita anterior si necesita consultar su información detallada.
7. El sistema muestra los datos disponibles de la visita seleccionada.

**Flujos alternativos:**

- Si no se encuentra al paciente, el sistema informa que no existen coincidencias.
- Si el paciente no tiene visitas registradas, el sistema muestra su expediente sin historial de visitas.
- Si no hay datos suficientes para mostrar una medida de evolución, el sistema omite ese dato sin inventar valores.

**Postcondiciones:**

- El médico puede consultar la evolución y los detalles clínicos registrados sin modificar la información histórica.

---

## CU-05. Registrar seguimiento clínico

**Actor principal:** Médico.

**Objetivo:** Registrar la información clínica de seguimiento de un paciente mediante una nueva visita.

**Precondiciones:**

- El médico ha iniciado sesión.
- El paciente está registrado.
- Existe una visita previa si el seguimiento requiere consultar antecedentes clínicos.

**Flujo principal:**

1. El médico busca y selecciona al paciente.
2. El sistema muestra su información clínica disponible.
3. El médico inicia una nueva visita de seguimiento.
4. El médico registra la información correspondiente al seguimiento y los estudios realizados.
5. El sistema valida los datos capturados.
6. El sistema guarda la nueva visita y los estudios asociados.
7. El sistema confirma el registro.

**Flujos alternativos:**

- Si existen campos obligatorios sin completar o valores inválidos, el sistema informa los errores.
- Si la operación se reintenta después de haberse completado, el sistema evita duplicar la visita.
- Si se intenta modificar una visita anterior, el sistema rechaza la operación.

**Postcondiciones:**

- El seguimiento queda registrado como una nueva visita.
- Los datos anteriores se conservan sin modificaciones.

---

## CU-06. Consultar cálculos antropométricos y calóricos

**Actor principal:** Médico.

**Objetivo:** Consultar los resultados de los cálculos clínicos obtenidos a partir de las mediciones y los datos del paciente.

**Precondiciones:**

- El médico ha iniciado sesión.
- El paciente cuenta con una visita y datos suficientes para realizar los cálculos solicitados.

**Flujo principal:**

1. El médico selecciona al paciente y la visita correspondiente.
2. El sistema recupera las mediciones y los datos requeridos.
3. El sistema identifica los cálculos que pueden realizarse con la información disponible.
4. El sistema calcula los resultados mediante las fórmulas clínicas aprobadas.
5. El sistema guarda los resultados asociados a la visita y a las mediciones utilizadas.
6. El sistema presenta los resultados al médico.

**Flujos alternativos:**

- Si faltan datos necesarios, el sistema indica qué información se requiere y no genera resultados incompletos como si fueran válidos.
- Si una fórmula no puede evaluarse con los valores capturados, el sistema informa que el cálculo no está disponible.
- Si se consulta una visita anterior, el sistema muestra los resultados históricos sin modificar la visita ni sus estudios.

**Postcondiciones:**

- Los resultados calculados quedan vinculados a la visita correspondiente.
- Los datos históricos permanecen sin modificaciones.

**Alcance de los cálculos:** Se utilizarán las fórmulas del archivo de Excel proporcionado por el consultorio, una vez validadas por el médico. Estas incluyen cálculos antropométricos y estimaciones energéticas, como IMC, peso ideal, composición corporal, gasto energético basal y gasto energético total.

---

## CU-07. Registrar dieta y medicamentos

**Actor principal:** Médico.

**Objetivo:** Registrar la dieta y los medicamentos indicados durante la atención de un paciente.

**Precondiciones:**

- El médico ha iniciado sesión.
- El paciente está registrado.
- Existe una visita a la que se asociará la información.

**Flujo principal:**

1. El médico busca y selecciona al paciente.
2. El médico selecciona la visita correspondiente.
3. El sistema presenta la información de la visita.
4. El médico captura los datos de dieta y medicamentos indicados.
5. El sistema valida los datos permitidos.
6. El sistema guarda la información en los campos autorizados de la visita.
7. El sistema confirma el registro.

**Flujos alternativos:**

- Si los datos no cumplen las validaciones, el sistema informa los errores.
- Si se intenta modificar una visita anterior, el sistema rechaza la operación.

**Postcondiciones:**

- La dieta y los medicamentos quedan asociados a la visita correspondiente.
- La información se conserva como parte del historial clínico.

**Restricción:** Los cambios se realizan únicamente en los campos autorizados y no sustituyen el documento completo de la visita.

---

## CU-08. Clasificar paciente por padecimiento

**Actor principal:** Médico.

**Objetivo:** Asociar al expediente del paciente los padecimientos identificados clínicamente.

**Precondiciones:**

- El médico ha iniciado sesión.
- El paciente está registrado.
- Los padecimientos que se desean asignar pertenecen al catálogo definido por el médico.

**Flujo principal:**

1. El médico busca y selecciona al paciente.
2. El sistema muestra los padecimientos actualmente asociados.
3. El médico selecciona los padecimientos que corresponden al paciente.
4. El sistema valida que los padecimientos pertenezcan al catálogo autorizado y que no se dupliquen.
5. El médico confirma los cambios.
6. El sistema guarda la clasificación.
7. El sistema confirma la operación.

**Flujos alternativos:**

- Si se selecciona un padecimiento que no pertenece al catálogo, el sistema rechaza la asociación.
- Si el padecimiento ya está asociado, el sistema evita duplicarlo.

**Postcondiciones:**

- Los padecimientos quedan asociados al paciente.
- La información puede utilizarse para consultar pacientes por padecimiento.

---

## CU-09. Vincular pacientes familiares

**Actor principal:** Médico.

**Objetivo:** Registrar relaciones familiares entre pacientes para mantener la información necesaria para los antecedentes heredofamiliares.

**Precondiciones:**

- El médico ha iniciado sesión.
- Los pacientes que se desean relacionar ya están registrados.

**Flujo principal:**

1. El médico busca y selecciona al paciente principal.
2. El médico elige la opción para vincular un familiar.
3. El médico busca y selecciona al otro paciente.
4. El médico especifica el parentesco.
5. El sistema valida que ambos pacientes existan y que la relación sea válida.
6. El sistema registra la relación en ambos expedientes, manteniendo la correspondencia entre los vínculos.
7. El sistema confirma la operación.

**Flujos alternativos:**

- Si alguno de los pacientes no existe, el sistema informa que no puede establecerse la relación.
- Si la relación ya existe, el sistema evita duplicarla.
- Si falla el registro de alguno de los vínculos, el sistema revierte la operación para evitar que la relación quede registrada solo en un expediente.

**Postcondiciones:**

- La relación familiar queda registrada de forma consistente en ambos pacientes.
- La relación puede utilizarse para consultar antecedentes heredofamiliares.

**Restricción:** El vínculo familiar no autoriza por sí mismo la consulta de los expedientes clínicos completos de los familiares.

---

## CU-10. Consultar antecedentes heredofamiliares

**Actor principal:** Médico.

**Objetivo:** Consultar los antecedentes heredofamiliares registrados para un paciente.

**Precondiciones:**

- El médico ha iniciado sesión.
- El paciente está registrado.
- Existen antecedentes heredofamiliares o relaciones familiares registradas para el paciente.

**Flujo principal:**

1. El médico busca y selecciona al paciente.
2. El sistema recupera los antecedentes heredofamiliares registrados.
3. El sistema identifica los familiares vinculados y los datos heredofamiliares disponibles.
4. El sistema presenta la información al médico.

**Flujos alternativos:**

- Si no existen antecedentes heredofamiliares registrados, el sistema informa que no hay información disponible.
- Si no hay familiares vinculados, el sistema muestra que no se han registrado relaciones familiares.

**Postcondiciones:**

- El médico puede consultar los antecedentes heredofamiliares disponibles sin modificar los registros.

**Restricción:** Este caso de uso se limita a antecedentes heredofamiliares. No permite consultar automáticamente las visitas, mediciones, dietas, medicamentos ni expedientes clínicos completos de los familiares.

---

## CU-11. Entregar expediente clínico

**Actor principal:** Médico.

**Objetivo:** Generar un expediente clínico en formato PDF para su entrega al paciente.

**Precondiciones:**

- El médico ha iniciado sesión.
- El paciente está registrado.
- Existe información clínica disponible para incluir en el expediente.

**Flujo principal:**

1. El médico busca y selecciona al paciente.
2. El médico solicita la generación del expediente para su entrega.
3. El sistema recupera la información clínica correspondiente al paciente.
4. El sistema prepara el documento con la información disponible y los documentos que correspondan según el alcance autorizado.
5. El sistema genera el expediente en formato PDF.
6. El sistema presenta el documento al médico para su entrega.

**Flujos alternativos:**

- Si no existe información suficiente para generar el expediente, el sistema informa la situación.
- Si ocurre un error durante la generación del PDF, el sistema informa que el documento no pudo generarse.

**Postcondiciones:**

- Se genera un documento PDF con el expediente preparado para su entrega.
- La generación del documento no modifica la información clínica almacenada.

**Pendiente de especificación:** El contenido exacto del PDF y la inclusión de documentos externos se definirán posteriormente.

---

## CU-12. Consultar pacientes por padecimiento

**Actor principal:** Médico.

**Objetivo:** Obtener un listado de pacientes asociados a uno o varios padecimientos.

**Precondiciones:**

- El médico ha iniciado sesión.
- Existen pacientes registrados y padecimientos definidos en el catálogo.

**Flujo principal:**

1. El médico selecciona la opción para consultar pacientes por padecimiento.
2. El sistema presenta los padecimientos disponibles en el catálogo.
3. El médico selecciona el padecimiento que desea consultar.
4. El sistema busca los pacientes asociados al padecimiento seleccionado.
5. El sistema presenta el listado de resultados.

**Flujos alternativos:**

- Si no hay pacientes asociados al padecimiento, el sistema informa que no se encontraron resultados.
- Si el padecimiento seleccionado no pertenece al catálogo, el sistema solicita seleccionar uno válido.

**Postcondiciones:**

- El médico obtiene un listado de pacientes clasificados con el padecimiento seleccionado.
- La consulta no modifica los expedientes de los pacientes.
