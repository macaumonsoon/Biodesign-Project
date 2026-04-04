# Umwelt Archive — Biodesign Challenge 2026 Project Plan

**Working title:** *Umwelt Archive* (Extinction Archive · Sensory–Temporal Dossiers)  
**Exhibition frame:** BDC 2026 · *Convergent Life*  
**Course:** Digital Art & AI Technology (MDes)  
**Team:** GUO XIAO YUE (MC569254) · LIU JIA QUN (MC569293)  
**Last updated:** 2026-04-04  

This document is the **single source of truth** for scope, narrative, science communication, build plan, and BDC deliverables. Pair with `SLIDE_DECK.md` for presentation structure.

---

## 1. Executive summary

**Provocation:** Species extinction is not only ecological absence—it is also **the fracture of shared human memory and responsibility**. When a lineage ends, its **temporal niche** (daily and seasonal rhythms, migration budgets, social synchrony) vanishes from the living world; our cultures simultaneously lose legible traces of coexistence.

**Project:** *Umwelt Archive* is a **biodigital installation + web experience** that turns **geo-temporal evidence** into an **honest, constrained sensory interface**. Users navigate a **planetary memory map**, open **species dossiers** grounded in published biology, layer **chrono-music** driven by rhythm and population dynamics, and conclude in an **ethics console** that links **funding/attention** to **memory politics** (who is written into the canon, who is muted).

**Prize alignment:** **Biodigital Excellence** (biology + computation load-bearing); **Outstanding Digital Submission** (interactive web / WebXR); strong **Context** (ethics, equity, risk); **Reflection** (AI + iteration logs, uncertainty UI).

---

## 2. Problem, insight, solution, impact

| Block | Content |
|-------|---------|
| **Problem** | Extinction removes **bodies** and **ecological function**; it also erodes **public sense of loss** (shifting baselines, hype cycles, uneven archives). Digital “revival” can distract from present conservation—or clarify stakes if designed as **critical infrastructure**. |
| **Insight** | Paleo-sensory and **chrono-biology** traces (isotopes, morphology, behavior histories, acoustics proxies) can **parameterize** experience without pretending to recover “truth footage.” |
| **Solution** | A **three-act** experience: **Absent Planet** (map + amnesia mechanics) → **Umwelt Capsule** (WebXR / 360 + chrono-music + living telemetry) → **Ethics Console** (tradeoffs + consequences on “default memory layers”). |
| **Impact** | Visitors leave with **epistemic discipline** (what evidence can/can’t imply), **emotional stake** (rhythm and synchrony loss), and **actionable framing** for de-extinction vs digital memorial vs funding reallocation. |

---

## 3. Biodesign positioning (biology + code both essential)

### 3.1 Definition fit

- **Biology is load-bearing:** Dossier parameters derive from **literature-class evidence** (per-species ladder); **living organisms** (plant photoperiod response + microbial metabolism proxy) provide **“still ticking time”** contrasted with **“stopped clocks”** of extinct lineages.  
- **Digital is load-bearing:** Amnesia **mechanics**, prior **fences** for generative media, **Web Audio** rhythm engine, **R → JSON** pipelines for isotope/time-series, **WebXR** dossier depth, **AR** evidence layers.

### 3.2 Red-flag tests

- Remove **evidence constraints** → experience collapses to spectacle (**fail**).  
- Remove **code** → cannot enact map mechanics, music mapping, or transparency logs (**fail**).  
- Remove **living layer** → weaker **biodesign** claim; compensate only if instructor agrees to “design *from* biology” framing with extra material honesty (**risk**).

---

## 4. User experience architecture (locked)

### Act I — Absent Planet (browser)

- **Planetary / archival VI:** administrative UI over heat-style extinction geography.  
- **Amnesia mechanics (primary):**  
  - **A · Zoom:** evidence density ↓, noise/glitch ↑ in “thin” regions.  
  - **B · Timeline scrub:** dossier **thickness** decreases toward last records.  
  - **C · Memory regime toggle:** museum / folk / institutional layers—**same coordinates, conflicting narratives**.  
- **Outcome:** user selects **three dossier anchors** (see §6).

### Act II — Species dossier · Umwelt capsule

- **Entry:** browser-first; **deep dive** via **WebXR** (single hero station per species to cap scope).  
- **Visual rule:** **naturalistic rendering only inside the “prior window”**; outer frame stays archival/planetary; **glitch** signals uncertainty.  
- **Chrono-music station:** multi-track mapping of **seasonality**, **migration budgets**, **acoustic density**; **passenger pigeon** implements **synchrony threshold** (population N → phase lock / collapse).  
- **Living telemetry (sidecar):** plant + microbe channels—**never equivalent** to extinct taxa; fixed copy: *“Non-equivalent, co-present time.”*

### Act III — Ethics console

- **Axes:** **A** funding & attention (extant vs flagship de-extinction vs digital memorial); **D** memory politics (who authors the map, who is default-visible).  
- **Consequence model:** not prophecy—**re-map default layers** (highlights/mutes) based on choices.  
- **Exit:** link or QR to **AI execution log** summary.

---

## 5. Physical & AR deliverables

| Artifact | Intent |
|----------|--------|
| **3D print / tactile maquette** | Species- or habitat-referenced **museum-politics object** (labels: last record dates, gaps, contested attributions). |
| **Mobile AR** | **A:** evidence stack (rights-safe media, citations); **B:** short **controlled Umwelt loop** with on-screen priors + confidence. |
| **Living bench** | **Plant** (photoperiod) + **microbe** proxy (class-safe, sealed)—real-time plot to dashboard. |

---

## 6. Species dossiers (depth targets)

| Species | Hero evidence | Hero interaction | Honesty note |
|---------|---------------|------------------|--------------|
| **Woolly mammoth lineage** | Isotope seasonality + Arctic adaptation narrative | Drag season / isotope → **color temperature + low-frequency rhythm** | No identifiable “hero animal” claims; aggregated public science only |
| **Passenger pigeon** | Social synchrony, historic roost geography | Flock **N** slider → **phase lock → cascade mute** at threshold | **N_c** didactic; cite Allee / flock literature |
| **Thylacine** | Diel activity priors + political memory layers | Toggle memory regime → **same prior window, different annotations / voiceover policy** | Sensitive history—**no sensationalism**; oral/Indigenous layers only with partners or explicit blank |

**Map rule:** many dots possible; **live demo rehearses only the 3-dossier loop**.

---

## 7. Sensory strategy

| Channel | Role |
|---------|------|
| **Vision** | Primary; split **prior window** vs **archive shell** |
| **Hearing** | Primary; **chrono-music** + constrained soundscape |
| **Smell / taste (auxiliary)** | **Absence-first:** chemical **signifiers** as icons/text, optional ultra-weak scent only if institutionally approved; **no** memory-implant claims |

---

## 8. AI governance (full stack)

**Roles:** fenced **scene synthesis**; **draft** curatorial copy (human final edit); **parametric** audio / spectrogram-informed layers.

**Non-negotiables:**

- `CLAIMS_REGISTER` — every audience-facing sentence → id + source or `speculative`.  
- `AI_EXECUTION_LOG.md` — model, prompt hash, params, failure dumps, deprecated outputs.  
- UI **confidence** and **“inferred, not footage”** badges on all generative windows.

---

## 9. Visual identity system (four registers, one grammar)

1. **Archival administrative** (primary UI chrome)  
2. **Planetary heat / absence** (map base)  
3. **Prior-window naturalism** (only inside fenced media)  
4. **Glitch / redaction** (uncertainty + amnesia)

**Internal rule:** *Archives frame everything; heat reads the globe; realism lives only in the prior aperture; cracks are honest.*

---

## 10. Technical stack (recommended)

| Layer | Tools |
|-------|--------|
| Web app | HTML/TS or framework already used in course; **Three.js** |
| WebXR | **A-Frame** or Three.js WebXR; **one station** per dossier |
| Shaders | Uncertainty, map thinning, prior-window mask |
| Audio | **Web Audio API**; optional FAUST/Tone.js; keep mapping functions in code |
| Data | **R** tidy pipeline → JSON schema shared by viz + audio |
| AR | WebXR hit-test or lightweight marker flow linked to printed artifact IDs |
| AI | API per course policy; logs required |

---

## 11. Data → parameter contract (schema sketch)

**Per species JSON (minimum keys):**

```text
species_id, display_name, geo_anchor, evidence_tier,
timeseries: [{ t, value, provenance_id }],
priors: { diel_activity, acoustic_proxy, notes },
uncertainty: { global: 0-1, per_channel: {...} },
ui_bindings: { color_temp_K: fn, audio_subdivision: fn, flock_nc: value_or_null }
```

**Living telemetry JSON:**

```text
channel_id, organism_class, sample_hz, safety_tier, narrative_label
```

---

## 12. Timeline (suggested for 10-week studio)

| Phase | Weeks | Outputs |
|-------|-------|---------|
| **Discovery** | 1–2 | Claims register v0; 3 species bibliographies; UX storyboard; risk list |
| **Prototype** | 3–5 | Act I map + one dossier pass; first R→audio mapping; print mock |
| **Integration** | 6–8 | WebXR stations; chrono-music; living bench; AR pass |
| **Polish** | 9–10 | Ethics console; trailer cut; slide deck; mock Q&A; gallery layout |

**Two-person guardrails:** parallelize **science/register** vs **engine/shaders**; **weekly 4h integration** on one shared JSON example end-to-end.

---

## 13. BDC deliverables checklist

| Deliverable | Status | Notes |
|-------------|--------|--------|
| 10 min presentation + 5 min Q&A | ☐ | Rehearse **two** failure questions weekly |
| Visual renderings / illustrations | ☐ | Prior fence diagrams + map layers |
| Physical model | ☐ | Print + plant/micro enclosure + labeling |
| 1–5 min creative trailer | ☐ | Not a screen capture of slides |
| Slides (PPT/Keynote) → Drive | ☐ | Export from `SLIDE_DECK.md` |
| Optional website + @biodesigned | ☐ | Host `AI_EXECUTION_LOG` summary |

---

## 14. Risk register (short)

| Risk | Mitigation |
|------|------------|
| Over-scoped WebXR / 3 species | Single XR vantage each; browser fallback path **100% feature-complete** |
| AI “fake nature” backlash | Fences + logs + explicit inferential language |
| Living hardware failure | Prerecorded telemetry + “frozen frame” museum mode |
| Sensitive histories (thylacine) | Partner review or deliberate **intentional blanks** |
| Smell/taste overclaim | Default to **absence design** |

---

## 15. Open decisions log

_Use this table during studio; do not delete rows—append resolutions._

| Date | Question | Decision | Owner |
|------|----------|----------|-------|
| | | | |

---

## 16. References (seed — replace with formal citations)

- BDC official: judging, prizes, guidelines (`biodesignchallenge.org`)  
- Team literature binders per species (genomics, isotope ecology, Allee/flocking, thylacine history)  
- Course materials: `biodesign_cursor_agent` workbook steps  

---

## 17. File index (repo)

| File | Purpose |
|------|---------|
| `PROJECT_PLAN.md` | This document |
| `SLIDE_DECK.md` | Slide-by-slide outline for Keynote / Google Slides |
| `CLAIMS_REGISTER.csv` | *(create)* evidence ↔ UI strings |
| `AI_EXECUTION_LOG.md` | *(create)* model + prompt governance |
