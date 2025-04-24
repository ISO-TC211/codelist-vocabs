from pathlib import Path
import csv
from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.namespace import RDF, SDO, SKOS, XSD
from datetime import datetime

CS_NS = Namespace("http://def.isotc211.org/19115/-1/2014/Language-CharactersetLocalizationInformation/code/CountryCode/")
CS = URIRef("http://def.isotc211.org/19115/-1/2014/Language-CharactersetLocalizationInformation/code/CountryCode")

THIS_FILE = Path(__file__).resolve()
COUNTRIES_FILE = THIS_FILE.parent / 'countries.csv'
COUNTRIES_VOCAB = THIS_FILE.parent.parent / "resources" / "19115" / "-1" / "2018" / "CountryCode.ttl"

g = Graph()

with open(COUNTRIES_FILE) as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        print(row)
        print(f'{row[0]}, {row[1]}, {row[2]}, {row[3]}')
        concept_iri = CS_NS[row[1]]
        g.add((
            concept_iri,
            RDF.type,
            SKOS.Concept,
        ))
        g.add((
            concept_iri,
            SKOS.prefLabel,
            Literal(row[0].strip(), lang="en"),
        ))
        g.add((
            concept_iri,
            SKOS.definition,
            Literal("the country of " + row[0].strip(), lang="en"),
        ))
        g.add((
            concept_iri,
            SKOS.notation,
            Literal(row[2], datatype=CS_NS.alpha3Code),
        ))
        g.add((
            concept_iri,
            SKOS.notation,
            Literal(row[3], datatype=CS_NS.numericCode),
        ))
        g.add((
            concept_iri,
            SKOS.inScheme,
            CS,
        ))
        g.add((
            concept_iri,
            SKOS.topConceptOf,
            CS,
        ))
        g.add((
            CS,
            SKOS.hasTopConcept,
            concept_iri,
        ))

g.parse(COUNTRIES_VOCAB, format="turtle")
g.bind("cs", CS)
g.bind("", CS_NS)

for s, o in g.subject_objects(SDO.dateModified):
    g.remove((s, SDO.dateModified, o))
    g.add((s, SDO.dateModified, Literal(datetime.now().isoformat()[:10], datatype=XSD.date)))

g.serialize(destination=COUNTRIES_FILE.with_suffix(".ttl"), format="longturtle")