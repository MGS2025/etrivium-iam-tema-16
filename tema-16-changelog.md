# Tema 16 — Registro de cambios

> **Título oficial**: Modelo conceptual de datos. Entidades, atributos y relaciones. Reglas de modelización. Diagramas de flujo de datos. Reglas de construcción. Descomposición en niveles. Flujogramas.

---

## v1.4 — 2026-10-06 — Revisión de diagramas

**Motivo**: barrido de los diagramas de los 40 temas tras la revisión jurídica y de normas.

### Cambios

- Los estilos de cada diagrama se aíslan (`.svdN`): la caja «FÍSICO» del D1 tenía el texto oscuro sobre fondo oscuro.
- Revisión visual de todos los diagramas, captura a captura (la medición automática no detecta contraste, flechas mal dirigidas ni textos pegados al borde): corregidos textos que se salían de su caja o del lienzo, cajas que se tocaban, flechas que no llegaban a su destino y textos con poco contraste. Sin cambios de contenido.

---

## v1.3 — 2026-10-01 — Normas vigentes y correcciones comunes de la revisión

**Motivo**: revisión de la serie del 01-10-2026 (decisiones de Joan y María): normas caducadas con el patrón de dos filas en Fuentes y correcciones comunes (referencias al cliente y al origen del material, promesas sobre el examen, AP → AAPP).

### Cambios

- Leyenda de las cajas: se quita «con alta probabilidad de aparecer en el test oficial».
- Fuera las promesas sobre el examen en siete cajas y párrafos («pregunta clásica», «se pregunta literalmente», «en el examen suele especificarse», «que más se preguntan», «que el examen busca confundir», «se pregunta en oposiciones con frecuencia», «muy típico preguntar», «la pregunta más repetida»).
- Validación: «índice del cliente» → «índice»; «Decisiones a confirmar por el cliente» → «Decisiones a confirmar».
- Títulos de las cajas homogeneizados con los temas 1-10 (revisión jurídica): «Dato clave», «Ejemplo de aplicación en el Ayto» y «Relación con otros temas»; las cajas «Ejercicio resuelto» no cambian.

---

## v1.2 — 2026-09-06 — Ajuste a la literalidad del título

**Estado**: pendiente de validación por el IAM.

**Motivo**: criterio de literalidad del título fijado por el IAM (Jesús Cuadrado, 02-09-2026). El título oficial enumera **siete** materias y el tema tenía **cinco** secciones que no se correspondían con ellas. El guion de partida agrupaba todo el tema en un solo bloque de primer nivel, que es de donde venía el desajuste.

### Alcance

- El tema pasa de **5 a 8 secciones**. Las **siete primeras son las siete materias del título**, en su orden y con sus palabras: modelo conceptual de datos · entidades, atributos y relaciones · reglas de modelización · diagramas de flujo de datos · reglas de construcción · descomposición en niveles · flujogramas.
- «Reglas de construcción» y «Descomposición en niveles» pasan a **sección propia** aunque no se subdividan: el título las enumera como materias sueltas.
- El **modelado dinámico (DTE)**, que el título no nombra, pasa al final como **sección 8 marcada como material complementario**, con el mismo criterio aplicado a los otros apartados de la serie que el temario no recoge.
- **No se ha reescrito contenido**: se ha reorganizado y renumerado. Las **127 referencias internas** (contenido, diagramas, test, índice y validación) se renumeraron en una sola pasada y se verificaron después: ninguna apunta a un epígrafe inexistente.
- Renumerado con `_tools-qa/renumera.py`.

---

## v1.1 — 2026-09-06 — Ficha de extensión y tiempo de estudio

**Estado**: sin cambios de contenido. Solo se añade información sobre el propio tema.

**Motivo**: petición del IAM (Jesús Cuadrado, 02-09-2026) al validar el Tema 30. Acepta la extensión de los temas «compuestos» a condición de que se informe de «su extensión en palabras y tiempo estimado de estudio». Al revisarlo se vio que ese dato solo aparecía en 16 de los 40 temas, y que faltaba justo en los más largos.

### Alcance

- Ficha bajo la cabecera del tema, y al final de la pestaña Índice donde esa pestaña existe:
  - **Extensión**: ~5.800 palabras · 12 diagramas · 60 preguntas de test
  - **Tiempo estimado de estudio**: 8-10 horas (primera vuelta completa, sin contar repasos)
- La cifra de palabras de la tabla de entregables se sincroniza con la ficha, para que el tema no muestre dos recuentos distintos.
- Las horas salen de una fórmula común a los 40 temas, para que sean comparables entre sí: contenido a 1.500 palabras/hora (ritmo de estudio activo), diagramas a una hora por cada cinco y test a dos minutos por pregunta. Se publica como intervalo de dos horas.
- Generado con `_tools-qa/ficha_estudio.py`, idempotente y reejecutable tras cualquier regeneración con `build_tNN.py`.

---

## v1.0 — 2026-06-20 (generación inicial, pendiente de validación)

Primera versión completa del Tema 16, generada con la metodología de la serie técnica (T13/T14/T15) y el conversor corregido (listas anidadas + pestaña Índice).

**Contenido generado:**

- **Contenido teórico** (5 secciones): el modelado de sistemas de información y arquitectura ANSI/SPARC; modelo Entidad-Relación (entidades, atributos, relaciones, cardinalidades, EER, notaciones, transformación a relacional); modelado dinámico (DTE); modelado funcional (DFD: componentes, reglas, descomposición por niveles, equilibrado, diccionario de datos); flujogramas (símbolos ISO 5807, estructuras de control de Böhm-Jacopini) y panorama UML.
- **12 diagramas SVG** inline (niveles de modelo, ANSI/SPARC, independencia de datos, las tres vistas, notación de Chen, cardinalidades, generalización, tres notaciones E-R, DTE de expediente, componentes del DFD, descomposición por niveles, símbolos de flujograma).
- **60 preguntas** de test A/B/C con corrección automática y penalización 1/3; distribución equilibrada por permutación determinista.
- **3 casos prácticos** del Ayuntamiento de Madrid (E-R del Padrón, DFD de la tasa de vado, DTE + flujograma de licencia en sede electrónica), puntuados sobre 10 con criterios de evaluación.
- **Fuentes** Tier 1/2/3 con citación inline (Chen, Elmasri, Date, ANSI/SPARC, DeMarco, Yourdon, Gane/Sarson, ISO 5807, Böhm-Jacopini, UML/OMG, MÉTRICA v3).

**Decisiones de generación:**

- Sin material de contenido del cliente (solo el esqueleto/índice oficial `Test_Prompting/temas junio/16.md`) → generado desde fuentes canónicas, todo referenciado.
- Parámetros de la serie técnica: 3 casos, 60 preguntas, 12 SVG, ambas notaciones (clásica + UML).
- Refs cruzadas validadas contra el temario oficial BOAM 10.032: T13, T15, T17, T18, T20.

**Pendiente:** validación de María / Ana / IAM. Posible expansión puntual de epígrafes si la revisión lo pide (longitud actual en el rango habitual de la serie técnica).
