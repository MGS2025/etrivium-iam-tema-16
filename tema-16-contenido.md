# Tema 16 — Contenido Teórico

> **Título oficial**: Modelo conceptual de datos. Entidades, atributos y relaciones. Reglas de modelización. Diagramas de flujo de datos. Reglas de construcción. Descomposición en niveles. Flujogramas.
>
> **Bloque**: Parte II — Técnico
> **Nivel**: C1 — Técnico Auxiliar TIC, Ayuntamiento de Madrid
> **Versión**: v1.0 — Pendiente validación
> **Fecha generación**: 2026-06-20
> **Fuentes**: Ver tema-16-fuentes.md · **Diagramas**: Ver tema-16-diagramas.md · **Cambios**: Ver tema-16-changelog.md

---

## Convenciones del documento

Este tema incluye cuatro tipos de **cajas callout** para facilitar el estudio:

> **[DATO CLAVE EXAMEN]** Información de alta densidad memorística, con alta probabilidad de aparecer en el test oficial.

> **[EJERCICIO RESUELTO]** Problema + solución paso a paso (modelado de un E-R, niveles de un DFD, traza de un flujograma).

> **[EJEMPLO AYTO MADRID]** Aplicación real de la teoría al entorno municipal (Padrón, callejero, tributos, sede electrónica).

> **[REFERENCIA CRUZADA]** Enlace conceptual a otros temas del temario oficial.

Las fuentes se referencian con etiquetas breves tipo `[CHEN]` o `[ELMASRI, cap. 3]` — el registro completo está en `tema-16-fuentes.md`. Este tema combina **notación clásica** (la tradicional en oposiciones, alineada con MÉTRICA v3) y **UML** (estándar moderno), señalando la equivalencia entre ambas en cada técnica.

---

## 1. El modelado de sistemas de información

### 1.1. Concepto de modelo, dato y modelo de datos

Un **dato** es la representación simbólica (numérica, alfabética, etc.) de un atributo de una entidad del mundo real; carece de significado por sí solo hasta que se procesa e interpreta como **información**. Un **sistema de información (SI)** capta, almacena, procesa y distribuye esa información para apoyar la toma de decisiones de una organización. [METRICA3]

Un **modelo** es una representación abstracta y simplificada de una parcela de la realidad (el *universo del discurso* o dominio), que retiene los aspectos relevantes para un propósito y descarta el resto. Modelar es, por tanto, **abstraer**: decidir qué es esencial y cómo representarlo. [PRESSMAN]

Un **modelo de datos** es un conjunto de **conceptos, reglas y notación** que permiten describir la estructura de una base de datos: los datos, sus relaciones, su semántica y las restricciones de integridad. [ELMASRI, cap. 2] Según el nivel de abstracción, se distinguen tres categorías:

- **Modelos conceptuales (de alto nivel o semánticos)**: próximos a cómo percibe los datos el usuario; independientes de cualquier gestor. El **modelo Entidad-Relación** es el más representativo.
- **Modelos lógicos (de implementación o representativos)**: próximos a cómo organiza los datos el SGBD. El **modelo relacional** es el dominante (ver Tema 17).
- **Modelos físicos (de bajo nivel)**: describen *cómo* se almacenan los datos en el soporte (ficheros, índices, bloques).

> **[DATO CLAVE EXAMEN]** **Modelo conceptual** = independiente del SGBD, cercano al usuario (E-R). **Modelo lógico** = dependiente del tipo de SGBD, cercano al diseñador (relacional). **Modelo físico** = dependiente del producto y del soporte (almacenamiento). No confundir los tres niveles: es la pregunta clásica del bloque de bases de datos.

> **[REFERENCIA CRUZADA]** El **modelo conceptual de datos** (este tema) precede al **diseño lógico y físico y la normalización** (Tema 17), y se materializa en algún tipo de **SGBD** (Tema 15). El modelo de datos es el puente entre el análisis de requisitos y la base de datos operativa.

### 1.2. Niveles de abstracción: la arquitectura ANSI/SPARC

En 1975, el comité **ANSI/X3/SPARC** propuso una arquitectura de **tres esquemas** para separar la visión que cada agente tiene de los datos y conseguir **independencia de datos**. [ANSI-SPARC] Es la base teórica de todo el modelado:

1. **Nivel externo (o de vistas)**: describe la parte de la base de datos que interesa a **cada grupo de usuarios**. Puede haber muchos esquemas externos (vistas), uno por perfil. Oculta el resto de los datos.
2. **Nivel conceptual (o lógico global)**: describe **toda** la estructura de la base de datos para la comunidad de usuarios: entidades, atributos, relaciones y restricciones. Es **único** y no contiene detalles de almacenamiento. Aquí vive el **modelo conceptual de datos**.
3. **Nivel interno (o físico)**: describe **cómo** se almacenan físicamente los datos: estructuras de ficheros, índices, rutas de acceso, ubicación en el soporte. Es **único**.

> **[DATO CLAVE EXAMEN]** ANSI/SPARC: **externo (vistas, varios)** → **conceptual (global, único)** → **interno (físico, único)**. La correspondencia entre esquemas se llama *mapping*. Es muy típico preguntar cuántos esquemas hay de cada tipo: **varios externos, un conceptual, un interno**.

### 1.3. Independencia de datos

La arquitectura de tres esquemas hace posible la **independencia de datos**: la capacidad de modificar el esquema de un nivel sin tener que alterar el del nivel superior. [DATE] Hay dos tipos:

- **Independencia física**: se puede cambiar el **esquema interno** (reorganizar ficheros, añadir un índice, cambiar de disco) sin modificar el esquema conceptual ni las aplicaciones. Es la más fácil de lograr.
- **Independencia lógica**: se puede cambiar el **esquema conceptual** (añadir una entidad o un atributo) sin modificar los esquemas externos ni reescribir las aplicaciones que no usan ese cambio. Es más difícil, porque las vistas dependen del esquema conceptual.

> **[DATO CLAVE EXAMEN]** **Física** = aísla el conceptual de cambios en el almacenamiento. **Lógica** = aísla las vistas/aplicaciones de cambios en el esquema conceptual. La independencia lógica es la **más difícil** de conseguir.

### 1.4. El modelo de dominio y el modelo conceptual de datos

El **modelo de dominio** (o modelo del *universo del discurso*) captura los conceptos del negocio y sus relaciones tal como existen en la realidad, **antes** de pensar en la solución informática. El **modelo conceptual de datos** es la formalización de ese dominio en términos de **entidades, atributos y relaciones**, usando una técnica como el E-R. [CHEN]

Sus características fundamentales son:

- **Independencia tecnológica**: no presupone ningún SGBD ni lenguaje.
- **Expresividad semántica**: refleja el significado del negocio, no detalles técnicos.
- **Validable por el usuario**: un experto del dominio (no informático) debe poder entenderlo y confirmarlo.
- **Estable**: cambia solo si cambia el negocio, no si cambia la tecnología.

> **[EJEMPLO AYTO MADRID]** El modelo de dominio del **Padrón Municipal de Habitantes** identifica conceptos como *Habitante*, *Vivienda*, *Vía* (calle del callejero), *Distrito* y *Barrio*, y relaciones como «un habitante *está empadronado en* una vivienda» o «una vía *pertenece a* un distrito». Esto se decide con los técnicos de Estadística del Ayuntamiento, **sin** hablar todavía de tablas ni de Oracle: es modelado conceptual puro.

### 1.5. Técnicas y tipos de modelado: estático, dinámico y funcional

Un sistema de información se describe desde **tres perspectivas complementarias**, cada una con su técnica de diagramado. Esta clasificación (heredada del análisis estructurado y de OMT) vertebra todo el tema: [RUMBAUGH][YOURDON]

| Perspectiva | Pregunta que responde | Técnica clásica | Equivalente UML |
|---|---|---|---|
| **Estática (datos)** | ¿Qué datos hay y cómo se relacionan? | Modelo Entidad-Relación (E-R) | Diagrama de clases |
| **Dinámica (comportamiento)** | ¿Cómo cambia de estado el sistema ante los eventos? | Diagrama de Transición de Estados (DTE) | Diagrama de estados |
| **Funcional (procesos)** | ¿Qué transformaciones sufren los datos al fluir? | Diagrama de Flujo de Datos (DFD) | Diagrama de actividad |

> **[DATO CLAVE EXAMEN]** Memoriza la terna: **estático → E-R**, **dinámico → DTE**, **funcional → DFD**. El enunciado oficial del tema recorre exactamente estas tres vistas más los **flujogramas** (que detallan la lógica de un proceso).

---

## 2. Modelado estático: el modelo Entidad-Relación (E-R)

### 2.1. Origen y propósito

El **modelo Entidad-Relación** fue propuesto por **Peter Chen en 1976** como una vista unificada de los datos, independiente de su implementación. [CHEN] Es el estándar *de facto* para el **diseño conceptual** de bases de datos: representa la realidad mediante tres construcciones básicas —**entidades**, **atributos** y **relaciones (interrelaciones)**— y un diagrama legible llamado **diagrama entidad-relación (DER)**.

### 2.2. Entidades

Una **entidad** es un objeto del mundo real, concreto o abstracto, con existencia propia y distinguible de los demás, sobre el que se quiere almacenar información. [ELMASRI, cap. 3] Hay que distinguir:

- **Tipo de entidad** (o entidad, en sentido genérico): la *plantilla* o categoría, p. ej. `HABITANTE`. En el diagrama es un **rectángulo**.
- **Ocurrencia** (o instancia, ejemplar): un elemento concreto de ese tipo, p. ej. el habitante con DNI 50.123.456-X. Las ocurrencias **no** se dibujan; pueblan la base de datos.

Según su dependencia de existencia, las entidades se clasifican en:

- **Entidad fuerte (regular)**: tiene existencia propia y un identificador (clave) formado por sus propios atributos. P. ej. `HABITANTE`.
- **Entidad débil**: su existencia depende de otra entidad (la *propietaria* o *fuerte*) y **no** puede identificarse solo con sus atributos; necesita la clave de la entidad fuerte más un **discriminante** (clave parcial). En el diagrama es un **rectángulo doble**. P. ej. `VOLUMEN_EXPEDIENTE` depende de `EXPEDIENTE`.

> **[DATO CLAVE EXAMEN]** **Entidad fuerte**: se identifica sola (rectángulo simple). **Entidad débil**: depende de otra y se identifica con la clave ajena + un discriminante propio (rectángulo doble; la relación que la liga es una *relación identificadora*, en rombo doble).

### 2.3. Atributos

Un **atributo** es una propiedad o característica de una entidad (o de una relación) que interesa almacenar. [CHEN] En notación de Chen se dibuja como una **elipse** unida a su entidad. El conjunto de valores válidos de un atributo es su **dominio** (p. ej. el dominio de *sexo* es {H, M}). [ISO11404] Tipos de atributos:

- **Simple (atómico)** vs **compuesto**: el compuesto se descompone en partes con significado propio. P. ej. `domicilio` = (vía, número, planta, puerta, código postal).
- **Monovaluado** vs **multivaluado**: el multivaluado puede tomar varios valores para una misma ocurrencia. P. ej. `teléfono` (varios). Se dibuja con **elipse doble**.
- **Almacenado** vs **derivado (calculado)**: el derivado se obtiene de otros. P. ej. `edad` se deriva de `fecha_nacimiento`. Se dibuja con **elipse de línea discontinua**.
- **Identificador (clave)**: atributo o conjunto de atributos cuyo valor identifica unívocamente cada ocurrencia. Se **subraya**. Puede haber varias claves candidatas; se elige una **clave primaria**.

> **[DATO CLAVE EXAMEN]** Representación en Chen: atributo = elipse; **clave = subrayado**; **multivaluado = elipse doble**; **derivado = elipse discontinua**; **compuesto = elipse con elipses hijas**. Esta «iconografía» se pregunta literalmente.

> **[EJEMPLO AYTO MADRID]** En `HABITANTE`, el atributo identificador es el **DNI/NIE** (subrayado); `nombre_completo` es **compuesto** (nombre + apellidos); `teléfono_contacto` puede ser **multivaluado**; y `edad` es **derivada** de la fecha de nacimiento (no se almacena, se calcula).

### 2.4. Relaciones: grado, cardinalidad y participación

Una **relación (interrelación)** es una asociación con significado entre dos o más entidades. [CHEN] En notación de Chen se dibuja como un **rombo** que une las entidades participantes. Una relación también puede tener atributos propios (p. ej. `fecha` en la relación `EMPADRONADO_EN`). Tres propiedades caracterizan una relación:

**a) Grado**: número de tipos de entidad que participan.

- **Unaria (recursiva)**: una entidad se relaciona consigo misma. P. ej. `EMPLEADO supervisa a EMPLEADO`.
- **Binaria**: dos entidades (el caso más frecuente).
- **Ternaria**: tres entidades. P. ej. `PROVEEDOR – PROYECTO – PIEZA`.

**b) Cardinalidad (razón de cardinalidad)**: número máximo de ocurrencias de una entidad que pueden asociarse a una ocurrencia de la otra. En relaciones binarias:

- **Uno a uno (1:1)**: cada ocurrencia de A se asocia con una de B y viceversa.
- **Uno a muchos (1:N)**: una ocurrencia de A se asocia con varias de B, pero cada B con una sola A.
- **Muchos a muchos (N:M)**: una ocurrencia de A se asocia con varias de B y viceversa.

**c) Participación (cardinalidad mínima)**: indica si la participación de una entidad en la relación es obligatoria u opcional.

- **Total (obligatoria)**: toda ocurrencia de la entidad debe participar en la relación (mínimo 1). Se dibuja con **línea doble** en Chen.
- **Parcial (opcional)**: alguna ocurrencia puede no participar (mínimo 0).

La notación **(mín, máx)** combina ambas: junto a cada entidad se anota el par cardinalidad mínima y máxima de sus ocurrencias en la relación. P. ej. `(1,1)` o `(0,N)`.

> **[DATO CLAVE EXAMEN]** No confundir **cardinalidad máxima** (1:1, 1:N, N:M → *cuántas* como tope) con **participación o cardinalidad mínima** (total/parcial → *si es obligatoria*). La notación (mín, máx) reúne las dos. Cuidado: la posición de la etiqueta (mín,máx) varía entre escuelas (Chen la pone *cruzada*, MÉTRICA la pone *del lado de la entidad*); en el examen suele especificarse.

> **[EJERCICIO RESUELTO]** *Modela: «Un distrito tiene muchos barrios; cada barrio pertenece a un único distrito; todo barrio pertenece obligatoriamente a un distrito y todo distrito tiene al menos un barrio».*
> Entidades: `DISTRITO`, `BARRIO`. Relación: `CONTIENE` (rombo). Cardinalidad: **1:N** (un distrito, muchos barrios). Participación: **total en ambos lados** (todo barrio tiene distrito → total en BARRIO; todo distrito tiene ≥1 barrio → total en DISTRITO). En notación (mín,máx): DISTRITO `(1,N)`, BARRIO `(1,1)`.

### 2.5. Reglas de modelización y construcción del diagrama E-R

Construir un buen modelo E-R sigue un proceso y unas reglas heurísticas: [ELMASRI, cap. 3][METRICA3]

1. **Identificar las entidades** a partir de los sustantivos relevantes del dominio (objetos sobre los que se guarda información). Descartar los que sean realmente atributos.
2. **Identificar las relaciones** a partir de los verbos que conectan entidades.
3. **Asignar los atributos** a la entidad o relación a la que pertenecen; elegir el **identificador** de cada entidad.
4. **Determinar grado, cardinalidad y participación** de cada relación.
5. **Detectar entidades débiles** y sus relaciones identificadoras.
6. **Aplicar generalización/especialización** cuando haya entidades con atributos comunes y específicos.
7. **Revisar y validar** con el usuario; eliminar redundancias.

Reglas de buena construcción (errores típicos a evitar):

- Un **atributo no debe modelarse como entidad** salvo que tenga atributos propios o participe en relaciones (p. ej. `color` es atributo, pero `MARCA` con sus propios datos es entidad).
- Evitar **relaciones redundantes** (una relación deducible de otras dos).
- Un atributo que solo tiene sentido para la combinación de dos entidades pertenece a la **relación**, no a una entidad.
- Nombrar entidades en **singular** y relaciones con un **verbo**.

### 2.6. Técnicas de descomposición: generalización/especialización, agregación y asociación

El **modelo E-R extendido (EER)** añade construcciones semánticas para casos complejos: [ELMASRI, cap. 4]

- **Generalización / Especialización (jerarquía «es-un», is-a)**: una entidad **supertipo** agrupa atributos comunes y varias entidades **subtipo** añaden atributos específicos. *Especializar* es el proceso descendente (de lo general a lo particular); *generalizar*, el ascendente. P. ej. supertipo `PERSONAL`, subtipos `FUNCIONARIO` y `LABORAL`. Restricciones:
  - **Disyunción**: *disjunta* (un ejemplar pertenece a un solo subtipo) vs *solapada* (puede pertenecer a varios).
  - **Completitud**: *total* (todo ejemplar del supertipo está en algún subtipo) vs *parcial*.
- **Agregación**: trata una **relación** como si fuera una entidad de nivel superior para poder relacionarla con otra entidad (relación de relaciones). P. ej. la relación `TRABAJA_EN(EMPLEADO, PROYECTO)` se agrega para relacionarla con `MAQUINARIA`.
- **Asociación**: vínculo «parte-de» (composición/agregación en sentido UML) entre un todo y sus partes.

> **[DATO CLAVE EXAMEN]** **Generalización/especialización** = jerarquía *es-un* (herencia de atributos del supertipo). Atención a las dos parejas de restricciones: **disjunta/solapada** y **total/parcial**. La **agregación** del EER es «tratar una relación como entidad»; no confundir con la agregación de UML.

> **[REFERENCIA CRUZADA]** La jerarquía de generalización/especialización del EER es el antecedente directo de la **herencia** en la **Programación Orientada a Objetos** (Tema 20). Un supertipo E-R ↔ una superclase; un subtipo ↔ una subclase que hereda y extiende.

### 2.7. Notaciones: Chen, pata de gallo y UML

La misma semántica E-R se dibuja con notaciones distintas; conviene reconocerlas todas: [SILBERSCHATZ][MARTIN]

- **Chen (1976)**: entidades en rectángulo, atributos en elipse, relaciones en rombo. Muy expresiva pero ocupa mucho espacio. La cardinalidad se anota con `1`, `N`, `M` sobre las líneas.
- **Pata de gallo (crow's foot, Information Engineering de Martin)**: entidades en rectángulo con sus atributos dentro; las relaciones son líneas cuyos **extremos** codifican la cardinalidad con símbolos (una raya = uno; «pata de gallo» = muchos; círculo = opcional/cero). Es la más usada en herramientas CASE.
- **UML (diagrama de clases)**: las entidades son **clases** (rectángulo con compartimentos), las relaciones son **asociaciones** con **multiplicidad** `1`, `0..1`, `1..*`, `*`. La generalización usa el triángulo de herencia. [UML]

| Concepto E-R | Chen | Pata de gallo | UML |
|---|---|---|---|
| Entidad | Rectángulo | Rectángulo con campos | Clase |
| Atributo | Elipse | Línea dentro del rectángulo | Atributo de clase |
| Relación | Rombo | Línea con extremos | Asociación |
| Cardinalidad N:M | `N`…`M` sobre líneas | doble pata de gallo | `*`…`*` |
| Generalización | Triángulo/«ISA» | — | Triángulo de herencia |

> **[DATO CLAVE EXAMEN]** En **pata de gallo**, los símbolos se leen *junto a la entidad del extremo*: «||» = uno y solo uno; «o<» = cero o muchos; «|<» = uno o muchos. Es la notación que generan casi todas las herramientas (ERwin, MySQL Workbench…). UML usa **multiplicidad** numérica (`0..1`, `1..*`).

### 2.8. Del modelo E-R al modelo relacional

El modelo conceptual E-R se **transforma** en un modelo lógico relacional siguiendo reglas mecánicas (este paso pertenece al diseño lógico, Tema 17, pero conviene conocerlo): [ELMASRI, cap. 9][CODD]

- Cada **entidad** → una **tabla (relación)**; sus atributos → columnas; su identificador → **clave primaria**.
- Relación **1:N** → la clave de la entidad del lado «1» se propaga como **clave ajena** a la tabla del lado «N».
- Relación **N:M** → se crea una **tabla intermedia** cuya clave primaria es la combinación de las claves de ambas entidades (más los atributos propios de la relación).
- Relación **1:1** → la clave ajena se coloca en cualquiera de las dos tablas (preferiblemente en la de participación total).
- Atributo **multivaluado** → tabla aparte con la clave de la entidad + el valor.
- **Entidad débil** → tabla con la clave de la entidad fuerte + su discriminante como clave primaria compuesta.

> **[REFERENCIA CRUZADA]** Esta transformación es la entrada del **Tema 17 (Diseño lógico y físico, modelo relacional y normalización)**. El resultado se refina con las **formas normales** para eliminar redundancias y anomalías. El SQL que crea esas tablas es el **Tema 19**.

---

## 3. Modelado dinámico: el diagrama de transición de estados (DTE)

### 3.1. Estados, transiciones, eventos, condiciones y acciones

El **modelado dinámico** describe el **comportamiento** del sistema a lo largo del tiempo: cómo reacciona ante los **eventos** y cómo va cambiando de **estado**. La técnica clásica es el **diagrama de transición de estados (DTE)**, una máquina de estados finita. [YOURDON][RUMBAUGH] Sus elementos:

- **Estado**: situación estable en la que se encuentra un objeto o el sistema durante un intervalo, esperando un evento. Se dibuja como un **rectángulo redondeado**. Hay un **estado inicial** (círculo relleno) y, opcionalmente, **estados finales** (círculo con borde).
- **Transición**: paso de un estado a otro. Se dibuja como una **flecha** etiquetada.
- **Evento (suceso)**: estímulo que dispara una transición (la llegada de un dato, una acción del usuario, el vencimiento de un plazo).
- **Condición (guarda)**: predicado que debe cumplirse para que la transición ocurra. Se escribe entre corchetes `[condición]`.
- **Acción**: operación que se ejecuta al producirse la transición (o al entrar/salir de un estado).

La etiqueta de una transición sigue el patrón **`evento [condición] / acción`**.

> **[EJEMPLO AYTO MADRID]** El ciclo de vida de un **expediente administrativo** en la sede electrónica es un DTE natural: estados `INICIADO` → `EN_TRAMITACIÓN` → `PENDIENTE_SUBSANACIÓN` → `RESUELTO` → `NOTIFICADO` → `ARCHIVADO`. El evento «presentar alegación» con condición `[plazo abierto]` dispara la transición a `EN_TRAMITACIÓN`; la acción asociada es «registrar entrada».

### 3.2. Reglas de construcción del DTE

- Todo diagrama tiene **un único estado inicial** y puede tener varios finales.
- Cada **transición** parte de un estado y llega a un estado (posiblemente el mismo: *autotransición*).
- Una transición se etiqueta con el **evento** que la dispara; sin evento no hay cambio de estado.
- Los estados deben ser **mutuamente excluyentes**: el sistema está en uno y solo uno en cada instante.
- No deben existir **estados inalcanzables** (sin transición de entrada) ni **callejones sin salida** no deseados (estados sin salida que no sean finales).

> **[DATO CLAVE EXAMEN]** En un DTE/máquina de estados: **un estado inicial**, **estados mutuamente excluyentes**, **transiciones disparadas por eventos**. Etiqueta de transición: `evento [guarda] / acción`. Las autotransiciones (vuelven al mismo estado) son válidas.

### 3.3. Equivalencia con las máquinas de estados y UML

El DTE clásico equivale a una **máquina de estados finita**. UML lo recoge y amplía en el **diagrama de estados (state machine diagram)**, que añade: estados compuestos (anidados), regiones concurrentes, acciones de entrada/salida (`entry/`, `exit/`), actividades internas (`do/`) y pseudoestados (histórico, unión, decisión). [UML][FOWLER]

> **[REFERENCIA CRUZADA]** Las máquinas de estados son también la base de muchos **algoritmos** (Tema 13) y del análisis léxico de **lenguajes** (Tema 18). Un autómata finito determinista es, formalmente, un DTE sin acciones.

---

## 4. Modelado funcional: el diagrama de flujo de datos (DFD)

### 4.1. Componentes del DFD

El **diagrama de flujo de datos (DFD)** modela el sistema como una **red de procesos** que transforman datos, mostrando *qué* hace el sistema con la información (no *cómo* ni *cuándo*). Es la herramienta central del **análisis estructurado** de DeMarco, Yourdon y Gane/Sarson. [DEMARCO][YOURDON] Tiene **cuatro** elementos:

1. **Proceso (función, burbuja)**: transforma flujos de datos de entrada en flujos de salida. Se dibuja como **círculo** (Yourdon/DeMarco) o **rectángulo redondeado** (Gane/Sarson). Se numera (1, 2, 3…). El nombre es un **verbo + objeto** («Validar solicitud»).
2. **Flujo de datos**: dato en movimiento entre componentes. Se dibuja como una **flecha** etiquetada con el nombre del dato.
3. **Almacén de datos (data store)**: dato en reposo (un fichero, una tabla, un archivo). Se dibuja como **dos líneas paralelas** (Yourdon) o un rectángulo abierto (Gane/Sarson). Se numera con D1, D2…
4. **Entidad externa (origen/destino, terminador)**: persona, organización u otro sistema, **externo** al ámbito modelado, que produce o consume datos. Se dibuja como un **rectángulo**.

> **[DATO CLAVE EXAMEN]** Los **cuatro** componentes del DFD: **proceso** (transforma), **flujo** (dato en movimiento), **almacén** (dato en reposo) y **entidad externa** (frontera del sistema). Es la pregunta más repetida del epígrafe. El DFD modela *función*, **no** secuencia temporal ni decisiones (eso es el flujograma).

### 4.2. Reglas de construcción del DFD

El análisis estructurado fija reglas estrictas de buena formación: [DEMARCO][GANE-SARSON]

- **Conservación de datos**: un proceso no puede generar de la nada datos de salida que no se deriven de sus entradas, ni «tragarse» entradas sin producir salida.
- **Un flujo siempre toca al menos un proceso**: están **prohibidos** los flujos directos entre dos almacenes, entre dos entidades externas, o entre una entidad externa y un almacén. Todo dato debe pasar por un proceso.
- **Procesos con entrada y salida**: un proceso solo con entradas es un *sumidero* erróneo («agujero negro»); solo con salidas, una *fuente* imposible («milagro»).
- **Nombres significativos**: procesos con verbo; flujos y almacenes con sustantivo.
- **Numeración jerárquica** de los procesos para soportar la descomposición.

> **[DATO CLAVE EXAMEN]** Reglas «negativas» del DFD que más se preguntan: **no** hay flujo directo almacén↔almacén, entidad↔entidad, ni entidad↔almacén; **siempre** media un proceso. Y todo proceso debe tener **al menos una entrada y una salida** (ni «agujero negro» ni «milagro»).

### 4.3. Descomposición en niveles

Un sistema real no cabe en un solo diagrama. El DFD se construye **por niveles**, mediante **descomposición funcional descendente** (top-down), explotando cada proceso en un diagrama más detallado: [DEMARCO][YOURDON]

- **Nivel 0 — Diagrama de contexto**: un **único proceso** (la «burbuja 0») que representa **todo el sistema**, rodeado de las **entidades externas** y los flujos que cruzan la frontera. No tiene almacenes visibles. Define el **alcance** del sistema.
- **Nivel 1 — Diagrama de sistema**: explota el proceso 0 en los **procesos principales** (1, 2, 3…), mostrando ya los almacenes internos.
- **Niveles 2, 3… — Explosión**: cada proceso `n` se descompone en subprocesos `n.1`, `n.2`… hasta llegar a procesos **elementales** (primitivas funcionales) que ya no se descomponen y se describen con una *mini-spec*.

La regla que garantiza la coherencia entre niveles es el **equilibrado (balanceo)**: los flujos de entrada y salida de un proceso deben **coincidir** con los flujos que cruzan la frontera de su diagrama hijo (explosión). Si un proceso recibe `A` y produce `B`, su diagrama de descomposición debe tener exactamente `A` entrando y `B` saliendo.

> **[DATO CLAVE EXAMEN]** **Diagrama de contexto = nivel 0 = una sola burbuja + entidades externas, sin almacenes.** La descomposición numera `1` → `1.1`, `1.2`… El **equilibrado/balanceo** exige que los flujos del proceso padre = flujos frontera del diagrama hijo. Un proceso que ya no se descompone es una **primitiva funcional**.

> **[EJERCICIO RESUELTO]** *Sitúa por niveles el sistema de «Gestión de tributos municipales».*
> **Nivel 0 (contexto)**: burbuja «0 · Gestión de tributos» con entidades externas `CONTRIBUYENTE`, `ENTIDAD_BANCARIA` y `PADRÓN` (otro sistema). Flujos: «declaración», «recibo», «cobro».
> **Nivel 1**: procesos «1 Liquidar tributo», «2 Emitir recibo», «3 Registrar cobro», con almacenes `D1 Liquidaciones`, `D2 Cobros`.
> **Nivel 2**: «1 Liquidar tributo» se explota en «1.1 Calcular base imponible», «1.2 Aplicar tipo», «1.3 Generar liquidación». Se comprueba el **equilibrado**: los flujos que entran/salen de «1» en el nivel 1 son los mismos que cruzan la frontera del diagrama 1.x.

### 4.4. Diccionario de datos y especificación de procesos

El DFD se acompaña de dos artefactos que completan el modelo funcional: [DEMARCO]

- **Diccionario de datos (DD)**: repositorio que **define** rigurosamente cada flujo, almacén y dato elemental del DFD, usando una notación de composición:
  - `=` (se compone de), `+` (y/concatenación), `{ }` (iteración/repetición), `[ | ]` (selección/alternativa), `( )` (opcional).
  - P. ej.: `solicitud = nº_registro + fecha + datos_solicitante + [presencial | telemática]`.
- **Especificación de procesos (mini-spec o P-SPEC)**: describe la **lógica** de cada proceso **primitivo** (los que ya no se descomponen), mediante **pseudocódigo**, **tablas de decisión** o **lenguaje estructurado**. Aquí es donde el modelado funcional enlaza con los **flujogramas**.

> **[DATO CLAVE EXAMEN]** El **diccionario de datos** define los datos (con `= + { } [ ] ( )`); la **mini-spec** define la lógica de los procesos primitivos. Juntos, DFD + DD + mini-specs forman el **modelo de procesos** completo del análisis estructurado.

### 4.5. Notaciones: Yourdon/DeMarco frente a Gane/Sarson

| Componente | Yourdon / DeMarco | Gane / Sarson |
|---|---|---|
| Proceso | Círculo (burbuja) | Rectángulo de esquinas redondeadas |
| Flujo de datos | Flecha curva | Flecha recta |
| Almacén | Dos líneas paralelas abiertas | Rectángulo abierto por la derecha |
| Entidad externa | Rectángulo | Rectángulo (a veces con sombra) |

Ambas notaciones son **semánticamente equivalentes**; la elección es de estilo o de la herramienta CASE. En UML, el papel del DFD lo cubre parcialmente el **diagrama de actividad** (flujo de acciones y objetos). [UML]

> **[REFERENCIA CRUZADA]** El DFD describe *qué* hace el sistema con los datos; las estructuras de esos datos en reposo (los almacenes) se diseñan con el **modelo E-R** (§2) y acaban en un **SGBD** (Tema 15). DFD (procesos) y E-R (datos) son las dos caras del análisis estructurado.

---

## 5. Flujogramas, reglas de construcción y UML

### 5.1. Concepto y propósito del flujograma

Un **flujograma** (diagrama de flujo, *flowchart*) es la representación gráfica de la **secuencia lógica de pasos** de un proceso o algoritmo, mostrando el **orden de ejecución** y las **decisiones**. A diferencia del DFD (que muestra *transformaciones* de datos sin orden temporal), el flujograma sí refleja la **secuencia y el control** del flujo. [ISO5807] Se usa para documentar algoritmos, procedimientos administrativos y la lógica de los procesos primitivos de un DFD.

> **[DATO CLAVE EXAMEN]** **DFD ≠ flujograma.** El DFD modela el **flujo de datos** (qué se transforma) sin secuencia temporal; el **flujograma** modela el **flujo de control** (en qué orden, con qué decisiones). Es una distinción que el examen busca confundir.

### 5.2. Símbolos normalizados (ISO 5807 / ANSI)

La norma **ISO 5807:1985** (heredera de ANSI X3.5) normaliza los símbolos del flujograma: [ISO5807][ANSI-X3.5]

| Símbolo | Forma | Significado |
|---|---|---|
| **Terminal** | Óvalo / rectángulo redondeado | Inicio y fin del proceso |
| **Proceso** | Rectángulo | Operación o acción (asignación, cálculo) |
| **Decisión** | Rombo | Bifurcación según una condición (sí/no) |
| **Entrada/Salida** | Romboide (paralelogramo) | Lectura o escritura de datos |
| **Subrutina** | Rectángulo con doble borde lateral | Llamada a un proceso predefinido |
| **Conector** | Círculo pequeño | Une partes del diagrama (misma página) |
| **Conector de página** | Pentágono | Une partes en distinta página |
| **Línea de flujo** | Flecha | Sentido del flujo (por defecto, arriba→abajo, izq→der) |

> **[DATO CLAVE EXAMEN]** Memoriza los tres símbolos básicos: **óvalo = inicio/fin (terminal)**, **rectángulo = proceso**, **rombo = decisión**. El **romboide/paralelogramo = entrada/salida**. El rombo es el único con **varias salidas** (las ramas de la condición).

### 5.3. Estructuras básicas: secuencia, selección e iteración

El **teorema de Böhm-Jacopini (1966)** demuestra que cualquier algoritmo puede expresarse combinando **solo tres estructuras de control**, sin saltos incondicionales (*goto*). Es el fundamento de la **programación estructurada**: [BOHM-JACOPINI]

1. **Secuencia**: una acción tras otra, en orden.
2. **Selección (condicional)**: se elige una rama u otra según una condición (`si-entonces-si_no`; en el flujograma, un **rombo**). Variante múltiple: `según` (switch/case).
3. **Iteración (bucle)**: se repite un bloque mientras se cumple una condición. Dos formas:
   - **Mientras** (`while`): la condición se evalúa **antes** (puede no ejecutarse ninguna vez).
   - **Repetir-hasta** (`do-until`): la condición se evalúa **después** (se ejecuta al menos una vez).

> **[DATO CLAVE EXAMEN]** Las **tres** estructuras de la programación estructurada (Böhm-Jacopini): **secuencia, selección e iteración**. La diferencia clave de los bucles: **mientras** comprueba *antes* (0 o más veces); **repetir-hasta** comprueba *después* (1 o más veces). Programación estructurada = **sin `goto`**.

> **[REFERENCIA CRUZADA]** Estas estructuras de control (condicionales, bucles, recursividad) son el núcleo del **Tema 18 (Lenguajes de programación)**. El flujograma es la representación gráfica de lo que en el Tema 18 se escribe como código.

### 5.4. Reglas de construcción del flujograma

- **Un único inicio y, preferiblemente, un único fin** (terminales).
- El flujo va, por convención, de **arriba abajo** y de **izquierda a derecha**; las flechas explicitan cualquier otro sentido.
- De un símbolo de **proceso** sale **una sola** línea; de un **rombo (decisión)** salen **dos o más** (etiquetadas con la condición: «Sí»/«No»).
- Las líneas de flujo **no deben cruzarse** si puede evitarse; usar **conectores** para saltos.
- Cada camino debe conducir finalmente a un **terminal de fin** (no debe haber caminos «perdidos»).
- Evitar `goto`/saltos arbitrarios: ceñirse a las tres estructuras básicas (flujograma **estructurado**).

> **[EJERCICIO RESUELTO]** *Flujograma de «validar si un habitante es mayor de edad».*
> `Inicio` (óvalo) → `Leer fecha_nacimiento` (romboide E/S) → `Calcular edad` (rectángulo) → `¿edad ≥ 18?` (rombo): rama **Sí** → `Mostrar "Mayor de edad"`; rama **No** → `Mostrar "Menor de edad"`; ambas → `Fin` (óvalo). Es una **selección** simple con un solo punto de fin.

### 5.5. Ordinograma, organigrama y pseudocódigo

En la tradición española conviene distinguir términos próximos: [METRICA3]

- **Organigrama (de proceso / del sistema)**: diagrama de **alto nivel** que muestra los grandes módulos o unidades y su relación (no el detalle del algoritmo). *No confundir* con el organigrama de una organización (estructura jerárquica de cargos).
- **Ordinograma (flujograma de detalle)**: el diagrama de flujo **detallado** de la lógica de un programa, con las estructuras de control. Es el flujograma «de programación» propiamente dicho.
- **Pseudocódigo**: descripción textual del algoritmo en lenguaje estructurado (cercano al lenguaje natural pero con `si/mientras/para`), equivalente al ordinograma pero sin dibujo. Es la alternativa de la **mini-spec** del DFD.

> **[DATO CLAVE EXAMEN]** **Organigrama** = visión de **conjunto/módulos** (qué partes hay). **Ordinograma** = **detalle** del algoritmo (cómo funciona por dentro). El **pseudocódigo** es la versión textual del ordinograma. Esta terna se pregunta en oposiciones españolas con frecuencia.

### 5.6. UML: panorama de los tipos de diagramas

El **Lenguaje Unificado de Modelado (UML)**, estandarizado por la OMG, unifica las técnicas anteriores en una notación única orientada a objetos. UML 2.5 define **14 tipos de diagramas** en dos grandes familias: [UML][FOWLER]

- **Diagramas de estructura** (vista estática): **clases**, objetos, componentes, despliegue, paquetes, estructura compuesta, perfiles. El **diagrama de clases** es el equivalente moderno del **E-R**.
- **Diagramas de comportamiento** (vista dinámica): **casos de uso**, **actividad**, **estados (máquina de estados)**, **secuencia**, comunicación, tiempos, visión global de interacción.
  - El **diagrama de estados** equivale al **DTE** (§3).
  - El **diagrama de actividad** cubre el papel del **flujograma** y, en parte, del **DFD** (incluye flujos de control y de objetos, decisiones, bifurcaciones y *swimlanes*).
  - El **diagrama de casos de uso** captura los requisitos funcionales (actores y casos de uso), sin equivalente clásico directo.

| Técnica clásica | Vista | Equivalente UML |
|---|---|---|
| Modelo E-R | Estática / datos | Diagrama de clases |
| DTE | Dinámica / comportamiento | Diagrama de estados |
| DFD / flujograma | Funcional / control | Diagrama de actividad |

> **[DATO CLAVE EXAMEN]** UML 2.5 = **14 diagramas** en dos familias: **estructura** (estáticos; el de **clases** es el rey) y **comportamiento** (dinámicos; **casos de uso, actividad, estados, secuencia**). Equivalencias: **E-R ↔ clases**, **DTE ↔ estados**, **flujograma/DFD ↔ actividad**.

> **[REFERENCIA CRUZADA]** UML, los **patrones de diseño** y la modelización orientada a objetos se desarrollan en el **Tema 20 (Diseño y programación orientada a objetos)**. Este tema cubre el modelado *conceptual y funcional*; el Tema 20, el modelado *orientado a objetos* y su implementación.

---

## Resumen integrador

El Tema 16 recorre el **modelado conceptual y funcional** de un sistema de información en tres vistas complementarias —**estática** (E-R: entidades, atributos, relaciones, cardinalidades, jerarquías), **dinámica** (DTE: estados y transiciones) y **funcional** (DFD: procesos, flujos, almacenes y entidades externas, con descomposición por niveles y equilibrado)— más los **flujogramas** que detallan la lógica de control (símbolos ISO 5807; secuencia, selección e iteración de Böhm-Jacopini). Todo ello se enmarca en la **arquitectura ANSI/SPARC** (independencia de datos) y se cierra con **UML** como síntesis moderna (clases ↔ E-R, estados ↔ DTE, actividad ↔ DFD/flujograma). El modelo conceptual es el puente entre el análisis de requisitos y el **diseño lógico relacional** (Tema 17) sobre un **SGBD** (Tema 15).
