# This file makes redirect files for codelist IRIs for the https://def.isotc211.org website

from pathlib import Path

IRIS = [
    "<http://def.isotc211.org/19115/-1/2014/CommonClasses/code/MD_ScopeCode" ,
    "http://def.isotc211.org/19115/-1/2014/ConstraintInformation/code/MD_ClassificationCode" ,
    "http://def.isotc211.org/19115/-1/2014/ConstraintInformation/code/MD_RestrictionCode" ,
    "http://def.isotc211.org/19115/-1/2014/DistributionInformation/code/MD_MediumFormatCode" ,
    "http://def.isotc211.org/19115/-1/2014/ExampleOfExtendedMatadata/code/KeywordTypeCode-Bio" ,
    "http://def.isotc211.org/19115/-1/2014/IdentificationInformation/code/DS_AssociationTypeCode" ,
    "http://def.isotc211.org/19115/-1/2014/IdentificationInformation/code/DS_InitiativeTypeCode" ,
    "http://def.isotc211.org/19115/-1/2014/IdentificationInformation/code/MD_KeywordTypeCode" ,
    "http://def.isotc211.org/19115/-1/2014/IdentificationInformation/code/MD_ProgressCode" ,
    "http://def.isotc211.org/19115/-1/2014/IdentificationInformation/code/MD_SpatialRepresentationTypeCode" ,
    "http://def.isotc211.org/19115/-1/2014/Language-CharactersetLocalizationInformation/code/CountryCode" ,
    "http://def.isotc211.org/19115/-1/2014/Language-CharactersetLocalizationInformation/code/LanguageCode" ,
    "http://def.isotc211.org/19115/-1/2014/Language-CharactersetLocalizationInformation/code/MD_CharacterSetCode" ,
    "http://def.isotc211.org/19115/-1/2014/MaintenanceInformation/code/MD_MaintenanceFrequencyCode" ,
    "http://def.isotc211.org/19115/-1/2014/MetadataExtensionInformation/code/MD_DatatypeCode" ,
    "http://def.isotc211.org/19115/-1/2014/ReferenceSystemInformation/code/MD_ReferenceSystemTypeCode" ,
    "http://def.isotc211.org/19115/-1/2014/ServiceMetadataInformation/code/DCPList" ,
    "http://def.isotc211.org/19115/-1/2014/ServiceMetadataInformation/code/SV_CouplingType" ,
    "http://def.isotc211.org/19115/-1/2018/CitationAndResponsiblePartyInformation/code/CI_DateTypeCode" ,
    "http://def.isotc211.org/19115/-1/2018/CitationAndResponsiblePartyInformation/code/CI_OnLineFunctionCode" ,
    "http://def.isotc211.org/19115/-1/2018/CitationAndResponsiblePartyInformation/code/CI_PresentationFormCode" ,
    "http://def.isotc211.org/19115/-1/2018/CitationAndResponsiblePartyInformation/code/CI_RoleCode" ,
    "http://def.isotc211.org/19115/-1/2018/CitationAndResponsiblePartyInformation/code/CI_TelephoneTypeCode" ,
    "http://def.isotc211.org/19115/-1/2018/ContentInformation/code/MD_CoverageContentTypeCode" ,
    "http://def.isotc211.org/19115/-1/2018/ContentInformation/code/MD_ImagingConditionCode" ,
    "http://def.isotc211.org/19115/-1/2018/SpatialRepresentationInformation/code/MD_CellGeometryCode" ,
    "http://def.isotc211.org/19115/-1/2018/SpatialRepresentationInformation/code/MD_DimensionNameTypeCode" ,
    "http://def.isotc211.org/19115/-1/2018/SpatialRepresentationInformation/code/MD_GeometricObjectTypeCode" ,
    "http://def.isotc211.org/19115/-1/2018/SpatialRepresentationInformation/code/MD_TopologyLevelCode" ,
    "http://def.isotc211.org/19135/-1/2015/CoreModel/code/RE_AmendmentType" ,
    "http://def.isotc211.org/19135/-1/2015/CoreModel/code/RE_DecisionStatus" ,
    "http://def.isotc211.org/19135/-1/2015/CoreModel/code/RE_Disposition" ,
    "http://def.isotc211.org/19135/-1/2015/CoreModel/code/RE_ItemStatus" ,
    "http://def.isotc211.org/19135/-1/2015/CoreModel/code/RE_SimilarityToSource" ,
    "http://def.isotc211.org/19157/-1/2023/DataQualityEvaluation/code/EvaluationMethodTypeCode" ,
    "http://def.isotc211.org/19157/-1/2023/DataQualityMeasures/code/ValueStructure" ,
    "http://def.isotc211.org/19160/-1/2015/Address/code/AddressAliasType" ,
    "http://def.isotc211.org/19160/-1/2015/Address/code/AddressClass" ,
    "http://def.isotc211.org/19160/-1/2015/Address/code/AddressComponentType" ,
    "http://def.isotc211.org/19160/-1/2015/Address/code/AddressComponentValueType" ,
    "http://def.isotc211.org/19160/-1/2015/Address/code/AddressLifecycleStage" ,
    "http://def.isotc211.org/19160/-1/2015/Address/code/AddressPositionType" ,
    "http://def.isotc211.org/19160/-1/2015/Address/code/AddressStatus" ,
    "http://def.isotc211.org/19160/-1/2015/Address/code/AddressTypology" ,
    "http://def.isotc211.org/19160/-1/2015/Address/code/AddressableObjectLifecycleStage" ,
    "http://def.isotc211.org/19160/-1/2015/Address/code/AddressableObjectType" ,
    "http://def.isotc211.org/19160/-1/2015/Address/code/ReferenceObjectType" ,
]


for iri in IRIS:
    slug = iri.split("/")[-1]
    p = iri.replace("http://def.isotc211.org", "")

    temp = f"""---
permalink: {p}
redirect_to: https://defs-hosted.opengis.net/prez-hosted/object?uri={iri}
---

This page will redirect...
"""
    print(temp)
    f = Path(f"{slug}.adoc")
    with f.open("w") as f:
        f.write(temp)


"""
https://defs-hosted.opengis.net/prez-hosted/catalogs/tc211:/collections/ns34:KeywordTypeCode-Bio
https://defs-hosted.opengis.net/prez-hosted/catalogs/tc211:/collections/ns33:DS_AssociationTypeCode
https://defs-hosted.opengis.net/prez-hosted/catalogs/tc211:/collections/ns33:DS_InitiativeTypeCode
https://defs-hosted.opengis.net/prez-hosted/catalogs/tc211:/collections/ns31:CountryCode
https://defs-hosted.opengis.net/prez-hosted/catalogs/tc211:/collections/ns32:DCPList
https://defs-hosted.opengis.net/prez-hosted/catalogs/tc211:/collections/ns30:CI_DateTypeCode
https://defs-hosted.opengis.net/prez-hosted/catalogs/tc211:/collections/ns30:CI_OnLineFunctionCode
https://defs-hosted.opengis.net/prez-hosted/catalogs/tc211:/collections/ns30:CI_PresentationFormCode
https://defs-hosted.opengis.net/prez-hosted/catalogs/tc211:/collections/ns30:CI_RoleCode
https://defs-hosted.opengis.net/prez-hosted/catalogs/tc211:/collections/ns30:CI_TelephoneTypeCode
https://defs-hosted.opengis.net/prez-hosted/catalogs/tc211:/collections/ns36:MD_ClassificationCode
https://defs-hosted.opengis.net/prez-hosted/catalogs/tc211:/collections/ns31:LanguageCode
https://defs-hosted.opengis.net/prez-hosted/catalogs/tc211:/collections/ns31:MD_CharacterSetCode
https://defs-hosted.opengis.net/prez-hosted/catalogs/tc211:/collections/ns39:MD_MaintenanceFrequencyCode
https://defs-hosted.opengis.net/prez-hosted/catalogs/tc211:/collections/ns38:MD_DatatypeCode
https://defs-hosted.opengis.net/prez-hosted/catalogs/tc211:/collections/ns37:MD_CoverageContentTypeCode
https://defs-hosted.opengis.net/prez-hosted/catalogs/tc211:/collections/ns37:MD_ImagingConditionCode
https://defs-hosted.opengis.net/prez-hosted/catalogs/tc211:/collections/ns35:MD_CellGeometryCode
https://defs-hosted.opengis.net/prez-hosted/catalogs/tc211:/collections/ns35:MD_DimensionNameTypeCode
https://defs-hosted.opengis.net/prez-hosted/catalogs/tc211:/collections/ns35:MD_GeometricObjectTypeCode
https://defs-hosted.opengis.net/prez-hosted/catalogs/tc211:/collections/ns42:MD_ScopeCode
https://defs-hosted.opengis.net/prez-hosted/catalogs/tc211:/collections/ns36:MD_RestrictionCode
https://defs-hosted.opengis.net/prez-hosted/catalogs/tc211:/collections/ns40:MD_MediumFormatCode
https://defs-hosted.opengis.net/prez-hosted/catalogs/tc211:/collections/ns33:MD_KeywordTypeCode
https://defs-hosted.opengis.net/prez-hosted/catalogs/tc211:/collections/ns33:MD_ProgressCode
https://defs-hosted.opengis.net/prez-hosted/catalogs/tc211:/collections/ns33:MD_SpatialRepresentationTypeCode
https://defs-hosted.opengis.net/prez-hosted/catalogs/tc211:/collections/ns41:MD_ReferenceSystemTypeCode
https://defs-hosted.opengis.net/prez-hosted/catalogs/tc211:/collections/ns32:SV_CouplingType
https://defs-hosted.opengis.net/prez-hosted/catalogs/tc211:/collections/ns35:MD_TopologyLevelCode
https://defs-hosted.opengis.net/prez-hosted/catalogs/tc211:/collections/ns43:RE_AmendmentType
https://defs-hosted.opengis.net/prez-hosted/catalogs/tc211:/collections/ns43:RE_DecisionStatus
https://defs-hosted.opengis.net/prez-hosted/catalogs/tc211:/collections/ns43:RE_Disposition
https://defs-hosted.opengis.net/prez-hosted/catalogs/tc211:/collections/ns43:RE_ItemStatus
https://defs-hosted.opengis.net/prez-hosted/catalogs/tc211:/collections/ns43:RE_SimilarityToSource
https://defs-hosted.opengis.net/prez-hosted/catalogs/tc211:/collections/ns44:EvaluationMethodTypeCode
https://defs-hosted.opengis.net/prez-hosted/catalogs/tc211:/collections/ns45:ValueStructure
https://defs-hosted.opengis.net/prez-hosted/catalogs/tc211:/collections/ns46:AddressAliasType
https://defs-hosted.opengis.net/prez-hosted/catalogs/tc211:/collections/ns46:AddressClass
https://defs-hosted.opengis.net/prez-hosted/catalogs/tc211:/collections/ns46:AddressableObjectLifecycleStage
https://defs-hosted.opengis.net/prez-hosted/catalogs/tc211:/collections/ns46:AddressableObjectType
"""