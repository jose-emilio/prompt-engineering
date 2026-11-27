"""Recuperación sencilla (TF-IDF) sobre los documentos de ../../comun/empresa.

No usa embeddings ni bibliotecas externas: es deliberadamente simple para poder
entender cada paso. En un sistema real se usarían embeddings y un índice vectorial,
pero el patrón (trocear → indexar → recuperar → citar) es el mismo.
"""
import math, os, re, unicodedata
from collections import Counter

DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "comun", "empresa")
STOP = set("a al algo ante con como cual cuando cuanto de del el ella en es esta este esto la las lo los me mi mis muy no nos o para pero por que se si sin sobre su sus te tu un una uno y ya hay son ser han he qué cuál cuánto cómo dónde puede pueden tiene tienen".split())


def normalizar(t):
    t = unicodedata.normalize("NFD", t.lower())
    return "".join(c for c in t if unicodedata.category(c) != "Mn")


# Sinónimos mínimos para acercar el vocabulario de las preguntas al de los documentos.
SINONIMOS = {"cuesta": "precio", "cuanto": "precio", "coste": "precio", "cobran": "precio", "tarifa": "precio",
             "devolver": "reembolso", "devuelvan": "reembolso", "devolucion": "reembolso"}
_STOP_N = {normalizar(s) for s in STOP}


def tokens(t):
    out = []
    for w in re.findall(r"[a-z0-9]+", normalizar(t)):
        if w in _STOP_N or len(w) < 2:
            continue
        out.append(SINONIMOS.get(w, w))
    return out


def trocear(nombre, texto):
    """Un fragmento por apartado (encabezado) con su título; los muy largos se parten."""
    trozos, titulo, buf = [], nombre, []
    def cerrar():
        cuerpo = "\n".join(buf).strip()
        if len(cuerpo) > 40:
            trozos.append((titulo, cuerpo))
    for linea in texto.splitlines():
        if linea.startswith("#"):
            cerrar(); buf = []; titulo = linea.lstrip("# ").strip()
        else:
            buf.append(linea)
    cerrar()
    return trozos


class Indice:
    def __init__(self):
        self.docs = []   # dicts: id, doc, titulo, texto, tf
        for f in sorted(os.listdir(DIR)):
            if not f.endswith(".md"):
                continue
            texto = open(os.path.join(DIR, f), encoding="utf-8").read()
            for i, (tit, cuerpo) in enumerate(trocear(f[:-3], texto), 1):
                tf = Counter(tokens(tit + " " + cuerpo))
                self.docs.append(dict(id=f"{f[:-3]}#{i}", doc=f, titulo=tit, texto=cuerpo, tf=tf))
        n = len(self.docs)
        df = Counter(w for d in self.docs for w in d["tf"])
        self.idf = {w: math.log((n + 1) / (c + 0.5)) for w, c in df.items()}

    def buscar(self, consulta, k=3):
        q = Counter(tokens(consulta))
        res = []
        for d in self.docs:
            num = sum(q[w] * d["tf"][w] * self.idf.get(w, 0) ** 2 for w in q if w in d["tf"])
            den = math.sqrt(sum((c * self.idf.get(w, 0)) ** 2 for w, c in d["tf"].items())) or 1
            res.append((num / den, d))
        res.sort(key=lambda x: -x[0])
        return [dict(puntuacion=round(s, 3), id=d["id"], doc=d["doc"], titulo=d["titulo"], texto=d["texto"]) for s, d in res[:k]]


_INDICE = None
def recuperar(consulta, k=3):
    global _INDICE
    if _INDICE is None:
        _INDICE = Indice()
    return _INDICE.buscar(consulta, k)


if __name__ == "__main__":
    import sys
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "comun"))
    from utiles import crear_parser
    ap = crear_parser(__doc__, ["python rag.py plazo para pagar una factura", "python rag.py certificación SOC 2"])
    ap.add_argument("consulta", nargs="*", help="palabras de la consulta; si se omiten, se usa «plazo para pagar una factura»")
    a = ap.parse_args()
    for r in recuperar(" ".join(a.consulta) or "plazo para pagar una factura"):
        print(f"{r['puntuacion']:.3f}  {r['id']}  {r['titulo']}\n   {r['texto'][:120]!r}")
