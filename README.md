# ISO TC-211 Codelist Vocabularies

This repository contains the source data of the [International Standards Organization](https://www.iso.org)'s [Technical Committee 211 (Geographic information/Geomatics)](https://committee.iso.org/home/tc211)'s codelist vocabularies.

The vocabularies are [Semantic Web](https://en.wikipedia.org/wiki/Semantic_Web) renditions of the codelists extpressed in standards in the 19* series, for example [ISO19115-1 Geographic information — Metadata Part 1: Fundamentals](https://www.iso.org/standard/53798.html).

These vocabularies are online at:

* *<https://defs-dev.opengis.net/prez-hosted/catalogs/tc211:>*



## Catalogue Manifest

The resources in this repository that constitute the catalogue of vocabularies online at <defs-dev.opengis.net/prez-hosted/catalogs/tc211:> are: 

| Resource                                                       | Role                                                                                                                | Description                                                                          |
|----------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| Catalogue Definition:<br />[`catalogue.ttl`](catalogue.ttl)    | [Catalogue Data](https://prez.dev/ManifestResourceRoles/CatalogueData)                                              | The definition of, and medata for, the container which here is a dcat:Catalog object |
| Resource Data:<br />[`resources/**/*.ttl`](resources/**/*.ttl) | [Resource Data](https://prez.dev/ManifestResourceRoles/ResourceData)                                                | skos:ConceptScheme objects in RDF (Turtle) files in the vocabs/ folder               |
| Labels:<br />[`labels.ttl`](labels.ttl)                        | [Complete Catalogue and Resource Labels](https://prez.dev/ManifestResourceRoles/CompleteCatalogueAndResourceLabels) | An RDF file containing all the labels for the container content                      |


## License & Use

These vocabularies are available for reuse under the conditions of the [Creative Commons BY 4.0 License](https://creativecommons.org/licenses/by/4.0/), a copy of the deed of which is contained in this repository in the LICENSE file.

These vocabularies and the software in this repository is copyright as follows:

&copy; International Organization for Standardization, 2025


## Contact

These vocabularies are produced by TC-211 and, within that, managed by the TC _Group on Ontology Maintenance_, GOM.

The following persons are the contact points for GOM:

**Nicholas J. Car**                     
*GOM Convenor*                           
ISO Technical Committee 211             
<nick@kurrawong.ai> 


**Ivana Ivánová**                     
*GOM Convenor*                           
ISO Technical Committee 211             
<ivana.ivanova@curtin.edu.au> 

> [!NOTE]  
> Contact points for individual vocabularies are not yet available but will become so in late 2025.
