#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generador del index.html del Tema 16 (ETRIVIUM IAM) a partir de los .md.

Generador COMPLETO (no quirúrgico) que produce el documento autosuficiente
con la estructura validada de la serie técnica (T13/T14/T15):

  - 8 pestañas: Inicio · Contenido · Índice · Diagramas · Test · Casos · Validación · Fuentes
  - Conversor md->HTML con listas anidadas REALES (corrige el bug de T14/T15)
  - Pestaña Índice cableada desde tema-16-indice.md
  - Diagramas: bloques ```svg``` embebidos en crudo (no escapados)
  - Banco de 60 preguntas parseado de tema-16-test.md + equilibrado A/B/C determinista
  - Motor de test con penalización 1/3 (idéntico a T13)

Es idempotente: re-ejecutarlo regenera index.html desde los .md (sincronizado).
"""
import re, html, json, random, os
from collections import Counter

BASE = os.path.dirname(os.path.abspath(__file__))
GEN_DATE = "2026-06-20"
SEED = 20260620


def read(name):
    with open(os.path.join(BASE, name), encoding="utf-8") as f:
        return f.read()


# ---------- Inline ----------
def inline(t):
    t = t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", t)
    t = t.replace("&lt;u&gt;", "<u>").replace("&lt;/u&gt;", "</u>")  # restaura subrayado explícito
    return t


CALLOUTS = {
    "DATO CLAVE EXAMEN": "dato",
    "EJERCICIO RESUELTO": "ejercicio",
    "EJEMPLO AYTO MADRID": "ayto",
    "REFERENCIA CRUZADA": "ref",
}


# ---------- Listas anidadas ----------
def build_list(items, i, indent, tag):
    out = f"<{tag}>"
    while i < len(items) and items[i][0] >= indent:
        ind, txt = items[i]
        if ind > indent:
            break
        out += "<li>" + inline(txt)
        i += 1
        if i < len(items) and items[i][0] > indent:
            child, i = build_list(items, i, items[i][0], tag)
            out += child
        out += "</li>"
    out += f"</{tag}>"
    return out, i


def _indent_of(line):
    return len(line) - len(line.lstrip(" "))


# ---------- Conversor Markdown -> HTML ----------
def md_to_html(md, skip_h1=True, drop_header_blockquote=True, raw_svg=False):
    lines = md.split("\n")
    out = []
    i, n = 0, len(lines)
    header_bq_dropped = False
    while i < n:
        line = lines[i]
        s = line.strip()
        # bloques de código ``` (con tratamiento especial para svg)
        if s.startswith("```"):
            lang = s[3:].strip()
            i += 1
            buf = []
            while i < n and lines[i].strip() != "```":
                buf.append(lines[i])
                i += 1
            i += 1  # salta cierre
            if raw_svg and lang == "svg":
                out.append("\n".join(buf))  # SVG en crudo
            else:
                out.append(f"<pre><code>{html.escape(chr(10).join(buf))}</code></pre>")
            continue
        if s == "---":
            out.append("<hr>")
            i += 1
            continue
        m = re.match(r"^(#{1,4})\s+(.*)$", s)
        if m:
            level = len(m.group(1))
            if level == 1 and skip_h1:
                i += 1
                continue
            out.append(f"<h{level}>{inline(m.group(2))}</h{level}>")
            i += 1
            continue
        if s.startswith("|") and i + 1 < n and re.match(r"^\|[\s:\-|]+\|$", lines[i + 1].strip()):
            header = [c.strip() for c in s.strip("|").split("|")]
            i += 2
            rows = []
            while i < n and lines[i].strip().startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            th = "".join(f"<th>{inline(c)}</th>" for c in header)
            trs = "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in rows)
            out.append(f"<table><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table>")
            continue
        if s.startswith(">"):
            bq = []
            while i < n and lines[i].strip().startswith(">"):
                bq.append(re.sub(r"^\s*>\s?", "", lines[i]))
                i += 1
            text = " ".join(x.strip() for x in bq if x.strip())
            if drop_header_blockquote and not header_bq_dropped and ("Título oficial" in text or "Título" in text or "Versión" in text):
                header_bq_dropped = True
                continue
            cm = re.match(r"^\*\*\[([^\]]+)\]\*\*\s*(.*)$", text)
            if cm and cm.group(1) in CALLOUTS:
                cls = CALLOUTS[cm.group(1)]
                out.append(f'<div class="callout {cls}"><span class="kicker">{cm.group(1)}</span>{inline(cm.group(2))}</div>')
            else:
                out.append(f"<blockquote>{inline(text)}</blockquote>")
            continue
        if re.match(r"^\s*-\s+", line):
            items = []
            while i < n and re.match(r"^\s*-\s+", lines[i]):
                items.append((_indent_of(lines[i]), re.sub(r"^\s*-\s+", "", lines[i]).strip()))
                i += 1
            base = min(it[0] for it in items)
            h, _ = build_list(items, 0, base, "ul")
            out.append(h)
            continue
        if re.match(r"^\s*\d+\.\s+", line):
            items = []
            while i < n and re.match(r"^\s*\d+\.\s+", lines[i]):
                items.append((_indent_of(lines[i]), re.sub(r"^\s*\d+\.\s+", "", lines[i]).strip()))
                i += 1
            base = min(it[0] for it in items)
            h, _ = build_list(items, 0, base, "ol")
            out.append(h)
            continue
        if s == "":
            i += 1
            continue
        para = [s]
        i += 1
        while i < n:
            nx = lines[i].strip()
            if nx == "" or nx.startswith(("#", "|", ">", "-", "---", "```")) or re.match(r"^\d+\.\s", nx):
                break
            para.append(nx)
            i += 1
        out.append(f"<p>{inline(' '.join(para))}</p>")
    return "\n".join(out)


# ---------- Índice ----------
def build_outline(entries, i, level):
    out = '<ol style="list-style:none">'
    while i < len(entries) and entries[i][0] >= level:
        lvl, txt = entries[i]
        if lvl > level:
            break
        out += "<li>" + txt
        i += 1
        if i < len(entries) and entries[i][0] > level:
            child, i = build_outline(entries, i, entries[i][0])
            out += child
        out += "</li>"
    out += "</ol>"
    return out, i


def indice_html(md):
    lines = md.split("\n")
    out = []
    i, n = 0, len(lines)
    while i < n:
        line = lines[i]
        s = line.strip()
        if s in ("---", ""):
            i += 1
            continue
        m = re.match(r"^(#{1,4})\s+(.*)$", s)
        if m:
            lvl = len(m.group(1))
            if lvl == 1:
                i += 1
                continue
            out.append(f"<h{lvl}>{inline(m.group(2))}</h{lvl}>")
            i += 1
            continue
        if s.startswith(">"):
            while i < n and lines[i].strip().startswith(">"):
                i += 1
            continue
        if s.startswith("|") and i + 1 < n and re.match(r"^\|[\s:\-|]+\|$", lines[i + 1].strip()):
            header = [c.strip() for c in s.strip("|").split("|")]
            i += 2
            rows = []
            while i < n and lines[i].strip().startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            th = "".join(f"<th>{inline(c)}</th>" for c in header)
            trs = "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in rows)
            out.append(f"<table><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table>")
            continue
        is_outline = (re.match(r"^\d+\.\s+\*\*", line) or re.match(r"^\s+\d+\.\d+", line))
        if is_outline:
            entries = []
            while i < n:
                ln = lines[i]
                t = ln.strip()
                mt = re.match(r"^(\d+)\.\s+\*\*(.+?)\*\*\s*$", t)
                m2 = re.match(r"^(\d+)\.(\d+)\.(\d+)\.\s+(.*)$", t)
                m1 = re.match(r"^(\d+)\.(\d+)\.\s+(.*)$", t)
                if mt:
                    entries.append((1, f"<strong>{mt.group(1)}. {inline(mt.group(2))}</strong>"))
                elif m2:
                    entries.append((3, inline(f"{m2.group(1)}.{m2.group(2)}.{m2.group(3)}. {m2.group(4)}")))
                elif m1:
                    entries.append((2, inline(f"{m1.group(1)}.{m1.group(2)}. {m1.group(3)}")))
                elif t == "":
                    if i + 1 < n and (re.match(r"^\d+\.\s+\*\*", lines[i + 1]) or re.match(r"^\s+\d+\.\d+", lines[i + 1])):
                        i += 1
                        continue
                    break
                else:
                    break
                i += 1
            h, _ = build_outline(entries, 0, 1)
            out.append(f'<div class="indice-outline">{h}</div>')
            continue
        out.append(f"<p>{inline(s)}</p>")
        i += 1
    return "\n".join(out)


# ---------- Test ----------
def parse_test(md):
    blocks = re.split(r"^###\s+Pregunta\s+\d+\s*$", md, flags=re.M)[1:]
    qs = []
    for b in blocks:
        lines = b.split("\n")
        enun = None
        opts = []
        correct = None
        expl = ""
        ref = ""
        for ln in lines:
            t = ln.strip()
            if enun is None:
                me = re.match(r"^\*\*(.+?)\*\*$", t)
                if me:
                    enun = me.group(1).strip()
                    continue
            mo = re.match(r"^([ABC])\)\s+(.*)$", t)
            if mo and correct is None:
                opts.append(mo.group(2).strip())
                continue
            mc = re.match(r"^\*\*Correcta:\s*([ABC])\)\s*(.*?)\*\*\s*(.*)$", t)
            if mc:
                correct = "ABC".index(mc.group(1))
                expl = mc.group(3).strip()
                continue
            mr = re.match(r"^\*Referencia:\s*(.*?)\*$", t)
            if mr:
                ref = mr.group(1).strip()
                continue
        if enun and len(opts) == 3 and correct is not None:
            qs.append({"q": enun, "opts": opts, "correct": correct, "expl": expl, "ref": ref})
    return qs


def balance(qs, seed=SEED):
    n = len(qs)
    targets = (["A"] * (n // 3 + 1) + ["B"] * (n // 3 + 1) + ["C"] * (n // 3 + 1))[:n]
    rnd = random.Random(seed)
    rnd.shuffle(targets)
    out = []
    for q, tgt in zip(qs, targets):
        correct_text = q["opts"][q["correct"]]
        others = [o for k, o in enumerate(q["opts"]) if k != q["correct"]]
        slots = {tgt: correct_text}
        rem = [x for x in "ABC" if x != tgt]
        for pos, txt in zip(rem, others):
            slots[pos] = txt
        out.append({
            "q": q["q"], "opts": [slots["A"], slots["B"], slots["C"]],
            "correct": "ABC".index(tgt), "expl": q["expl"], "ref": q["ref"],
        })
    return out


# ---------- CSS ----------
CSS = """:root{--azul:#0055a0;--azul-dark:#003d73;--azul-deep:#002a52;--azul-light:#e8f0f8;--azul-05:rgba(0,85,160,.05);--azul-10:rgba(0,85,160,.10);--verde:#2d8659;--verde-bg:#e8f5ee;--rojo:#d13c3c;--rojo-bg:#fbeeed;--amber:#e89822;--amber-bg:#fdf4e4;--g100:#f5f7fa;--g200:#e8ecf0;--g300:#d1d7df;--g600:#4a5568;--g800:#2d3748;--font:'DM Sans',-apple-system,system-ui,sans-serif;--rad:8px;--sh:0 1px 3px rgba(0,0,0,.08);--shl:0 4px 16px rgba(0,0,0,.08)}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:var(--font);color:var(--g800);background:var(--g100);line-height:1.65;-webkit-font-smoothing:antialiased}
.wrap{max-width:960px;margin:0 auto;padding:24px 20px 80px}
.tabs{position:sticky;top:0;z-index:10;background:var(--g100);display:flex;flex-wrap:wrap;gap:6px;padding:12px 0;border-bottom:2px solid var(--azul-10);margin-bottom:24px}
.tab-btn{border:1px solid var(--g300);background:#fff;color:var(--g600);padding:8px 14px;border-radius:6px;font:600 13px var(--font);cursor:pointer}
.tab-btn:hover{border-color:var(--azul)}
.tab-btn.active{background:var(--azul);color:#fff;border-color:var(--azul)}
.tab-btn .version-badge{background:var(--azul);color:#fff;border-radius:10px;padding:1px 7px;font-size:11px;margin-left:6px}
.tab-content{display:none}
.tab-content.active{display:block;animation:f .2s ease}
@keyframes f{from{opacity:0}to{opacity:1}}
h1{font-size:26px;color:var(--azul-dark);margin-bottom:10px;line-height:1.25}
h2{font-size:20px;color:var(--azul-dark);font-weight:700;margin:26px 0 12px;padding-bottom:6px;border-bottom:2px solid var(--azul-10)}
h3{font-size:16px;color:var(--azul);font-weight:600;margin:18px 0 8px}
h4{font-size:14px;color:var(--azul-dark);font-weight:600;margin:14px 0 6px}
p{margin:8px 0}
ul,ol{margin:8px 0 12px 22px}li{margin:4px 0}
u{text-decoration:underline}
hr{border:0;border-top:1px solid var(--g200);margin:18px 0}
code{background:var(--g200);padding:1px 6px;border-radius:3px;font-family:'SF Mono',Menlo,monospace;font-size:.88em;color:var(--azul-dark)}
pre{background:#0d1b2a;color:#e7ecf2;padding:14px 16px;border-radius:var(--rad);overflow-x:auto;margin:12px 0}
pre code{background:none;color:inherit;padding:0;font-size:13px;line-height:1.5}
table{width:100%;border-collapse:collapse;margin:12px 0;background:#fff;border-radius:var(--rad);overflow:hidden;box-shadow:var(--sh);font-size:14px}
th{background:var(--azul);color:#fff;padding:10px 12px;text-align:left;font-weight:600;font-size:13px}
td{padding:9px 12px;border-top:1px solid var(--g200);vertical-align:top}
tr:nth-child(even) td{background:var(--azul-05)}
.callout{border-left:4px solid var(--azul);background:var(--azul-light);padding:12px 16px;border-radius:4px;margin:14px 0}
.callout .kicker{display:inline-block;font:700 11px var(--font);letter-spacing:.6px;text-transform:uppercase;color:var(--azul-dark);margin-right:8px}
.callout.dato{border-left-color:var(--amber);background:var(--amber-bg)}.callout.dato .kicker{color:var(--amber)}
.callout.ejercicio{border-left-color:var(--verde);background:var(--verde-bg)}.callout.ejercicio .kicker{color:var(--verde)}
.callout.ayto{border-left-color:var(--azul);background:var(--azul-light)}
.callout.ref{border-left-color:var(--g600);background:var(--g100)}.callout.ref .kicker{color:var(--g600)}
.indice-outline ol{margin-left:18px}.indice-outline>ol{margin-left:0}
svg{max-width:100%;height:auto;display:block;margin:14px auto;background:#fff;border:1px solid var(--g200);border-radius:var(--rad);padding:8px}
.hero{background:linear-gradient(135deg,var(--azul-deep),var(--azul));color:#fff;padding:30px 28px;border-radius:var(--rad);margin-bottom:22px;box-shadow:var(--shl);position:relative}
.hero h1{color:#fff}
.hero .vbadge{position:absolute;top:18px;right:22px;background:var(--amber);color:#fff;padding:6px 12px;border-radius:6px;font:700 13px var(--font);letter-spacing:1px}
.hero .sub{opacity:.92;font-size:14px;margin-top:6px}
.hero .banner{margin-top:16px;padding-top:14px;border-top:1px solid rgba(255,255,255,.22);font-size:13px;opacity:.92}
.test-bar{position:sticky;top:64px;z-index:5;background:#fff;border:1px solid var(--g200);border-radius:var(--rad);padding:12px 16px;display:flex;gap:18px;flex-wrap:wrap;align-items:center;box-shadow:var(--sh);margin-bottom:18px}
.test-bar .kpi{font-size:13px;color:var(--g600)}
.test-bar .kpi b{font-size:18px;color:var(--azul-dark);display:block}
.test-bar button{border:0;border-radius:6px;padding:8px 14px;font:600 13px var(--font);cursor:pointer}
.btn-c{background:var(--verde);color:#fff}.btn-r{background:var(--g200);color:var(--g800)}
.question{background:#fff;border:1px solid var(--g200);border-radius:var(--rad);padding:16px 18px;margin-bottom:14px;box-shadow:var(--sh)}
.q-num{font:700 12px var(--font);color:var(--azul);letter-spacing:.5px;margin-bottom:6px}
.q-text{font-weight:600;margin-bottom:10px}
.q-opt{display:flex;gap:10px;align-items:center;border:1px solid var(--g200);border-radius:6px;padding:9px 12px;margin:6px 0;cursor:pointer}
.q-opt:hover{border-color:var(--azul)}
.q-opt.selected{border-color:var(--azul);background:var(--azul-05)}
.q-opt.correct{border-color:var(--verde);background:var(--verde-bg)}
.q-opt.wrong{border-color:var(--rojo);background:var(--rojo-bg)}
.q-letter{width:26px;height:26px;flex:0 0 26px;border-radius:50%;background:var(--azul);color:#fff;display:flex;align-items:center;justify-content:center;font:700 13px var(--font)}
.q-answer{display:none;margin-top:10px;padding:12px 14px;background:var(--verde-bg);border-left:4px solid var(--verde);border-radius:4px;font-size:14px}
.q-answer.show{display:block}
.q-ref{font-size:12px;color:var(--g600);margin-top:6px}
.footer{margin-top:40px;padding-top:20px;border-top:1px solid var(--g300);font-size:12px;color:var(--g600);text-align:center}
@media(max-width:640px){.tabs{top:0}.test-bar{top:0}}"""


ENGINE = """
function renderQuestions(){
  const c=document.getElementById('test-container');
  c.innerHTML=questions.map((q,i)=>`
    <div class="question" data-q="${i}">
      <div class="q-num">Pregunta ${i+1}</div>
      <div class="q-text">${q.q}</div>
      <div class="q-options">${q.opts.map((o,j)=>`<div class="q-opt" data-opt="${j}" onclick="selectOption(${i},${j})"><div class="q-letter">${String.fromCharCode(65+j)}</div><div>${o}</div></div>`).join('')}</div>
      <div class="q-answer"><strong>Correcta: ${String.fromCharCode(65+q.correct)}) ${q.opts[q.correct]}</strong><br>${q.expl}<div class="q-ref">Referencia: ${q.ref}</div></div>
    </div>`).join('');
}
const answers={};
function selectOption(qi,oi){answers[qi]=oi;const q=document.querySelector(`[data-q="${qi}"]`);q.querySelectorAll('.q-opt').forEach(e=>e.classList.remove('selected'));q.querySelector(`[data-opt="${oi}"]`).classList.add('selected');updateScore();}
function correctAll(){questions.forEach((q,i)=>{const el=document.querySelector(`[data-q="${i}"]`);el.querySelectorAll('.q-opt').forEach((e,j)=>{e.classList.remove('selected','correct','wrong');if(j===q.correct)e.classList.add('correct');else if(answers[i]===j)e.classList.add('wrong');});el.querySelector('.q-answer').classList.add('show');});}
function resetTest(){Object.keys(answers).forEach(k=>delete answers[k]);document.querySelectorAll('.q-opt').forEach(e=>e.classList.remove('selected','correct','wrong'));document.querySelectorAll('.q-answer').forEach(e=>e.classList.remove('show'));updateScore();}
function updateScore(){const r=Object.keys(answers).length;const ok=Object.entries(answers).filter(([i,v])=>questions[i].correct===v).length;const w=r-ok;document.getElementById('s-resp').textContent=r;document.getElementById('s-correct').textContent=ok;document.getElementById('s-wrong').textContent=w;document.getElementById('s-score').textContent=Math.max(0,ok-w/3).toFixed(2);}
function showTab(name,btn){document.querySelectorAll('.tab-content').forEach(e=>e.classList.remove('active'));document.querySelectorAll('.tab-btn').forEach(e=>e.classList.remove('active'));const t=document.getElementById('tab-'+name);if(t)t.classList.add('active');if(btn)btn.classList.add('active');try{window.scrollTo(0,0);}catch(e){}}
function initTabs(){document.querySelectorAll('.tab-btn[data-tab]').forEach(b=>b.addEventListener('click',function(){showTab(this.dataset.tab,this);}));try{renderQuestions();}catch(e){console.error(e);}}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',initTabs);else initTabs();
"""


# ---------- Build ----------
def build():
    def strip_lead_hr(s):
        return re.sub(r"^\s*<hr>\s*", "", s)

    contenido = strip_lead_hr(md_to_html(read("tema-16-contenido.md")))
    indice = indice_html(read("tema-16-indice.md"))
    diagramas = strip_lead_hr(md_to_html(read("tema-16-diagramas.md"), raw_svg=True))
    casos = strip_lead_hr(md_to_html(read("tema-16-caso-practico.md")))
    validacion = strip_lead_hr(md_to_html(read("tema-16-validacion.md")))
    fuentes = strip_lead_hr(md_to_html(read("tema-16-fuentes.md")))

    raw_qs = parse_test(read("tema-16-test.md"))
    qs = balance(raw_qs)
    dist = Counter(q["correct"] for q in qs)
    dist_abc = {"A": dist[0], "B": dist[1], "C": dist[2]}

    words = len(re.findall(r"\w+", read("tema-16-contenido.md")))
    words_es = f"{words:,}".replace(",", ".")  # millares estilo ES
    n_svg = read("tema-16-diagramas.md").count("```svg")

    questions_js = "[\n" + ",\n".join(
        "{q:%s,opts:%s,correct:%d,expl:%s,ref:%s}" % (
            json.dumps(q["q"], ensure_ascii=False),
            json.dumps(q["opts"], ensure_ascii=False),
            q["correct"],
            json.dumps(q["expl"], ensure_ascii=False),
            json.dumps(q["ref"], ensure_ascii=False),
        ) for q in qs) + "\n]"

    nav = ('<nav class="tabs">'
           '<button class="tab-btn active" data-tab="inicio">Inicio <span class="version-badge">v1.0</span></button>'
           '<button class="tab-btn" data-tab="contenido">Contenido</button>'
           '<button class="tab-btn" data-tab="indice">Índice</button>'
           '<button class="tab-btn" data-tab="diagramas">Diagramas</button>'
           '<button class="tab-btn" data-tab="test">Test</button>'
           '<button class="tab-btn" data-tab="casos">Casos</button>'
           '<button class="tab-btn" data-tab="validacion">Validación</button>'
           '<button class="tab-btn" data-tab="fuentes">Fuentes</button></nav>')

    inicio = f'''<section id="tab-inicio" class="tab-content active"><div class="hero">
  <span class="vbadge">v1.0</span>
  <h1>Tema 16 — Modelo conceptual de datos</h1>
  <div class="sub">Entidades, atributos y relaciones · Reglas de modelización · Diagramas de flujo de datos · Descomposición en niveles · Flujogramas</div>
  <div class="banner"><strong>Parte II — Técnico · C1 Ayuntamiento de Madrid</strong> · Piloto v1.0 · {GEN_DATE} · Pendiente de validación</div>
</div>
<h2>Qué incluye este tema</h2>
<table><thead><tr><th>Entregable</th><th>Cantidad</th></tr></thead><tbody>
<tr><td>Contenido teórico</td><td>5 secciones · ~{words_es} palabras</td></tr>
<tr><td>Diagramas SVG inline</td><td>{n_svg} diagramas autosuficientes</td></tr>
<tr><td>Banco de preguntas tipo test</td><td>{len(qs)} preguntas A/B/C con corrección y penalización 1/3</td></tr>
<tr><td>Casos prácticos Ayto Madrid</td><td>3 casos (Padrón, tasa de vado, licencia en sede electrónica)</td></tr>
<tr><td>Fuentes Tier 1</td><td>14 referencias canónicas (Chen, DeMarco, ISO 5807, UML, MÉTRICA v3…)</td></tr>
</tbody></table>
<div class="callout ref"><span class="kicker">Cómo estudiar</span>Lee el <strong>Contenido</strong>, apóyate en los <strong>Diagramas</strong>, autoevalúate en el <strong>Test</strong> y practica con los <strong>Casos</strong>. Las cajas naranjas (DATO CLAVE) marcan lo más memorizable.</div>
</section>'''

    test_section = '''<section id="tab-test" class="tab-content">
<div class="test-bar">
  <div class="kpi">Respondidas<b id="s-resp">0</b></div>
  <div class="kpi">Aciertos<b id="s-correct">0</b></div>
  <div class="kpi">Fallos<b id="s-wrong">0</b></div>
  <div class="kpi">Nota (−1/3)<b id="s-score">0.00</b></div>
  <button class="btn-c" onclick="correctAll()">Corregir todo</button>
  <button class="btn-r" onclick="resetTest()">Reiniciar</button>
</div>
<div id="test-container"></div>
</section>'''

    doc = f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Tema 16 v1.0 — Modelo conceptual de datos | ETRIVIUM IAM</title>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
{CSS}
</style>
</head>
<body>
<div class="wrap">
{nav}
{inicio}<section id="tab-contenido" class="tab-content">
<hr>
{contenido}
</section><section id="tab-indice" class="tab-content">
<hr>
{indice}
</section><section id="tab-diagramas" class="tab-content"><hr>
{diagramas}
</section>{test_section}<section id="tab-casos" class="tab-content"><hr>
{casos}
</section><section id="tab-validacion" class="tab-content"><hr>
{validacion}
</section><section id="tab-fuentes" class="tab-content"><hr>
{fuentes}
</section>
<div class="footer">ETRIVIUM · Material formativo TIC C1 · IAM Ayuntamiento de Madrid · Expediente 300_2026_00147<br>Tema 16 · v1.0 · {GEN_DATE} · Generado desde los .md (sincronizado)</div>
</div>
<script>
const questions = {questions_js};
{ENGINE}
</script>
</body>
</html>'''

    with open(os.path.join(BASE, "index.html"), "w", encoding="utf-8") as f:
        f.write(doc)

    nested = len(re.findall(r"[^>]<ul><li>", contenido)) + len(re.findall(r"[^>]<ol><li>", contenido))
    print(f"index.html generado: {len(doc):,} bytes")
    print(f"  · Preguntas: {len(qs)} · distribución A/B/C: {dist_abc}")
    print(f"  · Diagramas SVG: {n_svg} · Palabras contenido: {words:,}")
    print(f"  · Listas anidadas reales en Contenido: {nested}")
    print(f"  · Markdown crudo filtrado (** sueltos): {contenido.count('**') + diagramas.count('**')}")


if __name__ == "__main__":
    build()
