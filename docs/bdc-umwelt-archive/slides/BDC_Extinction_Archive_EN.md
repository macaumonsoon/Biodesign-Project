---
marp: true
theme: default
paginate: true
footer: Extinction Archive · Umwelt Hypothesis Dossiers · BDC 2026
---

<!-- _class: lead -->

# Extinction Archive

## Umwelt Hypothesis Dossiers

*A Sensory Time Capsule · AI memorial — not resurrection*

Biodesign Challenge 2026 · **Convergent Life**  
WebXR + **in-repo data layer** · literature-grounded biodigital experience

---

# Repository & research layer (2026)

- **Web-only shipped build:** browser / WebXR — no live biosensor demo; QR + optional citation sheet  
- **51 taxa** → `animals_full.csv` · `archive.json` · `archive_import.sql` (PostgreSQL)  
- **`archival_media_research.csv`** — ~349 rows (IUCN, GBIF, BHL, NFSA, SI, BOW, PMC…)  
- **Planning + tiers:** `BDC_2026_Extinction_Archive_Planning_Document.md` · `docs/research/bdc_showcase_species_shortlist.md`  
- **Deep research:** `02_research/biology/biodigital_chronobiology_research.md` · regenerate: `scripts/extinction_archive_db/`

---

# The fracture

Extinction removes **bodies**, **ecological roles**, and **temporal niches**:

- circadian and seasonal fit to landscape  
- migration and isotope-recorded mobility  
- social synchrony (e.g. historic megaflocks)  

Public memory often **flattens** into icons.  
This project makes **absence** and **evidence** discussable — with **structured uncertainty**.

---

# Three guiding questions

1. How can **extinction–absence** become **perceptible** without false precision?  
2. How can **AI + biological data** support memory **transparently** — without replacing conservation or Indigenous knowledge systems?  
3. How can the senses act as **gentle cues** (optional layers, intensity caps)?

---

# Experience spine

- **Map → coordinate → species dossier** (full vision; **WebXR MVP = two deep species**)  
- **Bio layer:** genomics, morphology, isotopes, **museum & GBIF** traces  
- **Digital layer:** constrained generative scenes + **Web Audio** / stem metaphor  
- **Exit:** ethics fork + reflection → stewardship of **extant** biodiversity  

---

# Three modules

| Module | Role |
|--------|------|
| **Species Dossier** | Time, movement, sensory proxies — **scene → citation** |
| **Polyphony Mixer** | Season, diel rhythm, migration, density — harmony vs collapse |
| **Ethics Console** | Funding, invasion risk, **sovereignty** — incompatible choices |

---

# Species tiers

| Tier | Taxa | Role |
|------|------|------|
| **P0 WebXR** | *Mammuthus primigenius* · *Thylacinus cynocephalus* | Full interactive depth + epistemic UI |
| **P0 dossier** | *Ectopistes migratorius* | Slides / appendix: Martha, synchrony, **acoustic absence** |
| **P1 dossier** | Dodo · Great auk (*Raphus* · *Pinguinus*) | 14+ URLs each — Context lane; not WebXR v1 |

**51 taxa** in `data/extinction_archive/animals_full.csv` — systematic research, not 49 extra WebXR scenes.

---

# Bio + Digital (web-only build)

- **Biology:** palaeo-chronobiology; tusk isotopes; orbit → diel activity — **papers first**  
- **Digital:** A-Frame / Three.js; generative env with **constraint doc**; honesty UI always visible  
- **Shipped course build:** no live biosensor demo  

---

# Honesty UI

**Cited** · **Interpolated** · **Speculative**

- **Cited** — paper, catalogue, dataset row  
- **Interpolated** — justified model (e.g. RGC POV not measured on thylacine)  
- **Speculative** — creative; never “recovered reality”  

**NFSA / SI / BOW:** check **licence** before trailer or embed.

---

# Data layer (repository)

- `animals_full.csv` — pharm flags, Umwelt scores, 3D refs  
- `archive.json` · `archive_import.sql` — bundle + PostgreSQL  
- `archival_media_research.csv` — ~349 rows: IUCN, GBIF, BHL, NFSA, …  
- `docs/database/extinction_archive_schema.*` — future map + `reconstruction_layer`  

---

# Mammoth — anchors

- Lynch et al., 2015 — circadian-related gene enrichment (**conservative on PER2** until PDF verified)  
- Zimov et al., 2012 — mammoth steppe  
- Wooller et al., 2021 — **tusk isotope mobility** (*Science*) → sonification of movement  

---

# Thylacine — archives + ethics

- Pozniak et al., 2018 — orbit → crepuscular niche  
- **NFSA** moving image — **licence required**  
- **Palawa-led** sources + Clements / Schlunke — sovereignty vs de-extinction spectacle  

---

# Passenger pigeon — dossier

- Smithsonian **Martha** · Birds of the World · Project Passenger Pigeon  
- Social synchrony **collapse** — sonic metaphor  
- Sparse **xeno-canto** = honest **acoustic loss**  

---

# BDC alignment

- **Narrative** — immersion → uncertainty → ethical fork  
- **Concept** — Umwelt + temporal phenotype + biodigital load-bearing  
- **Context** — de-extinction trade-offs, pharm/trade, colonial archives  
- **Reflection** — AI limits, what archives omit, user reflection  

**Target:** **Biodigital Excellence**

---

# Deliverables · 4 weeks

- Live WebXR · citation grid · **one** ethical choice + reflection · trailer · QR  
- **EN PDF:** `slides/export/Extinction_Archive_Umwelt_Hypothesis_Dossiers_BDC2026_EN.pdf`  
- **GitHub alias (same file):** `slides/export/[FINAL-SMALL] Extinction Archive Umwelt Hypothesis Dossiers_BDC2026.pdf`  

**Build:** `python3 docs/bdc-umwelt-archive/scripts/build_extinction_archive_slides.py` (requires `fpdf2`, macOS Arial Unicode)

---

# Thank you

**Extinction Archive / Umwelt Archive**  
Questions?
