from pathlib import Path
import csv
from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.namespace import RDF, SDO, SKOS, XSD
from datetime import datetime

CS_NS = Namespace("http://def.isotc211.org/19115/-1/2014/Language-CharactersetLocalizationInformation/code/LanguageCode/")
CS = URIRef("http://def.isotc211.org/19115/-1/2014/Language-CharactersetLocalizationInformation/code/LanguageCode")

THIS_FILE = Path(__file__).resolve()
LANGUAGES_FILE = THIS_FILE.parent / 'languages.csv'
LANGUAGES_VOCAB = THIS_FILE.parent.parent / "resources" / "19115" / "-1" / "2018" / "LanguageCode.ttl"

g = Graph()

with open(LANGUAGES_FILE) as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        print(row)
        print(f'{row[0]}, {row[1]}, {row[2]}, {row[3]}')
        concept_iri = CS_NS[row[0]]
        g.add((
            concept_iri,
            RDF.type,
            SKOS.Concept,
        ))
        g.add((
            concept_iri,
            SKOS.prefLabel,
            Literal(row[2].strip(), lang="en"),
        ))
        g.add((
            concept_iri,
            SKOS.definition,
            Literal("The language " + row[2].strip(), lang="en"),
        ))
        if row[1] != "":
            g.add((
                concept_iri,
                SKOS.notation,
                Literal(row[1], datatype=CS_NS["iso639-1Code"]),
            ))
        g.add((
            concept_iri,
            SKOS.altLabel,
            Literal(row[3], lang="fr"),
        ))
        g.add((
            concept_iri,
            SKOS.altLabel,
            Literal(row[4], lang="de"),
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

g.parse(LANGUAGES_VOCAB, format="turtle")
g.bind("cs", CS)
g.bind("", CS_NS)

for s, o in g.subject_objects(SDO.dateModified):
    g.remove((s, SDO.dateModified, o))
    g.add((s, SDO.dateModified, Literal(datetime.now().isoformat()[:10], datatype=XSD.date)))

g.serialize(destination=LANGUAGES_FILE.with_suffix(".ttl"), format="longturtle")