# Tema 16 — Validación

> **Título oficial**: Modelo conceptual de datos. Entidades, atributos y relaciones. Reglas de modelización. Diagramas de flujo de datos. Reglas de construcción. Descomposición en niveles. Flujogramas.
>
> **Versión**: v1.0 — Pendiente validación · **Fecha**: 2026-06-20

Checklist de revisión para **María / Ana (IAM)** y, en su caso, **Jesús Cuadrado**. Marcar cada punto al validarlo.

---

## 1. Cobertura del enunciado oficial

- [ ] **Modelo conceptual de datos** tratado (§1) — concepto, niveles conceptual/lógico/físico.
- [ ] **Entidades, atributos y relaciones** (§2.2-§2.4) — tipos de cada uno y su iconografía.
- [ ] **Reglas de modelización** (§2.5) — proceso y errores típicos del E-R.
- [ ] **Diagramas de flujo de datos** (§4) — cuatro componentes y reglas.
- [ ] **Reglas de construcción** del DFD (§4.2) y del flujograma (§5.4).
- [ ] **Descomposición en niveles** (§4.3) — contexto, nivel 1, explosión y equilibrado.
- [ ] **Flujogramas** (§5) — símbolos ISO 5807 y estructuras de control.
- [ ] Epígrafes del índice del cliente cubiertos: arquitectura ANSI (§1.2), modelado estático/dinámico/funcional (§1.5, §2, §3, §4), DTE (§3), DFD (§4), UML y tipos de diagramas (§5.6).

## 2. Rigor técnico

- [ ] Definiciones de entidad fuerte/débil, atributos (compuesto/multivaluado/derivado/clave) correctas.
- [ ] Cardinalidad (máxima) vs participación (mínima) bien diferenciadas.
- [ ] Reglas «negativas» del DFD correctas (sin flujos directos almacén↔almacén, etc.).
- [ ] Equilibrado/balanceo bien explicado.
- [ ] Símbolos de flujograma (óvalo/rectángulo/rombo/romboide) correctos.
- [ ] Teorema de Böhm-Jacopini y diferencia while/do-until correctos.
- [ ] Equivalencias UML (clases ↔ E-R, estados ↔ DTE, actividad ↔ DFD/flujograma) correctas.

## 3. Referencias cruzadas (vs BOAM 10.032)

- [ ] **T13** (Estructuras de datos) — citado en §3.3 (máquinas de estados).
- [ ] **T15** (SGBD) — citado en §1.1, §4.5.
- [ ] **T17** (Diseño lógico, modelo relacional, normalización) — citado en §1.1, §2.8.
- [ ] **T18** (Lenguajes de programación) — citado en §5.3 (estructuras de control).
- [ ] **T20** (POO, UML, patrones) — citado en §2.6 (herencia), §5.6 (UML).
- [ ] Ninguna referencia cruzada inventa un enunciado de otro tema (revisión anti-alucinación).

## 4. Aspectos pedagógicos y de formato

- [ ] Callouts (DATO CLAVE, EJERCICIO RESUELTO, EJEMPLO AYTO MADRID, REFERENCIA CRUZADA) bien empleados.
- [ ] Ejemplos del Ayuntamiento de Madrid realistas (Padrón, tributos, sede electrónica).
- [ ] 12 diagramas SVG legibles, con paleta corporativa y atribución de fuente.
- [ ] 60 preguntas de test con respuesta única y explicación; distribución A/B/C equilibrada.
- [ ] 3 casos prácticos con cuestiones puntuadas (suman 10) y criterios de evaluación.
- [ ] Pestaña Índice presente y sincronizada con el contenido.

## 5. Decisiones a confirmar por el cliente

1. **Profundidad**: ¿el nivel de detalle (incluir EER, agregación, notación pata de gallo, UML) es el adecuado para C1, o se prefiere recortar a notación de Chen + DFD + flujograma?
2. **UML**: ¿se mantiene UML como equivalencia transversal o se trata como epígrafe independiente más extenso (último punto del índice oficial)?
3. **MÉTRICA v3**: ¿interesa reforzar la terminología MÉTRICA (técnica del Modelo E-R, DFD, DTE del MAP) por ser la metodología de referencia en la Administración española?

_(Espacio para anotaciones de María, Ana y la revisión IAM.)_
