# Tema 16 — Índice

> **Título oficial**: Modelo conceptual de datos. Entidades, atributos y relaciones. Reglas de modelización. Diagramas de flujo de datos. Reglas de construcción. Descomposición en niveles. Flujogramas.
>
> **Bloque**: Parte II — Técnico (Temas 11-40)
> **Nivel**: C1 — Técnico Auxiliar TIC, Ayuntamiento de Madrid

---

## Estructura del tema

1. **El modelado de sistemas de información**
   1.1. Concepto de modelo, dato y modelo de datos
   1.2. Niveles de abstracción: arquitectura ANSI/SPARC (externo, conceptual, interno)
   1.3. Independencia de datos (física y lógica)
   1.4. El modelo de dominio y el modelo conceptual de datos
   1.5. Técnicas y tipos de modelado: estático, dinámico y funcional

2. **Modelado estático: el modelo Entidad-Relación (E-R)**
   2.1. Origen (Chen, 1976) y propósito del modelo E-R
   2.2. Entidades: concepto, tipos (fuertes y débiles) y ocurrencias
   2.3. Atributos: simples/compuestos, monovaluados/multivaluados, derivados e identificadores
   2.4. Relaciones (interrelaciones): grado, cardinalidad y participación
   2.5. Reglas de modelización y construcción del diagrama E-R
   2.6. Técnicas de descomposición: generalización/especialización, agregación y asociación
   2.7. Notaciones: Chen, pata de gallo (crow's foot) y UML
   2.8. Del modelo E-R al modelo relacional (transformación)

3. **Modelado dinámico: el diagrama de transición de estados (DTE)**
   3.1. Estados, transiciones, eventos, condiciones y acciones
   3.2. Reglas de construcción del DTE
   3.3. Equivalencia con las máquinas de estados y el diagrama de estados UML

4. **Modelado funcional: el diagrama de flujo de datos (DFD)**
   4.1. Componentes: proceso, flujo de datos, almacén y entidad externa
   4.2. Reglas de construcción del DFD
   4.3. Descomposición en niveles: contexto (nivel 0), nivel 1, nivel N y equilibrado
   4.4. Diccionario de datos y especificación de procesos (mini-spec)
   4.5. Notaciones: Yourdon/DeMarco frente a Gane/Sarson

5. **Flujogramas, reglas de construcción y UML**
   5.1. Concepto y propósito del flujograma (diagrama de flujo)
   5.2. Símbolos normalizados (ISO 5807 / ANSI)
   5.3. Estructuras básicas: secuencia, selección e iteración (programación estructurada)
   5.4. Reglas de construcción del flujograma
   5.5. Ordinograma, organigrama y pseudocódigo
   5.6. UML: panorama de los tipos de diagramas (estructura y comportamiento)

---

## Conceptos clave del tema

| Concepto | Dónde se trata |
|---|---|
| Arquitectura ANSI/SPARC (3 esquemas) | §1.2 |
| Independencia física y lógica de datos | §1.3 |
| Entidad, atributo, relación | §2.2-§2.4 |
| Grado y cardinalidad (1:1, 1:N, N:M) | §2.4 |
| Participación total/parcial | §2.4 |
| Generalización/especialización, agregación | §2.6 |
| Notación pata de gallo (crow's foot) | §2.7 |
| Diagrama de transición de estados (DTE) | §3 |
| Procesos, flujos, almacenes, entidades externas | §4.1 |
| Diagrama de contexto y explosión por niveles | §4.3 |
| Equilibrado (balanceo) de DFD | §4.3 |
| Diccionario de datos | §4.4 |
| Símbolos ISO 5807 (terminal, proceso, decisión) | §5.2 |
| Secuencia, selección, iteración (Böhm-Jacopini) | §5.3 |
| Diagramas UML (estructura vs comportamiento) | §5.6 |
