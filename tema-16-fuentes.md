# Tema 16 — Fuentes y normas de citación

> **Título oficial**: Modelo conceptual de datos. Entidades, atributos y relaciones. Reglas de modelización. Diagramas de flujo de datos. Reglas de construcción. Descomposición en niveles. Flujogramas.
>
> **Bloque**: Parte II — Técnico (Temas 11-40)
> **Nivel**: C1 — Técnico Auxiliar TIC, Ayuntamiento de Madrid
> **Versión**: v1.0 — Pendiente validación
> **Fecha**: 2026-06-20

---

## Cómo se citan las fuentes en este tema

Cada afirmación técnica del contenido va acompañada de una **etiqueta breve** entre corchetes, p. ej. `[CHEN]` o `[ELMASRI, cap. 3]`. El registro completo de cada etiqueta está en este documento. Las fuentes se agrupan en tres niveles:

- **Tier 1 — Canónicas**: obras y normas de referencia mundial sobre las que se construye el contenido. Todo dato relevante cita al menos una.
- **Tier 2 — Complementarias**: manuales y especificaciones que amplían o ilustran.
- **Tier 3 — Contexto (no citadas inline)**: material de apoyo y verificación, no usado como cita directa.

---

## Tier 1 — Fuentes canónicas

| ID | Referencia |
|---|---|
| `[CHEN]` | Chen, P. P. (1976). *The Entity-Relationship Model — Toward a Unified View of Data*. ACM Transactions on Database Systems, 1(1), 9-36. Artículo fundacional del modelo entidad-relación. |
| `[ELMASRI]` | Elmasri, R. & Navathe, S. B. *Fundamentals of Database Systems* (7ª ed.). Pearson. Caps. 3-4 (modelo E-R y E-R extendido/EER), cap. 9 (paso a relacional). |
| `[DATE]` | Date, C. J. *An Introduction to Database Systems* (8ª ed.). Addison-Wesley. Niveles de abstracción, independencia de datos. |
| `[SILBERSCHATZ]` | Silberschatz, A., Korth, H. F. & Sudarshan, S. *Database System Concepts* (7ª ed.). McGraw-Hill. Cap. 6 (modelo E-R), notaciones. |
| `[ANSI-SPARC]` | ANSI/X3/SPARC Study Group on Data Base Management Systems (1975). *Interim Report*. Arquitectura de tres esquemas (externo, conceptual, interno). |
| `[CODD]` | Codd, E. F. (1970). *A Relational Model of Data for Large Shared Data Banks*. CACM 13(6). Modelo relacional (destino de la transformación del E-R). |
| `[DEMARCO]` | DeMarco, T. (1979). *Structured Analysis and System Specification*. Yourdon Press. Diagramas de flujo de datos (DFD), descomposición por niveles, diccionario de datos. |
| `[GANE-SARSON]` | Gane, C. & Sarson, T. (1979). *Structured Systems Analysis: Tools and Techniques*. Prentice-Hall. Notación alternativa de DFD (rectángulos redondeados). |
| `[YOURDON]` | Yourdon, E. (1989). *Modern Structured Analysis*. Yourdon Press. Análisis estructurado moderno, modelo esencial, DTE. |
| `[ISO5807]` | ISO 5807:1985. *Information processing — Documentation symbols and conventions for data, program and system flowcharts, program network charts and system resources charts*. Símbolos normalizados de diagramas de flujo. |
| `[BOHM-JACOPINI]` | Böhm, C. & Jacopini, G. (1966). *Flow Diagrams, Turing Machines and Languages with Only Two Formation Rules*. CACM 9(5). Teorema de la programación estructurada (secuencia, selección, iteración). |
| `[UML]` | Object Management Group (OMG). *Unified Modeling Language (UML) Specification*, v2.5.1 (2017). Diagramas de estructura y de comportamiento. |
| `[METRICA3]` | Ministerio de Administraciones Públicas (España). *MÉTRICA versión 3*. Metodología de planificación, desarrollo y mantenimiento de sistemas de información. Técnicas: Modelo E-R, Diagrama de Flujo de Datos, Diagrama de Transición de Estados, Diccionario de Datos. |
| `[ISO11404]` | ISO/IEC 11404:2007. *General-Purpose Datatypes (GPD)*. Tipos de datos independientes del lenguaje (dominios de atributos). |

---

## Tier 2 — Fuentes complementarias

| ID | Referencia |
|---|---|
| `[FOWLER]` | Fowler, M. *UML Distilled* (3ª ed.). Addison-Wesley. Síntesis práctica de los diagramas UML. |
| `[PRESSMAN]` | Pressman, R. S. *Ingeniería del Software: un enfoque práctico* (7ª ed.). McGraw-Hill. Modelado de análisis (datos, flujo, comportamiento). |
| `[RUMBAUGH]` | Rumbaugh, J. et al. (1991). *Object-Modeling Technique (OMT)*. Precursor de UML; modelado de objetos, dinámico y funcional. |
| `[BACHMAN]` | Bachman, C. W. (1969). *Data Structure Diagrams*. Diagramas de Bachman, antecedente del E-R. |
| `[MARTIN]` | Martin, J. *Information Engineering*. Notación "pata de gallo" (crow's foot) para cardinalidades. |
| `[ANSI-X3.5]` | ANSI X3.5-1970. *Flowchart Symbols and Their Usage in Information Processing*. Antecedente estadounidense de ISO 5807. |

---

## Tier 3 — Contexto y verificación (no citadas inline)

| ID | Referencia |
|---|---|
| `[BOAM10032]` | Convocatoria oficial del proceso selectivo (BOAM 10.032, 23-dic-2025). Define el enunciado del Tema 16 y la estructura del examen. |
| `[NTI]` | Esquema Nacional de Interoperabilidad (RD 4/2010) y sus Normas Técnicas. Contexto de modelado de datos en la Administración. |
| `[PORTAL-DATOS-MADRID]` | Portal de Datos Abiertos del Ayuntamiento de Madrid (datos.madrid.es). Ejemplos de conjuntos de datos municipales (Padrón, callejero, censo). |

---

## Nota sobre las dos grandes familias de notación

El temario mezcla **notación clásica** (Chen para E-R; DeMarco/Yourdon y Gane/Sarson para DFD; ISO 5807 para flujogramas) con **UML** (último epígrafe). Este material presenta **ambas a la par**: la notación clásica es la que tradicionalmente piden los exámenes de oposición españoles (alineada con MÉTRICA v3), y UML se añade como equivalencia moderna y estándar de la industria, indicando en cada técnica su correspondencia (E-R ↔ diagrama de clases; DTE ↔ diagrama de estados; flujograma ↔ diagrama de actividad).
