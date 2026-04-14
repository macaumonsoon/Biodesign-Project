---
marp: true
theme: default
paginate: true
footer: Extinction Archive · Umwelt Hypothesis Dossiers · BDC 2026
---

<!-- _class: lead -->

# Extinction Archive

## Umwelt Hypothesis Dossiers

*AI Memorial for Lost Species · A Sensory Time Capsule — not resurrection*

Biodesign Challenge 2026 · **Convergent Life** · **Ideas 3 + 6**  
Macau University · Mentor **Atticus SIMS**  
**GUO XIAO YUE** (MC569254) · **LIU JIA QUN** (MC569293)

---

# Creative arc — two dossiers → living database

- **Proof-of-concept:** woolly mammoth + thylacine — full WebXR depth + citations + ethics  
- **87 high-priority species** — sensory (1–10) + music layering (1–10) + data H/M/L  
- Curated from **900+** documented extinctions (Holocene, IUCN, 2025 confirmations)  
- **Criteria:** human intervention link, palaeo-data, sensory / chronobiology reconstruction potential  
- **Repo:** `animals_full.csv` — **51 taxa** imported now; merge full **87** for production exports  

---

# Research process (four steps)

1. **Preliminary concept** — pharm-related extinctions → collective biological memory  
2. **Unified CSV** — 87 species with sensory & music scores  
3. **Biodigital chronobiology** — genes, orbits, temporal niches (`biodigital_chronobiology_research.md`)  
4. **Bio + digital + ethics** — WebXR, constrained AI, Web Audio, decision interface + reflection  

---

# Repository & research layer

- **Shipped build:** browser / WebXR — no live biosensor MVP  
- **87 master list · 51 taxa** in `animals_full.csv` · `archive.json` · `archive_import.sql`  
- **`archival_media_research.csv`** — ~349 rows (IUCN, GBIF, BHL, NFSA, SI, BOW, PMC…)  
- **Planning:** `BDC_2026_Extinction_Archive_Planning_Document.md` · species tiers shortlist  
- **Regenerate:** `scripts/extinction_archive_db/`  

---

# The fracture

Extinction removes **bodies**, **ecological roles**, and **temporal niches**:

- circadian and seasonal fit to landscape  
- migration and isotope-recorded mobility  
- social synchrony (e.g. historic megaflocks)  

Public memory **flattens** into icons.  
This project makes **absence** discussable — with **structured uncertainty**.

---

# Umwelt dossiers — definition

- Each species = **folder of testable claims** — not fantasy safari  
- **Genes & circadian** · **orbit → diel** · **palaeo-climate / season** · **sight, sound, smell**  
- **AI memorial:** generative media **constrained** by peer-reviewed + licenced archives  
- **Sensory time capsule:** **when** they lived (temporal niche), not only **what** they looked like  

---

# Biodigital chronobiology — highlights

- **Mammoth:** Lynch 2015 — circadian genes (PER2/BMAL1 per primary read + planning log), TRPV3; Kim preprint — disclose in UI  
- **Polar analogy:** Lu 2010 reindeer — flexible clock ( **Interpolated** for mammoth )  
- **Nocturnal bottleneck** — mammalian diel evolution under dinosaur pressure  
- **Orbit proxy:** Pozniak 2018 — skull metrics vs diel pattern (>80% in study taxa)  
- **Sonification:** migration, vocalization, rhythm → Web Audio layers  
- **Insight:** extinction silences one voice in the planet’s **biological symphony**  

---

# Three guiding questions

1. How can **extinction–absence** become **perceptible** without false precision?  
2. How can **AI + biological data** support memory **transparently** — without replacing conservation or Indigenous knowledge?  
3. How can the senses act as **gentle cues** (optional layers, intensity caps)?  

---

# Experience spine & user journey

1. **Discover rhythm** — planetary map  
2. **Epistemic layers** — dossier (Cited / Interpolated / Speculative)  
3. **Immersive sensory** — 360° + chrono-music (**WebXR MVP = two deep species**)  
4. **Ethics sliders** — resources, risk, sovereignty, tech boundaries  
5. **Reflection log** — stewardship of **extant** biodiversity  

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

**87** master database — **51** taxa in repo CSV for systematic research, not 85 extra WebXR scenes.

---

# Ten representative species (scores = sensory / music)

| Species | Scores | Note |
|---------|--------|------|
| *Mammuthus primigenius* | 10 / 9 | Arctic circadian; steppe soundscape |
| *Thylacinus cynocephalus* | 10 / 10 | Recordings; skull → diel activity |
| *Ectopistes migratorius* | 10 / 10 | Megaflock sonification |
| *Raphus cucullatus* | 9 / 8 | Dodo; AR-ready 3D |
| *Pinguinus impennis* | 9 / 9 | Great auk; marine low-freq |
| *Smilodon fatalis* | 9 / 9 | Saber-toothed cat |
| *Hydrodamalis gigas* | 8 / 7 | Steller’s sea cow |
| *Chelonoidis abingdonii* | 9 / 6 | Lonesome George |
| *Ninox albifacies* | 8 / 9 | Laughing owl |
| *Incilius periglenes* | 7 / 6 | Golden toad |

---

# Bio + digital · physical + AR

- **Biology:** palaeo-chronobiology, morphology, isotopes, museum & GBIF — papers first  
- **Digital:** A-Frame / Three.js; constrained diffusion; **Web Audio**  
- **Full ideation:** plants + bacterial sensors — **not** in shipped MVP  
- **Physical:** 3D prints + **mobile AR** — evidence first, short Umwelt loop  
- **Course build:** web-first + one QR anchor  

---

# Honesty UI

**Cited** · **Interpolated** · **Speculative**

- **Cited** — paper, catalogue, dataset row  
- **Interpolated** — justified model (e.g. RGC POV not measured on thylacine)  
- **Speculative** — creative; never “recovered reality”  

**NFSA / SI / BOW:** check **licence** before trailer or embed.

---

# Data layer (repository)

- `animals_full.csv` — **51 taxa** now; **87** target master merge  
- `archive.json` · `archive_import.sql` — bundle + PostgreSQL  
- `archival_media_research.csv` — ~349 rows  
- `docs/database/extinction_archive_schema.*` — future map + `reconstruction_layer`  

---

# Mammoth — anchors

- Lynch et al., 2015 — circadian-related gene enrichment (**PER2 wording per planning PDF pass**)  
- Zimov et al., 2012 — mammoth steppe  
- Wooller et al., 2021 — **tusk isotope mobility** (*Science*) → sonification  

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

# BDC 2026 alignment

- **Ideas:** 3 (Extinction Archive) + 6 (Biorhythm Composer)  
- **Theme:** Convergent Life  
- **Prizes:** **Biodigital Excellence** · **Outstanding Digital Submission**  
- **Rubric:** Narrative → Concept → Context → Reflection  

---

# Deliverables · next steps

- Live WebXR · citation grid · **one** ethical choice + reflection · trailer · QR  
- **Next:** full **87** in exports · WebXR polish · AR models · **1–5 min** video  
- **EN PDF:** `slides/export/Extinction_Archive_Umwelt_Hypothesis_Dossiers_BDC2026_EN.pdf`  
- **GitHub alias (same file):** `slides/export/[FINAL-SMALL] Extinction Archive Umwelt Hypothesis Dossiers_BDC2026.pdf`  

**Build:** `python3 docs/bdc-umwelt-archive/scripts/build_extinction_archive_slides.py` (requires `fpdf2`, macOS Arial Unicode)

---

# Thank you

**Extinction Archive / Umwelt Hypothesis Dossiers**  
Macau University · 2026  
Questions?
