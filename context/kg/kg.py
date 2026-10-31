#!/usr/bin/env python3
"""Consulta del grafo de conocimiento (graph.json). Solo biblioteca estándar.

Uso:
  kg.py get ID                 Nodo completo + aristas entrantes y salientes
  kg.py ctx ID [-d N]          Vecindario compacto hasta profundidad N (def. 1)
  kg.py brief ID               Ficha de implementación (ideal para un CU-xx)
  kg.py find TEXTO             Búsqueda sin acentos ni mayúsculas en todo el nodo
  kg.py list [TIPO] [-s ESTADO]  Lista nodos (filtra por tipo y/o estado)
  kg.py inputs CALC-ID         Cierre transitivo de entradas de un cálculo
  kg.py open                   Pendientes, conflictos y vacíos no resueltos
  kg.py check                  Valida integridad del grafo
  kg.py render                 Regenera INDEX.md
"""
import json
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
GRAPH = HERE / "graph.json"
INDEX = HERE / "INDEX.md"

OPEN_STATUSES = {"PENDIENTE", "POR_VALIDAR", "PARCIAL", "ABIERTO"}
BASE_KEYS = ("id", "type", "title", "status", "src")


def load():
    data = json.loads(GRAPH.read_text(encoding="utf-8"))
    nodes = {n["id"]: n for n in data["nodes"]}
    out, inc = defaultdict(list), defaultdict(list)
    for e in data["edges"]:
        src, rel, dst = e[0], e[1], e[2]
        props = e[3] if len(e) > 3 else {}
        out[src].append((rel, dst, props))
        inc[dst].append((rel, src, props))
    return data, nodes, out, inc


def norm(s):
    s = unicodedata.normalize("NFKD", str(s))
    return "".join(c for c in s if not unicodedata.combining(c)).lower()


def label(nodes, nid):
    n = nodes.get(nid)
    if not n:
        return f"{nid} (¡inexistente!)"
    return f"{nid} [{n['type']}·{n['status']}] {n['title']}"


def fmt_props(props):
    return f"  ({'; '.join(f'{k}: {v}' for k, v in props.items())})" if props else ""


def print_node(n):
    print(f"# {n['id']} — {n['title']}")
    print(f"tipo: {n['type']} | estado: {n['status']} | src: {n.get('src', '-')}")
    for k, v in n.items():
        if k in BASE_KEYS:
            continue
        if isinstance(v, list):
            print(f"{k}:")
            for item in v:
                print(f"  - {item}")
        else:
            print(f"{k}: {v}")


def resolve(nodes, nid):
    if nid in nodes:
        return nid
    matches = [k for k in nodes if norm(k) == norm(nid)]
    if matches:
        return matches[0]
    sys.exit(f"Nodo no encontrado: {nid}. Prueba: kg.py find {nid}")


def cmd_get(nid):
    _, nodes, out, inc = load()
    nid = resolve(nodes, nid)
    print_node(nodes[nid])
    if out[nid]:
        print("\n→ salientes:")
        for rel, dst, p in sorted(out[nid]):
            print(f"  {rel} → {label(nodes, dst)}{fmt_props(p)}")
    if inc[nid]:
        print("\n← entrantes:")
        for rel, src, p in sorted(inc[nid]):
            print(f"  {label(nodes, src)} —{rel}→{fmt_props(p)}")


def cmd_ctx(nid, depth=1):
    _, nodes, out, inc = load()
    nid = resolve(nodes, nid)
    seen, frontier = {nid}, [nid]
    print(label(nodes, nid))
    for level in range(1, depth + 1):
        nxt = []
        for cur in frontier:
            for rel, other, _ in out[cur]:
                if other not in seen:
                    print(f"{'  ' * level}{cur} —{rel}→ {label(nodes, other)}")
                    seen.add(other)
                    nxt.append(other)
            for rel, other, _ in inc[cur]:
                if other not in seen:
                    print(f"{'  ' * level}{label(nodes, other)} —{rel}→ {cur}")
                    seen.add(other)
                    nxt.append(other)
        frontier = nxt


def cmd_brief(nid):
    """Ficha de implementación: el nodo, sus vecinos agrupados por tipo y
    lo que llega a través de sus patrones (colecciones, índices) y sus reglas
    (pendientes, conflictos, vacíos, criterios de aceptación)."""
    _, nodes, out, inc = load()
    nid = resolve(nodes, nid)
    print_node(nodes[nid])

    related = {}

    def add(other, via):
        related.setdefault(other, set()).add(via)

    for rel, other, _ in out[nid] + inc[nid]:
        add(other, rel)
    for first in list(related):
        ftype = nodes.get(first, {}).get("type")
        if ftype in ("Patron", "Regla", "Modulo", "Calculo"):
            for rel, other, _ in out[first] + inc[first]:
                otype = nodes.get(other, {}).get("type")
                if other != nid and otype in (
                    "Coleccion", "Indice", "Pendiente", "Conflicto", "Vacio",
                    "CriterioAceptacion", "ADR", "Infraestructura",
                ):
                    add(other, f"vía {first}")

    by_type = defaultdict(list)
    for other, vias in related.items():
        by_type[nodes.get(other, {}).get("type", "?")].append((other, vias))
    order = ["Actor", "Patron", "Modulo", "Infraestructura", "Regla", "ReglaArquitectura",
             "Seguridad", "Coleccion", "Indice", "Entidad", "Calculo", "ADR",
             "Pendiente", "Conflicto", "Vacio", "CriterioAceptacion", "FueraDeAlcance"]
    print()
    for t in order + sorted(set(by_type) - set(order)):
        if t not in by_type:
            continue
        print(f"## {t}")
        for other, vias in sorted(by_type[t]):
            n = nodes.get(other, {})
            extra = ""
            if t == "Regla":
                extra = f"\n      garante: {n.get('garante', '-')} | {n.get('mecanismo', n.get('regla', ''))}"
            elif t in ("Conflicto",):
                extra = f"\n      {n.get('regla_provisional') or n.get('vigente') or n.get('detalle', '')}"
            elif t == "Pendiente":
                extra = f"\n      {n.get('definir', '')}"
            elif t == "Patron":
                extra = f"\n      costo: {n.get('costo', '-')}" + (f" | {n['condicion']}" if n.get("condicion") else "")
            print(f"  - {label(nodes, other)}  ({', '.join(sorted(vias))}){extra}")
    flagged = [o for o in related if nodes.get(o, {}).get("status") in OPEN_STATUSES]
    if flagged:
        print(f"\n⚠ {len(flagged)} nodos relacionados no están cerrados: no completar con supuestos.")


def cmd_find(text):
    _, nodes, _, _ = load()
    q = norm(text)
    hits = [n for n in nodes.values() if q in norm(json.dumps(n, ensure_ascii=False))]
    for n in hits:
        print(label(nodes, n["id"]))
    if not hits:
        print("Sin resultados.")


def cmd_list(ntype=None, status=None):
    _, nodes, _, _ = load()
    for n in nodes.values():
        if ntype and norm(n["type"]) != norm(ntype):
            continue
        if status and n["status"] != status.upper():
            continue
        print(label(nodes, n["id"]))


def cmd_inputs(nid):
    _, nodes, out, _ = load()
    nid = resolve(nodes, nid)
    leaves, steps, stack, seen = set(), [], [nid], set()
    while stack:
        cur = stack.pop()
        if cur in seen:
            continue
        seen.add(cur)
        reqs = [dst for rel, dst, _ in out[cur] if rel == "requiere"]
        if cur != nid and nodes[cur]["type"] == "Calculo":
            steps.append(cur)
        if not reqs and cur != nid:
            leaves.add(cur)
        stack.extend(reqs)
    print(label(nodes, nid))
    print("cálculos intermedios:" if steps else "cálculos intermedios: ninguno")
    for s in sorted(steps):
        print(f"  - {label(nodes, s)}")
    print("datos de captura requeridos:")
    for leaf in sorted(leaves):
        print(f"  - {label(nodes, leaf)}")


def cmd_open():
    _, nodes, _, _ = load()
    for t in ("Pendiente", "Conflicto", "Vacio", "Calculo", "Regla", "Indice", "Coleccion", "CasoDeUso"):
        rows = [n for n in nodes.values() if n["type"] == t and n["status"] in OPEN_STATUSES]
        if rows:
            print(f"## {t}")
            for n in rows:
                print(f"  - {label(nodes, n['id'])}")


def cmd_check():
    data, nodes, _, _ = load()
    errors = []
    statuses = set(data["meta"]["estados"])
    rels = set(data["meta"]["relaciones"])
    ids = [n["id"] for n in data["nodes"]]
    for dup in {i for i in ids if ids.count(i) > 1}:
        errors.append(f"id duplicado: {dup}")
    for n in data["nodes"]:
        for k in BASE_KEYS:
            if k not in n:
                errors.append(f"{n.get('id')}: falta '{k}'")
        if n.get("status") not in statuses:
            errors.append(f"{n['id']}: estado desconocido '{n.get('status')}'")
    seen_edges = set()
    for e in data["edges"]:
        if e[1] not in rels:
            errors.append(f"relación desconocida: {e}")
        for end in (e[0], e[2]):
            if end not in nodes:
                errors.append(f"arista a nodo inexistente '{end}': {e}")
        key = (e[0], e[1], e[2])
        if key in seen_edges:
            errors.append(f"arista duplicada: {e}")
        seen_edges.add(key)
    linked = {e[0] for e in data["edges"]} | {e[2] for e in data["edges"]}
    orphans = sorted(set(nodes) - linked)
    if errors:
        print("\n".join(errors))
        sys.exit(1)
    print(f"OK: {len(nodes)} nodos, {len(data['edges'])} aristas.")
    if orphans:
        print(f"Nodos sin aristas ({len(orphans)}): {', '.join(orphans)}")


def cmd_render():
    data, nodes, out, inc = load()
    by_type = defaultdict(list)
    for n in data["nodes"]:
        by_type[n["type"]].append(n)
    lines = [
        "# Índice del grafo de conocimiento",
        "",
        "> Generado por `python3 context/kg/kg.py render` desde `graph.json`. No editar a mano.",
        f"> Versión {data['meta']['version']} · actualizado {data['meta']['actualizado']} · "
        f"{len(nodes)} nodos · {len(data['edges'])} aristas.",
        "",
        "## Precedencia de fuentes",
        "",
        *[f"- {p}" for p in data["meta"]["precedencia"]],
        "",
        "## Fuentes (`src`)",
        "",
        *[f"- **{k}**: {v}" for k, v in data["meta"]["fuentes"].items()],
        "",
    ]
    for t, rows in by_type.items():
        lines += [f"## {t} ({len(rows)})", "", "| ID | Título | Estado | Grado |", "|---|---|---|---|"]
        for n in rows:
            title = n["title"].replace("|", "\\|")
            lines.append(f"| {n['id']} | {title} | {n['status']} | {len(out[n['id']]) + len(inc[n['id']])} |")
        lines.append("")
    INDEX.write_text("\n".join(lines), encoding="utf-8")
    print(f"Escrito {INDEX.relative_to(HERE.parent.parent)}")


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return
    cmd, args = argv[0], argv[1:]

    def opt(flag, default=None):
        if flag in args:
            i = args.index(flag)
            val = args[i + 1]
            del args[i:i + 2]
            return val
        return default

    if cmd == "get":
        cmd_get(args[0])
    elif cmd == "ctx":
        depth = int(opt("-d", 1))
        cmd_ctx(args[0], depth)
    elif cmd == "brief":
        cmd_brief(args[0])
    elif cmd == "find":
        cmd_find(" ".join(args))
    elif cmd == "list":
        status = opt("-s")
        cmd_list(args[0] if args else None, status)
    elif cmd == "inputs":
        cmd_inputs(args[0])
    elif cmd == "open":
        cmd_open()
    elif cmd == "check":
        cmd_check()
    elif cmd == "render":
        cmd_render()
    else:
        sys.exit(f"Comando desconocido: {cmd}\n{__doc__}")


if __name__ == "__main__":
    main(sys.argv[1:])
