#!/usr/bin/env python3
"""
Build Extinction Archive slide PDFs (EN + ZH) — theme: archival biodigital (dark base, accent rule).
Output: REPO_ROOT/slides/export/ — EN compact + [FINAL-SMALL] alias + ZH + optional full judge deck.
Requires: pip install fpdf2
Font: Arial Unicode (macOS) for Latin + CJK.

Full judge deck (new file; does not overwrite BDC_Deck_EN.pdf or FINAL-SMALL):
  Extinction_Archive_Umwelt_BDC_Judge_Full_Deck_EN_2026.pdf
"""
from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

from fpdf import FPDF

# Repo root: .../Biodesign_Project_2 (scripts live under docs/bdc-umwelt-archive/scripts/)
REPO_ROOT = Path(__file__).resolve().parents[3]
EXPORT = REPO_ROOT / "slides" / "export"
# macOS Arial Unicode paths
FONT_CANDIDATES = [
    Path("/Library/Fonts/Arial Unicode.ttf"),
    Path("/System/Library/Fonts/Supplemental/Arial Unicode.ttf"),
]

BG = (20, 18, 16)
FG = (230, 223, 214)
ACCENT = (196, 92, 42)
SIGNAL = (92, 184, 154)
MUTED = (154, 143, 132)

# Standard widescreen 16:9 — same as PowerPoint / Keynote default (13.333" × 7.5")
INCH_TO_MM = 25.4
SLIDE_W_MM = 13.333 * INCH_TO_MM   # 338.6662 mm
SLIDE_H_MM = 7.5 * INCH_TO_MM      # 190.5 mm
MARGIN_X = 22.0
MARGIN_BULLET_INDENT = 4.0
# Content column width inside horizontal margins
CONTENT_W = SLIDE_W_MM - 2 * MARGIN_X
BOTTOM_SAFE = 16.0  # keep text above bottom crop on projectors


class Deck(FPDF):
    def __init__(self, font_path: Path):
        super().__init__(
            format=(round(SLIDE_W_MM, 2), round(SLIDE_H_MM, 2)),
            orientation="landscape",
            unit="mm",
        )
        self.set_auto_page_break(False)
        self.add_font("Archival", "", str(font_path))
        self._font = "Archival"
        self._w = float(SLIDE_W_MM)
        self._h = float(SLIDE_H_MM)

    def slide_bg(self) -> None:
        self.set_fill_color(*BG)
        self.rect(0, 0, self._w, self._h, "F")
        self.set_draw_color(*ACCENT)
        self.set_line_width(1.2)
        self.line(0, 6, self._w, 6)

    def title_slide(self, title: str, subtitle: str, lines: list[str]) -> None:
        self.add_page()
        self.slide_bg()
        self.set_font(self._font, "", 24)
        self.set_text_color(*FG)
        self.set_xy(MARGIN_X, 38)
        self.multi_cell(CONTENT_W, 13, title, align="L")
        self.set_font(self._font, "", 15)
        self.set_text_color(*ACCENT)
        self.set_xy(MARGIN_X, 64)
        self.multi_cell(CONTENT_W, 9, subtitle, align="L")
        self.set_font(self._font, "", 11.5)
        self.set_text_color(*MUTED)
        y = 94
        for line in lines:
            self.set_xy(MARGIN_X, y)
            self.multi_cell(CONTENT_W, 7.5, line, align="L")
            y += 8.5

    def body_slide(self, title: str, bullets: list[str], small: bool = False) -> None:
        self.add_page()
        self.slide_bg()
        self.set_font(self._font, "", 17)
        self.set_text_color(*ACCENT)
        self.set_xy(MARGIN_X, 24)
        self.multi_cell(CONTENT_W, 10, title, align="L")
        self.set_font(self._font, "" if not small else "", 11.5 if not small else 10)
        self.set_text_color(*FG)
        y = 46
        bullet_x = MARGIN_X + MARGIN_BULLET_INDENT
        bullet_w = CONTENT_W - MARGIN_BULLET_INDENT
        lim = self._h - BOTTOM_SAFE
        for b in bullets:
            self.set_xy(bullet_x, y)
            self.multi_cell(bullet_w, 6.8 if not small else 6.0, f"  •  {b}", align="L")
            y += 7.0 if not small else 6.4
            if y > lim:
                break

    def table_slide(self, title: str, headers: tuple[str, ...], rows: list[tuple[str, ...]], small: bool = True) -> None:
        self.add_page()
        self.slide_bg()
        self.set_font(self._font, "", 17)
        self.set_text_color(*ACCENT)
        self.set_xy(MARGIN_X, 24)
        self.multi_cell(CONTENT_W, 10, title, align="L")
        fs = 8.6 if small else 9.2
        col_w = CONTENT_W / len(headers)
        y = 42
        self.set_font(self._font, "", fs)
        self.set_text_color(*SIGNAL)
        x0 = MARGIN_X
        for i, h in enumerate(headers):
            self.set_xy(x0 + i * col_w, y)
            self.cell(col_w, 7.5, h, align="L")
        y += 10
        self.set_draw_color(80, 72, 65)
        self.line(MARGIN_X, y, MARGIN_X + CONTENT_W, y)
        y += 3.5
        self.set_font(self._font, "", fs - 0.2)
        self.set_text_color(*FG)
        lim = self._h - BOTTOM_SAFE
        for row in rows:
            for i, cell in enumerate(row):
                self.set_xy(x0 + i * col_w, y)
                self.multi_cell(col_w - 2, 4.8, cell, align="L")
            y += max(15, 4.8 * 2)
            if y > lim:
                break


def find_font() -> Path:
    for p in FONT_CANDIDATES:
        if p.exists():
            return p
    print("No Arial Unicode.ttf found; install a Unicode TTF and edit FONT_CANDIDATES.", file=sys.stderr)
    sys.exit(1)


def build_en(font: Path) -> None:
    d = Deck(font)
    d.title_slide(
        "Extinction Archive",
        "Umwelt Hypothesis Dossiers — A Sensory Time Capsule",
        [
            "AI Memorial for Lost Species · Biodesign Challenge 2026 · Convergent Life",
            "Macau University · Mentor: Atticus SIMS",
            "GUO XIAO YUE (MC569254) · LIU JIA QUN (MC569293)",
        ],
    )
    d.body_slide(
        "Creative concept — two dossiers → living database",
        [
            "Proof-of-concept: woolly mammoth + thylacine — full WebXR depth, citations, ethics.",
            "Expanded: unified high-priority database of 87 species (sensory 1–10, music 1–10, data H/M/L).",
            "Curated from 900+ documented extinctions (Holocene, IUCN Red List, 2025 confirmations).",
            "Criteria: human intervention link, palaeo-data availability, sensory / chronobiology potential.",
            "Repo slice: 51 taxa in animals_full.csv now — merge full 87-row master for production exports.",
        ],
        small=True,
    )
    d.body_slide(
        "Research process — four steps",
        [
            "1 Preliminary concept: pharm-related extinctions → collective biological memory reconstruction.",
            "2 Unified 87-species CSV — sensory & music layering scores + extinction context.",
            "3 Biodigital chronobiology — genes, orbits, temporal niches (see chronobiology slide).",
            "4 Bio + digital layering + ethical decision interface + reflection log.",
        ],
    )
    d.body_slide(
        "Repository & research layer (2026)",
        [
            "Shipped build: browser / WebXR — no live biosensor demo; QR + optional citation sheet.",
            "87 master list · 51 taxa in data/extinction_archive/animals_full.csv + archive.json + archive_import.sql.",
            "archival_media_research.csv — ~349 rows (IUCN, GBIF, BHL, NFSA, SI, BOW, PMC…).",
            "Planning: BDC_2026_Extinction_Archive_Planning_Document.md · bdc_showcase_species_shortlist.md",
            "Spine: 02_research/biology/biodigital_chronobiology_research.md · scripts/extinction_archive_db/",
        ],
        small=True,
    )
    d.body_slide(
        "The fracture (Umwelt + time)",
        [
            "Extinction removes DNA and ecological roles — and temporal niches (day, season, social synchrony).",
            "Public memory flattens into icons; we lose how another species lived in time.",
            "Collective amnesia about biodiversity integrity — shifting baselines, de-extinction hype.",
            "This dossier makes absence narratable with structured uncertainty.",
        ],
    )
    d.body_slide(
        "Three guiding questions",
        [
            "How can extinction–absence become perceivable without false precision?",
            "How can AI + biological data evoke memory transparently (no replacement for conservation or Indigenous knowledge)?",
            "How can touch, sight, smell, sound act as gentle cues — optional layers, no sensory overload?",
        ],
    )
    d.body_slide(
        "Umwelt hypothesis dossiers — core definition",
        [
            "Each species = folder of testable claims — not fantasy safari.",
            "Genes & circadian · orbit & RGC models · palaeo-climate & seasonality · sight / sound / smell.",
            "AI memorial: generative media constrained by peer-reviewed + licenced archives.",
            "Sensory time capsule: reconstruct when they lived (temporal niche), not only what they looked like.",
        ],
    )
    d.body_slide(
        "Biodigital chronobiology — highlights",
        [
            "Mammoth: Lynch 2015 — circadian-related genes incl. PER2/BMAL1, TRPV3; Kim preprint — label in UI.",
            "Polar analogy: Lu 2010 reindeer — flexible clock under extreme photoperiod (Interpolated for mammoth).",
            "Nocturnal bottleneck — early mammals under dinosaur pressure → modern diel patterns.",
            "Pozniak 2018: bony orbit predicts nocturnal/crepuscular/diurnal behaviour (>80% in study set).",
            "Sonification: migration, heart rate, vocalizations → layered music (Web Audio API).",
            "Key insight: extinction removes a unique temporal rhythm from the planet’s biological symphony.",
        ],
        small=True,
    )
    d.body_slide(
        "Experience spine & user journey",
        [
            "1 Discover rhythm — planetary biological map.",
            "2 Epistemic layers — deep scientific dossier (Cited / Interpolated / Speculative).",
            "3 Immersive sensory — 360° + layered chrono-music. WebXR MVP = mammoth + thylacine depth.",
            "4 Ethics sliders — trade-offs (resources, risk, Indigenous perspectives, tech limits).",
            "5 Reflection log — stewardship of extant biodiversity.",
        ],
        small=True,
    )
    d.table_slide(
        "Three load-bearing modules",
        ("Module", "Role"),
        [
            ("Species Dossier", "Evidence cards, sensory proxies, extinction drivers — scene to citation"),
            ("Polyphony Mixer", "Seasonal / diel / migration / density — harmony vs collapse"),
            ("Ethics Console", "Trade-offs (funding, invasion risk, sovereignty) + evidence gate"),
        ],
    )
    d.table_slide(
        "Species tiers (research + build)",
        ("Tier", "Taxa", "Role"),
        [
            (
                "P0 WebXR",
                "Mammuthus primigenius\nThylacinus cynocephalus",
                "Full interactive depth; chronobiology + orbit/POV; citation strip",
            ),
            (
                "P0 dossier",
                "Ectopistes migratorius",
                "Deck / appendix: Martha, synchrony, acoustic absence (xeno-canto may be empty)",
            ),
            (
                "P1 dossier",
                "Dodo · Great auk\n(Raphus · Pinguinus)",
                "14+ curated URLs each — islands, BHL, SI; Context lane, not WebXR v1",
            ),
        ],
        small=True,
    )
    d.table_slide(
        "Ten representative species (87-species database)",
        ("Species", "Sens/Mus", "Human link & strength"),
        [
            ("Mammuthus primigenius — Woolly mammoth", "10 / 9", "Arctic circadian genomics; steppe soundscape"),
            ("Thylacinus cynocephalus — Thylacine", "10 / 10", "Last recordings; skull → diel activity"),
            ("Ectopistes migratorius — Passenger pigeon", "10 / 10", "Megaflock sonification; overhunting"),
            ("Raphus cucullatus — Dodo", "9 / 8", "Classic overhunting; AR-ready 3D"),
            ("Pinguinus impennis — Great auk", "9 / 9", "Marine low-freq context; oil hunting"),
            ("Smilodon fatalis — Saber-toothed cat", "9 / 9", "Roar / bite sim; megafauna collapse"),
            ("Hydrodamalis gigas — Steller’s sea cow", "8 / 7", "Rapid extinction; underwater low-freq"),
            ("Chelonoidis abingdonii — Pinta tortoise", "9 / 6", "Lonesome George; recent loss"),
            ("Ninox albifacies — Laughing owl", "8 / 9", "Distinctive calls; NZ invasion"),
            ("Incilius periglenes — Golden toad", "7 / 6", "Climate-linked amphibian case"),
        ],
        small=True,
    )
    d.body_slide(
        "Bio + digital layering · physical + AR",
        [
            "Biology: palaeo-chronobiology, isotopes (e.g. tusk mobility), orbit → diel activity — papers first.",
            "Digital: A-Frame / Three.js WebXR; diffusion + prompt discipline; Web Audio chrono-music.",
            "Full ideation: living plants + bacterial sensors (not in shipped MVP).",
            "Physical: 3D-printed fossils / skulls + mobile AR — evidence stack first; short Umwelt loop second.",
            "Course build: web-first + one QR anchor — no live biosensor demo.",
        ],
        small=True,
    )
    d.body_slide(
        "Honesty UI: Cited · Interpolated · Speculative",
        [
            "Cited — peer-reviewed paper, museum catalogue, or dataset row.",
            "Interpolated — justified inference (e.g. RGC model not measured on thylacine).",
            "Speculative — creative extension; never sold as recovered reality.",
            "Archival media (NFSA, SI): licence check before trailer or embed.",
        ],
    )
    d.table_slide(
        "Data layer in repository",
        ("Asset", "Purpose"),
        [
            ("animals_full.csv (51 taxa; 87 target)", "Names, extinction, pharm flags, Umwelt scores, 3D refs"),
            ("archive.json + archive_import.sql", "Frontend bundle + PostgreSQL animals / media / refs"),
            ("archival_media_research.csv", "~349 rows: IUCN, GBIF, BHL, NFSA, BOW, PMC…"),
            ("extinction_archive_schema.*", "Future map sites + reconstruction_layer + scenes"),
        ],
        small=True,
    )
    d.body_slide(
        "Mammoth — cited anchors",
        [
            "Comparative genomics & circadian-related gene enrichment (Lynch et al., 2015) — conservative on PER2 until PDF verified.",
            "Mammoth steppe habitat framing (Zimov et al., 2012).",
            "Lifetime mobility from tusk isotopes (Wooller et al., 2021, Science) — migration as sonification input.",
        ],
    )
    d.body_slide(
        "Thylacine — archives + ethics",
        [
            "Orbit to crepuscular / nocturnal niche (Pozniak et al., 2018); POV filter Interpolated from RGC topology methods.",
            "Moving image: NFSA collection — clearance required; TMAG / NMA for specimen narrative.",
            "Context: Palawa-led sources + Clements / Schlunke on sovereignty vs de-extinction spectacle.",
        ],
    )
    d.body_slide(
        "Passenger pigeon — dossier beat",
        [
            "Smithsonian Martha + Project Passenger Pigeon + Birds of the World account.",
            "Social synchrony collapse: sonic metaphor of phase lock breaking.",
            "Empty or sparse sound archives = evidence of acoustic loss — honest UI copy.",
        ],
    )
    d.table_slide(
        "BDC 2026 alignment",
        ("Lane", "Fit"),
        [
            ("Ideas", "BDC Idea 3 (Extinction Archive) + Idea 6 (Biorhythm Composer)"),
            ("Theme", "Convergent Life — deep biology + digital convergence"),
            ("Prizes", "Biodigital Excellence · Outstanding Digital Submission"),
            ("Rubric", "Narrative → Concept → Context → Reflection (epistemic + ethics + data layer)"),
        ],
        small=True,
    )
    d.body_slide(
        "Deliverables · next steps · 4-week spine",
        [
            "Ship: live WebXR · citation grid · ethics + reflection · trailer · QR / physical anchor.",
            "Next: merge 87-species exports · full WebXR polish · AR models · 1–5 min video.",
            "EN PDF: slides/export/Extinction_Archive_Umwelt_Hypothesis_Dossiers_BDC2026_EN.pdf",
            "GitHub alias: [FINAL-SMALL] Extinction Archive … Dossiers_BDC2026.pdf",
            "Sprint: W1 literature/URLs → W2 mammoth + UI → W3 thylacine + ethics → W4 polish + Q&A.",
            "Rebuild: python3 docs/bdc-umwelt-archive/scripts/build_extinction_archive_slides.py",
        ],
        small=True,
    )
    d.body_slide(
        "Thank you · Q&A",
        [
            "Extinction Archive: Umwelt Hypothesis Dossiers",
            "Macau University · Biodesign Challenge 2026",
            "We welcome questions on evidence, sovereignty, temporal niches, and scope.",
        ],
    )
    out = EXPORT / "Extinction_Archive_Umwelt_Hypothesis_Dossiers_BDC2026_EN.pdf"
    d.output(out)
    print(f"Wrote {out}")
    small_alias = (
        EXPORT / "[FINAL-SMALL] Extinction Archive Umwelt Hypothesis Dossiers_BDC2026.pdf"
    )
    shutil.copy2(out, small_alias)
    print(f"Wrote {small_alias}")


def build_en_full_judge(font: Path) -> None:
    """BDC judge-oriented full deck: ideation + research + planning + rubric (new filename)."""
    d = Deck(font)
    d.title_slide(
        "Extinction Archive: Umwelt Hypothesis Dossiers",
        "Extinction Archive: AI Memorial for Lost Species — “Umwelt Archive” · A Sensory Time Capsule",
        [
            "Macau University · Mentor: Atticus SIMS",
            "GUO XIAO YUE (MC569254) · LIU JIA QUN (MC569293)",
            "BDC 2026 · Convergent Life · Ideas 3 + 6 · full judge deck (EN)",
        ],
    )
    d.table_slide(
        "Team · institution · build constraint",
        ("Role", "Focus"),
        [
            ("GUO XIAO YUE (MC569254)", "Experience: narrative, chronobiology→Umwelt, ethics, dossier curation"),
            ("LIU JIA QUN (MC569293)", "Tech: WebXR (A-Frame / Three.js), generative env, epistemic + ethics UI"),
            ("Shipped scope", "Web-only MVP — no live biosensor demo; QR + optional citation sheet"),
        ],
        small=True,
    )
    d.body_slide(
        "Problem (ideation + ecology)",
        [
            "Extinction removes genomes, roles, and temporal niches — day, season, migration, social synchrony.",
            "Public memory flattens into icons; shifting baselines and de-extinction hype hide the texture of loss.",
            "We address the human gap in sensing extinction: another species’ time and Umwelt, not only its image.",
        ],
    )
    d.body_slide(
        "Design hypothesis",
        [
            "If temporal phenotypes + sensory proxies are reconstructed under Cited / Interpolated / Speculative labels,",
            "using chronobiology, morphology, isotopes, and curated archival media,",
            "absence becomes narratable without false certainty — steering reflection toward extant biodiversity stewardship.",
        ],
        small=True,
    )
    d.body_slide(
        "Three guiding questions (research + exhibit)",
        [
            "How can extinction–absence be perceptible as structured uncertainty, not fake precision?",
            "How can AI + biological data transparently evoke memory — without replacing conservation or Indigenous knowledge?",
            "How can multisensory cues stay optional and gentle — intensity caps, clear tiers?",
        ],
    )
    d.body_slide(
        "Why biodesign (bio + digital load-bearing)",
        [
            "Biological layer: papers, specimens, isotopes, clock-related genomics, orbit→diel proxies — scene→citation.",
            "Digital layer: constrained generative visuals/audio, Web Audio sonification, inspectable AI use.",
            "Removing either layer collapses the proposition; course build stays browser-first / WebXR.",
        ],
        small=True,
    )
    d.body_slide(
        "Research spine (canonical doc)",
        [
            "02_research/biology/biodigital_chronobiology_research.md — palaeo-chronobiology, Umwelt frame, ethics hooks.",
            "Flagship science: Lynch et al. 2015 (mammoth; conservative clock copy), Pozniak et al. 2018 (thylacine orbit).",
            "Mobility narrative: Wooller et al. 2021 (tusk isotopes); ethics framing: Sherkow & Greely 2013; Clements 2025 + Palawa-led sources.",
        ],
        small=True,
    )
    d.body_slide(
        "Experience architecture",
        [
            "Planetary map → coordinate → species dossier (full vision); WebXR MVP = depth on two species.",
            "Polyphony: season, diel rhythm, migration, density — harmony vs collapse (e.g. passenger pigeon synchrony).",
            "Exit: ethics fork + reflection — resource trade-offs, sovereignty, technological fixism (templates/reflection-log-webxr.html).",
        ],
        small=True,
    )
    d.table_slide(
        "Three modules",
        ("Module", "Role"),
        [
            ("Species Dossier", "Evidence cards, sensory proxies, drivers — every scene ties to citation or tier"),
            ("Polyphony Mixer", "Rhythm / density / migration — user hears loss of synchrony"),
            ("Ethics Console", "Incompatible choices + evidence gate — no single “win” ending"),
        ],
    )
    d.table_slide(
        "Species tiers (planning + dataset)",
        ("Tier", "Taxa / scope", "Role"),
        [
            ("P0 WebXR", "Mammuthus primigenius · Thylacinus cynocephalus", "Full interactives; citation strip; Indigenous context UI"),
            ("P0 dossier", "Ectopistes migratorius", "Martha, BOW, acoustic absence; may sit outside WebXR v1"),
            ("P1 dossier", "Raphus · Pinguinus", "14+ URLs each — Context lane; museum/archive literacy"),
            ("P2 catalogue", "87 master list · 51 taxa in-repo CSV + schema", "Systematic research; future map — not 85 extra WebXR scenes"),
        ],
        small=True,
    )
    d.body_slide(
        "Species A — Woolly mammoth (cited beats)",
        [
            "Circadian-related gene category enrichment vs extant elephants — careful PER2 wording until PDF verified (planning log).",
            "Mammoth steppe / productivity priors (Zimov et al., 2012); cold / TRPV3 — prefer Lynch 2015 over preprint-only claims.",
            "Tusk isotope mobility (Wooller et al., 2021) as honest input to sonification — label Interpolated if not raw-data-mapped.",
        ],
        small=True,
    )
    d.body_slide(
        "Species B — Thylacine (science + context)",
        [
            "Orbit → crepuscular/nocturnal niche (Pozniak et al., 2018); POV metaphor Interpolated from Mass & Supin (2020) dolphin RGC methods.",
            "Colonial entanglement: bounty, habitat (Paddle; Sleightholme & Campbell) — UI_Indigenous_Context + Palawa-first bibliography.",
            "NFSA / museum moving image: licence gate — never assume public domain.",
        ],
        small=True,
    )
    d.body_slide(
        "Passenger pigeon + P1 island dossiers",
        [
            "Pigeon: Smithsonian Martha, Project Passenger Pigeon, BOW — social synchrony collapse as sonic metaphor.",
            "Sparse xeno-canto / sound archives as evidence of acoustic loss — honest UI, not filler ambience.",
            "Dodo + great auk: curated archival rows in archival_media_research.csv for Context slides or film — not WebXR v1 unless surplus.",
        ],
        small=True,
    )
    d.body_slide(
        "Honesty UI · literature verification",
        [
            "Cited — paper, catalogue, dataset row. Interpolated — justified model (e.g. POV not measured on thylacine).",
            "Speculative — creative; never sold as recovered reality. Archival licences checked before trailer/embed.",
            "Planning doc holds verification log (M1 PER2, M4 preprint, T2 RGC DOI) — mirror short tags in WebXR comments.",
        ],
        small=True,
    )
    d.body_slide(
        "AI in biodesign (Reflection lane)",
        [
            "Roles: fenced scene synthesis, human-edited curation, parametric audio — not black-box truth.",
            "Aim: CLAIMS_REGISTER-style discipline: claim ↔ source or explicit Speculative; log models, prompts, failures.",
            "Judges see limits as feature — e.g. conservative mammoth genetics copy, failed renders documented.",
        ],
        small=True,
    )
    d.table_slide(
        "Repository · data layer",
        ("Asset", "Purpose"),
        [
            ("animals_full.csv (51 taxa; 87 target)", "Names, extinction, pharm flags, Umwelt scores, 3D refs"),
            ("archive.json · archive_import.sql", "Static bundle + PostgreSQL animals / media / literature_references"),
            ("archival_media_research.csv", "~349 curated portal rows — regenerate via generate_archival_media_research.py"),
            ("extinction_archive_schema.*", "Future map sites, reconstruction_layer, scenes — PostGIS deferred"),
        ],
        small=True,
    )
    d.body_slide(
        "Physical presence · minimum viable",
        [
            "One tactile anchor + QR → WebXR (or static citation page). Optional A3 scene→citation sheet.",
            "Aligns with “heavy evidence, light hardware” — full ideation plant/sensor strand stays documentation-only for course build.",
        ],
    )
    d.table_slide(
        "BDC rubric — how we score ourselves",
        ("Dimension", "Evidence in submission"),
        [
            ("Narrative", "Rhythm: immersion → graded uncertainty → ethical fork; pigeon “silence” beat; thylacine care"),
            ("Concept", "Umwelt + temporal phenotype + biodigital coupling; two-layer honesty UI; two-species depth rule"),
            ("Context", "De-extinction trade-offs, pharm_related flags, colonial archives, Palawa-led sourcing for lutruwita"),
            ("Reflection", "AI limits, verification log, user reflection UI, what archives omit"),
        ],
        small=True,
    )
    d.body_slide(
        "Risks · mitigations (from project plan)",
        [
            "“Just VR art” — persistent scene→citation strip; judges can freeze on proxies.",
            "Overclaiming aDNA — mammoth clock language locked to abstract-level until gene-level PDF pass.",
            "Indigenous tokenism — Palawa-first texts alongside academic cross-cites; label positionality.",
            "Scope creep — cut stretch before epistemic or ethics UI breaks.",
        ],
        small=True,
    )
    d.table_slide(
        "Milestones (4-week spine)",
        ("Week", "Outcomes"),
        [
            ("1", "Literature + archival URLs; storyboard ↔ citation grid; WebXR shell"),
            ("2", "Time scrubber; generative constraints; epistemic toggles (mammoth)"),
            ("3", "Sonification; ethics + Indigenous copy; reflection panel (thylacine)"),
            ("4", "Rehearsal, 1–5 min video, deploy, cheat sheet, Q&A drill"),
        ],
        small=True,
    )
    d.body_slide(
        "Deliverables · documentation index",
        [
            "Live: WebXR + one ethical choice + reflection · trailer · images · process doc.",
            "Canonical plan: BDC_2026_Extinction_Archive_Planning_Document.md · Executive: PROJECT_PLAN.md.",
            "Compact decks (unchanged on GitHub): Extinction_Archive_Umwelt_Hypothesis_Dossiers_BDC2026_EN.pdf + [FINAL-SMALL] alias.",
            "This file: full judge walkthrough — add alongside legacy BDC_Deck_EN.pdf if present; do not overwrite backups.",
        ],
        small=True,
    )
    d.body_slide(
        "Thank you",
        [
            "Extinction Archive / Umwelt Archive — questions on evidence, sovereignty, and scope welcome.",
            "Rebuild all PDFs: python3 docs/bdc-umwelt-archive/scripts/build_extinction_archive_slides.py",
        ],
    )
    out = EXPORT / "Extinction_Archive_Umwelt_BDC_Judge_Full_Deck_EN_2026.pdf"
    d.output(out)
    print(f"Wrote {out}")


def build_zh(font: Path) -> None:
    d = Deck(font)
    d.title_slide(
        "灭绝档案 · Extinction Archive",
        "Umwelt Archive · 集体记忆断裂",
        [
            "Biodesign Challenge 2026 · 展览主题 Convergent Life",
            "数字艺术与 AI 技术 · MDes",
            "生物—数字纪念装置 — 非「复活」。",
        ],
    )
    d.body_slide(
        "断裂是什么",
        [
            "物种灭绝带走的不仅是身体，还有生态功能。",
            "共同记忆被磨损：基线漂移、复活叙事过热与奇观化。",
            "失去的是时间中的共存：迁徙、同步、昼夜与季节节律。",
            "本项目让缺席与证据变得可感知、可争论。",
        ],
    )
    d.body_slide(
        "设计问题",
        [
            "如何把「灭绝—缺席」转译为可感知、可讨论的体验？",
            "如何用 AI + 生物数据支撑有纪律的公共记忆？",
            "如何从沉浸回落到责任：保护、风险与正义的真实权衡？",
        ],
    )
    d.body_slide(
        "一句话概念",
        [
            "将可引用的科学痕迹转化为受约束的 Umwelt 假设空间。",
            "物种档案 + 多声部混音台 + 伦理控制台。",
            "每一层都带引用与置信度。",
        ],
    )
    d.table_slide(
        "三大模块",
        ("模块", "作用"),
        [
            ("Species Dossier", "时间、运动、感官代理 — 谨慎引用"),
            ("Polyphony Mixer", "季节、群体同步、迁徙 — 和谐或崩塌"),
            ("Ethics Console", "分支卡片 + 证据门禁 — 不同声景终曲"),
        ],
    )
    d.table_slide(
        "英雄物种（已定）",
        ("物种", "锚点", "隐喻"),
        (
            ("真猛犸 M. primigenius", "象牙同位素、光周期、基因组", "长周期、低频律动"),
            ("旅鸽 E. migratorius", "社会同步、历史大群", "相位锁定→寂静（Modeled）"),
        ),
    )
    d.body_slide(
        "生物层 + 数字层（缺一不可）",
        [
            "生物层：古代理、同位素、行为与灭绝机制 — 可追溯。",
            "数字层：条件生成（B 主）+ 程序化 / shader（A 辅）；WebAR + 桌面兜底。",
            "去掉任一层，项目即不成立。",
        ],
    )
    d.body_slide(
        "诚实界面：三档标签",
        [
            "Cited 已引用 — 文献或数据集",
            "Modeled 建模 — 推断与局限",
            "Speculative 推测 — 绝不冒充实拍",
            "提示：推断 — 非复原的真实",
        ],
    )
    d.body_slide(
        "实体入口（轻装置）",
        [
            "课程构建：Web-only，无活体生物传感器演示。",
            "一件 3D 打印或卡片 + QR → WebXR；可选一页 scene→citation 备忘。",
            "完整 ideation 中的植物/传感层可作为展陈愿景，不进入 MVP 范围。",
        ],
    )
    d.body_slide(
        "伦理控制台",
        [
            "门禁 C：陈述归入 Cited / Modeled / Speculative。",
            "分支 B：资金、入侵种、土地与知识 — 不可兼得。",
            "输出：终曲混音 + 系统后果（规则优先）。",
        ],
    )
    d.table_slide(
        "与 BDC 对齐",
        ("交付 / 评审", "说明"),
        [
            ("五件套", "陈述、视觉、实体、短片、幻灯片 — 与三模块绑定"),
            ("四维 ×4 分", "铂金须四维均 ≥2.75"),
        ],
        small=True,
    )
    d.body_slide(
        "奖项与冲刺",
        [
            "主攻：Biodigital Excellence。",
            "四周：证据与故事板 → 猛犸切片 → 旅鸽与伦理与 AR → 稽核与预告片。",
            "谢谢 — 欢迎提问。",
        ],
    )
    out = EXPORT / "Extinction_Archive_ZH.pdf"
    d.output(out)
    print(f"Wrote {out}")


def main() -> None:
    ap = argparse.ArgumentParser(description="Build Extinction Archive slide PDFs.")
    ap.add_argument(
        "--full-only",
        action="store_true",
        help="Only build Extinction_Archive_Umwelt_BDC_Judge_Full_Deck_EN_2026.pdf",
    )
    ap.add_argument(
        "--no-full",
        action="store_true",
        help="Skip full judge deck (compact EN + FINAL-SMALL alias + ZH only)",
    )
    args = ap.parse_args()

    EXPORT.mkdir(parents=True, exist_ok=True)
    font = find_font()
    if args.full_only:
        build_en_full_judge(font)
        return
    build_en(font)
    build_zh(font)
    if not args.no_full:
        build_en_full_judge(font)


if __name__ == "__main__":
    main()
