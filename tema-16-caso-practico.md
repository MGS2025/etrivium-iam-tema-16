# Tema 16 — Casos Prácticos

> **Título oficial**: Modelo conceptual de datos. Entidades, atributos y relaciones. Reglas de modelización. Diagramas de flujo de datos. Reglas de construcción. Descomposición en niveles. Flujogramas.
>
> **Versión**: v1.0 — Pendiente validación · **Fecha**: 2026-06-20

Tres casos aplicados al Ayuntamiento de Madrid. Cada caso suma **10 puntos** e integra las tres vistas del modelado (estática, funcional y dinámica) más los flujogramas, en línea con la parte práctica del examen del Grupo II.

---

## Caso 1 — Modelo conceptual (E-R) del Padrón Municipal de Habitantes

### Enunciado

El Servicio de Estadística del Ayuntamiento de Madrid encarga el **modelo conceptual de datos** del Padrón Municipal. Del análisis de requisitos se extrae:

- Cada **habitante** se identifica por su **DNI/NIE**, y se registran nombre, apellidos, fecha de nacimiento, sexo y uno o varios teléfonos de contacto.
- Cada habitante está **empadronado en una vivienda**, y en una vivienda pueden estar empadronados varios habitantes. Todo habitante debe estar empadronado en una vivienda; una vivienda puede no tener a nadie empadronado.
- Cada **vivienda** se identifica por la combinación de su **vía** y un número/planta/puerta, y pertenece a un **distrito**.
- El **distrito** se identifica por un código y tiene un nombre. Un distrito agrupa muchas viviendas.

### Cuestiones

1. **(3 puntos)** Identifica las **entidades** y sus **atributos**, señalando el identificador (clave) de cada una y clasificando los atributos especiales (compuesto, multivaluado, derivado) que detectes.
2. **(3 puntos)** Define las **relaciones** entre las entidades, indicando **grado** y **cardinalidad máxima** (1:1, 1:N, N:M).
3. **(2 puntos)** Especifica la **participación** (total/parcial) de cada entidad en la relación «empadronamiento», justificándola con el enunciado.
4. **(2 puntos)** Indica cómo quedaría la transformación de la relación «empadronamiento» al **modelo relacional** (tablas y claves ajenas).

### Solución orientativa

1. **Entidades y atributos**:
   - `HABITANTE` (clave: <u>DNI/NIE</u>); `nombre_completo` (compuesto: nombre + apellidos); `fecha_nacimiento`; `sexo`; `teléfono` (multivaluado); `edad` sería un atributo **derivado** de `fecha_nacimiento` (no se almacena).
   - `VIVIENDA`: clave compuesta por la vía + número + planta + puerta; podría modelarse como **entidad débil** dependiente de `VÍA`.
   - `DISTRITO` (clave: <u>código_distrito</u>); `nombre`.
2. **Relaciones**:
   - `EMPADRONADO_EN` (HABITANTE–VIVIENDA): binaria, **1:N** (una vivienda, muchos habitantes; cada habitante, una vivienda). Atributo de la relación: `fecha_alta`.
   - `PERTENECE` (VIVIENDA–DISTRITO): binaria, **1:N** (un distrito, muchas viviendas).
3. **Participación** en `EMPADRONADO_EN`: HABITANTE participa de forma **total** («todo habitante debe estar empadronado»); VIVIENDA, **parcial** («una vivienda puede no tener a nadie»). En notación (mín,máx): HABITANTE (1,1), VIVIENDA (0,N).
4. **Transformación**: al ser **1:N**, la clave de VIVIENDA (lado «1») se propaga como **clave ajena** a la tabla `HABITANTE` (lado «N»), junto con `fecha_alta`. No se crea tabla intermedia (eso solo en N:M).

### Criterios de evaluación

- Distinguir atributo derivado (`edad`) y multivaluado (`teléfono`): hasta 1 punto.
- Cardinalidades correctas (1:N en ambas relaciones): hasta 1,5 puntos.
- Participación total/parcial bien justificada: hasta 2 puntos.
- Transformación 1:N con clave ajena en el lado «N» (no tabla intermedia): hasta 2 puntos.

---

## Caso 2 — Diagrama de flujo de datos (DFD) de la gestión de una tasa municipal

### Enunciado

La Agencia Tributaria de Madrid quiere modelar, mediante **análisis estructurado**, el sistema de **gestión de la tasa de paso de vehículos (vado)**. Se sabe que:

- El **contribuyente** presenta una **solicitud** (presencial o telemática). El sistema **valida** los datos y, si son correctos, **liquida** la tasa calculando la base imponible y aplicando el tipo. La **liquidación** se guarda y se envía un **recibo** al contribuyente.
- Cuando el contribuyente paga en una **entidad bancaria**, esta comunica el **cobro**, que el sistema **registra**, marcando la liquidación como pagada.
- Existen dos almacenes: `D1 Liquidaciones` y `D2 Cobros`.

### Cuestiones

1. **(2 puntos)** Dibuja (o describe) el **diagrama de contexto (nivel 0)**: el proceso único, las entidades externas y los flujos de frontera.
2. **(3 puntos)** Descompón el sistema en un **DFD de nivel 1** con los procesos principales y los almacenes.
3. **(2 puntos)** Enuncia **dos reglas de construcción** del DFD y verifica que tu diagrama las cumple.
4. **(3 puntos)** Explica la regla de **equilibrado (balanceo)** y cómo la aplicarías al explotar el proceso «Liquidar tasa» en un nivel 2.

### Solución orientativa

1. **Contexto (nivel 0)**: una sola burbuja «0 · Gestión de la tasa de vado», con entidades externas `CONTRIBUYENTE` y `ENTIDAD_BANCARIA`. Flujos frontera: `solicitud` y `recibo` (con el contribuyente), `cobro` (con el banco). Sin almacenes visibles.
2. **Nivel 1**: procesos «1 Validar solicitud», «2 Liquidar tasa», «3 Registrar cobro». Almacenes `D1 Liquidaciones` (escrito por 2, leído por 3) y `D2 Cobros` (escrito por 3). Flujos internos: `solicitud_válida` (1→2), `liquidación` (2→D1 y 2→recibo), `datos_cobro` (3→D2).
3. **Reglas** (dos cualesquiera): (a) todo flujo pasa por un proceso → no hay flujo directo banco↔almacén; (b) todo proceso tiene ≥1 entrada y ≥1 salida → ni «agujero negro» ni «milagro». El diagrama las cumple.
4. **Equilibrado**: al explotar «2 Liquidar tasa» en «2.1 Calcular base», «2.2 Aplicar tipo», «2.3 Generar liquidación», los flujos que cruzan la frontera del diagrama hijo deben ser **exactamente** los del proceso «2» en el nivel 1: entra `solicitud_válida`, salen `liquidación` (a D1) y `recibo`. Si en el hijo apareciera un flujo de entrada/salida nuevo no presente en el padre, el DFD estaría **desequilibrado**.

### Criterios de evaluación

- Diagrama de contexto con una sola burbuja y sin almacenes: hasta 2 puntos.
- Nivel 1 coherente (procesos verbo+objeto, almacenes numerados): hasta 3 puntos.
- Reglas correctamente enunciadas y verificadas: hasta 2 puntos.
- Equilibrado bien explicado (flujos padre = flujos frontera del hijo): hasta 3 puntos.

---

## Caso 3 — Modelado dinámico (DTE) y flujograma del trámite de una licencia en la sede electrónica

### Enunciado

La sede electrónica del Ayuntamiento gestiona el ciclo de vida de una **licencia urbanística**. El comportamiento es:

- La licencia nace **INICIADA** al presentarse la solicitud. Si se **admite**, pasa a **EN TRAMITACIÓN**.
- Durante la tramitación, si faltan documentos, se **requiere subsanación** (estado **SUBSANACIÓN**); cuando el ciudadano **subsana** dentro de plazo, vuelve a **EN TRAMITACIÓN**.
- Tras el informe técnico, la licencia se **RESUELVE** (concedida o denegada) y, al **notificarse**, queda **ARCHIVADA** (estado final).

Además, el proceso «**comprobar plazo de subsanación**» debe documentarse como **flujograma**: se lee la fecha límite; si la fecha actual es posterior, se declara la solicitud **caducada**; en caso contrario, se admite la documentación subsanada.

### Cuestiones

1. **(3 puntos)** Construye el **diagrama de transición de estados (DTE)**: estados, transiciones y los **eventos** que las disparan; señala el estado inicial y el final.
2. **(2 puntos)** Etiqueta al menos una transición con el patrón **`evento [condición] / acción`**.
3. **(3 puntos)** Dibuja el **flujograma** del proceso «comprobar plazo de subsanación» usando los símbolos normalizados (terminal, E/S, proceso, decisión).
4. **(2 puntos)** Indica qué **estructura de control** (secuencia, selección o iteración) emplea ese flujograma y por qué.

### Solución orientativa

1. **DTE**: estados `INICIADA` → `EN TRAMITACIÓN` → (`SUBSANACIÓN`) → `RESUELTA` → `ARCHIVADA`. Estado inicial: pseudoestado inicial → `INICIADA`. Estado final: `ARCHIVADA`. Eventos: `admitir`, `requerir`, `subsanar`, `resolver`, `notificar`.
2. **Transición etiquetada**: `requerir [falta documentación] / registrar requerimiento` (de EN TRAMITACIÓN a SUBSANACIÓN); o `subsanar [dentro de plazo] / aceptar documentación` (de SUBSANACIÓN a EN TRAMITACIÓN).
3. **Flujograma**: `Inicio` (óvalo) → `Leer fecha_límite y fecha_actual` (romboide E/S) → `¿fecha_actual > fecha_límite?` (rombo): rama **Sí** → `Marcar solicitud CADUCADA` (rectángulo); rama **No** → `Admitir documentación subsanada` (rectángulo); ambas ramas → `Fin` (óvalo).
4. **Estructura de control**: es una **selección** (condicional simple `si-entonces-si_no`), representada por el único rombo con dos ramas excluyentes. No hay repetición (no es iteración) ni mera sucesión (no es solo secuencia).

### Criterios de evaluación

- DTE con estado inicial único, estados excluyentes y eventos en las transiciones: hasta 3 puntos.
- Etiqueta `evento [condición] / acción` correcta: hasta 2 puntos.
- Flujograma con símbolos normalizados correctos (óvalo/romboide/rombo/rectángulo) y un solo fin: hasta 3 puntos.
- Identificación de la selección como estructura de control: hasta 2 puntos.
