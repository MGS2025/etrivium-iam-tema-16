# Tema 16 — Test de Autoevaluación

> **Título**: Modelo conceptual de datos. Entidades, atributos y relaciones. Reglas de modelización. Diagramas de flujo de datos. Reglas de construcción. Descomposición en niveles. Flujogramas.
> **Formato**: 60 preguntas tipo test A/B/C (formato oficial oposición)
> **Nivel**: C1 — Técnico Auxiliar TIC, Ayuntamiento de Madrid
> **Versión**: v1.0 — Pendiente validación
> **Fecha**: 2026-06-20
> **Fuentes**: ver tema-16-fuentes.md

---

## Instrucciones

- Cada pregunta tiene **3 opciones** (A, B, C). Solo una es correcta.
- Penalización en examen real: respuesta incorrecta descuenta **1/3** del valor de una correcta.
- Distribución temática: Modelado y ANSI/SPARC (P1-P10), Modelo E-R (P11-P28), DTE (P29-P35), DFD (P36-P50), Flujogramas y UML (P51-P60).

---

### Pregunta 1

**Un modelo de datos conceptual se caracteriza por:**

A) Describir cómo se almacenan físicamente los datos en disco
B) Ser independiente del SGBD y estar próximo a la visión del usuario
C) Depender del producto concreto de base de datos elegido

<details><summary>Respuesta</summary>

**Correcta: B) Ser independiente del SGBD y estar próximo a la visión del usuario** El modelo conceptual (E-R) es independiente de la tecnología; el lógico depende del tipo de SGBD y el físico, del producto y el soporte.

*Referencia: §1.1 [ELMASRI]*
</details>

---

### Pregunta 2

**En la arquitectura ANSI/SPARC, ¿cuántos esquemas de cada tipo existen?**

A) Varios externos, uno conceptual y uno interno
B) Uno externo, varios conceptuales y uno interno
C) Uno de cada tipo

<details><summary>Respuesta</summary>

**Correcta: A) Varios externos, uno conceptual y uno interno** Puede haber muchas vistas (esquemas externos), pero el esquema conceptual y el interno son únicos.

*Referencia: §1.2 [ANSI-SPARC]*
</details>

---

### Pregunta 3

**El nivel conceptual de la arquitectura ANSI/SPARC contiene:**

A) Las rutas de acceso, índices y la ubicación física de los datos
B) Las vistas particulares de cada grupo de usuarios
C) La estructura global de la base de datos: entidades, atributos, relaciones y restricciones

<details><summary>Respuesta</summary>

**Correcta: C) La estructura global de la base de datos: entidades, atributos, relaciones y restricciones** El nivel conceptual describe toda la base de datos para la comunidad de usuarios, sin detalles de almacenamiento.

*Referencia: §1.2 [ANSI-SPARC]*
</details>

---

### Pregunta 4

**La independencia física de datos permite:**

A) Cambiar el almacenamiento interno sin alterar el esquema conceptual
B) Cambiar el esquema conceptual sin alterar las vistas
C) Cambiar las vistas sin alterar las aplicaciones

<details><summary>Respuesta</summary>

**Correcta: A) Cambiar el almacenamiento interno sin alterar el esquema conceptual** La independencia física aísla el nivel conceptual de los cambios en el nivel interno (índices, ficheros).

*Referencia: §1.3 [DATE]*
</details>

---

### Pregunta 5

**¿Cuál de estas afirmaciones sobre la independencia de datos es correcta?**

A) La independencia física es la más difícil de lograr
B) La independencia lógica es la más difícil de lograr
C) Ambas son igual de sencillas de conseguir

<details><summary>Respuesta</summary>

**Correcta: B) La independencia lógica es la más difícil de lograr** La independencia lógica es más difícil porque las vistas dependen directamente del esquema conceptual.

*Referencia: §1.3 [DATE]*
</details>

---

### Pregunta 6

**El "universo del discurso" o dominio en el modelado de datos es:**

A) El conjunto de SGBD disponibles en el mercado
B) La parcela de la realidad que se quiere representar
C) El lenguaje de programación elegido para la implementación

<details><summary>Respuesta</summary>

**Correcta: B) La parcela de la realidad que se quiere representar** El modelo de dominio captura los conceptos del negocio antes de pensar en la solución informática.

*Referencia: §1.4 [METRICA3]*
</details>

---

### Pregunta 7

**El modelado dinámico de un sistema de información se ocupa de:**

A) La estructura de los datos y sus relaciones
B) Las transformaciones que sufren los datos al fluir entre procesos
C) Cómo cambia de estado el sistema ante los eventos

<details><summary>Respuesta</summary>

**Correcta: C) Cómo cambia de estado el sistema ante los eventos** El modelado dinámico (DTE) describe el comportamiento; el estático, los datos (E-R); el funcional, los procesos (DFD).

*Referencia: §1.5 [RUMBAUGH]*
</details>

---

### Pregunta 8

**La técnica clásica del modelado funcional es:**

A) El diagrama de flujo de datos (DFD)
B) El modelo entidad-relación (E-R)
C) El diagrama de transición de estados (DTE)

<details><summary>Respuesta</summary>

**Correcta: A) El diagrama de flujo de datos (DFD)** El DFD modela la vista funcional (procesos); el E-R, la estática (datos); el DTE, la dinámica (comportamiento).

*Referencia: §1.5 [YOURDON]*
</details>

---

### Pregunta 9

**Un dato se convierte en información cuando:**

A) Se almacena en un fichero binario
B) Se procesa y se interpreta dándole significado en un contexto
C) Se representa en código ASCII

<details><summary>Respuesta</summary>

**Correcta: B) Se procesa y se interpreta dándole significado en un contexto** El dato es la representación simbólica; la información es el dato procesado e interpretado.

*Referencia: §1.1 [METRICA3]*
</details>

---

### Pregunta 10

**El modelo lógico de datos más extendido es:**

A) El modelo jerárquico
B) El modelo en red (CODASYL)
C) El modelo relacional

<details><summary>Respuesta</summary>

**Correcta: C) El modelo relacional** El modelo relacional de Codd (tablas) es el dominante en el nivel lógico; el conceptual usa E-R.

*Referencia: §1.1 [CODD]*
</details>

---

### Pregunta 11

**El modelo Entidad-Relación fue propuesto por:**

A) Edgar F. Codd en 1970
B) Peter Chen en 1976
C) Tom DeMarco en 1979

<details><summary>Respuesta</summary>

**Correcta: B) Peter Chen en 1976** Chen propuso el E-R como vista unificada de los datos. Codd (1970) propuso el modelo relacional; DeMarco (1979), el DFD.

*Referencia: §2.1 [CHEN]*
</details>

---

### Pregunta 12

**En notación de Chen, una entidad se representa mediante:**

A) Un rectángulo
B) Un rombo
C) Una elipse

<details><summary>Respuesta</summary>

**Correcta: A) Un rectángulo** En Chen: entidad = rectángulo; relación = rombo; atributo = elipse.

*Referencia: §2.2 [CHEN]*
</details>

---

### Pregunta 13

**La diferencia entre un tipo de entidad y una ocurrencia es que:**

A) Son sinónimos
B) El tipo es la plantilla o categoría; la ocurrencia es un ejemplar concreto
C) La ocurrencia se dibuja en el diagrama y el tipo no

<details><summary>Respuesta</summary>

**Correcta: B) El tipo es la plantilla o categoría; la ocurrencia es un ejemplar concreto** El tipo `HABITANTE` se dibuja; las ocurrencias (cada habitante) pueblan la base de datos y no se dibujan.

*Referencia: §2.2 [ELMASRI]*
</details>

---

### Pregunta 14

**Una entidad débil se caracteriza porque:**

A) Tiene pocos atributos
B) No puede identificarse solo con sus atributos y depende de una entidad fuerte
C) No participa en ninguna relación

<details><summary>Respuesta</summary>

**Correcta: B) No puede identificarse solo con sus atributos y depende de una entidad fuerte** La entidad débil necesita la clave de la entidad fuerte más un discriminante (clave parcial). Se dibuja con rectángulo doble.

*Referencia: §2.2 [ELMASRI]*
</details>

---

### Pregunta 15

**En notación de Chen, un atributo identificador (clave) se representa:**

A) Con la elipse subrayada
B) Con una elipse doble
C) Con una elipse de línea discontinua

<details><summary>Respuesta</summary>

**Correcta: A) Con la elipse subrayada** El identificador se subraya; la elipse doble es multivaluado y la discontinua, derivado.

*Referencia: §2.3 [CHEN]*
</details>

---

### Pregunta 16

**Un atributo multivaluado se representa en notación de Chen con:**

A) Una elipse de línea discontinua
B) Una elipse doble
C) Un rombo

<details><summary>Respuesta</summary>

**Correcta: B) Una elipse doble** El multivaluado (p. ej. varios teléfonos) se dibuja con elipse doble; el derivado, con elipse discontinua.

*Referencia: §2.3 [CHEN]*
</details>

---

### Pregunta 17

**El atributo "edad", obtenido a partir de la fecha de nacimiento, es un atributo:**

A) Compuesto
B) Multivaluado
C) Derivado (calculado)

<details><summary>Respuesta</summary>

**Correcta: C) Derivado (calculado)** Un atributo derivado se calcula a partir de otros; no se almacena. Se dibuja con elipse discontinua.

*Referencia: §2.3 [ELMASRI]*
</details>

---

### Pregunta 18

**Un atributo compuesto es aquel que:**

A) Toma varios valores para una misma ocurrencia
B) Se descompone en partes con significado propio
C) Se calcula a partir de otros atributos

<details><summary>Respuesta</summary>

**Correcta: B) Se descompone en partes con significado propio** Ejemplo: `domicilio` = (vía, número, planta, puerta, CP). El que toma varios valores es multivaluado; el calculado, derivado.

*Referencia: §2.3 [ELMASRI]*
</details>

---

### Pregunta 19

**El "grado" de una relación es:**

A) El número de tipos de entidad que participan en ella
B) El número máximo de ocurrencias asociadas
C) El número de atributos de la relación

<details><summary>Respuesta</summary>

**Correcta: A) El número de tipos de entidad que participan en ella** Grado unario (1), binario (2), ternario (3). El máximo de ocurrencias asociadas es la cardinalidad.

*Referencia: §2.4 [CHEN]*
</details>

---

### Pregunta 20

**Una relación en la que una entidad se asocia consigo misma es:**

A) Ternaria
B) Recursiva (unaria)
C) De cardinalidad N:M

<details><summary>Respuesta</summary>

**Correcta: B) Recursiva (unaria)** Una relación recursiva o unaria liga una entidad consigo misma (p. ej. EMPLEADO supervisa a EMPLEADO).

*Referencia: §2.4 [ELMASRI]*
</details>

---

### Pregunta 21

**La razón de cardinalidad de una relación binaria indica:**

A) Si la participación es obligatoria u opcional
B) El número máximo de ocurrencias de una entidad asociadas a una de la otra
C) El número de atributos de cada entidad

<details><summary>Respuesta</summary>

**Correcta: B) El número máximo de ocurrencias de una entidad asociadas a una de la otra** La cardinalidad máxima da los tipos 1:1, 1:N, N:M. La obligatoriedad es la participación (cardinalidad mínima).

*Referencia: §2.4 [ELMASRI]*
</details>

---

### Pregunta 22

**"Un distrito tiene muchos barrios y cada barrio pertenece a un solo distrito" es una relación de cardinalidad:**

A) 1:1
B) N:M
C) 1:N

<details><summary>Respuesta</summary>

**Correcta: C) 1:N** Un distrito (1) se asocia con muchos barrios (N), pero cada barrio con un solo distrito.

*Referencia: §2.4 [ELMASRI]*
</details>

---

### Pregunta 23

**La participación total de una entidad en una relación significa que:**

A) Toda ocurrencia de la entidad debe participar en la relación (mínimo 1)
B) Alguna ocurrencia puede no participar (mínimo 0)
C) Todas las entidades del modelo participan

<details><summary>Respuesta</summary>

**Correcta: A) Toda ocurrencia de la entidad debe participar en la relación (mínimo 1)** La participación total (obligatoria) se dibuja con línea doble en Chen; la parcial es opcional (mínimo 0).

*Referencia: §2.4 [ELMASRI]*
</details>

---

### Pregunta 24

**En la notación (mín, máx), el par (0, N) indica:**

A) Participación obligatoria y cardinalidad máxima 1
B) Participación opcional y cardinalidad máxima muchos
C) Participación obligatoria y cardinalidad máxima muchos

<details><summary>Respuesta</summary>

**Correcta: B) Participación opcional y cardinalidad máxima muchos** El mínimo 0 indica opcionalidad (parcial); el máximo N indica muchos.

*Referencia: §2.4 [METRICA3]*
</details>

---

### Pregunta 25

**Al transformar una relación N:M al modelo relacional se obtiene:**

A) Una clave ajena en una de las dos tablas
B) Una tabla intermedia con las claves de ambas entidades
C) Una única tabla que fusiona las dos entidades

<details><summary>Respuesta</summary>

**Correcta: B) Una tabla intermedia con las claves de ambas entidades** La N:M genera una tabla cuya clave primaria es la combinación de las claves de las dos entidades, más los atributos de la relación.

*Referencia: §2.8 [ELMASRI]*
</details>

---

### Pregunta 26

**Al transformar una relación 1:N al modelo relacional:**

A) La clave del lado "1" se propaga como clave ajena a la tabla del lado "N"
B) Se crea siempre una tabla intermedia
C) La clave del lado "N" se propaga al lado "1"

<details><summary>Respuesta</summary>

**Correcta: A) La clave del lado "1" se propaga como clave ajena a la tabla del lado "N"** En 1:N, la clave del lado "1" pasa como clave ajena al lado "N". La tabla intermedia es propia de N:M.

*Referencia: §2.8 [ELMASRI]*
</details>

---

### Pregunta 27

**La relación de generalización/especialización del modelo E-R extendido es del tipo:**

A) "parte-de" (composición)
B) "es-un" (is-a), con herencia de atributos del supertipo
C) "muchos-a-muchos"

<details><summary>Respuesta</summary>

**Correcta: B) "es-un" (is-a), con herencia de atributos del supertipo** Los subtipos heredan los atributos comunes del supertipo y añaden los específicos.

*Referencia: §2.6 [ELMASRI]*
</details>

---

### Pregunta 28

**En una jerarquía de especialización, una restricción "disjunta" significa que:**

A) Todo ejemplar del supertipo está en algún subtipo
B) Un ejemplar puede pertenecer a varios subtipos a la vez
C) Un ejemplar pertenece a un solo subtipo

<details><summary>Respuesta</summary>

**Correcta: C) Un ejemplar pertenece a un solo subtipo** Disjunta = un solo subtipo; solapada = varios. La cobertura total/parcial es la otra restricción (¿todo ejemplar está en algún subtipo?).

*Referencia: §2.6 [ELMASRI]*
</details>

---

### Pregunta 29

**En un diagrama de transición de estados, un "estado" es:**

A) Un estímulo que provoca un cambio
B) Una situación estable en la que se encuentra el sistema esperando un evento
C) Una operación que se ejecuta en la transición

<details><summary>Respuesta</summary>

**Correcta: B) Una situación estable en la que se encuentra el sistema esperando un evento** El estímulo es el evento; la operación es la acción.

*Referencia: §3.1 [YOURDON]*
</details>

---

### Pregunta 30

**El elemento que dispara una transición en un DTE es:**

A) El evento (suceso)
B) La acción
C) El estado final

<details><summary>Respuesta</summary>

**Correcta: A) El evento (suceso)** El evento dispara la transición; la condición (guarda) la habilita; la acción es lo que se ejecuta.

*Referencia: §3.1 [YOURDON]*
</details>

---

### Pregunta 31

**La etiqueta de una transición en un DTE/UML sigue el patrón:**

A) acción [evento] / condición
B) evento [condición] / acción
C) condición / evento [acción]

<details><summary>Respuesta</summary>

**Correcta: B) evento [condición] / acción** El evento dispara, la condición (entre corchetes) restringe y la acción se ejecuta.

*Referencia: §3.1 [UML]*
</details>

---

### Pregunta 32

**En un DTE bien construido:**

A) Puede haber varios estados iniciales
B) Hay un único estado inicial y los estados son mutuamente excluyentes
C) Los estados pueden solaparse en el tiempo

<details><summary>Respuesta</summary>

**Correcta: B) Hay un único estado inicial y los estados son mutuamente excluyentes** El sistema está en un único estado en cada instante; el estado inicial es único, aunque puede haber varios finales.

*Referencia: §3.2 [YOURDON]*
</details>

---

### Pregunta 33

**Una autotransición en un DTE es:**

A) Una transición que vuelve al mismo estado de partida
B) Una transición sin evento
C) Un estado sin salida

<details><summary>Respuesta</summary>

**Correcta: A) Una transición que vuelve al mismo estado de partida** Las autotransiciones (mismo estado origen y destino) son válidas.

*Referencia: §3.2 [UML]*
</details>

---

### Pregunta 34

**El DTE clásico equivale formalmente a:**

A) Una tabla relacional
B) Una máquina de estados finita
C) Un diagrama de flujo de datos

<details><summary>Respuesta</summary>

**Correcta: B) Una máquina de estados finita** El DTE es una máquina de estados finita; UML lo amplía en el diagrama de estados (estados compuestos, regiones concurrentes).

*Referencia: §3.3 [UML]*
</details>

---

### Pregunta 35

**¿Cuál es el equivalente del DTE clásico en UML?**

A) El diagrama de clases
B) El diagrama de actividad
C) El diagrama de estados (máquina de estados)

<details><summary>Respuesta</summary>

**Correcta: C) El diagrama de estados (máquina de estados)** En UML: E-R ↔ clases; DTE ↔ estados; DFD/flujograma ↔ actividad.

*Referencia: §3.3 [FOWLER]*
</details>

---

### Pregunta 36

**El diagrama de flujo de datos (DFD) modela:**

A) El orden temporal y las decisiones de un algoritmo
B) El sistema como una red de procesos que transforman datos
C) La estructura estática de los datos

<details><summary>Respuesta</summary>

**Correcta: B) El sistema como una red de procesos que transforman datos** El DFD muestra qué transformaciones sufren los datos, sin orden temporal (eso es el flujograma).

*Referencia: §4.1 [DEMARCO]*
</details>

---

### Pregunta 37

**¿Cuáles son los cuatro componentes del DFD?**

A) Proceso, flujo de datos, almacén y entidad externa
B) Estado, transición, evento y acción
C) Entidad, atributo, relación y cardinalidad

<details><summary>Respuesta</summary>

**Correcta: A) Proceso, flujo de datos, almacén y entidad externa** El proceso transforma, el flujo es el dato en movimiento, el almacén el dato en reposo y la entidad externa la frontera.

*Referencia: §4.1 [DEMARCO]*
</details>

---

### Pregunta 38

**En un DFD, un almacén de datos (data store) representa:**

A) Un dato en movimiento
B) Un dato en reposo (fichero, tabla)
C) Una transformación de datos

<details><summary>Respuesta</summary>

**Correcta: B) Un dato en reposo (fichero, tabla)** El almacén es el dato en reposo; el flujo, el dato en movimiento; el proceso, la transformación.

*Referencia: §4.1 [DEMARCO]*
</details>

---

### Pregunta 39

**Una entidad externa en un DFD es:**

A) Un almacén de datos interno
B) Una persona, organización o sistema externo que produce o consume datos
C) Un proceso de alto nivel

<details><summary>Respuesta</summary>

**Correcta: B) Una persona, organización o sistema externo que produce o consume datos** La entidad externa (terminador) marca la frontera del sistema; se dibuja como rectángulo.

*Referencia: §4.1 [DEMARCO]*
</details>

---

### Pregunta 40

**¿Cuál de estas conexiones está PROHIBIDA en un DFD?**

A) Un flujo directo entre dos almacenes de datos
B) Un flujo entre una entidad externa y un proceso
C) Un flujo entre un proceso y un almacén

<details><summary>Respuesta</summary>

**Correcta: A) Un flujo directo entre dos almacenes de datos** Todo flujo debe pasar por un proceso; están prohibidos los flujos directos almacén↔almacén, entidad↔entidad y entidad↔almacén.

*Referencia: §4.2 [DEMARCO]*
</details>

---

### Pregunta 41

**Un proceso de un DFD que solo tiene flujos de entrada y ninguno de salida se denomina, informalmente:**

A) "Milagro"
B) "Agujero negro" (error de modelado)
C) Primitiva funcional

<details><summary>Respuesta</summary>

**Correcta: B) "Agujero negro" (error de modelado)** Un proceso solo con entradas es un "agujero negro"; solo con salidas, un "milagro". Todo proceso debe tener al menos una entrada y una salida.

*Referencia: §4.2 [DEMARCO]*
</details>

---

### Pregunta 42

**El diagrama de contexto (nivel 0) de un DFD se caracteriza por:**

A) Contener un único proceso que representa todo el sistema, sin almacenes visibles
B) Mostrar todos los procesos elementales del sistema
C) Detallar la lógica interna de cada proceso

<details><summary>Respuesta</summary>

**Correcta: A) Contener un único proceso que representa todo el sistema, sin almacenes visibles** El diagrama de contexto (nivel 0) tiene una sola burbuja rodeada de entidades externas y define el alcance del sistema.

*Referencia: §4.3 [YOURDON]*
</details>

---

### Pregunta 43

**La descomposición de un DFD por niveles es un proceso:**

A) Ascendente (bottom-up), de las primitivas al contexto
B) Descendente (top-down), explotando cada proceso en otro más detallado
C) Horizontal, sin jerarquía

<details><summary>Respuesta</summary>

**Correcta: B) Descendente (top-down), explotando cada proceso en otro más detallado** Se parte del contexto y se explota cada proceso (1 → 1.1, 1.2…) hasta llegar a primitivas funcionales.

*Referencia: §4.3 [DEMARCO]*
</details>

---

### Pregunta 44

**Un proceso de un DFD que ya no se descompone más se denomina:**

A) Entidad externa
B) Diagrama de contexto
C) Primitiva funcional

<details><summary>Respuesta</summary>

**Correcta: C) Primitiva funcional** La primitiva funcional es el proceso elemental que ya no se descompone y se describe con una mini-spec.

*Referencia: §4.3 [DEMARCO]*
</details>

---

### Pregunta 45

**La regla de equilibrado (balanceo) entre niveles de un DFD exige que:**

A) Todos los procesos tengan el mismo número de flujos
B) Los flujos de entrada/salida de un proceso coincidan con los flujos frontera de su diagrama hijo
C) Cada nivel tenga el mismo número de procesos

<details><summary>Respuesta</summary>

**Correcta: B) Los flujos de entrada/salida de un proceso coincidan con los flujos frontera de su diagrama hijo** El equilibrado garantiza la coherencia: lo que entra y sale del proceso padre debe cruzar la frontera de su explosión.

*Referencia: §4.3 [DEMARCO]*
</details>

---

### Pregunta 46

**El diccionario de datos de un análisis estructurado sirve para:**

A) Definir rigurosamente cada flujo, almacén y dato elemental del DFD
B) Describir la lógica de los procesos primitivos
C) Dibujar las cardinalidades del modelo E-R

<details><summary>Respuesta</summary>

**Correcta: A) Definir rigurosamente cada flujo, almacén y dato elemental del DFD** El diccionario de datos define los datos con notación `= + { } [ ] ( )`; la lógica de procesos la describe la mini-spec.

*Referencia: §4.4 [DEMARCO]*
</details>

---

### Pregunta 47

**En la notación del diccionario de datos, las llaves { } indican:**

A) Selección/alternativa
B) Iteración/repetición
C) Dato opcional

<details><summary>Respuesta</summary>

**Correcta: B) Iteración/repetición** `{ }` = iteración; `[ | ]` = selección; `( )` = opcional; `+` = concatenación; `=` = se compone de.

*Referencia: §4.4 [DEMARCO]*
</details>

---

### Pregunta 48

**La especificación de procesos (mini-spec o P-SPEC) describe:**

A) La estructura de los datos almacenados
B) La lógica de los procesos primitivos (con pseudocódigo o tablas de decisión)
C) Las entidades externas del sistema

<details><summary>Respuesta</summary>

**Correcta: B) La lógica de los procesos primitivos (con pseudocódigo o tablas de decisión)** La mini-spec detalla cómo funciona cada proceso que ya no se descompone; aquí enlaza con los flujogramas.

*Referencia: §4.4 [DEMARCO]*
</details>

---

### Pregunta 49

**¿Qué notación de DFD dibuja los procesos como círculos (burbujas)?**

A) Gane/Sarson
B) Yourdon/DeMarco
C) Crow's foot (pata de gallo)

<details><summary>Respuesta</summary>

**Correcta: B) Yourdon/DeMarco** Yourdon/DeMarco usa círculos; Gane/Sarson usa rectángulos de esquinas redondeadas. La pata de gallo es notación E-R, no DFD.

*Referencia: §4.5 [GANE-SARSON]*
</details>

---

### Pregunta 50

**El equivalente UML del DFD/flujograma es, aproximadamente:**

A) El diagrama de clases
B) El diagrama de estados
C) El diagrama de actividad

<details><summary>Respuesta</summary>

**Correcta: C) El diagrama de actividad** El diagrama de actividad UML cubre el flujo de control y de objetos, papel parcialmente análogo al DFD y al flujograma.

*Referencia: §4.5 [UML]*
</details>

---

### Pregunta 51

**La principal diferencia entre un DFD y un flujograma es que:**

A) El DFD muestra el flujo de control (orden y decisiones) y el flujograma, el flujo de datos
B) El flujograma muestra el flujo de control y el DFD, el flujo de datos sin secuencia temporal
C) Son notaciones idénticas con distinto nombre

<details><summary>Respuesta</summary>

**Correcta: B) El flujograma muestra el flujo de control y el DFD, el flujo de datos sin secuencia temporal** El DFD modela transformaciones de datos; el flujograma, la secuencia y las decisiones (control).

*Referencia: §5.1 [ISO5807]*
</details>

---

### Pregunta 52

**¿Qué norma internacional normaliza los símbolos de los diagramas de flujo?**

A) ISO 5807:1985
B) ISO 9001
C) ISO/IEC 27001

<details><summary>Respuesta</summary>

**Correcta: A) ISO 5807:1985** ISO 5807 (heredera de ANSI X3.5) normaliza los símbolos de los flujogramas.

*Referencia: §5.2 [ISO5807]*
</details>

---

### Pregunta 53

**En un flujograma, el símbolo de decisión (bifurcación según condición) es:**

A) Un rectángulo
B) Un óvalo
C) Un rombo

<details><summary>Respuesta</summary>

**Correcta: C) Un rombo** El rombo representa la decisión y es el único símbolo con varias salidas (las ramas de la condición). El rectángulo es proceso; el óvalo, terminal.

*Referencia: §5.2 [ISO5807]*
</details>

---

### Pregunta 54

**El símbolo de terminal (inicio/fin) de un flujograma es:**

A) Un óvalo o rectángulo redondeado
B) Un paralelogramo (romboide)
C) Un rombo

<details><summary>Respuesta</summary>

**Correcta: A) Un óvalo o rectángulo redondeado** El terminal (inicio/fin) es un óvalo; el romboide es entrada/salida; el rombo, decisión.

*Referencia: §5.2 [ISO5807]*
</details>

---

### Pregunta 55

**El símbolo romboide (paralelogramo) en un flujograma representa:**

A) Una decisión
B) Una operación de entrada/salida de datos
C) El inicio del proceso

<details><summary>Respuesta</summary>

**Correcta: B) Una operación de entrada/salida de datos** El romboide es E/S (lectura/escritura). La decisión es el rombo; el inicio, el óvalo terminal.

*Referencia: §5.2 [ISO5807]*
</details>

---

### Pregunta 56

**El teorema de Böhm-Jacopini establece que todo algoritmo puede expresarse con:**

A) Secuencia, selección e iteración, sin saltos incondicionales (goto)
B) Únicamente secuencia y saltos goto
C) Recursividad y punteros

<details><summary>Respuesta</summary>

**Correcta: A) Secuencia, selección e iteración, sin saltos incondicionales (goto)** Es el fundamento de la programación estructurada: tres estructuras de control bastan, sin goto.

*Referencia: §5.3 [BOHM-JACOPINI]*
</details>

---

### Pregunta 57

**La diferencia entre el bucle "mientras" (while) y "repetir-hasta" (do-until) es:**

A) "Mientras" comprueba la condición después; "repetir-hasta", antes
B) "Mientras" comprueba la condición antes (0 o más veces); "repetir-hasta", después (1 o más veces)
C) Ambos comprueban la condición exactamente igual

<details><summary>Respuesta</summary>

**Correcta: B) "Mientras" comprueba la condición antes (0 o más veces); "repetir-hasta", después (1 o más veces)** El while puede no ejecutar el cuerpo ninguna vez; el do-until lo ejecuta al menos una.

*Referencia: §5.3 [BOHM-JACOPINI]*
</details>

---

### Pregunta 58

**En la terminología española de diagramas, un "ordinograma" es:**

A) El diagrama de alto nivel de los módulos del sistema
B) El diagrama de flujo detallado de la lógica de un programa
C) El organigrama de cargos de la organización

<details><summary>Respuesta</summary>

**Correcta: B) El diagrama de flujo detallado de la lógica de un programa** El ordinograma es el flujograma de detalle; el organigrama (de proceso) es la visión de conjunto de los módulos.

*Referencia: §5.5 [METRICA3]*
</details>

---

### Pregunta 59

**¿A qué familia de diagramas UML pertenece el diagrama de clases?**

A) Diagramas de comportamiento
B) Diagramas de estructura
C) Diagramas de interacción

<details><summary>Respuesta</summary>

**Correcta: B) Diagramas de estructura** El diagrama de clases es de estructura (vista estática) y es el equivalente moderno del modelo E-R. Casos de uso, actividad, estados y secuencia son de comportamiento.

*Referencia: §5.6 [UML]*
</details>

---

### Pregunta 60

**¿Cuál es el equivalente UML del modelo Entidad-Relación?**

A) El diagrama de casos de uso
B) El diagrama de actividad
C) El diagrama de clases

<details><summary>Respuesta</summary>

**Correcta: C) El diagrama de clases** El diagrama de clases (estructura) es el equivalente del E-R: clases ↔ entidades, asociaciones ↔ relaciones, multiplicidad ↔ cardinalidad.

*Referencia: §5.6 [UML]*
</details>
