# Tema 16 — Catálogo de Diagramas

> **Título oficial**: Modelo conceptual de datos. Entidades, atributos y relaciones. Reglas de modelización. Diagramas de flujo de datos. Reglas de construcción. Descomposición en niveles. Flujogramas.
>
> **Versión**: v1.0
> **Fecha**: 2026-06-20
> **Autor**: ETRIVIUM
> **Formato**: SVG inline (zero-dependencias, escalable, imprimible, accesible con role/aria-label)
> **Paleta**: Ayuntamiento de Madrid #0055a0 (primario) + #d13c3c (alertas) + #2d8659 (ventajas) + #e89822 (callouts)

---

## Índice de diagramas

| ID | Título | Sección | Tipo |
|---|---|---|---|
| D1 | Tres niveles de modelo de datos | §1.1 | Capas |
| D2 | Arquitectura ANSI/SPARC (tres esquemas) | §1.2 | Capas |
| D3 | Independencia de datos: física y lógica | §1.3 | Conceptual |
| D4 | Las tres vistas del modelado | §1.5 | Mapa |
| D5 | Notación de Chen: entidad, atributo y relación | §2.3 | Estructura |
| D6 | Cardinalidades 1:1, 1:N y N:M | §2.4 | Comparativa |
| D7 | Generalización / especialización (jerarquía es-un) | §2.6 | Jerarquía |
| D8 | Tres notaciones E-R: Chen, pata de gallo y UML | §2.7 | Comparativa |
| D9 | Diagrama de transición de estados (expediente) | §3.1 | Estados |
| D10 | Componentes del DFD | §4.1 | Bloques |
| D11 | Descomposición del DFD por niveles + equilibrado | §4.3 | Niveles |
| D12 | Flujograma: símbolos ISO 5807 y estructuras básicas | §5.2 | Símbolos |

---

## D1 · Tres niveles de modelo de datos

**Sección**: §1.1 — Modelo conceptual, lógico y físico · **Propósito**: Situar el modelo conceptual de datos respecto al lógico y al físico, y su grado de dependencia del SGBD.

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 660 300" role="img" aria-label="Tres niveles de modelo de datos: conceptual, lógico y físico, con dependencia creciente del SGBD">
  <style>.t{font:700 14px system-ui,sans-serif;fill:#fff}.s{font:12px system-ui,sans-serif;fill:#1a1a1a}.lab{font:11px system-ui,sans-serif;fill:#666}.h{font:700 13px system-ui,sans-serif;fill:#0055a0}</style>
  <text x="330" y="26" text-anchor="middle" class="h">Del concepto al almacenamiento</text>
  <rect x="120" y="45" width="420" height="60" rx="8" fill="#0055a0"/>
  <text x="330" y="72" text-anchor="middle" class="t">CONCEPTUAL — modelo Entidad-Relación</text>
  <text x="330" y="92" text-anchor="middle" class="s" fill="#dce8f5">Independiente del SGBD · cercano al usuario</text>
  <rect x="120" y="120" width="420" height="60" rx="8" fill="#3378b9"/>
  <text x="330" y="147" text-anchor="middle" class="t">LÓGICO — modelo relacional (tablas)</text>
  <text x="330" y="167" text-anchor="middle" class="s" fill="#e7eff8">Depende del TIPO de SGBD · cercano al diseñador</text>
  <rect x="120" y="195" width="420" height="60" rx="8" fill="#002a52"/>
  <text x="330" y="222" text-anchor="middle" class="t">FÍSICO — ficheros, índices, bloques</text>
  <text x="330" y="242" text-anchor="middle" class="s" fill="#cdd9e6">Depende del PRODUCTO y el soporte</text>
  <path d="M 70 55 L 70 245" stroke="#e89822" stroke-width="2.5" marker-end="url(#a1)"/>
  <defs><marker id="a1" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 Z" fill="#e89822"/></marker></defs>
  <text x="58" y="155" text-anchor="middle" class="lab" fill="#e89822" transform="rotate(-90 58 155)">+ dependencia tecnológica →</text>
  <text x="572" y="280" text-anchor="end" class="lab">[Fuente: ELMASRI, cap. 2]</text>
</svg>
```

---

## D2 · Arquitectura ANSI/SPARC (tres esquemas)

**Sección**: §1.2 — Niveles externo, conceptual e interno · **Propósito**: Mostrar los tres esquemas y su cardinalidad (varios externos, un conceptual, un interno).

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 660 320" role="img" aria-label="Arquitectura ANSI/SPARC con tres niveles: varios esquemas externos, un esquema conceptual y un esquema interno">
  <style>.t{font:700 13px system-ui,sans-serif;fill:#fff}.s{font:11px system-ui,sans-serif;fill:#1a1a1a}.lab{font:11px system-ui,sans-serif;fill:#666}.h{font:700 13px system-ui,sans-serif;fill:#0055a0}</style>
  <text x="330" y="24" text-anchor="middle" class="h">Tres esquemas e independencia de datos</text>
  <rect x="40" y="40" width="150" height="46" rx="6" fill="#2d8659"/><text x="115" y="60" text-anchor="middle" class="t">Vista A</text><text x="115" y="77" text-anchor="middle" class="s" fill="#dff0e7">contribuyentes</text>
  <rect x="255" y="40" width="150" height="46" rx="6" fill="#2d8659"/><text x="330" y="60" text-anchor="middle" class="t">Vista B</text><text x="330" y="77" text-anchor="middle" class="s" fill="#dff0e7">padrón</text>
  <rect x="470" y="40" width="150" height="46" rx="6" fill="#2d8659"/><text x="545" y="60" text-anchor="middle" class="t">Vista C</text><text x="545" y="77" text-anchor="middle" class="s" fill="#dff0e7">estadística</text>
  <text x="635" y="105" text-anchor="end" class="lab">NIVEL EXTERNO (varios)</text>
  <line x1="115" y1="86" x2="250" y2="135" stroke="#888"/><line x1="330" y1="86" x2="330" y2="135" stroke="#888"/><line x1="545" y1="86" x2="410" y2="135" stroke="#888"/>
  <rect x="160" y="135" width="340" height="55" rx="8" fill="#0055a0"/>
  <text x="330" y="158" text-anchor="middle" class="t">ESQUEMA CONCEPTUAL (único)</text>
  <text x="330" y="178" text-anchor="middle" class="s" fill="#dce8f5">entidades · atributos · relaciones · restricciones</text>
  <text x="635" y="210" text-anchor="end" class="lab">NIVEL CONCEPTUAL (uno)</text>
  <line x1="330" y1="190" x2="330" y2="235" stroke="#888"/>
  <rect x="160" y="235" width="340" height="55" rx="8" fill="#002a52"/>
  <text x="330" y="258" text-anchor="middle" class="t">ESQUEMA INTERNO (único)</text>
  <text x="330" y="278" text-anchor="middle" class="s" fill="#cdd9e6">ficheros · índices · rutas de acceso</text>
  <text x="635" y="305" text-anchor="end" class="lab">NIVEL INTERNO (uno) — [ANSI-SPARC]</text>
</svg>
```

---

## D3 · Independencia de datos: física y lógica

**Sección**: §1.3 — Los dos tipos de independencia · **Propósito**: Visualizar qué nivel aísla cada tipo de independencia.

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 660 250" role="img" aria-label="Independencia lógica entre externo y conceptual; independencia física entre conceptual e interno">
  <style>.t{font:700 13px system-ui,sans-serif;fill:#fff}.lab{font:11px system-ui,sans-serif;fill:#444}.h{font:700 13px system-ui,sans-serif;fill:#0055a0}.tag{font:700 12px system-ui,sans-serif;fill:#d13c3c}</style>
  <text x="330" y="24" text-anchor="middle" class="h">¿Qué aísla cada independencia?</text>
  <rect x="210" y="40" width="240" height="40" rx="6" fill="#2d8659"/><text x="330" y="65" text-anchor="middle" class="t">VISTAS / APLICACIONES</text>
  <line x1="120" y1="100" x2="540" y2="100" stroke="#d13c3c" stroke-width="2" stroke-dasharray="6 4"/>
  <text x="120" y="95" class="tag">⇅ Independencia LÓGICA</text>
  <text x="540" y="95" text-anchor="end" class="lab">cambiar el conceptual sin tocar vistas</text>
  <rect x="210" y="120" width="240" height="40" rx="6" fill="#0055a0"/><text x="330" y="145" text-anchor="middle" class="t">ESQUEMA CONCEPTUAL</text>
  <line x1="120" y1="180" x2="540" y2="180" stroke="#e89822" stroke-width="2" stroke-dasharray="6 4"/>
  <text x="120" y="175" class="tag" fill="#e89822">⇅ Independencia FÍSICA</text>
  <text x="540" y="175" text-anchor="end" class="lab">cambiar el almacenamiento sin tocar el conceptual</text>
  <rect x="210" y="200" width="240" height="40" rx="6" fill="#002a52"/><text x="330" y="225" text-anchor="middle" class="t">ESQUEMA INTERNO (físico)</text>
  <text x="650" y="246" text-anchor="end" class="lab" fill="#888">La lógica es la más difícil de lograr · [DATE]</text>
</svg>
```

---

## D4 · Las tres vistas del modelado

**Sección**: §1.5 — Estático, dinámico y funcional · **Propósito**: Asociar cada perspectiva con su técnica clásica y su equivalente UML.

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 660 280" role="img" aria-label="Tres vistas del modelado: estática con E-R, dinámica con DTE y funcional con DFD, y sus equivalentes UML">
  <style>.t{font:700 13px system-ui,sans-serif;fill:#fff}.s{font:11px system-ui,sans-serif;fill:#1a1a1a}.q{font:italic 11px system-ui,sans-serif;fill:#555}.h{font:700 13px system-ui,sans-serif;fill:#0055a0}.uml{font:11px system-ui,sans-serif;fill:#2d8659}</style>
  <text x="330" y="24" text-anchor="middle" class="h">Sistema de información: tres perspectivas</text>
  <rect x="30" y="50" width="190" height="180" rx="10" fill="#eaf1f8" stroke="#0055a0"/>
  <rect x="40" y="60" width="170" height="34" rx="6" fill="#0055a0"/><text x="125" y="83" text-anchor="middle" class="t">ESTÁTICA</text>
  <text x="125" y="118" text-anchor="middle" class="q">¿qué datos y cómo</text><text x="125" y="133" text-anchor="middle" class="q">se relacionan?</text>
  <text x="125" y="170" text-anchor="middle" class="s" font-weight="700">Modelo E-R</text>
  <text x="125" y="210" text-anchor="middle" class="uml">UML: clases</text>
  <rect x="235" y="50" width="190" height="180" rx="10" fill="#eaf1f8" stroke="#0055a0"/>
  <rect x="245" y="60" width="170" height="34" rx="6" fill="#0055a0"/><text x="330" y="83" text-anchor="middle" class="t">DINÁMICA</text>
  <text x="330" y="118" text-anchor="middle" class="q">¿cómo cambia de</text><text x="330" y="133" text-anchor="middle" class="q">estado ante eventos?</text>
  <text x="330" y="170" text-anchor="middle" class="s" font-weight="700">DTE</text>
  <text x="330" y="210" text-anchor="middle" class="uml">UML: estados</text>
  <rect x="440" y="50" width="190" height="180" rx="10" fill="#eaf1f8" stroke="#0055a0"/>
  <rect x="450" y="60" width="170" height="34" rx="6" fill="#0055a0"/><text x="535" y="83" text-anchor="middle" class="t">FUNCIONAL</text>
  <text x="535" y="118" text-anchor="middle" class="q">¿qué transformaciones</text><text x="535" y="133" text-anchor="middle" class="q">sufren los datos?</text>
  <text x="535" y="170" text-anchor="middle" class="s" font-weight="700">DFD</text>
  <text x="535" y="210" text-anchor="middle" class="uml">UML: actividad</text>
  <text x="630" y="262" text-anchor="end" class="q">[Fuente: RUMBAUGH · YOURDON]</text>
</svg>
```

---

## D5 · Notación de Chen: entidad, atributo y relación

**Sección**: §2.3 — Iconografía del E-R · **Propósito**: Recoger la simbología de Chen, incluida la de los tipos de atributo.

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 660 320" role="img" aria-label="Notación de Chen: entidad en rectángulo, relación en rombo, y tipos de atributos en elipses">
  <style>.t{font:700 12px system-ui,sans-serif;fill:#0055a0}.w{font:700 12px system-ui,sans-serif;fill:#fff}.lab{font:11px system-ui,sans-serif;fill:#555}.h{font:700 13px system-ui,sans-serif;fill:#0055a0}</style>
  <text x="330" y="22" text-anchor="middle" class="h">Símbolos del modelo Entidad-Relación (Chen)</text>
  <!-- entidad + relacion + entidad -->
  <rect x="40" y="120" width="120" height="50" fill="#0055a0" rx="2"/><text x="100" y="150" text-anchor="middle" class="w">HABITANTE</text>
  <polygon points="300,120 360,145 300,170 240,145" fill="#e89822"/><text x="300" y="149" text-anchor="middle" class="w" font-size="11">EMPADRON.</text>
  <rect x="440" y="120" width="120" height="50" fill="#0055a0" rx="2"/><text x="500" y="150" text-anchor="middle" class="w">VIVIENDA</text>
  <line x1="160" y1="145" x2="240" y2="145" stroke="#333" stroke-width="1.5"/><text x="200" y="138" text-anchor="middle" class="lab">N</text>
  <line x1="360" y1="145" x2="440" y2="145" stroke="#333" stroke-width="1.5"/><text x="400" y="138" text-anchor="middle" class="lab">1</text>
  <!-- atributos de habitante -->
  <ellipse cx="60" cy="60" rx="48" ry="20" fill="#fff" stroke="#0055a0"/><text x="60" y="64" text-anchor="middle" class="t" text-decoration="underline">DNI</text>
  <line x1="70" y1="78" x2="90" y2="118" stroke="#0055a0"/>
  <ellipse cx="165" cy="55" rx="50" ry="20" fill="#fff" stroke="#0055a0"/><ellipse cx="165" cy="55" rx="45" ry="15" fill="none" stroke="#0055a0"/><text x="165" y="59" text-anchor="middle" class="t" font-size="10">teléfono</text>
  <line x1="150" y1="72" x2="110" y2="118" stroke="#0055a0"/>
  <ellipse cx="270" cy="55" rx="46" ry="20" fill="#fff" stroke="#0055a0" stroke-dasharray="4 3"/><text x="270" y="59" text-anchor="middle" class="t" font-size="10">edad</text>
  <line x1="250" y1="70" x2="135" y2="118" stroke="#0055a0" stroke-dasharray="3 3"/>
  <!-- leyenda -->
  <rect x="40" y="220" width="580" height="80" rx="8" fill="#f5f7fa" stroke="#d1d7df"/>
  <text x="55" y="243" class="lab"><tspan font-weight="700">Rectángulo</tspan> = entidad   ◆ <tspan font-weight="700">Rombo</tspan> = relación   ⬭ <tspan font-weight="700">Elipse</tspan> = atributo</text>
  <text x="55" y="266" class="lab"><tspan font-weight="700">Subrayado</tspan> = identificador (clave)   ·   <tspan font-weight="700">Elipse doble</tspan> = multivaluado</text>
  <text x="55" y="289" class="lab"><tspan font-weight="700">Elipse discontinua</tspan> = derivado   ·   <tspan font-weight="700">Rectángulo doble</tspan> = entidad débil</text>
  <text x="630" y="315" text-anchor="end" class="lab" fill="#888">[Fuente: CHEN · ELMASRI cap. 3]</text>
</svg>
```

---

## D6 · Cardinalidades 1:1, 1:N y N:M

**Sección**: §2.4 — Razón de cardinalidad · **Propósito**: Distinguir los tres tipos de cardinalidad máxima en relaciones binarias.

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 660 300" role="img" aria-label="Tres cardinalidades: uno a uno, uno a muchos y muchos a muchos">
  <style>.w{font:700 11px system-ui,sans-serif;fill:#fff}.c{font:700 13px system-ui,sans-serif;fill:#d13c3c}.lab{font:11px system-ui,sans-serif;fill:#555}.h{font:700 13px system-ui,sans-serif;fill:#0055a0}</style>
  <text x="330" y="22" text-anchor="middle" class="h">Razón de cardinalidad (máxima)</text>
  <!-- 1:1 -->
  <text x="110" y="55" text-anchor="middle" class="c">1 : 1</text>
  <rect x="40" y="70" width="60" height="34" rx="4" fill="#0055a0"/><text x="70" y="92" text-anchor="middle" class="w">PERSONA</text>
  <line x1="100" y1="87" x2="150" y2="87" stroke="#333"/><text x="125" y="80" text-anchor="middle" class="lab">1   1</text>
  <rect x="150" y="70" width="60" height="34" rx="4" fill="#0055a0"/><text x="180" y="92" text-anchor="middle" class="w">DNI</text>
  <text x="125" y="125" text-anchor="middle" class="lab">cada persona, un DNI</text>
  <!-- 1:N -->
  <text x="330" y="55" text-anchor="middle" class="c">1 : N</text>
  <rect x="250" y="70" width="60" height="34" rx="4" fill="#0055a0"/><text x="280" y="92" text-anchor="middle" class="w">DISTRITO</text>
  <line x1="310" y1="87" x2="360" y2="87" stroke="#333"/><text x="335" y="80" text-anchor="middle" class="lab">1   N</text>
  <rect x="360" y="70" width="60" height="34" rx="4" fill="#0055a0"/><text x="390" y="92" text-anchor="middle" class="w">BARRIO</text>
  <text x="335" y="125" text-anchor="middle" class="lab">un distrito, muchos barrios</text>
  <!-- N:M -->
  <text x="560" y="55" text-anchor="middle" class="c">N : M</text>
  <rect x="470" y="70" width="80" height="34" rx="4" fill="#0055a0"/><text x="510" y="92" text-anchor="middle" class="w">FUNCIONARIO</text>
  <line x1="550" y1="87" x2="600" y2="87" stroke="#333"/><text x="575" y="80" text-anchor="middle" class="lab">N   M</text>
  <rect x="600" y="70" width="50" height="34" rx="4" fill="#0055a0"/><text x="625" y="92" text-anchor="middle" class="w">CURSO</text>
  <text x="560" y="125" text-anchor="middle" class="lab">varios en varios</text>
  <!-- nota transformacion -->
  <rect x="40" y="160" width="610" height="100" rx="8" fill="#e8f5ee" stroke="#2d8659"/>
  <text x="55" y="184" class="h" fill="#2d8659">Al pasar a tablas (modelo relacional):</text>
  <text x="55" y="208" class="lab">• <tspan font-weight="700">1:1</tspan> → clave ajena en una de las dos tablas</text>
  <text x="55" y="230" class="lab">• <tspan font-weight="700">1:N</tspan> → la clave del lado «1» se propaga como clave ajena al lado «N»</text>
  <text x="55" y="252" class="lab">• <tspan font-weight="700">N:M</tspan> → se crea una <tspan font-weight="700">tabla intermedia</tspan> con las claves de ambas entidades</text>
  <text x="630" y="285" text-anchor="end" class="lab" fill="#888">[Fuente: ELMASRI cap. 9]</text>
</svg>
```

---

## D7 · Generalización / especialización (jerarquía es-un)

**Sección**: §2.6 — EER · **Propósito**: Mostrar el supertipo, los subtipos y las restricciones (disjunta/solapada, total/parcial).

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 660 280" role="img" aria-label="Jerarquía de generalización: supertipo PERSONAL con subtipos FUNCIONARIO y LABORAL">
  <style>.w{font:700 12px system-ui,sans-serif;fill:#fff}.lab{font:11px system-ui,sans-serif;fill:#555}.h{font:700 13px system-ui,sans-serif;fill:#0055a0}.at{font:10px system-ui,sans-serif;fill:#0055a0}</style>
  <text x="330" y="24" text-anchor="middle" class="h">Generalización / especialización (es-un)</text>
  <rect x="250" y="45" width="160" height="50" rx="3" fill="#0055a0"/><text x="330" y="68" text-anchor="middle" class="w">PERSONAL</text><text x="330" y="86" text-anchor="middle" class="at" fill="#cfe0f0">dni · nombre · fecha_alta</text>
  <text x="425" y="80" class="lab">supertipo (atributos comunes)</text>
  <!-- triangulo ISA -->
  <line x1="330" y1="95" x2="330" y2="120" stroke="#333"/>
  <polygon points="330,120 312,145 348,145" fill="#fff" stroke="#333"/><text x="330" y="139" text-anchor="middle" class="lab" font-size="9">ISA</text>
  <line x1="200" y1="160" x2="312" y2="140" stroke="#333"/><line x1="460" y1="160" x2="348" y2="140" stroke="#333"/>
  <rect x="120" y="160" width="160" height="55" rx="3" fill="#3378b9"/><text x="200" y="183" text-anchor="middle" class="w">FUNCIONARIO</text><text x="200" y="201" text-anchor="middle" class="at" fill="#e3edf7">cuerpo · nº_registro</text>
  <rect x="380" y="160" width="160" height="55" rx="3" fill="#3378b9"/><text x="460" y="183" text-anchor="middle" class="w">LABORAL</text><text x="460" y="201" text-anchor="middle" class="at" fill="#e3edf7">convenio · categoría</text>
  <rect x="120" y="235" width="420" height="38" rx="6" fill="#fdf4e4" stroke="#e89822"/>
  <text x="135" y="251" class="lab"><tspan font-weight="700" fill="#e89822">Restricciones:</tspan> disjunta / solapada (¿un ejemplar en uno o varios subtipos?)</text>
  <text x="135" y="267" class="lab">total / parcial (¿todo ejemplar del supertipo está en algún subtipo?) — [ELMASRI cap. 4]</text>
</svg>
```

---

## D8 · Tres notaciones E-R: Chen, pata de gallo y UML

**Sección**: §2.7 — Notaciones equivalentes · **Propósito**: Comparar cómo cada notación dibuja la misma relación 1:N.

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 660 300" role="img" aria-label="La misma relación uno a muchos dibujada en notación Chen, pata de gallo y UML">
  <style>.w{font:700 10px system-ui,sans-serif;fill:#fff}.lab{font:11px system-ui,sans-serif;fill:#555}.h{font:700 13px system-ui,sans-serif;fill:#0055a0}.tt{font:700 12px system-ui,sans-serif;fill:#0055a0}</style>
  <text x="330" y="22" text-anchor="middle" class="h">«Un distrito contiene muchos barrios» (1:N) en tres notaciones</text>
  <!-- Chen -->
  <text x="110" y="55" text-anchor="middle" class="tt">CHEN</text>
  <rect x="45" y="70" width="58" height="30" fill="#0055a0" rx="2"/><text x="74" y="90" text-anchor="middle" class="w">DISTRITO</text>
  <polygon points="130,85 152,72 174,85 152,98" fill="#e89822"/><text x="152" y="89" text-anchor="middle" class="w" font-size="8">contiene</text>
  <rect x="118" y="120" width="58" height="30" fill="#0055a0" rx="2"/><text x="147" y="140" text-anchor="middle" class="w">BARRIO</text>
  <line x1="103" y1="85" x2="130" y2="85" stroke="#333"/><text x="116" y="79" class="lab" font-size="9">1</text>
  <line x1="152" y1="98" x2="152" y2="120" stroke="#333"/><text x="158" y="113" class="lab" font-size="9">N</text>
  <!-- Crow's foot -->
  <text x="330" y="55" text-anchor="middle" class="tt">PATA DE GALLO</text>
  <rect x="260" y="75" width="64" height="30" fill="#0055a0" rx="2"/><text x="292" y="95" text-anchor="middle" class="w">DISTRITO</text>
  <rect x="340" y="135" width="64" height="30" fill="#0055a0" rx="2"/><text x="372" y="155" text-anchor="middle" class="w">BARRIO</text>
  <line x1="292" y1="105" x2="372" y2="135" stroke="#333" stroke-width="1.5"/>
  <line x1="300" y1="112" x2="312" y2="116" stroke="#333"/>
  <path d="M 360 130 L 372 135 L 360 140 M 372 135 L 360 135" stroke="#333" fill="none"/>
  <text x="300" y="128" class="lab" font-size="9">uno</text><text x="320" y="150" class="lab" font-size="9">muchos</text>
  <!-- UML -->
  <text x="560" y="55" text-anchor="middle" class="tt">UML (clases)</text>
  <rect x="500" y="72" width="120" height="34" fill="#2d8659" rx="2"/><text x="560" y="93" text-anchor="middle" class="w">Distrito</text>
  <rect x="500" y="140" width="120" height="34" fill="#2d8659" rx="2"/><text x="560" y="161" text-anchor="middle" class="w">Barrio</text>
  <line x1="560" y1="106" x2="560" y2="140" stroke="#333"/>
  <text x="566" y="120" class="lab" font-size="10">1</text><text x="566" y="138" class="lab" font-size="10">1..*</text>
  <rect x="45" y="210" width="575" height="60" rx="8" fill="#f5f7fa" stroke="#d1d7df"/>
  <text x="60" y="234" class="lab">Las tres dicen lo mismo. <tspan font-weight="700">Chen</tspan>: rótulos 1/N. <tspan font-weight="700">Pata de gallo</tspan>: símbolos en los extremos (la «pata» = muchos).</text>
  <text x="60" y="256" class="lab"><tspan font-weight="700">UML</tspan>: multiplicidad numérica (1, 1..*, 0..1, *). — [Fuente: SILBERSCHATZ · MARTIN · UML]</text>
</svg>
```

---

## D9 · Diagrama de transición de estados (expediente)

**Sección**: §3.1 — Modelado dinámico · **Propósito**: Ilustrar estados, transiciones y eventos con el ciclo de vida de un expediente.

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 660 290" role="img" aria-label="Diagrama de transición de estados del ciclo de vida de un expediente administrativo">
  <style>.w{font:700 11px system-ui,sans-serif;fill:#fff}.ev{font:10px system-ui,sans-serif;fill:#d13c3c}.h{font:700 13px system-ui,sans-serif;fill:#0055a0}.lab{font:11px system-ui,sans-serif;fill:#555}</style>
  <text x="330" y="22" text-anchor="middle" class="h">Ciclo de vida de un expediente (DTE)</text>
  <defs><marker id="ar" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 Z" fill="#0055a0"/></marker></defs>
  <circle cx="45" cy="90" r="7" fill="#002a52"/>
  <rect x="75" y="70" width="105" height="40" rx="20" fill="#0055a0"/><text x="127" y="94" text-anchor="middle" class="w">INICIADO</text>
  <rect x="235" y="70" width="125" height="40" rx="20" fill="#0055a0"/><text x="297" y="94" text-anchor="middle" class="w">EN TRAMITACIÓN</text>
  <rect x="235" y="170" width="125" height="40" rx="20" fill="#e89822"/><text x="297" y="194" text-anchor="middle" class="w">SUBSANACIÓN</text>
  <rect x="420" y="70" width="105" height="40" rx="20" fill="#0055a0"/><text x="472" y="94" text-anchor="middle" class="w">RESUELTO</text>
  <rect x="555" y="70" width="95" height="40" rx="20" fill="#2d8659"/><text x="602" y="94" text-anchor="middle" class="w">ARCHIVADO</text>
  <line x1="52" y1="90" x2="73" y2="90" stroke="#0055a0" marker-end="url(#ar)"/>
  <line x1="180" y1="90" x2="233" y2="90" stroke="#0055a0" marker-end="url(#ar)"/><text x="206" y="83" text-anchor="middle" class="ev">admitir</text>
  <line x1="297" y1="110" x2="297" y2="168" stroke="#0055a0" marker-end="url(#ar)"/><text x="303" y="142" class="ev">requerir [falta doc.]</text>
  <path d="M 360 185 Q 410 150 360 112" stroke="#0055a0" fill="none" marker-end="url(#ar)"/><text x="412" y="150" class="ev">subsanar</text>
  <line x1="360" y1="90" x2="418" y2="90" stroke="#0055a0" marker-end="url(#ar)"/><text x="389" y="83" text-anchor="middle" class="ev">resolver</text>
  <line x1="525" y1="90" x2="553" y2="90" stroke="#0055a0" marker-end="url(#ar)"/><text x="540" y="83" text-anchor="middle" class="ev">notificar</text>
  <circle cx="602" cy="140" r="9" fill="none" stroke="#2d8659" stroke-width="2"/><circle cx="602" cy="140" r="4" fill="#2d8659"/>
  <line x1="602" y1="110" x2="602" y2="131" stroke="#0055a0" marker-end="url(#ar)"/>
  <text x="45" y="250" class="lab">Etiqueta de transición: <tspan font-weight="700">evento [guarda] / acción</tspan> · estado inicial (●), estados, estado final (◎)</text>
  <text x="630" y="275" text-anchor="end" class="lab" fill="#888">[Fuente: YOURDON · UML]</text>
</svg>
```

---

## D10 · Componentes del DFD

**Sección**: §4.1 — Los cuatro elementos · **Propósito**: Fijar los cuatro componentes del DFD y su simbología (Yourdon).

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 660 270" role="img" aria-label="Los cuatro componentes del diagrama de flujo de datos: proceso, flujo, almacén y entidad externa">
  <style>.w{font:700 12px system-ui,sans-serif;fill:#fff}.b{font:700 12px system-ui,sans-serif;fill:#0055a0}.lab{font:11px system-ui,sans-serif;fill:#555}.h{font:700 13px system-ui,sans-serif;fill:#0055a0}</style>
  <text x="330" y="22" text-anchor="middle" class="h">Cuatro componentes del DFD (notación Yourdon/DeMarco)</text>
  <!-- proceso -->
  <circle cx="100" cy="90" r="40" fill="#0055a0"/><text x="100" y="86" text-anchor="middle" class="w">1</text><text x="100" y="102" text-anchor="middle" class="w" font-size="9">Validar</text>
  <text x="100" y="155" text-anchor="middle" class="b">PROCESO</text><text x="100" y="172" text-anchor="middle" class="lab">transforma datos</text>
  <!-- flujo -->
  <line x1="200" y1="90" x2="300" y2="90" stroke="#333" stroke-width="2" marker-end="url(#fl)"/>
  <defs><marker id="fl" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#333"/></marker></defs>
  <text x="250" y="82" text-anchor="middle" class="lab">solicitud</text>
  <text x="250" y="155" text-anchor="middle" class="b">FLUJO</text><text x="250" y="172" text-anchor="middle" class="lab">dato en movimiento</text>
  <!-- almacen -->
  <line x1="360" y1="72" x2="460" y2="72" stroke="#0055a0" stroke-width="2"/>
  <line x1="360" y1="108" x2="460" y2="108" stroke="#0055a0" stroke-width="2"/>
  <line x1="360" y1="72" x2="360" y2="108" stroke="#0055a0" stroke-width="2"/>
  <text x="375" y="94" class="b" font-size="11">D1</text><text x="415" y="94" text-anchor="middle" class="lab">Padrón</text>
  <text x="410" y="155" text-anchor="middle" class="b">ALMACÉN</text><text x="410" y="172" text-anchor="middle" class="lab">dato en reposo</text>
  <!-- entidad externa -->
  <rect x="510" y="60" width="120" height="60" rx="2" fill="#2d8659"/><text x="570" y="95" text-anchor="middle" class="w">CONTRIBUYENTE</text>
  <text x="570" y="155" text-anchor="middle" class="b">ENTIDAD EXTERNA</text><text x="570" y="172" text-anchor="middle" class="lab">frontera del sistema</text>
  <rect x="40" y="200" width="590" height="56" rx="8" fill="#fbeeed" stroke="#d13c3c"/>
  <text x="55" y="223" class="lab"><tspan font-weight="700" fill="#d13c3c">Regla:</tspan> todo flujo pasa por un proceso. PROHIBIDO almacén↔almacén, entidad↔entidad, entidad↔almacén directos.</text>
  <text x="55" y="245" class="lab">Todo proceso tiene ≥1 entrada y ≥1 salida (ni «agujero negro» ni «milagro»). — [DEMARCO]</text>
</svg>
```

---

## D11 · Descomposición del DFD por niveles + equilibrado

**Sección**: §4.3 — Niveles y balanceo · **Propósito**: Mostrar contexto (nivel 0), nivel 1 y explosión, y la regla de equilibrado.

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 660 330" role="img" aria-label="Descomposición del DFD: diagrama de contexto nivel 0, nivel 1 y explosión de un proceso con equilibrado de flujos">
  <style>.w{font:700 11px system-ui,sans-serif;fill:#fff}.lab{font:11px system-ui,sans-serif;fill:#555}.h{font:700 12px system-ui,sans-serif;fill:#0055a0}.eq{font:700 11px system-ui,sans-serif;fill:#2d8659}</style>
  <text x="330" y="20" text-anchor="middle" class="h">Top-down: del contexto a las primitivas funcionales</text>
  <!-- nivel 0 -->
  <text x="100" y="48" text-anchor="middle" class="h">Nivel 0 · contexto</text>
  <rect x="40" y="60" width="50" height="26" rx="2" fill="#2d8659"/><text x="65" y="78" text-anchor="middle" class="w" font-size="9">CONTRIB.</text>
  <circle cx="135" cy="95" r="28" fill="#0055a0"/><text x="135" y="99" text-anchor="middle" class="w">0</text>
  <rect x="180" y="105" width="50" height="26" rx="2" fill="#2d8659"/><text x="205" y="123" text-anchor="middle" class="w" font-size="9">BANCO</text>
  <line x1="90" y1="78" x2="108" y2="88" stroke="#333" marker-end="url(#m2)"/><text x="92" y="72" class="lab" font-size="9">declarac.</text>
  <line x1="160" y1="110" x2="180" y2="116" stroke="#333" marker-end="url(#m2)"/><text x="150" y="135" class="lab" font-size="9">cobro</text>
  <defs><marker id="m2" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 Z" fill="#333"/></marker></defs>
  <text x="100" y="160" text-anchor="middle" class="lab" font-size="10">1 burbuja · sin almacenes</text>
  <!-- nivel 1 -->
  <text x="400" y="48" text-anchor="middle" class="h">Nivel 1 · sistema</text>
  <circle cx="320" cy="85" r="22" fill="#0055a0"/><text x="320" y="89" text-anchor="middle" class="w">1</text>
  <circle cx="400" cy="85" r="22" fill="#0055a0"/><text x="400" y="89" text-anchor="middle" class="w">2</text>
  <circle cx="480" cy="85" r="22" fill="#0055a0"/><text x="480" y="89" text-anchor="middle" class="w">3</text>
  <line x1="342" y1="85" x2="378" y2="85" stroke="#333" marker-end="url(#m2)"/>
  <line x1="422" y1="85" x2="458" y2="85" stroke="#333" marker-end="url(#m2)"/>
  <line x1="350" y1="125" x2="450" y2="125" stroke="#0055a0"/><line x1="350" y1="140" x2="450" y2="140" stroke="#0055a0"/><line x1="350" y1="125" x2="350" y2="140" stroke="#0055a0"/><text x="360" y="137" class="h" font-size="10">D1 Liquidaciones</text>
  <line x1="400" y1="107" x2="400" y2="125" stroke="#333" marker-end="url(#m2)"/>
  <text x="400" y="165" text-anchor="middle" class="lab" font-size="10">procesos 1,2,3 + almacenes</text>
  <!-- nivel 2 explosion -->
  <text x="330" y="205" text-anchor="middle" class="h">Nivel 2 · explosión del proceso «1»</text>
  <rect x="150" y="220" width="360" height="80" rx="8" fill="#eaf1f8" stroke="#0055a0" stroke-dasharray="5 4"/>
  <circle cx="220" cy="260" r="20" fill="#3378b9"/><text x="220" y="264" text-anchor="middle" class="w" font-size="10">1.1</text>
  <circle cx="330" cy="260" r="20" fill="#3378b9"/><text x="330" y="264" text-anchor="middle" class="w" font-size="10">1.2</text>
  <circle cx="440" cy="260" r="20" fill="#3378b9"/><text x="440" y="264" text-anchor="middle" class="w" font-size="10">1.3</text>
  <line x1="240" y1="260" x2="310" y2="260" stroke="#333" marker-end="url(#m2)"/>
  <line x1="350" y1="260" x2="420" y2="260" stroke="#333" marker-end="url(#m2)"/>
  <line x1="110" y1="260" x2="200" y2="260" stroke="#2d8659" stroke-width="2" marker-end="url(#m3)"/><text x="120" y="253" class="eq" font-size="9">declarac.</text>
  <line x1="460" y1="260" x2="550" y2="260" stroke="#2d8659" stroke-width="2" marker-end="url(#m3)"/><text x="500" y="253" class="eq" font-size="9">liquidación</text>
  <defs><marker id="m3" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 Z" fill="#2d8659"/></marker></defs>
  <text x="330" y="320" text-anchor="middle" class="eq">EQUILIBRADO: los flujos verdes (frontera del hijo) = entradas/salidas del proceso «1» del nivel 1 — [DEMARCO]</text>
</svg>
```

---

## D12 · Flujograma: símbolos ISO 5807 y estructuras básicas

**Sección**: §5.2 — Símbolos y control · **Propósito**: Recoger los símbolos normalizados y las tres estructuras de la programación estructurada.

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 660 340" role="img" aria-label="Símbolos de flujograma ISO 5807 y las tres estructuras básicas: secuencia, selección e iteración">
  <style>.w{font:700 11px system-ui,sans-serif;fill:#fff}.lab{font:10px system-ui,sans-serif;fill:#555}.h{font:700 13px system-ui,sans-serif;fill:#0055a0}.t{font:11px system-ui,sans-serif;fill:#1a1a1a}</style>
  <text x="330" y="20" text-anchor="middle" class="h">Símbolos (ISO 5807) y estructuras de control</text>
  <!-- simbolos -->
  <rect x="30" y="40" width="90" height="34" rx="17" fill="#002a52"/><text x="75" y="61" text-anchor="middle" class="w">inicio/fin</text><text x="75" y="88" text-anchor="middle" class="lab">terminal (óvalo)</text>
  <rect x="140" y="40" width="90" height="34" fill="#0055a0"/><text x="185" y="61" text-anchor="middle" class="w">proceso</text><text x="185" y="88" text-anchor="middle" class="lab">acción</text>
  <polygon points="295,40 335,57 295,74 255,57" fill="#e89822"/><text x="295" y="61" text-anchor="middle" class="w" font-size="10">¿cond?</text><text x="295" y="88" text-anchor="middle" class="lab">decisión (rombo)</text>
  <polygon points="370,40 460,40 440,74 350,74" fill="#2d8659"/><text x="405" y="61" text-anchor="middle" class="w">E/S</text><text x="405" y="88" text-anchor="middle" class="lab">entrada/salida</text>
  <circle cx="540" cy="57" r="17" fill="#666"/><text x="540" y="61" text-anchor="middle" class="w" font-size="10">A</text><text x="540" y="88" text-anchor="middle" class="lab">conector</text>
  <line x1="30" y1="105" x2="630" y2="105" stroke="#d1d7df"/>
  <!-- secuencia -->
  <text x="110" y="128" text-anchor="middle" class="h" font-size="12">SECUENCIA</text>
  <rect x="80" y="138" width="60" height="24" fill="#0055a0"/><text x="110" y="155" text-anchor="middle" class="w" font-size="10">A</text>
  <rect x="80" y="178" width="60" height="24" fill="#0055a0"/><text x="110" y="195" text-anchor="middle" class="w" font-size="10">B</text>
  <line x1="110" y1="162" x2="110" y2="178" stroke="#333" marker-end="url(#mf)"/>
  <defs><marker id="mf" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 Z" fill="#333"/></marker></defs>
  <!-- seleccion -->
  <text x="330" y="128" text-anchor="middle" class="h" font-size="12">SELECCIÓN</text>
  <polygon points="330,140 366,158 330,176 294,158" fill="#e89822"/><text x="330" y="162" text-anchor="middle" class="w" font-size="9">¿c?</text>
  <rect x="250" y="195" width="50" height="22" fill="#0055a0"/><text x="275" y="211" text-anchor="middle" class="w" font-size="9">sí</text>
  <rect x="360" y="195" width="50" height="22" fill="#0055a0"/><text x="385" y="211" text-anchor="middle" class="w" font-size="9">no</text>
  <line x1="305" y1="170" x2="275" y2="195" stroke="#333" marker-end="url(#mf)"/>
  <line x1="355" y1="170" x2="385" y2="195" stroke="#333" marker-end="url(#mf)"/>
  <!-- iteracion -->
  <text x="555" y="128" text-anchor="middle" class="h" font-size="12">ITERACIÓN</text>
  <polygon points="555,140 591,158 555,176 519,158" fill="#e89822"/><text x="555" y="162" text-anchor="middle" class="w" font-size="9">¿c?</text>
  <rect x="525" y="198" width="60" height="22" fill="#0055a0"/><text x="555" y="214" text-anchor="middle" class="w" font-size="9">cuerpo</text>
  <line x1="555" y1="176" x2="555" y2="198" stroke="#333" marker-end="url(#mf)"/><text x="562" y="190" class="lab">sí</text>
  <path d="M 585 209 Q 625 185 591 158" stroke="#333" fill="none" marker-end="url(#mf)"/>
  <rect x="40" y="245" width="590" height="80" rx="8" fill="#f5f7fa" stroke="#d1d7df"/>
  <text x="55" y="268" class="t"><tspan font-weight="700">Böhm-Jacopini (1966):</tspan> todo algoritmo se expresa con secuencia + selección + iteración, sin «goto».</text>
  <text x="55" y="291" class="t"><tspan font-weight="700">mientras</tspan> (while): comprueba antes (0..n veces). <tspan font-weight="700">repetir-hasta</tspan> (do-until): comprueba después (1..n veces).</text>
  <text x="55" y="314" class="t">Del rombo salen ≥2 ramas; del proceso, 1. Flujo por defecto: arriba→abajo. — [ISO5807 · BOHM-JACOPINI]</text>
</svg>
```
