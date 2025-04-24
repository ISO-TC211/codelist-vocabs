from pathlib import Path
from rdflib import Graph, Literal, URIRef
from rdflib.namespace import DCAT, DCTERMS, RDF, SDO, XSD
from datetime import datetime


THIS_FILE = Path(__file__).resolve()
RESOURCES_DIR = THIS_FILE.parent.parent / "resources"
codelist_files = sorted(RESOURCES_DIR.rglob("*.ttl"))
CATALOGUE_FILE = THIS_FILE.parent.parent / "catalogue.ttl"

vocab_iris = []

for f in codelist_files:
    for line in f.read_text().splitlines():
        if line.startswith("PREFIX cs:"):
            vocab_iris.append(URIRef(line.replace("PREFIX cs: ", "").strip("<>")))

g = Graph().parse(CATALOGUE_FILE)

for s, o in g.subject_objects(DCTERMS.hasPart):
    g.remove((s, DCTERMS.hasPart, o))

for s in g.subjects(RDF.type, DCAT.Catalog):
    for iri in vocab_iris:
        g.add((s, DCTERMS.hasPart, iri))

for s, o in g.subject_objects(SDO.dateModified):
    g.remove((s, SDO.dateModified, o))
    g.add((s, SDO.dateModified, Literal(datetime.now().isoformat()[:10], datatype=XSD.date)))

g.serialize(CATALOGUE_FILE, format="longturtle")