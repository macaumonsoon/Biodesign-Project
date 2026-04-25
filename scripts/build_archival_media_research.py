"""Regenerate data/archival_media_research.{json,csv} from research_extinct_animals_list.json."""
from __future__ import annotations

import csv
import json
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


def enc(q: str) -> str:
    return urllib.parse.quote(q.strip(), safe="")


def urls_for_taxon(sci: str) -> dict[str, str]:
    q = sci.strip()
    return {
        "iucn_red_list_search": f"https://www.iucnredlist.org/search?query={enc(q)}",
        "gbif_species_search": f"https://www.gbif.org/species/search?q={enc(q)}",
        "gbif_occurrence_search": (
            "https://www.gbif.org/occurrence/search?"
            f"advanced=1&occurrence_status=present%2Cabsent&q={enc(q)}"
        ),
        "morphosource_search": f"https://www.morphosource.org/catalog?utf8=%E2%9C%93&q={enc(q)}",
        "pbdb_taxon_api": f"https://paleobiodb.org/data1.2/taxa/list.json?name={enc(q)}&limit=10",
        "pbdb_classic_ui": f"https://paleobiodb.org/#/taxon/list?taxon_name={enc(q)}",
        "bhl_literature_search": f"https://www.biodiversitylibrary.org/search?searchTerm={enc(q)}",
        "eol_search": f"https://eol.org/search?utf8=%E2%9C%93&q={enc(q)}",
        "smithsonian_3d_search": f"https://3d.si.edu/search?q={enc(q)}",
        "sketchfab_search": f"https://sketchfab.com/search?q={enc(q)}",
        "wikipedia": f"https://en.wikipedia.org/wiki/Special:Search?search={enc(q)}",
    }


NOTABLE: dict[str, list[dict[str, str]]] = {
    "Mammuthus primigenius": [
        {
            "type": "3d_portal",
            "label": "Smithsonian 3D — search mammoth / proboscidean entries",
            "url": "https://3d.si.edu/search?q=mammuthus",
        },
        {
            "type": "aggregator",
            "label": "MorphoSource — CT/mesh for comparative mammoth material",
            "url": "https://www.morphosource.org/catalog?q=mammuthus",
        },
    ],
    "Thylacinus cynocephalus": [
        {
            "type": "moving_image",
            "label": "National Film and Sound Archive of Australia — search thylacine (rights vary)",
            "url": "https://www.nfsa.gov.au/search?query=thylacine",
        },
        {
            "type": "museum",
            "label": "Tasmanian Museum and Art Gallery",
            "url": "https://www.tmag.tas.gov.au/",
        },
    ],
    "Ectopistes migratorius": [
        {
            "type": "audio",
            "label": "Xeno-canto — check for recordings / related columbids",
            "url": "https://xeno-canto.org/explore?query=Ectopistes+migratorius",
        },
        {
            "type": "specimen",
            "label": "Study skins via GBIF-linked institutions",
            "url": "https://www.gbif.org/species/search?q=Ectopistes+migratorius",
        },
    ],
    "Raphus cucullatus": [
        {
            "type": "specimen",
            "label": "Subfossil bone — query GBIF + NHM London collections portal",
            "url": "https://www.gbif.org/species/search?q=Raphus+cucullatus",
        },
    ],
    "Smilodon fatalis": [
        {
            "type": "museum",
            "label": "La Brea Tar Pits / NHMLAC (public + research programs)",
            "url": "https://tarpits.org/",
        },
    ],
    "Pinguinus impennis": [
        {
            "type": "specimen",
            "label": "Skins & eggs — European natural history collections (GBIF)",
            "url": "https://www.gbif.org/species/search?q=Pinguinus+impennis",
        },
    ],
    "Coelodonta antiquitatis": [
        {
            "type": "3d_portal",
            "label": "MorphoSource / museums — woolly rhino CTs and meshes",
            "url": "https://www.morphosource.org/catalog?q=Coelodonta",
        },
    ],
    "Hydrodamalis gigas": [
        {
            "type": "historical_record",
            "label": "BHL — Steller and expedition-era descriptions",
            "url": "https://www.biodiversitylibrary.org/search?searchTerm=Hydrodamalis+gigas",
        },
    ],
    "Psephurus gladius": [
        {
            "type": "specimen",
            "label": "Ichthyology collections — GBIF + institutional catalogs",
            "url": "https://www.gbif.org/species/search?q=Psephurus+gladius",
        },
    ],
    "Chelonoidis abingdonii": [
        {
            "type": "museum",
            "label": "Galápagos institutions + global NH collections (Lonesome George)",
            "url": "https://www.gbif.org/species/search?q=Chelonoidis+abingdonii",
        },
    ],
    "Lipotes vexillifer": [
        {
            "type": "literature_media",
            "label": "IUCN account + references for survey imagery (open species page from search)",
            "url": "https://www.iucnredlist.org/search?query=Lipotes%20vexillifer",
        },
    ],
    "Corvus hawaiiensis": [
        {
            "type": "audio",
            "label": "Macaulay Library / institutional recordings (verify license)",
            "url": "https://search.macaulaylibrary.org/catalog?searchField=species&q=Corvus+hawaiiensis",
        },
    ],
    "Ninox albifacies": [
        {
            "type": "audio",
            "label": "Historic laughing owl accounts + any archived recordings (verify)",
            "url": "https://xeno-canto.org/explore?query=Ninox+albifacies",
        },
    ],
    "Incilius periglenes": [
        {
            "type": "specimen_literature",
            "label": "Monteverde herpetology literature + museum vouchers (GBIF)",
            "url": "https://www.gbif.org/species/search?q=Incilius+periglenes",
        },
    ],
    "Glaucopsyche xerces": [
        {
            "type": "type_specimen",
            "label": "Lepidoptera collections — California Academy / AMNH (search catalogs)",
            "url": "https://www.gbif.org/species/search?q=Glaucopsyche+xerces",
        },
    ],
}


def main() -> None:
    src = DATA / "research_extinct_animals_list.json"
    out_json = DATA / "archival_media_research.json"
    out_csv = DATA / "archival_media_research.csv"

    bundle = json.loads(src.read_text(encoding="utf-8"))
    records: list[dict] = []

    for sp in bundle["species"]:
        sci = sp["scientific_name"]
        cat = sp.get("category", "")
        common = sp.get("common_name_en", "")
        pu = urls_for_taxon(sci)
        if cat.strip() == "Birds":
            pu["xeno_canto_search"] = f"https://xeno-canto.org/explore?query={enc(sci)}"
            pu["macaulay_library_search"] = (
                "https://search.macaulaylibrary.org/catalog?"
                f"searchField=species&q={enc(sci)}"
            )

        records.append(
            {
                "scientific_name": sci,
                "common_name_en": common,
                "category": cat,
                "list_source": sp.get("list_source", ""),
                "project_notes_existing_media": sp.get("model_3d_ref", "") or sp.get("notes", ""),
                "portal_urls": pu,
                "notable_archives_curated": NOTABLE.get(sci, []),
                "research_protocol": [
                    "Confirm IUCN category and dates on species page before citing.",
                    "Prefer institution catalog numbers + DOIs (MorphoSource) over unlicensed uploads.",
                    "For film/audio, verify rights before web embed.",
                ],
            }
        )

    meta = {
        "title": "Archival & open-media research pointers per species",
        "generated_for": "Umwelt Archive / Extinction Archive",
        "disclaimer": "URLs are search entry points and curated hints, not guaranteed specimen-level links. Verify with holding institution.",
        "global_portals": [
            {"name": "MorphoSource", "url": "https://www.morphosource.org/", "use": "CT/microCT + mesh; cite DOI"},
            {"name": "GBIF", "url": "https://www.gbif.org/", "use": "Occurrences, museum records"},
            {"name": "Paleobiology Database", "url": "https://paleobiodb.org/", "use": "Fossil occurrences + refs"},
            {"name": "Biodiversity Heritage Library", "url": "https://www.biodiversitylibrary.org/", "use": "Historic literature"},
            {"name": "Smithsonian 3D", "url": "https://3d.si.edu/", "use": "CC0 models (subset)"},
            {"name": "Digimorph", "url": "https://digimorph.org/", "use": "CT archive (subset)"},
            {"name": "UMORF", "url": "https://umorf.ummp.lsa.umich.edu/", "use": "Fossil 3D (Michigan)"},
        ],
        "species_count": len(records),
    }

    out_json.write_text(
        json.dumps({"meta": meta, "species": records}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    flat_fields = [
        "scientific_name",
        "common_name_en",
        "category",
        "list_source",
        "project_existing_media_note",
        "iucn_search",
        "gbif_species",
        "morphosource",
        "pbdb_ui",
        "bhl",
        "smithsonian_3d_search",
        "sketchfab_search",
        "xeno_canto",
        "macaulay",
        "notable_curated_count",
    ]
    with out_csv.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(flat_fields)
        for r in records:
            pu = r["portal_urls"]
            w.writerow(
                [
                    r["scientific_name"],
                    r["common_name_en"],
                    r["category"],
                    r["list_source"],
                    r["project_notes_existing_media"],
                    pu.get("iucn_red_list_search", ""),
                    pu.get("gbif_species_search", ""),
                    pu.get("morphosource_search", ""),
                    pu.get("pbdb_classic_ui", ""),
                    pu.get("bhl_literature_search", ""),
                    pu.get("smithsonian_3d_search", ""),
                    pu.get("sketchfab_search", ""),
                    pu.get("xeno_canto_search", ""),
                    pu.get("macaulay_library_search", ""),
                    len(r["notable_archives_curated"]),
                ]
            )

    print(f"Wrote {out_json} and {out_csv} ({len(records)} species)")


if __name__ == "__main__":
    main()
