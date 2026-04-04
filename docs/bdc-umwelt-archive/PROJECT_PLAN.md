# Biodesign Project Plan — Extinction Archive (Mammoth)

**Document type:** Planning & scope baseline for course / BDC-aligned development  
**Team:** 2 people · **Timeline:** 2–3 weeks (MVP sprint)  
**Last updated:** 2026-04-04  

**中文摘要：** 真猛犸 *Mammuthus primigenius* 单物种深做；浏览器主路径 + 可选手机 WebAR；三件式产品：**Dossier（档案）→ Mixer（节律声景）→ Ethics（分支伦理 + 证据门禁）**；全链路标注 **Cited / Modeled / Speculative**；实体为 **3D 打印 + AR** 轻量化配套。

**Related:** Operational detail (day-by-day, ethics copy, risk) lives in [`biodesign.md`](./biodesign.md); competition context in [`biodesign_cursor_agent.md`](./biodesign_cursor_agent.md).

---

## 1. Project identity

| Field | Content |
|-------|---------|
| **Working title** | Extinction Archive / *Umwelt Archive* — sensory–temporal capsule |
| **Hero species (locked)** | Woolly mammoth — *Mammuthus primigenius* |
| **Module baseline (locked)** | **Group1Slim** — Dossier + Mixer + full short Ethics (~2 min in talk) |
| **Competition lens** | Biodesign Challenge 2026 — **Biodigital Excellence**; strong Narrative & Context via ethics + labeling |
| **Exhibition theme (2026)** | *Convergent Life* — framed as biological–digital convergence around **lost temporal niches** |

---

## 2. Problem & design thesis

**Problem.** When a species goes extinct, we lose not only bodies but **patterns in time**: seasonal movement, light–dark entrainment, social rhythms, and sensory worlds (*Umwelt*). Public memory often flattens into icons; rigorous science stays in PDFs.

**Thesis.** *Extinction Archive* is a **browser-first interactive memorial** that reconstructs a **hypothesis-grade Umwelt** for one mammoth, grounded in **citable biology** (e.g. tusk isotope stratigraphy, circadian / Arctic adaptation literature), expressed through **parameterized visuals + Web Audio**, and closed with **branching ethics** and **explicit uncertainty** — so digital “resurrection” does not replace conservation urgency.

**Secondary thread (narrative only).** “Collective amnesia” ties ecological absence to cultural memory — **not** a separate system.

---

## 3. Scope

### 3.1 MVP (must ship)

1. **Dossier (single-species deep)**  
   - Geographic & temporal anchors for mammoth range (LGM–Early Holocene framing); every claim tagged **Cited / Modeled / Speculative**.  
   - **Science foldout:** tusk **Sr / O (etc.)** isotope profiles and published individual-life reconstructions → **1–2 static `ggplot` figures** for slides + web thumbnail.  
   - Immersive **360° / panorama placeholder** scene driven by **lit parameters** (season, sun height, fog), not raw “magic prompt.”

2. **Mixer (Web Audio)**  
   - ≥3 layers (recommended): **seasonal / photoperiod pulse**, **steppe–tundra sound bed** (mark elephant-relative parts *Speculative*), **Anthropocene pressure layer** (*Cited/Modeled* where possible).  
   - **Harmony → conflict** via documented DSP rules (compress/limit/dissonance when layers compete) — rules summarized on one slide + README.

3. **Ethics (short)**  
   - **Gate C:** ~45s, 3 statements (evidence literacy).  
   - **Branch B:** 2–3 cards (e.g. conservation vs de-extinction funding; invasive-species management framing; data/sovereignty reflection) → different **ending mix preset** + caption.

4. **Physical + AR (light)**  
   - One **3D print**: e.g. abstract **tusk growth “core”** or skull silhouette token.  
   - **Mobile WebAR** (`?ar=1` or dedicated entry): same GLB/stems as desktop; QR fallback to dossier anchor.

5. **BDC-aligned deliverable bundle**  
   - Talk (target **8 min + 2 min demo**).  
   - Visuals: UI screen capture + 3–5 stills.  
   - Physical artifact + AR capture.  
   - **45–90 s** trailer (Mixer + Ethics pivot + label flash).  
   - Deck: **Methods · Citations · Limitations** (minimum 3 slides).

### 3.2 Stretch (only if time remains)

- Tactile **material token** (non-food) + card copy.  
- Optional **second “ghost” layer** in Mixer only (no second dossier).  
- Optional desk **plant + light/moisture read** as **“still here”** contrast — labeled as metaphor, not habitat reconstruction.

---

## 4. Science pillars (mammoth)

| Pillar | Role in experience | Evidence posture |
|--------|--------------------|------------------|
| **Isotope + growth layers** | Dossier foldout + R figures; optional printed “year ring” metaphor | Mostly **Cited**; plotting = **Modeled** |
| **Photoperiod / seasonality** | Mixer pulse + scene lighting | **Cited + Modeled** split explicit |
| **Sensory / social proxies** | Scene composition; low-acuity / elephant-relative cues | Visual detail **Speculative** |
| **Extinction narrative** | Context slide + ethics copy | Consensus **Cited**; avoid single-cause dogma |

**Frozen boundary:** No parallel hero species (passenger pigeon / thylacine) in MVP.

---

## 5. Bio + digital architecture

| Layer | Inputs | Outputs | Stack (suggested) |
|-------|--------|---------|-------------------|
| Bio | ≥3 core papers (isotope case + adaptation review + extinction framing); museum dates | `dossier.json` + bib | Zotero |
| Viz | JSON → sun band, fog, ground | R3F / Three + shaders | Vite |
| Gen AI (**B main, A assist**) | Masks / palettes / control maps | Texture or detail pass | Local SD or API — cost/policy checked |
| Audio | STEM design table + tags | `AudioContext` layers | Web Audio; optional DAW bounce |
| Ethics | Branch JSON | Mixer master + captions | React state |

**Living bio:** Not required for thesis (Step 3 stance **B**); stretch only with disclaimers.

---

## 6. Narrative arc (10-minute talk target)

| Segment | Time | Focus |
|---------|------|--------|
| Hook | 0:45 | Memory × Umwelt |
| Dossier demo | 3:30 | Mammoth deep dive + **C/M/S** labels + isotope foldout |
| Mixer demo | 3:00 | Layers + conflict rules |
| Ethics | 2:00 | Gate C + Branch B + finale |
| Reflection | 1:00 | Iteration, limits, next steps |

---

## 7. Timeline (summary)

- **Week 1:** Stack + Dossier UI + mammoth data JSON + scene + Mixer prototype; **evidence audit #1**; ggplot v1.  
- **Week 2:** Ethics UI + GLB + WebAR minimal + print + slides (Methods / Citations / Limits) + rehearsal + trailer.  
- **Week 3 (if available):** Polish, accessibility, mock Q&A, P0 bugs only.

Full day-by-day grid: [`biodesign.md` §9](./biodesign.md).

---

## 8. Success criteria (Definition of Done)

- [ ] Happy path without a guide: Dossier → Mixer → Ethics → finale.  
- [ ] Every **Cited** claim has bibliographic metadata.  
- [ ] ≥3 explicit **Speculative** UI disclosures.  
- [ ] Mixer rules documented (non-black-box).  
- [ ] 3D print + AR backup recording.  
- [ ] Methods / Citations / Limitations slides complete.  
- [ ] README: run instructions + asset provenance + trade-offs.

---

## 9. Risks & mitigations

| Risk | Mitigation |
|------|------------|
| Generative imagery over-truth | Controlled generation + labels + muted palette / optional watermark |
| Literature overload | **Cap at 5** core papers; rest appendix |
| WebAR fragmentation | Desktop recording primary; AR bonus + QR fallback |
| Overclaiming mammoth “experience” | Elephant-relative **Modeled**; sounds & fine visuals **Speculative** |
| Scope creep | Species & module baseline **locked** (§1) |

---

## 10. Locked parameters (archive)

```text
Species = Mammoth
Group2 = Group1Slim
```

---

*End of PROJECT_PLAN.md*
