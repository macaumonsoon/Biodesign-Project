#!/usr/bin/env python3
"""
Build archival_media_research.csv: portal rows per species + curated special URLs.

Run from repo root:
  python3 scripts/extinction_archive_db/generate_archival_media_research.py
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path
from urllib.parse import quote

REPO_ROOT = Path(__file__).resolve().parents[2]
ANIMALS_CSV = REPO_ROOT / "data" / "extinction_archive" / "animals_full.csv"
OUT_CSV = REPO_ROOT / "data" / "extinction_archive" / "archival_media_research.csv"


def wikipedia_article_url(scientific_name: str) -> str:
    name = scientific_name.replace(" spp.", "").replace(" spp", "").strip()
    parts = name.split()
    if len(parts) >= 2:
        return f"https://en.wikipedia.org/wiki/{parts[0]}_{parts[1]}"
    if len(parts) == 1:
        return f"https://en.wikipedia.org/wiki/{parts[0]}"
    return "https://en.wikipedia.org/wiki/Extinction"


# Curated URLs (verify periodically; IUCN assessment IDs can change).
# BDC deep showcase (10+ institutional / dataset links each): see docs/research/bdc_showcase_species_shortlist.md
SPECIAL: dict[str, list[tuple[str, str, str, str, str]]] = {
    # --- Tier P0: PROJECT_PLAN MVP + ideation spine (chronobiology / ethics / social time) ---
    "Thylacinus cynocephalus": [
        (
            "conservation_record",
            "IUCN Red List — assessment (verify ID if site reorganises)",
            "https://www.iucnredlist.org/species/21866/21949291",
            "IUCN",
            "Official EX narrative; cite assessment version and date.",
        ),
        (
            "audiovisual",
            "NFSA — ‘last footage’ thylacine (moving image, licensed use)",
            "https://www.nfsa.gov.au/collection/item/tasmanian-tiger-last-footage-thylacine",
            "National Film and Sound Archive of Australia",
            "Exhibition/WebXR: request NFSA licence; do not assume YouTube rips are sufficient.",
        ),
        (
            "audiovisual",
            "NFSA — Hobart 1932 thylacine (collection item)",
            "https://www.nfsa.gov.au/collection/item/hobart-1932-thylacine",
            "NFSA",
            "Same licensing workflow as other NFSA collection items.",
        ),
        (
            "audiovisual",
            "NFSA catalogue search — additional clips & metadata",
            "https://www.nfsa.gov.au/search?q=thylacine",
            "NFSA",
            "Use for provenance of any film stills used in UI.",
        ),
        (
            "occurrence",
            "Atlas of Living Australia — species page (aggregated records)",
            "https://bie.ala.org.au/species/Thylacinus+cynocephalus",
            "Atlas of Living Australia",
            "National aggregation; follow through to publisher for catalogue numbers.",
        ),
        (
            "occurrence",
            "GBIF backbone taxon (example ID — confirm in UI)",
            "https://www.gbif.org/species/113394899",
            "GBIF",
            "Use for specimen/observation leads; check dataset licence per publisher.",
        ),
        (
            "specimen",
            "TMAG — Shaping Tasmania (articulated skeleton A315, online object)",
            "https://shapingtasmania.tmag.tas.gov.au/M/object.aspx?id=63",
            "Tasmanian Museum and Art Gallery",
            "Museum interpretation + accession context for cited 3D/AR anchors.",
        ),
        (
            "museum_education",
            "National Museum of Australia — collection highlight (thylacine)",
            "https://www.nma.gov.au/explore/collection/highlights/thylacine",
            "National Museum of Australia",
            "Public history framing; pair with Palawa-led scholarship for ethics copy.",
        ),
        (
            "museum_education",
            "NMA — Defining Moments resource (extinction narrative)",
            "https://www.nma.gov.au/defining-moments/resources/extinction-of-thylacine",
            "National Museum of Australia",
            "Teaching resource; not a substitute for Indigenous sovereignty literature.",
        ),
        (
            "museum_education",
            "Australian Museum — extinct species overview (thylacine)",
            "https://australian.museum/learn/australia-over-time/extinct-animals/the-thylacine/",
            "Australian Museum",
            "Orientation; cross-check facts against peer-reviewed sources.",
        ),
        (
            "genomics",
            "Nature Ecology & Evolution — thylacine genome (Feigin et al., 2018)",
            "https://www.nature.com/articles/s41559-017-0417-y",
            "Springer Nature",
            "Cited layer for aDNA / comparative marsupial genomics; read SI for data access.",
        ),
        (
            "genomics",
            "PMC — chromosome-scale hybrid assembly (Genome Biol. Evol.)",
            "https://pmc.ncbi.nlm.nih.gov/articles/PMC9007325/",
            "NIH / authors",
            "Higher-contiguity assembly; cite original paper and SRA/BioProject IDs from text.",
        ),
        (
            "morphology",
            "Palaeontologia Electronica — skeletal atlas of the thylacine (open PDF)",
            "https://palaeo-electronica.org/content/pdfs/947.pdf",
            "Palaeontologia Electronica",
            "CC BY; strong for orbit / postcranial cited reconstruction.",
        ),
        (
            "education",
            "Animal Diversity Web — species account",
            "https://animaldiversity.org/accounts/Thylacinus_cynocephalus/",
            "University of Michigan Museum of Zoology",
            "Student-oriented; trace references to primary literature.",
        ),
        (
            "literature",
            "BHL — full-text search (historic hunting & bounty discourse)",
            "https://www.biodiversitylibrary.org/search?searchTerm=Thylacinus+cynocephalus",
            "Biodiversity Heritage Library",
            "Volume-level rights vary; ideal for colonial-era primary quotes.",
        ),
        (
            "newspaper_archive",
            "NLA Trove — newspaper search (‘thylacine’ / ‘Tasmanian tiger’)",
            "https://trove.nla.gov.au/search/category/newspapers?keyword=thylacine",
            "National Library of Australia",
            "Public domain era-dependent; cite article date and title in exhibit.",
        ),
        (
            "research_lab",
            "TIGRR Lab (University of Melbourne) — marsupial / thylacine genomics hub",
            "https://tigrrlab.science.unimelb.edu.au/",
            "University of Melbourne",
            "Use for **ethics fork** on de-extinction biotech; not neutral ‘archive only’.",
        ),
    ],
    "Mammuthus primigenius": [
        (
            "occurrence",
            "GBIF backbone taxon (example ID — confirm in UI)",
            "https://www.gbif.org/species/4825833",
            "GBIF",
            "Fossil and modern collection records; filter basisOfRecord.",
        ),
        (
            "paleo",
            "Paleobiology Database — taxon check",
            "https://paleobiodb.org/classic/checkTaxonInfo?taxon_name=Mammuthus+primigenius&is_real_user=1",
            "Paleobiology Database",
            "CC BY 4.0; backbone for map + deep-time chronobiology framing.",
        ),
        (
            "genomics",
            "NCBI Taxonomy browser",
            "https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?name=Mammuthus+primigenius",
            "NCBI",
            "Gateway to nucleotide/SRA records; cite each BioProject’s primary publication.",
        ),
        (
            "paleo_science",
            "Science — ‘Lifetime mobility of an Arctic woolly mammoth’ (isotope tusk, 2021)",
            "https://www.science.org/doi/10.1126/science.abg1134",
            "AAAS",
            "Core **cited** paper for seasonal movement / sonification of migration legs.",
        ),
        (
            "popular_science",
            "Smithsonian Magazine — popular account of Kik tusk isotope study",
            "https://www.smithsonianmag.com/science-nature/scientists-tracked-movements-17000-year-old-woolly-mammoth-180983064/",
            "Smithsonian",
            "Secondary journalism; link to Science paper for claims.",
        ),
        (
            "genomics",
            "PMC — 3D genome architecture from ancient mammoth skin (Cell lineage)",
            "https://pmc.ncbi.nlm.nih.gov/articles/PMC12128189/",
            "NIH / authors",
            "Cutting-edge paleogenomics; label as cited molecular layer.",
        ),
        (
            "genomics",
            "bioRxiv / literature — elephantid genomes & mammoth Arctic adaptations (Lynch et al. lineage)",
            "https://www.biorxiv.org/content/10.1101/018366v1",
            "Cold Spring Harbor Laboratory",
            "Preprint or subsequent journal version — confirm final DOI for exhibition.",
        ),
        (
            "museum_data",
            "NHM London — Data Portal (search institutional mammoth records)",
            "https://data.nhm.ac.uk/",
            "Natural History Museum, London",
            "Query portal for specimen metadata; follow dataset licence.",
        ),
        (
            "dataset",
            "GBIF — NHM London collection dataset (occurrence publisher example)",
            "https://www.gbif.org/dataset/7e380070-f762-11e1-a439-00145eb45e9a",
            "GBIF / NHM",
            "Large specimen export; attribute NHM + GBIF.",
        ),
        (
            "morphology",
            "MorphoSource — search for published 3D mammoth scans",
            "https://www.morphosource.org/catalog/search?q=mammuthus+primigenius",
            "Duke University / contributors",
            "Per-object CC licences; required for honest ‘mesh source’ strip in WebXR.",
        ),
        (
            "literature",
            "BHL — full-text search (historic steppe / hunt accounts)",
            "https://www.biodiversitylibrary.org/search?searchTerm=Mammuthus+primigenius",
            "Biodiversity Heritage Library",
            "Historical illustration and prose for **interpolated** sensory prompts only.",
        ),
        (
            "news",
            "UAF news — university press on mammoth mobility study (outreach)",
            "https://uaf.edu/news/study-takes-unprecedented-peek-into-life-of-17000-year-old-mammoth.php",
            "University of Alaska Fairbanks",
            "Outreach summary; cite Wooller et al. Science for methods.",
        ),
        (
            "aggregator",
            "iDigBio portal — specimen search (US digitised collections)",
            "https://portal.idigbio.org/search",
            "iDigBio",
            "Filter by scientific name in UI; per-record media rights vary.",
        ),
        (
            "data_blog",
            "GBIF Data Blog — working with extinct species on GBIF",
            "https://data-blog.gbif.org/post/2024-02-06-working-with-extinct-species-on-gbif/",
            "GBIF",
            "Methodological context for your map / occurrence QA workflow.",
        ),
    ],
    "Ectopistes migratorius": [
        (
            "specimen",
            "NMNH — Martha (last individual) overview",
            "https://naturalhistory.si.edu/research/vertebrate-zoology/birds/collections-overview/martha-last-passenger-pigeon",
            "Smithsonian National Museum of Natural History",
            "USNM 30936; anchor for ‘endling’ narrative and ethics UI.",
        ),
        (
            "museum_archive",
            "Smithsonian — Martha object record (SIRIS)",
            "https://www.si.edu/object/martha-passenger-pigeon%3Asiris_sic_11640",
            "Smithsonian Institution",
            "Archival metadata; not a substitute for specimen database for research.",
        ),
        (
            "species_account",
            "Birds of the World — Passenger Pigeon (Blockstein 2020)",
            "https://birdsoftheworld.org/bow/species/paspig/cur/introduction",
            "Cornell Lab of Ornithology",
            "Subscription institution may be required; DOI 10.2173/bow.paspig.01.",
        ),
        (
            "multimedia",
            "Birds of the World — figures / media tab",
            "https://birdsoftheworld.org/bow/species/paspig/cur/multimedia?media=figures",
            "Cornell Lab of Ornithology",
            "Historic images; check BOW terms for screenshot reuse in deck.",
        ),
        (
            "education",
            "Project Passenger Pigeon (Chicago Academy of Sciences)",
            "https://naturemuseum.org/cas/project-passenger-pigeon",
            "Peggy Notebaert Nature Museum",
            "Public-education hub tied to 2014 centenary programming.",
        ),
        (
            "education",
            "Project Passenger Pigeon — archives & downloadable resources",
            "https://naturemuseum.org/cas/project-passenger-pigeon/p3-archives",
            "Peggy Notebaert Nature Museum",
            "Lesson plans & exhibit panels; verify allowed redistribution.",
        ),
        (
            "occurrence",
            "GBIF — species search",
            "https://www.gbif.org/species/search?q=Ectopistes+migratorius",
            "GBIF",
            "Eggs, skins, and legacy observation rows — cite publisher.",
        ),
        (
            "literature",
            "BHL — full-text search",
            "https://www.biodiversitylibrary.org/search?searchTerm=Ectopistes+migratorius",
            "Biodiversity Heritage Library",
            "Market hunting, nesting colony accounts; primary historical texture.",
        ),
        (
            "literature",
            "Internet Archive — Mershon, The Passenger Pigeon (1907)",
            "https://archive.org/details/passengerpigeon00mers",
            "Internet Archive",
            "Public-domain era likely; confirm on IA rights tab.",
        ),
        (
            "literature",
            "Internet Archive — French, Passenger Pigeon in Pennsylvania (1919)",
            "https://archive.org/details/passengerpigeoni00fren",
            "Internet Archive",
            "Regional hunting history; cite page images used.",
        ),
        (
            "journalism",
            "Audubon — long-form on extinction drivers",
            "https://www.audubon.org/magazine/why-passenger-pigeon-went-extinct",
            "National Audubon Society",
            "Secondary synthesis; link to Schorger / primary sources for claims.",
        ),
        (
            "audiovisual",
            "xeno-canto — species page (sparse but check for historical uploads)",
            "https://xeno-canto.org/species/Ectopistes-migratorius",
            "xeno-canto",
            "Likely empty; documents **acoustic absence** — powerful for Umwelt ‘silence’.",
        ),
        (
            "conservation_record",
            "IUCN Red List — search (assessment text if indexed)",
            "https://www.iucnredlist.org/search?query=Ectopistes+migratorius",
            "IUCN",
            "Use assessment citations for any ‘official’ threat narrative.",
        ),
        (
            "journalism",
            "All About Birds — essay on collecting & memory",
            "https://www.allaboutbirds.org/news/a-passion-for-a-pigeon/",
            "Cornell Lab of Ornithology",
            "Humanities angle for reflection panel prompts.",
        ),
        (
            "open_access",
            "Smithsonian Open Access — search gateway (related media)",
            "https://www.si.edu/openaccess",
            "Smithsonian Institution",
            "Filter for CC0 2D assets where available; not all Martha-adjacent items are OA.",
        ),
    ],
    # --- Tier P1: iconic “absence” + island coloniality + North Atlantic archive density ---
    "Raphus cucullatus": [
        (
            "specimen",
            "Oxford University Museum of Natural History — Oxford Dodo",
            "https://oumnh.ox.ac.uk/learn-the-oxford-dodo",
            "Oxford University Museum of Natural History",
            "Soft-tissue relic; DNA/CT literature cited from museum + journals.",
        ),
        (
            "specimen",
            "OUMNH — Oxford Dodo (alternate public page)",
            "https://oumnh.ox.ac.uk/oxford-dodo-en",
            "Oxford University Museum of Natural History",
            "Duplicate entry point; use for visitor-facing copy consistency.",
        ),
        (
            "interpretation",
            "NHM London — ‘real facts’ popular science article",
            "https://www.nhm.ac.uk/discover/the-dodo-bird-the-real-facts-about-this-icon-of-extinction.html",
            "Natural History Museum, London",
            "Secondary; good for AR / iconography context, not primary taxonomy.",
        ),
        (
            "interpretation",
            "NHM London — DinoDirectory entry",
            "https://www.nhm.ac.uk/discover/dino-directory/dodo.html",
            "Natural History Museum, London",
            "Kid-facing; still useful for glossary copy discipline.",
        ),
        (
            "genomics",
            "PMC — columbiform mitogenomes incl. dodo & solitaire (Soares et al.)",
            "https://pmc.ncbi.nlm.nih.gov/articles/PMC5080718/",
            "NIH / authors",
            "Cited molecular phylogeny; supports Nicobar pigeon comparative framing.",
        ),
        (
            "morphology",
            "PMC — convex-hull mass from CT (Brassey et al.)",
            "https://pmc.ncbi.nlm.nih.gov/articles/PMC4715441/",
            "NIH / authors",
            "Cited body-size / locomotion constraints for animation rig honesty.",
        ),
        (
            "occurrence",
            "GBIF — species search",
            "https://www.gbif.org/species/search?q=Raphus+cucullatus",
            "GBIF",
            "Few modern occurrences; mostly historical specimen digitisation.",
        ),
        (
            "morphology",
            "MorphoSource — search for dodo / Raphus scans",
            "https://www.morphosource.org/catalog/search?q=Raphus+cucullatus",
            "MorphoSource",
            "Check each mesh licence before WebXR import.",
        ),
        (
            "literature",
            "BHL — full-text search",
            "https://www.biodiversitylibrary.org/search?searchTerm=Raphus+cucullatus",
            "Biodiversity Heritage Library",
            "Colonial voyage accounts and early plates.",
        ),
        (
            "literature",
            "Internet Archive — search",
            "https://archive.org/search?query=Raphus+cucullatus",
            "Internet Archive",
            "Mixed rights; evaluate each item.",
        ),
        (
            "taxonomy",
            "NCBI Taxonomy",
            "https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?name=Raphus+cucullatus",
            "NCBI",
            "Links to sequence records if deposited.",
        ),
        (
            "education",
            "Animal Diversity Web — species account",
            "https://animaldiversity.org/accounts/Raphus_cucullatus/",
            "University of Michigan Museum of Zoology",
            "Secondary; verify against monographs.",
        ),
        (
            "conservation_record",
            "IUCN Red List — search",
            "https://www.iucnredlist.org/search?query=Raphus+cucullatus",
            "IUCN",
            "Historical assessments; cross-check with Reunion/Mauritius literature.",
        ),
        (
            "commons",
            "Wikimedia Commons — category (historical images)",
            "https://commons.wikimedia.org/wiki/Category:Raphus_cucullatus",
            "Wikimedia",
            "Per-file author/licence; many are centuries-old PD, some modern CC.",
        ),
        (
            "research_article",
            "Taylor & Francis — Oxford Dodo micro-CT / provenance spotlight (2020)",
            "https://www.tandfonline.com/doi/full/10.1080/08912963.2020.1782396",
            "Taylor & Francis",
            "Publisher page; use institutional access or author manuscript if needed.",
        ),
    ],
    "Pinguinus impennis": [
        (
            "literature",
            "BHL blog — Once There Were Billions (Great Auk corpus intro)",
            "https://blog.biodiversitylibrary.org/2014/06/once-there-were-billions-great-auk",
            "Biodiversity Heritage Library",
            "Entry to thousands of digitised pages mentioning the species.",
        ),
        (
            "literature",
            "Internet Archive — Crofford monograph example",
            "https://archive.org/details/greatauk0000crof",
            "Internet Archive",
            "Check copyright for this scan before commercial video reuse.",
        ),
        (
            "species_account",
            "Birds of the World — Great Auk",
            "https://birdsoftheworld.org/bow/species/greauk/cur/introduction",
            "Cornell Lab of Ornithology",
            "Synthesises historic accounts; cite BOW DOI on species page.",
        ),
        (
            "multimedia",
            "Birds of the World — figures / media tab",
            "https://birdsoftheworld.org/bow/species/greauk/cur/multimedia?media=figures",
            "Cornell Lab of Ornithology",
            "Historic skins / lithographs; BOW terms apply.",
        ),
        (
            "exhibition",
            "Smithsonian Libraries — Once There Were Billions digital exhibition",
            "https://library.si.edu/exhibition/once-there-were-billions",
            "Smithsonian Institution",
            "Curated extinct-bird narrative; strong for Context judging lane.",
        ),
        (
            "exhibition",
            "Smithsonian — Research Case: Great Auk (event/exhibit record)",
            "https://www.si.edu/exhibitions/research-case-great-auk-event-event-exhib-4482",
            "Smithsonian Institution",
            "Institutional framing of specimen culture.",
        ),
        (
            "blog",
            "Smithsonian Libraries Unbound — Great Auk essay",
            "https://blog.library.si.edu/blog/2014/06/27/great-auk-flightless-socialand-doomed/",
            "Smithsonian Institution",
            "Secondary essay with links into BHL items.",
        ),
        (
            "museum_object",
            "Smithsonian — mounted Great Auk skeleton (object record)",
            "https://www.si.edu/object/great-auk-skeleton-mounted-exhibit%3Asiris_arc_390394",
            "Smithsonian Institution",
            "Verify current URL if SI reorganises collections site.",
        ),
        (
            "occurrence",
            "GBIF — species search",
            "https://www.gbif.org/species/search?q=Pinguinus+impennis",
            "GBIF",
            "Eggs & skins in many NHMs; essential for global ‘last localities’ map QA.",
        ),
        (
            "literature",
            "BHL — full-text search",
            "https://www.biodiversitylibrary.org/search?searchTerm=Pinguinus+impennis",
            "Biodiversity Heritage Library",
            "Newfoundland / Iceland exploitation primary sources.",
        ),
        (
            "education",
            "Animal Diversity Web — species account",
            "https://animaldiversity.org/accounts/Pinguinus_impennis/",
            "University of Michigan Museum of Zoology",
            "Secondary overview with bibliographic hooks.",
        ),
        (
            "conservation_record",
            "IUCN Red List — search",
            "https://www.iucnredlist.org/search?query=Pinguinus+impennis",
            "IUCN",
            "Historic EX listing narrative.",
        ),
        (
            "genomics_literature",
            "PubMed — species search",
            "https://pubmed.ncbi.nlm.nih.gov/?term=Pinguinus+impennis",
            "NIH",
            "Ancient DNA / museomics papers on skins and eggs.",
        ),
        (
            "interpretation",
            "NHM London — extinction overview (context)",
            "https://www.nhm.ac.uk/discover/extinction.html",
            "Natural History Museum, London",
            "General framing; species-specific claims still need primary cites.",
        ),
        (
            "scholarship",
            "Environment & Society Portal — multimedia essay on historic testimony",
            "https://www.environmentandsociety.org/mml/piecing-together-the-extinct-great-auk-techniques-and-charms-of-contiguity",
            "Rachel Carson Center / LMU Munich",
            "Humanities framing for ethics / colonial extraction of skins & eggs.",
        ),
    ],
    # --- Other list species (shorter curated sets) ---
    "Megaloceros giganteus": [
        (
            "specimen",
            "National Museum of Ireland — Natural History (Giant Irish Deer)",
            "https://www.museum.ie/en-ie/museum-natural-history",
            "National Museum of Ireland – Natural History",
            "Public galleries; research access via collections enquiries.",
        ),
    ],
    "Numenius tenuirostris": [
        (
            "audiovisual",
            "xeno-canto — species page (rare flight-call recordings)",
            "https://xeno-canto.org/species/Numenius-tenuirostris",
            "xeno-canto",
            "Creative Commons per recording; read each track’s licence.",
        ),
    ],
    "Hydrodamalis gigas": [
        (
            "literature",
            "BHL search — Steller / historical voyage accounts",
            "https://www.biodiversitylibrary.org/search?searchTerm=Hydrodamalis+gigas",
            "Biodiversity Heritage Library",
            "Primary historical descriptions often in expedition literature.",
        ),
        (
            "marine_occurrence",
            "GBIF — species search",
            "https://www.gbif.org/species/search?q=Hydrodamalis+gigas",
            "GBIF",
            "Historical locality data sparse; treat as cited not interpolated.",
        ),
    ],
    "Chelonoidis abingdonii": [
        (
            "conservation_record",
            "IUCN Red List — search",
            "https://www.iucnredlist.org/search?query=Chelonoidis+abingdonii",
            "IUCN",
            "Assessment text documents last wild individuals narrative.",
        ),
    ],
    "Psephurus gladius": [
        (
            "taxonomy_occurrence",
            "FishBase — species summary",
            "https://www.fishbase.se/search.php?action=species&SpeciesName=Psephurus+gladius",
            "FishBase",
            "Check data version; useful for morphology & historic range notes.",
        ),
    ],
    "Corvus hawaiiensis": [
        (
            "audiovisual",
            "Macaulay Library — Hawaiian Crow search",
            "https://search.macaulaylibrary.org/catalog?searchField=species&species=hawaiian+crow",
            "Cornell Lab of Ornithology",
            "Per-asset media usage terms on Macaulay pages.",
        ),
    ],
    "Equus quagga quagga": [
        (
            "specimen",
            "NHM London — Scanning the Quagga",
            "https://www.nhm.ac.uk/discover/scanning-the-quagga.html",
            "Natural History Museum, London",
            "Museum interpretation; 3D data may have separate usage terms.",
        ),
    ],
}


def portal_rows(scientific_name: str, common_name: str) -> list[dict[str, str]]:
    q = quote(scientific_name)
    base = [
        {
            "scientific_name": scientific_name,
            "common_name": common_name,
            "resource_category": "portal_search",
            "title": "IUCN Red List — search",
            "url": f"https://www.iucnredlist.org/search?query={q}",
            "institution": "IUCN",
            "access_license_notes": "Red List text and maps have specific citation requirements; see IUCN terms.",
            "relevance_to_umwelt": "Authoritative extinction status narrative and threats summary.",
        },
        {
            "scientific_name": scientific_name,
            "common_name": common_name,
            "resource_category": "occurrence",
            "title": "GBIF — species search (specimens, fossils, observations)",
            "url": f"https://www.gbif.org/species/search?q={q}",
            "institution": "GBIF",
            "access_license_notes": "Per-dataset licences via dataset DOI; many CC BY.",
            "relevance_to_umwelt": "Georeferenced material for map layer; label per-record uncertainty.",
        },
        {
            "scientific_name": scientific_name,
            "common_name": common_name,
            "resource_category": "literature",
            "title": "Biodiversity Heritage Library — full-text search",
            "url": f"https://www.biodiversitylibrary.org/search?searchTerm={q}",
            "institution": "BHL consortium",
            "access_license_notes": "Volume-level rights vary; many pre-1928 works are public domain.",
            "relevance_to_umwelt": "Historical behaviour, habitat, and anthropogenic exploitation accounts.",
        },
        {
            "scientific_name": scientific_name,
            "common_name": common_name,
            "resource_category": "encyclopedia",
            "title": "Wikipedia — species article (verify against primary sources)",
            "url": wikipedia_article_url(scientific_name),
            "institution": "Wikimedia Foundation",
            "access_license_notes": "CC BY-SA; trace citations to primary literature for exhibit copy.",
            "relevance_to_umwelt": "Orientation only; use epistemic UI as Interpolated unless cross-cited.",
        },
        {
            "scientific_name": scientific_name,
            "common_name": common_name,
            "resource_category": "genomics_literature",
            "title": "PubMed / Europe PMC — scientific name search",
            "url": f"https://pubmed.ncbi.nlm.nih.gov/?term={q}",
            "institution": "NIH / Europe PMC",
            "access_license_notes": "Abstracts and OA full text vary by publisher.",
            "relevance_to_umwelt": "aDNA, morphology, ecology papers for cited reconstruction layers.",
        },
    ]
    # Paleobiology hint for prehistoric megafauna genera
    if any(
        x in scientific_name
        for x in (
            "Mammuthus",
            "Mammut",
            "Smilodon",
            "Megatherium",
            "Coelodonta",
            "Aenocyon",
            "Megaloceros",
            "Ursus",
            "Glyptodon",
        )
    ):
        pb_taxon = quote(
            scientific_name.replace(" spp.", "").replace(" spp", "").strip()
        )
        base.append(
            {
                "scientific_name": scientific_name,
                "common_name": common_name,
                "resource_category": "paleo",
                "title": "Paleobiology Database — taxon check",
                "url": f"https://paleobiodb.org/classic/checkTaxonInfo?taxon_name={pb_taxon}&is_real_user=1",
                "institution": "Paleobiology Database",
                "access_license_notes": "PBDB data CC BY 4.0; cite release snapshot.",
                "relevance_to_umwelt": "Fossil localities and temporal ranges for map + narrative.",
            }
        )
    return base


def main() -> None:
    if not ANIMALS_CSV.exists():
        print(f"Missing {ANIMALS_CSV}", file=sys.stderr)
        sys.exit(1)

    rows: list[dict[str, str]] = []
    with ANIMALS_CSV.open(encoding="utf-8", newline="") as f:
        for rec in csv.DictReader(f):
            sn = (rec.get("scientific_name") or "").strip()
            cn = (rec.get("common_name") or "").strip()
            if not sn:
                continue
            rows.extend(portal_rows(sn, cn))
            for cat, title, url, inst, note in SPECIAL.get(sn, []):
                rows.append(
                    {
                        "scientific_name": sn,
                        "common_name": cn,
                        "resource_category": cat,
                        "title": title,
                        "url": url,
                        "institution": inst,
                        "access_license_notes": note,
                        "relevance_to_umwelt": "Curated lead; verify before production embed.",
                    }
                )

    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "scientific_name",
        "common_name",
        "resource_category",
        "title",
        "url",
        "institution",
        "access_license_notes",
        "relevance_to_umwelt",
    ]
    with OUT_CSV.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)

    print(f"Wrote {len(rows)} rows to {OUT_CSV}")


if __name__ == "__main__":
    main()
