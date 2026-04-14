# Umwelt Archive — Ideation & Planning Document (2026 Update)

**（Ideation）Preliminary Concept:** *Extinction Archive and The Reshaping of Human Biological Memory — (“Umwelt Archive” — A Sensory Time Capsule)*

**Formal project line (competition-facing):** *Extinction Archive: AI Memorial for Lost Species – Umwelt Archive: A Sensory Time Capsule*

**Program:** Biodesign Challenge 2026 · Theme *Convergent Life* · Targets *Biodigital Excellence* (+ *Outstanding Digital Submission* where applicable)

**Institution / team (from prior planning export):** Macau University · 2-person team · Web-first / no living-sensor demo in v1 · Mentor: Atticus SIMS · Members: GUO XIAO YUE (MC569254), LIU JIA QUN (MC569293)

---

## 0. Purpose of this document

This file **consolidates** the **8-step ideation workbook** as it evolved in Cursor (`cursor_2_biodesign_project_context_revi.md`) and adds **April 2026 planning deltas**: expanded **species catalog** for the MVP, **data/schema** alignment, and **archival media research** pipeline.

**Execution strategy (locked from prior agreement):** **重内容、轻装置** — invest in **deep scientific narrative**, **honest epistemic UI**, and **reflection**; **physical presence** stays **minimal** (e.g. tactile anchor + QR → web experience), not a sensor lab.

---

## 0.1 What changed in this update (April 2026)

| Area | Prior baseline (from message history) | **Update now** |
|------|----------------------------------------|----------------|
| **Species scope in MVP** | **2 hero species** (woolly mammoth + thylacine) for **depth**; full WebXR “day arc” + literature dossiers | **MVP prototype also presents a broad archive layer: ≥80 extinct species (target band ~80–90+ as data is merged; filename goal “87种”).** Heroes remain **depth**; the many others are **breadth** (cards, filters, provenance, archival links—not equal full Umwelt simulation each). |
| **Data layer** | Storyboard + citation tables (M1–M5, T1–T5) | **`research_extinct_animals_list`**, **`archival_media_research`**, JSON Schema bundle (`schemas/`), import fieldmap—support **scale** without losing **tier discipline**. |
| **Thematic lens (optional curator track)** | Idea 3 memorial + de-extinction ethics | **Pharm-related / human entanglement** tags can annotate species (`pharm_human_hook`) **without replacing** chronobiology + Umwelt core. |
| **Memory framing** | Temporal niche + collective amnesia | **Memory reshaping** (multisensory reminiscence + safeguards against “false certainty”) stays **prominent** on key narrative beats (slides 4–5, 11 in deck history). |

**Interpretation note:** “**80+90**” in the brief is recorded here as **≥80 species in the MVP archive UI**, scaling toward **~90** (or the **87** unified list) as CSV merge completes—**not** a promise of 170 fully simulated species unless you explicitly adopt that scope later.

---

## 1. Eight-step framework (official BDC agent definitions)

*Source: `biodesign_cursor_agent.md` — condensed.*

| Step | Output |
|------|--------|
| **1** | Interests & skills maps |
| **2** | Intersection statements (“What if we used [code] to [verb] [bio] for [problem]?”) |
| **3** | Rubric stress-test (Narrative, Concept, Context, Reflection) |
| **4** | Biology research sprints + prior art |
| **5** | Bio + digital split + red-flag test |
| **6** | Concept narrative (~200 words) + one-sentence pitch |
| **7** | Prototype + BDC deliverables (MVP / Target / Stretch) |
| **8** | Build sprint (Discovery → Prototype → Integrate → Polish) |

---

## 2. Step 1 — Map interests & skills *(historical record + update)*

### 2.1 Original record (from conversation export)

- **Member A (Experience Lead):** narrative & sensory direction; translation of palaeo-chronobiology; critical narrative; ethics oversight.  
- **Member B (Tech/AI Lead):** digital architecture; WebXR (A-Frame / Three.js); generative environments; **epistemic / uncertainty UI**.  
- **Core lens:** **Chronobiology + temporal niche** — reconstructing **rhythms** of extinct species, not only static morphology.

### 2.2 Update

- **Member A** additionally owns **curatorial voice** for **80+ archive entries** (short hooks, ethics flags, Indigenous-context gates).  
- **Member B** owns **data pipeline** (CSV → JSON Schema), **browse UI** performance, and **search/filter** (by category, data availability, pharm tag).  
- **New skill surface:** light **information architecture** + **provenance display** (IUCN verify notes, archival portal links).

---

## 3. Step 2 — Intersection statements *(historical + update)*

### 3.1 Locked primary intersection (historical)

> *What if we used **generative AI + WebXR** to **reconstruct and visualize** the **temporal phenotype** of extinct species from **comparative genomics, morphology, and palaeo-environment proxies**, to address **humanity’s flattened perception of extinction** (loss of **time** and **Umwelt**)?*

**Supporting intersections (stretch):** living entrainment (deferred in web-only v1); policy-style ethics fork after immersive beat.

### 3.2 Update — intersection for the **archive at scale**

> *What if we used a **structured species database + epistemic tiers** to **browse 80+ vanished taxa**, linking each to **literature, museum data portals, and uncertainty**, so “memorial” scales beyond two heroes **without** pretending equal simulation depth?*

This **does not replace** the hero intersection; it **grounds** the MVP breadth in **honest metadata**.

---

## 4. Step 3 — Rubric stress-test *(historical + update)*

### 4.1 Historical self-scores (example from export)

| Dimension | Score | Notes |
|-----------|-------|--------|
| **Narrative** | 3/3 | Beat: discover rhythm → feel loss → ethical choice (+ memory reshaping). |
| **Concept** | 3/3 | **Time** as design axis; biodigital integration. |
| **Context** | 2/3 | Needs depth: de-extinction risk, ecosystem effects, **Indigenous sovereignty / TEK** with serious sourcing. |
| **Reflection** | 2.5/3 | Push interactive **three epistemic layers** (Cited / Interpolated / Speculative), not footnotes only. |

### 4.2 Update — risks from scaling to 80+ species

| Dimension | New risk | Mitigation |
|-----------|----------|------------|
| **Concept** | Looks like a **database art** piece | Keep **two hero dossiers** as the **proof of biodigital depth**; tag others **“card depth”** in UI. |
| **Context** | **Biopiracy / flattening** of sensitive stories | **Sovereignty_and_ethics** field per species; **no** decorative TEK; partner or cite Palawa-led sources where used. |
| **Reflection** | **Curation at scale** hides limits | **Global “methods & limits”** panel + per-species **verification_note** + batch **claims_to_verify**. |

---

## 5. Step 4 — Research sprints *(historical + update)*

### 5.1 Historical focus

- **Species A — Woolly mammoth (*Mammuthus primigenius*):** circadian / Arctic adaptation; **PER2 / circadian gene claims** → conservative copy unless primary PDF confirms gene-level wording.  
- **Species B — Thylacine (*Thylacinus cynocephalus*):** orbit / diel pattern; **RGC / vision metaphor** → **Interpolated** tier; colonial + Palawa context.

**Literature slots M1–M5 / T1–T5** (with DOIs) and **storyboard ↔ citation mapping** were integrated in the long-form planning export; **M1** hardened to avoid overstating *PER2* from abstract alone; **T2** resolved to **Mass & Supin (2020)** DOI + official PDF after the 2025 DOI string could not be resolved reliably.

### 5.2 Update — research at archive scale

- **Per-species (80+):** use **`archival_media_research.json`** (IUCN, GBIF, MorphoSource, BHL, etc.) as **starting points**, not final citations.  
- **Pharm-human track (optional):** fill **`pharm_human_hook`** + **`claims_to_verify`** when species support it (e.g. trade, toxins, model organisms).  
- **Completion rule:** hero species keep **M/T slot** rigor; archive species need **at least** IUCN status check + one **archival** or **primary** anchor before public copy.

---

## 6. Step 5 — Bio + digital split *(historical + update)*

### 6.1 Historical split

- **Biology:** literature-grounded chronotypes & sensory ecology; stakes for **extant biodiversity**; no wet lab in v1.  
- **Digital:** WebXR scenes, generative environment hypothesis, **sonification**, **epistemic UI**, ethics console.  
- **Red line:** no purely speculative visuals without mapped biological proxy.

### 6.2 Update — split for **hero vs archive**

| Layer | **Hero dossiers (2)** | **Archive browse (80+)** |
|--------|------------------------|---------------------------|
| **Bio** | Deep proxies (genes, orbit, habitat, ethics) | Summaries + drivers + **data_availability** + verification notes |
| **Digital** | Full interactive “day / season” experience | **Cards**, filters, external links, optional light audio/visual **preset** |

**Red-flag test (unchanged):** Removing **biology** should break meaning; removing **code** should break access to **tiered** truth and interaction.

---

## 7. Step 6 — Concept narrative *(historical + update)*

### 7.1 Historical elevator (structure)

- **Problem:** extinction erases **rhythms** and shared **time** in ecosystems → **collective memory flattening**.  
- **Insight:** palaeo-chronobiology + morphology let us **hypothesize** temporal niches **honestly**.  
- **Solution:** **WebXR memorial** — multisensory **time capsule**, **two species** in depth, **AI** as **translator** not oracle.  
- **Impact:** ethics fork steers from **resurrection spectacle** toward **living biodiversity responsibility**; **reflection** logged.

### 7.2 Update — one sentence with archive

*The **Umwelt Archive** is a biodigital memorial that restores **hypotheses** of extinct **temporal niches** through **two immersive dossiers**, while a **catalog of 80+ species** grounds the same ethical and epistemic discipline at scale—**memory reshaping without false certainty**.*

*(Rewrite in team voice for submission.)*

---

## 8. Step 7 — Prototype & deliverables *(historical + update)*

### 8.1 BDC deliverables (unchanged)

10-minute presentation + 5 Q&A; visuals; **physical model** (minimal tactile + QR); **1–5 min creative video**; slides (Drive); optional site.

### 8.2 MVP / Target / Stretch (updated)

| Tier | Scope |
|------|--------|
| **MVP** | **2 hero WebXR chapters** (mammoth + thylacine) + **epistemic UI** + **ethics fork** + **reflection**; **≥80 species** in **browse/archive** with schema-backed metadata + archival links; **no** living sensor. |
| **Target** | Polish UX; **pharm**-tagged collections; more **sonification**; **Storyboard ↔ citation** fully tagged. |
| **Stretch** | Third species shallow chapter; advanced filters; optional **Gaussian splat** scene for one hero **if** time & rights allow. |

### 8.3 New internal deliverables (data)

- `data/research_extinct_animals_list.json`  
- `data/archival_media_research.json`  
- `schemas/*.schema.json` + `registry.json`  
- Regenerate scripts: `scripts/build_archival_media_research.py`

---

## 9. Step 8 — Build sprint *(historical + update)*

### 9.1 Historical 4-week spine (web-only, 2 people)

1. **Discovery:** lock heroes; citations; storyboard; rubric weak points.  
2. **Prototyping:** WebXR vertical slice; placeholder assets OK; epistemic UI early.  
3. **Integration:** audio + ethics + rehearsal.  
4. **Polish:** video, minimal physical, Q&A drills (risk, AI transparency, sovereignty).

### 9.2 Update — parallel track for **data sprint**

| Week | Hero track (A/B) | Archive track (shared) |
|------|------------------|-------------------------|
| **1** | Storyboard + M/T citations | Finalize **CSV ≥80 rows**; import → JSON; **IUCN spot-check** batch |
| **2** | WebXR slice | **Card UI** + filters; link **archival_media_research** |
| **3** | Sonification + ethics | **Pharm** tags optional; **Context** copy review |
| **4** | Deck + video + Q&A | **Consistency pass** on tiers; remove any overstated gene claims |

---

## 10. Risk register (delta)

| Risk | Mitigation |
|------|------------|
| **Scope creep** to 170 fully simulated species | **Label** depth in UI; **hero = simulate**, **archive = situate**. |
| **Weak biodesign read** | Opening statement: **living biodiversity stakes** + **literature-constrained** design; heroes carry **bio** proof. |
| **Indigenous context harm** | Consultation / Palawa-led citations; **UI_Indigenous_Context** gates; no tourism copy. |
| **AI washing** | Tooling disclosure; **three tiers**; failure modes in Reflection. |

---

## 11. File cross-reference (this repo)

| Asset | Path |
|-------|------|
| Research species list | `Biodesign_Project_3/data/research_extinct_animals_list.json` |
| Archival portals per taxon | `Biodesign_Project_3/data/archival_media_research.json` |
| Schemas | `Biodesign_Project_3/schemas/` |
| Archival script | `Biodesign_Project_3/scripts/build_archival_media_research.py` |

**Related GitHub project (from prior export):** [macaumonsoon/Biodesign-Project](https://github.com/macaumonsoon/Biodesign-Project) — sync PDF/deck and narrative docs there if this folder is merged into that repo.

---

## 12. Next actions (checklist)

- [ ] Merge unified CSV to **≥80** species; re-run list + archival research scripts.  
- [ ] Map **80+** `slug`s to `umwelt-species.schema.json`; fill **hero** records first.  
- [ ] UI: distinguish **“Dossier depth”** vs **“Archive card”** visually and in copy.  
- [ ] Rehearse **10-min** talk: **2 heroes** in detail, **archive** as **scale + humility** argument.  
- [ ] Context pass: **T5 / Palawa** sources + **de-extinction** trade-offs (Sherkow & Greely hooks).  
- [ ] Lock **Reflection** UX: three-tier toggle + optional reflection log (template from prior `reflection-log-webxr.html` if ported).

---

*Document version: 2026-04-14 · Merges ideation history from `cursor_2_biodesign_project_context_revi.md` + April 2026 MVP archive-scale update.*
