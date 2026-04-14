# Extinction Archive: Umwelt Hypothesis Dossiers  
### *(Extinction Archive: AI Memorial for Lost Species — “Umwelt Archive”: A Sensory Time Capsule)*

**BDC 2026 · Exhibition theme:** Convergent Life  
**Institution:** Macau University  
**Mentor:** Atticus SIMS  
**Team:** GUO XIAO YUE (ID MC569254) · LIU JIA QUN (ID MC569293) — 2 members  
**Build scope:** Web-only shipped course build (no live biosensor demo); full ideation includes optional bio + physical layers as **documented vision**  
**Core angle:** Palaeo-chronobiology + **Umwelt** (species-specific world-as-sensed) + temporal niche reconstruction via WebXR, generative environments, and **epistemic UI**  
**Target prizes:** **Biodigital Excellence Prize** · **Outstanding Digital Submission Prize**; strong **Narrative · Context · Reflection**  
**BDC idea alignment:** **Idea 3** (Extinction Archive) + **Idea 6** (Biorhythm Composer)

**Canonical short names:** **Extinction Archive** / **Umwelt Archive**  
**Planning doc role:** Single **hypothesis dossier** for judges and collaborators—links science claims, UX beats, ethics, and the **data + archival layer** now in-repo.

---

## Creative concept — from two dossiers to a living database (ideation update)

- **Proof-of-concept:** Two deep-dossier species — **woolly mammoth** (*Mammuthus primigenius*) and **thylacine** (*Thylacinus cynocephalus*) — anchor WebXR, citations, and ethics UI.  
- **Expanded scope:** A **unified high-priority species database** of **87 taxa**, each scored for **sensory reconstruction potential (1–10)**, **music-layering potential (1–10)**, and **data availability (High / Medium / Low)**.  
- **Curation pool:** Taxa drawn from **900+** documented extinct / extirpated species and recent confirmations (**Holocene extinctions, IUCN Red List, 2025 status updates** where applicable).  
- **Selection criteria:** Strong link to **human intervention**; high **palaeo- and archival data** availability; exceptional potential for **sensory** and **chronobiological** reconstruction (orbit, genomics, behaviour, sound archives).  
- **Repository note:** [`data/extinction_archive/animals_full.csv`](data/extinction_archive/animals_full.csv) currently holds **51 taxa** for JSON/SQL/Web bundle; **production step** = merge the full **87-row** master sheet (team CSV: `extinct_animals_database统一高优先级数据库（87种）.csv`) into exports and schema without expanding WebXR MVP beyond the two-species depth rule unless schedule allows.

---

## Research process — four-step iterative journey

1. **Step 1 — Preliminary concept:** Pharm- and trade-linked extinct animals → **collective biological memory** reconstruction (“Umwelt Archive — A Sensory Time Capsule”).  
2. **Step 2 — Unified database:** **87-species** CSV with sensory + music scores and extinction-context fields; supports planetary-map narrative and judging **Biodigital** depth.  
3. **Step 3 — Biodigital chronobiology:** Genes, orbits, **temporal niches** (day / season / social rhythm); literature spine in [`02_research/biology/biodigital_chronobiology_research.md`](02_research/biology/biodigital_chronobiology_research.md).  
4. **Step 4 — Bio + digital layering + ethics:** WebXR + generative AI (constrained) + Web Audio; **ethical decision interface** (resources, ecological risk, Indigenous perspectives, tech boundaries) + reflection log.

---

## Umwelt hypothesis dossiers — core definition (for judges)

Each extinct species is a **folder of testable scientific claims**, not a fantasy safari:

- **Genes & circadian** pathways (where aDNA / comparative genomics allows).  
- **Eye-orbit morphology** & retinal-ganglion-cell **models** (label **Interpolated** when not measured on that taxon).  
- **Palaeo-climate & seasonal rhythms**; isotope mobility where published.  
- **Sensory worlds** — sight, sound, smell — only inside a **prior fence** from peer-reviewed or archival sources.

**AI memorial:** Generative media **strictly constrained** by literature and licence-cleared archives.  
**Sensory time capsule:** Reconstruct **when** they lived (temporal niche), not only **what** they looked like.

---

### Ten representative species (high-priority database)

| Species | Common name | Sensory | Music | Human link & reconstruction strength |
|---------|-------------|---------|-------|----------------------------------------|
| *Mammuthus primigenius* | Woolly mammoth | 10 | 9 | Arctic circadian genomics; steppe soundscape |
| *Thylacinus cynocephalus* | Thylacine | 10 | 10 | Last-individual recordings; skull → diel activity |
| *Ectopistes migratorius* | Passenger pigeon | 10 | 10 | Massive-flock sonification; commercial overhunting |
| *Raphus cucullatus* | Dodo | 9 | 8 | Classic overhunting; AR-ready 3D refs |
| *Pinguinus impennis* | Great auk | 9 | 9 | Marine low-frequency context; feather/oil hunting |
| *Smilodon fatalis* | Saber-toothed cat | 9 | 9 | Bite-force / vocal simulation potential; megafauna collapse |
| *Hydrodamalis gigas* | Steller’s sea cow | 8 | 7 | Rapid ~27-year extinction arc; underwater low-frequency |
| *Chelonoidis abingdonii* | Pinta giant tortoise | 9 | 6 | “Lonesome George”; recent extinction (2012) |
| *Ninox albifacies* | Laughing owl | 8 | 9 | Distinctive vocal recordings; NZ invasion ecology |
| *Incilius periglenes* | Golden toad | 7 | 6 | Early climate-linked amphibian extinction case |

---

### User journey (experience spine)

1. **Discover rhythm** — Interactive planetary biological map.  
2. **Epistemic layers** — Deep scientific dossier per species.  
3. **Immersive sensory experience** — 360° environment + layered chronobiological music (Web Audio).  
4. **Ethics sliders** — Trade-off decision interface (de-extinction vs conservation, risk, sovereignty).  
5. **Reflection log** — Personal reflection ([`templates/reflection-log-webxr.html`](templates/reflection-log-webxr.html)) / export-friendly HTML.

### Physical model & AR (full vision)

3D-printed fossil replicas, miniature habitats, skeletal elements; **mobile AR scan** bridges tangible artefact and dossier (evidence stack first, short Umwelt loop second). **Course MVP:** one anchor + QR; full print farm = stretch.

### Bio + digital layering (ideation-complete / build-prioritized)

- **Biological layer:** Living plants + bacterial sensors (vision); real-time response — represents **extant** thriving ecosystems **co-present** with “stopped clocks” of extinct lineages (non-equivalent framing).  
- **Digital layer:** WebXR (A-Frame / Three.js); diffusion + prompt discipline; Web Audio **sonification of temporal niches**.  
**Shipped build:** digital + citations + ethics; **no** live biosensor demo in v1.

---

## Execution strategy — 重内容、轻装置 (agreed)

**Principle:** Redirect limited bandwidth away from hardware you cannot ship, into **evidence-linked narrative**, **epistemic transparency**, and **ethics**; **dossier-grade** background data (species list, archival URLs, schema) supports depth without expanding the WebXR MVP past two species unless time allows.

**English:** *Heavy on evidence-linked narrative, archival provenance, and honest AI limits; light on physical apparatus.*  
**中文：** *把精力集中在「有据的节律与感官叙事」「档案与不确定度」「语境与伦理」；装置只做 WebXR 入口的最低配套。*

**Non-goals (explicit):** Custom sensors, live bioelectric demos, projection-mapped dioramas, multi-piece AR hardware—unless narrative/reflection time goes to zero, do not reopen.

---

## Umwelt hypothesis & ideation spine (2026 synthesis)

**Problem (extended):** Extinction removes genomes and **temporal niches**—how a species partitioned **day, season, and social synchrony**. Public memory often **flattens** loss into a still image, not **time-in-the-world** or **multi-sensory Umwelt**. That gap is a form of **collective amnesia** about biodiversity integrity.

**Hypothesis (design-research):** If we reconstruct **temporal phenotypes** and **sensory proxies** under strict **Cited / Interpolated / Speculative** labelling—using chronobiology, morphology, isotopes, and **curated archival media** (museums, GBIF, film/sound archives)—we can make **absence narratable** without false certainty, and steer reflection toward **stewardship of extant life** and informed **de-extinction** debate.

**Three guiding questions (ideation → exhibit copy):**

1. How can **extinction–absence** become a **perceptible, narratable absence** (structured uncertainty, not fake precision)?  
2. How can **AI + biological data** **transparently** evoke lost biodiversity—without replacing conservation practice or **Indigenous knowledge systems**?  
3. How can **touch, sight, smell, hearing, taste** act as **gentle memory cues**—optional layers, intensity caps, clear tiers—avoiding sensory overload?

**Experience hooks (full vision; WebXR MVP = subset):**

- **Planetary map → coordinate → species dossier** (last-known or culturally salient place).  
- **Bio layer:** papers, specimens, isotopes, clock genes, orbit→diel proxies.  
- **Digital layer:** constrained generative visuals/audio; **stem-layering** / sonification for ecological synchrony metaphor.  
- **Post-immersion:** calm **ethical decision interfaces** (resource trade-offs, sovereignty, technological fixism)—then **reflection capture**.

**Deep research narrative (literature review):** [`02_research/biology/biodigital_chronobiology_research.md`](02_research/biology/biodigital_chronobiology_research.md)

---

## Repository: data layer, schema & archival dossiers

| Asset | Path | Purpose |
|--------|------|---------|
| **Species table (51 taxa in repo; 87 target master list)** | [`data/extinction_archive/animals_full.csv`](data/extinction_archive/animals_full.csv) | Wide CSV: names, extinction, **pharm_related / pharm_notes**, Umwelt scores, 3D refs. **Merge** full **87-row** unified high-priority sheet when expanding production exports. |
| **PostgreSQL bundle** | [`data/extinction_archive/archive_import.sql`](data/extinction_archive/archive_import.sql) | `animals`, `archival_media`, `literature_references` (+ extended schema doc below). |
| **Static API shape** | [`data/extinction_archive/archive.json`](data/extinction_archive/archive.json) | Single-file frontend bundle with nested media/refs. |
| **Full relational schema (map, layers, scenes)** | [`docs/database/extinction_archive_schema.md`](docs/database/extinction_archive_schema.md) · [`extinction_archive_schema.sql`](docs/database/extinction_archive_schema.sql) | **PostGIS deferred**; geographic sites + `reconstruction_layer` for when you add coordinates. |
| **Archival URL matrix** | [`data/extinction_archive/archival_media_research.csv`](data/extinction_archive/archival_media_research.csv) | Per-species **IUCN, GBIF, BHL, NFSA, SI, BOW, PMC…** (~350 rows). Regenerate: `python3 scripts/extinction_archive_db/generate_archival_media_research.py` |
| **BDC showcase shortlist** | [`docs/research/bdc_showcase_species_shortlist.md`](docs/research/bdc_showcase_species_shortlist.md) | **P0 / P1 / P2** species tiers + rationale. |
| **Archival research methodology** | [`docs/research/archival_media_by_species.md`](docs/research/archival_media_by_species.md) | How to use portals, licences, flagship links. |
| **Export generators** | [`scripts/extinction_archive_db/`](scripts/extinction_archive_db/) | Python: CSV/SQL/JSON + archival CSV. |

**Pharmaceutical / conservation pharmacology (dataset column):** `pharm_related` flags cases such as **horn trade / traditional-medicine demand** (e.g. western black rhino subspecies on the list). Use for **Context** judging lane and ethics copy—**not** as therapeutic claims.

---

### Content priorities (invest here) / 内容投入清单

| Track | What “done” looks like |
|--------|-------------------------|
| **Scientific narrative depth** | Per **shipped species**: parameter card (photoperiod, cited clock/morph claims, confidence); **scene→citation** map; plain-language “why time matters” thread. **Dossier species**: 1-slide or appendix with **top 3 archival URLs** from `archival_media_research.csv`. |
| **Honest technical reflection** | **3 epistemic layers** always visible: *Cited / Interpolated / Speculative*; tooling disclosure; **archival licence** note where NFSA / museum / xeno-canto applies. |
| **Context upgrade** | De-extinction trade-offs, ecological risk, **Indigenous sovereignty / TEK**—named sources; **pharm/trade** angle where `pharm_related` is true. |
| **Data provenance** | Judges can trace claims to **paper + institution URL**; regenerate exports after list edits. |

### Physical presence — minimum viable / 实体最低配

- **One** tactile anchor + **QR / short URL** → WebXR.  
- Optional: A3 **scene→citation** cheat sheet; optional **“dossier QR”** linking to a static page listing P0 archival sources (no extra build if timeboxed).

---

## Step 1 — Map Interests and Skills / 兴趣与技能地图

| Role | Focus |
|------|-------|
| **Member A — Experience Lead** | Narrative & sensory direction; palaeo-chronobiology + **Umwelt** translation; ethics; **dossier / archival** curation for deck |
| **Member B — Tech/AI Lead** | WebXR (A-Frame / Three.js); generative environments; epistemic + ethics UI; data pipeline from `archive.json` if needed |

**Project thesis / 项目核心视角:** Merge **chronobiology** with **temporal niche** and **sensory ecology** to reconstruct how extinct species lived inside **cycles of day, season, environment, and (where evidenced) social synchrony**—not only static anatomy.

---

## Step 2 — Find Overlaps / 交集句

**Core proposition / 核心命题:**  
*If we use **generative AI + WebXR** to **reconstruct and visualize** the **temporal phenotype** and **graded sensory proxies** of extinct species—anchored in **literature and archival media**—can we address **the human gap in sensing extinction**: the loss of another species’ **time** and **Umwelt**, not only its image?*

---

## Step 3 — Stress-test vs. BDC Rubric / 压力测试 (self-scores 1–3)

| Dimension | Score | Notes |
|-----------|-------|--------|
| **Narrative** | **3** | Beat: **discover rhythm / Umwelt → feel absence → ethical fork**. **Dossier** list supports “archive as planetary memorial” without bloating MVP. |
| **Concept** | **3** | **Time + sensory honesty** as spine; every scene tied to **cited proxy** or flagged inference. |
| **Context** | **2 → 3** | Upgrade with **archival coloniality** (skins, bounty, trade) + **pharm_notes** where relevant + **Palawa-first** framing for thylacine. |
| **Reflection** | **2.5 → 3** | Interactive epistemic UI + **what archives omit** + user reflection. |

---

## Step 4 — Research Sprint: species tiers & WebXR lock

### Tier policy (new — aligns with `bdc_showcase_species_shortlist.md`)

| Tier | Species (examples) | Role in submission |
|------|---------------------|---------------------|
| **P0 — WebXR MVP (locked depth)** | *Mammuthus primigenius*, *Thylacinus cynocephalus* | Full scene graph, citation strip, ethics + Indigenous UI—**this is the hypothesis test**. |
| **P0 — Narrative / acoustic flagship (dataset + deck)** | *Ectopistes migratorius* | **Social synchrony + “silence”** (e.g. empty xeno-canto as *evidence of acoustic loss*); Martha/Smithsonian dossier links in slides or static appendix—not required inside WebXR v1. |
| **P1 — Dossier depth (optional film / appendix / future map)** | *Raphus cucullatus*, *Pinguinus impennis* | **14+ curated URLs** each in CSV; use for **Context** and **museum/archive literacy**—do not scope into WebXR unless Week 4 surplus. |
| **P2 — Back catalogue** | Remaining rows in `animals_full.csv` + full **87** master list when merged | Map/GIS **future**; judges see **systematic research**, not 85 extra WebXR scenes. |

**Decision (unchanged for shipped interactive):** **Depth on mammoth + thylacine** for WebXR v1. **Passenger pigeon + others** enrich **narrative, dossier, and database story** without breaking the two-species build rule.

**Archival deep links (P0 trio + P1 pair):** pre-compiled in `generate_archival_media_research.py` → `archival_media_research.csv` (**10–17 curated rows per flagship taxon**).

### Required citations — slots filled (DOI / ISBN) / 必引文献槽位（已填标识符）

**How to use:** Keep `[x]` only after **PDF read + claim check**. If a verification note below applies, fix on-screen copy before tagging as **Cited**.

#### Literature verification log / 核验备忘（必读）

| Slot | Issue | Resolution (2026-04 audit) |
|------|--------|------------------------------|
| **M1** | **PER2** variant count / gene-specific wording in Lynch et al. (2015) | **Cursor 未能在本环境中打开 Elsevier 全文 / 补充表。** PubMed 摘要仅确认 **circadian biology 等功能富集**与 **TRPV3** 实验。**已采用保守 UI 文案**（见 `Scene_Bio_01`）。若课程周内有全文权限，可再搜全文 “PER2”；在此之前 **不得** 写具体 *PER2* 突变数目。 |
| **M4** | `10.1101/151746` is **bioRxiv** (preprint). **TRPV3** functional mammoth–elephant contrast is also in **Lynch et al. (2015)** (peer-reviewed). | Prefer **Lynch et al., 2015** for jury-safe *TRPV3* claims; use **Kim et al., 2017** as optional structural detail + label **preprint** in epistemic UI. |
| **T2** | Mass & Supin **2025** DOI 多版本无法在 Crossref 可靠解析。 | **已改为可验证的出版 PDF：** Mass & Supin **(2020)** 瓶鼻海豚视网膜 RGC 拓扑与分辨率，**同一作者方法谱系**，DOI [10.31857/S0002332920060107](https://doi.org/10.31857/S0002332920060107)，[Publisher PDF](https://sciencejournals.ru/issues/izvbio/2020/vol_2020/iss_6/IzvBio2006010Mass/IzvBio2006010Mass.pdf)。Scene_POV_01 仍为 **Interpolated**（非袋狼实测）。若日后找到 2025 文，可在 epistemic 层并列更新。 |
| **T5** | Clements (2025) + Palawa-first sourcing | 已增 **Palawa 主导 / 相关**补全文献与 `UI_Indigenous_Context` 文案；Clements 作学术交叉引用，**不**替代原住民第一声音。 |

---

#### Species A — Woolly mammoth (*Mammuthus primigenius*) — polar rhythm & cold

| # | 建议主题 | 选定文献（短引文） | DOI / ID | 对应分镜 / 界面 ID | Tier |
|---|----------|-------------------|----------|-------------------|------|
| M1 | 比较基因组 / 节律相关通路 | Lynch et al., 2015 | [10.1016/j.celrep.2015.06.027](https://doi.org/10.1016/j.celrep.2015.06.027) · PMID [26146078](https://pubmed.ncbi.nlm.nih.gov/26146078/) | `Scene_Bio_01` | Cited |
| M2 | 极地节律弱化类比 | Lu et al., 2010 | [10.1016/j.cub.2010.01.042](https://doi.org/10.1016/j.cub.2010.01.042) | `Scene_Environment_02` | Interpolated |
| M3 | 高产草原 / 猛犸草原生境 | Zimov et al., 2012 | [10.1016/j.quascirev.2012.08.004](https://doi.org/10.1016/j.quascirev.2012.08.004) | `Scene_Landscape_01` | Cited |
| M4 | 冷觉与毛发生长 (*TRPV3* 等) | Kim et al., 2017 (bioRxiv) | [10.1101/151746](https://doi.org/10.1101/151746) | `Scene_Sensory_01` | Cited* |
| M5 | 去灭绝伦理 / 资源与生态权衡 | Sherkow & Greely, 2013 | [10.1126/science.1236946](https://doi.org/10.1126/science.1236946) | `UI_Ethics_Fork` · `UI_Reflection_Log` | Cited |

\*M4: disclose preprint status; anchor core *TRPV3* phenotype to **Lynch et al., 2015** when possible.

**Plus — dossier / isotope narrative (for talk + citation strip optional beat):** Wooller et al., 2021 — tusk isotope mobility (*Science* [10.1126/science.abg1134](https://doi.org/10.1126/science.abg1134)); popular explainer in Smithsonian Magazine (URL in `archival_media_research.csv`). Label **Cited** for migration **science**; **Interpolated** if mapped 1:1 to generative music without raw data.

#### Species B — Thylacine (*Thylacinus cynocephalus*) — crepuscular vision & colonial context

| # | 建议主题 | 选定文献（短引文） | DOI / ID | 对应分镜 / 界面 ID | Tier |
|---|----------|-------------------|----------|-------------------|------|
| T1 | 眶径与昼夜活动型 | Pozniak et al., 2018 | [10.1002/ar.23910](https://doi.org/10.1002/ar.23910) | `Scene_Bio_02` | Cited |
| T2 | 视网膜 / RGC 拓扑方法（外推至陆生哺乳类视觉隐喻） | Mass & Supin, 2020 | [10.31857/S0002332920060107](https://doi.org/10.31857/S0002332920060107) · [PDF](https://sciencejournals.ru/issues/izvbio/2020/vol_2020/iss_6/IzvBio2006010Mass/IzvBio2006010Mass.pdf) | `Scene_POV_01` | Interpolated |
| T3 | 灭绝史与行为记录 | Paddle, 2000 | ISBN `9780521782196` (Cambridge Univ. Press) | `Scene_Context_01` | Cited |
| T4 | 人为干扰 / 赏金与栖息地 | Sleightholme & Campbell, 2016 | [10.1080/00222933.2016.1217037](https://doi.org/10.1080/00222933.2016.1217037) | `Scene_Context_01` · `UI_Ethics_Fork` | Cited |
| T5 | 文化主权 / 殖民与复活叙事 | Clements, 2025 | [10.1177/13534858251272203](https://doi.org/10.1177/13534858251272203) | `UI_Indigenous_Context` | Context |

**Plus — dossier / moving image:** NFSA catalogue items (licence required for exhibit); TMAG Shaping Tasmania object; NMA resources—URLs in `archival_media_research.csv`. **Never** present NFSA footage as **public domain** without clearance.

**Checklist — 文献审核状态 (toggle after PDF pass)**  
M1 [x] · M2 [ ] · M3 [ ] · M4 [ ] · M5 [ ] · T1 [ ] · T2 [x] · T3 [ ] · T4 [ ] · T5 [ ]  

- **M1 [x]:** 保守文案已锁定（无全文则不提 *PER2* 具体变异）。  
- **T2 [x]:** DOI + Publisher PDF 已核对可访问（Mass & Supin 2020）；仍为 **Interpolated** 用于袋狼 POV。

---

### Storyboard — interaction notes + on-screen tags / 分镜交互说明与短引文挂载

Use these strings **in Figma / doc / WebXR comments** and mirror the **short tag** in the epistemic panel when that scene loads.

| ID | Interaction / 交互说明 | On-screen tag (short) / 角标 |
|----|-------------------------|------------------------------|
| `Scene_Bio_01` | **Locked copy (EN):** *“Woolly mammoths carry **mammoth-specific amino-acid changes enriched in circadian-related genes** among other Arctic adaptations (Lynch et al., 2015).”* **Do not** state *PER2* counts until verified in primary PDF.**中文：** 「猛犸象基因组相对现生象，存在**与昼夜节律相关的基因类别**中的猛犸特异氨基酸改变（Lynch et al., 2015）。」**勿写** *PER2* 具体突变数。 | (Lynch et al., 2015) |
| `Scene_Environment_02` | **Interpolated:** Polar day/night scrub; copy explains reindeer “molecular clock attenuation” as **analogical** support for how high-latitude life decouples from strict 24h entrainment—not a mammoth measurement. | (Lu et al., 2010) · **Interpolated** |
| `Scene_Landscape_01` | Vegetation density / productivity tied to **mammoth steppe** / savanna-like pulse; constrain generative prompts with Zimov parameters (seasonal productivity), not fantasy jungle. | (Zimov et al., 2012) |
| `Scene_Sensory_01` | Cold / thermo narrative: *TRPV3* mammoth substitution → altered temperature sensitivity & hair-associated phenotypes; **cite Lynch 2015 for validated channel**; Kim 2017 as **preprint** detail if used. | (Lynch et al., 2015); optional (Kim et al., 2017) |
| `Scene_Bio_02` | Skull / orbit measurement beat → **crepuscular or nocturnal** predation niche; no overstated “night vision” without Interpolated flag. | (Pozniak et al., 2018) |
| `Scene_POV_01` | **Interpolated:** 依据 **Mass & Supin (2020)** 对哺乳动物视网膜 **RGC 拓扑与分辨率** 的方法与结论，**隐喻式**强化运动/对比线索；**非**袋狼视网膜实测。示例句：*“POV 运动—对比强调借鉴 Mass & Supin (2020) 的 RGC 分布模型（海豚物种）；袋狼仅为推演。”* **WebXR 外链：** [DOI](https://doi.org/10.31857/S0002332920060107) · [Publisher PDF](https://sciencejournals.ru/issues/izvbio/2020/vol_2020/iss_6/IzvBio2006010Mass/IzvBio2006010Mass.pdf) | (Mass & Supin, 2020) · **Interpolated** |
| `Scene_Context_01` | Historical behaviors, habitat, hunting; layer Sleightholme for **bounty / land-use** after Paddle baseline. | (Paddle, 2000); (Sleightholme & Campbell, 2016) |
| `UI_Indigenous_Context` | 见下文 **「T5 殖民暴力与生态记忆」** 文案 + Palawa 补全文献表。 | (Clements, 2025); Schlunke (2025); Rimmer (2020); Lehman (2013) |
| `UI_Ethics_Fork` | **Resource sliders** (e.g. de-extinction vs. field conservation; legal personhood of “products”; ecosystem risk) scripted from **Sherkow & Greely (2013)** tensions—each slider footnoted to a clause or theme from the paper, not generic sci-fi. | (Sherkow & Greely, 2013) |
| `UI_Reflection_Log` | User short reflection + team **limits**: aDNA, protein folding, circadian phenotype uncertainty; cross-link to Sherkow for **why trade-offs matter**. | (Sherkow & Greely, 2013); team process |

**`UI_Ethics_Fork` — Sherkow & Greely–aligned prompts (draft copy hooks)**  
- *“Should public funding prioritize laboratory de-extinction or **in situ** conservation of extant species and landscapes?”*  
- *“If a revived lineage is legally novel, who bears liability for **ecological harm**?”*  
- *“Does revival rhetoric repeat extractive relationships to **Country** and Indigenous governance?”* (bridge from Clements / separate Palawa sources)

---

### T5 — `UI_Indigenous_Context` copy / 殖民暴力与生态记忆（袋狼档案）

**参考 Clements (2025) 的论证轴：** 去灭绝话语不仅是实验室技术，也可能延续 **殖民暴力之后果**——包括对 **Country（lutruwita / 塔斯马尼亚土地与水系）** 的关系性伤害与对灭绝的政治性遗忘。袋狼的消失与殖民开拓、赏金与土地剥夺 **同一历史织物**；将袋狼仅当作“可复活图标”，可能 **遮蔽** 这段交织史。

**介绍文案（中，可置于 UI 首屏）：**  
「袋狼的灭绝不是孤立的‘自然事件’，而是与殖民开拓、土地剥夺与针对 Palawa 人民的暴力相互缠绕。今天关于‘复活’的讨论，同样牵动 **谁有权定义生命、记忆与责任**——这是 **文化主权** 问题，而不只是基因问题。」

**English (subtitle option):**  
*Thylacine extinction is entangled with colonial violence against Palawa peoples and Country. De-extinction discourse raises questions of **cultural sovereignty**—who defines life, memory, and responsibility—not genetics alone.*

#### Palawa-led / Palawa-centred supplementary sources / 原住民主导或中心文献补全

| 文献 | 说明 | 稳定链接 / ID |
|------|------|----------------|
| **Rimmer, Z.** (2020). *palawa kani: Expressing the power of language in art and the museum context.* **Artlink** 40(2). **Pakana** 作者；语言、博物馆与殖民知识断裂。 | [artlink.com.au 文章页](https://www.artlink.com.au/articles/4846/palawa-kani-expressing-the-power-of-language-in-art-and-the-museum-context/) |
| **Lehman, G.** (2013). *Tasmanian Gothic.* **Griffith Review**（随笔；**Trawulwuy** / 塔斯马尼亚原住民学者；殖民景观与再现政治）。 | [griffithreview.com 文章](https://www.griffithreview.com/articles/tasmanian-gothic/) |
| **Schlunke, K.** (2025). *De-extinction and poetry.* **Cambridge Prism Extinct** 3:e14. 非原住民作者；明确将袋狼去灭绝与 **对 Indigenous peoples and country 的暴力** 并置，并列出 **Palawa 对袋狼的多种称谓**。 | DOI [10.1017/ext.2025.10008](https://doi.org/10.1017/ext.2025.10008) · [PMC12722039](https://pmc.ncbi.nlm.nih.gov/articles/PMC12722039/) |

**Use protocol:** 并置 **Clements + Schlunke** 作批判理论，**Rimmer + Lehman** 作 **Palawa 声音优先**层；界面脚注写明作者身份与局限。

---

### `UI_Reflection_Log` — WebXR 反思输入框代码模版

**路径:** [`templates/reflection-log-webxr.html`](templates/reflection-log-webxr.html)  

- 含 `<textarea>`、**本地** `localStorage` 暂存、以及基于关键词的 **文献伦理片段对照**（Sherkow & Greely 框架 + 项目交叉引用）。  
- **非** LLM：匹配规则可审计；适合答辩时解释「实时比对」= **启发式并列文献观点**。  
- 嵌入 A-Frame：可将该 HTML 作为 **2D overlay**（如 `a-entity` + `html` 组件或 iframe），置于体验结尾 `UI_Reflection_Log` 场景。

---

**Scene / UI ID index (compact) / 分镜索引**

| ID | Role |
|----|------|
| `Scene_Bio_01` | Mammoth: genomics / circadian |
| `Scene_Environment_02` | Mammoth: polar photoperiod (reindeer analogy) |
| `Scene_Landscape_01` | Mammoth: mammoth-steppe staging |
| `Scene_Sensory_01` | Mammoth: TRPV3 / cold sensation |
| `Scene_Bio_02` | Thylacine: orbit → diel activity |
| `Scene_POV_01` | Thylacine: POV (RGC model, Interpolated) |
| `Scene_Context_01` | Thylacine: history + drivers |
| `UI_Indigenous_Context` | Sovereignty / colonial critique |
| `UI_Ethics_Fork` | Resource & legal / ecological trade-offs |
| `UI_Reflection_Log` | Limits + user reflection |

**Completion rule / 完成规则:** All **10** checklist boxes `[x]` after PDF read; every **Storyboard** row shows the **same** tag in the shipped WebXR epistemic strip; **M2** and `Scene_POV_01` always display **Interpolated**.

---

## Step 5 — Bio + Digital Split / 生物与数字层自检 (web-only)

**Biology layer (non-negotiable):** Daylight regimes, chronobiology proxies, sensory ecology **anchored in papers** + **where used**, **museum / occurrence** metadata from the dossier CSV. Narrative climax: **stewardship of extant biodiversity**.

**Digital layer (non-negotiable):** WebXR scene graph; generative environments **constrained** by paleo-environment proxies; **sonification** of phase (day/night, season, optional **stem metaphor** for synchrony); **epistemic UI** separating measured vs. inferred vs. imagined; **prompt / model disclosure** for AI assets.

**Red lines / 红线:** No purely ornamental AI vistas—every shot maps to **a data column** or **explicit unknown band**.

**Living-sensor note:** Replace wet-lab with (1) comparison to extant relatives in copy, (2) optional **public daylight API** vs. paleo-latitude (labelled), (3) **archival stills/video** only with **institution licence**.

---

## Step 6 — Concept Narrative / 概念叙事 (~200 字电梯演讲)

**[Problem 问题]** 物种灭绝不仅是 DNA 的丢失，更是 **时间位** 与 **Umwelt** 的断裂；公众记忆常被压成静态图像，难以感知“它如何活在昼夜与季节里”，形成一种对生物多样性的 **结构性遗忘**。

**[Insight 洞见]** 古生物钟学、同位素轨迹与档案（标本、影像、声库）让我们能把 **节律与感官代理** 转译成可讨论、可标注不确定度的体验材料。

**[Solution 方案]** 《灭绝档案 / Umwelt 档案》是以 WebXR 为核心的 **假说卷宗**：在文献与馆际数据约束下，用生成式环境与音化呈现 **猛犸的极地时间结构** 与 **袋狼的晨昏视觉隐喻**；并以 **认识论 UI** 区分证据、推演与想象。**87 种高优先级统一数据库**（仓库内先行 **51 类** 导入）支撑“行星纪念地图”的叙事与 BDC **Biodigital** 深度，而不绑架双物种 WebXR MVP 范围。

**[Impact 影响]** 在“去灭绝”话语前，它把观众带回 **生命时间与档案政治** 的不可逆性；伦理权衡与反思界面促使人们从奇观转向对 **现生生物多样性** 与 **文化主权** 的负责讨论。

*(Rewrite in your own voice for submission; 终稿须为你们本人的语气。)*

---

## Step 7 — Prototype & Deliverables / 原型与交付物

**Strategy:** **Content-first** + **dossier-first** (CSV/JSON/SQL + archival matrix as proof of systematic research).

| Deliverable | MVP (must ship) | Target | Stretch (if time) |
|-------------|-----------------|--------|-------------------|
| **Live demo (Summit)** | One species **“day arc”** in WebXR + **interactive** epistemic UI + ethics fork | **Both species** (mammoth + thylacine) + **contrast** (polar vs. crepuscular **time shape**) | Extra mammoth season slice; optional **passenger pigeon** audio slide in deck only |
| **Narrative / science pack** | **Scene→citation** table + talking points | **Methods & limits** PDF; **1-page dossier appendix** (P0–P1 species + top archival URLs) | Link to `archival_media_research.csv` on GitHub Pages |
| **Data proof (Biodigital)** | Point judges to **`animals_full.csv` + `archive.json`** + generator scripts | **`archive_import.sql`** loaded in demo DB or screenshot | PostGIS geo sites when coordinates curated |
| **Visual system** | **3-layer** epistemic legend + data panel synced to scenes | Full type / color / motion | One **evidence board** print |
| **Physical (minimal)** | **One** object or card + **QR → WebXR** | Same; optional second QR → **dossier list** | — |
| **Video (1–5 min)** | Trailer: rhythm → **uncertainty** → ethics | Sonification + archival stills (licensed) | — |
| **Slides** | Map to **Narrative · Concept · Context · Reflection** | **Reflection**: biases, cuts, unknowns; **Context**: pharm/trade + sovereignty | — |

**MVP done when:** User completes **immersive interval → manipulates uncertainty layers → one ethical choice + short reflection**.

---

## Step 8 — Build Sprint Plan / 4 周节奏 (2-person)

**Priority order if time crunches:** (1) epistemic UI + scene→citation, (2) ethics fork + Context copy, (3) second species scenes, (4) sonification polish, (5) dossier slide + CSV pointer for judges, (6) print collateral, (7) physical anchor.

| Week | Phase | Member A | Member B |
|------|--------|----------|----------|
| **1** | Discovery | Literature + **archival deep links** for P0; scene→citation grid; ethics draft | WebXR shell; epistemic UI wireframe; **pipeline sketch** (`archive.json` optional read) |
| **2** | Prototyping | Parameter tables; **NFSA / SI licence** checklist for any embed | Time scrubber; generative **constraint doc**; bind citations |
| **3** | Integration | Sonification + ethics; **dossier appendix** for deck; Q&A risk list | Full epistemic layers + ethics UI; methods panel; perf pass |
| **4** | Polish | **10-min + Q&A**; honest-AI talking points | Deploy; video; print **QR** + optional dossier one-sheet |

**Buffer:** If Week 3 slips, **cut** stretch—not epistemic UI, ethics, or citation mapping.

---

## BDC Q&A — Likely prompts (prep bullets)

- **Is this biodesign without living matter?** *Biology is the **constraint system**: literature + specimens + occurrence archives drive the experience; the living stake is **extant biodiversity** and honest inference limits.*  
- **How do you prevent AI hallucination?** *Cited → interpolated → speculative; archival assets **licence-checked**; nothing speculative without UI flag.*  
- **Why 87 species in the master list but 51 rows in-repo and two in WebXR?** ***Hypothesis dossiers*** scale research and **map narrative**; the repo bundle is an **import slice** expanding toward the full **87**; **interactive depth** stays falsifiable on two taxa for the build window.*  
- **Indigenous / local knowledge?** *Name sources; state limits; no partnership claims without real consultation.*

---

## Risk register (web-only + content-first)

| Risk | Mitigation |
|------|------------|
| “Just a VR art piece” | **Scene→citation** + **`archival_media_research.csv`** + synced data panel |
| Ethics feels bolted-on | **Structural** fork; **T5** + **pharm_notes** where relevant |
| Archival copyright surprise | **NFSA / SI / BOW** licence pass before Summit video; prefer **link-out** over rip |
| Reflection reads shallow | Interactive epistemic layers + **what archives omit** |
| Scope creep | **Non-goals** locked; physical = **one** QR; WebXR = **two species** unless explicit Week 4 surplus |

---

*Document title updated April 2026: **Umwelt Hypothesis Dossiers** — integrates ideation (sensory time capsule, 87-species database narrative, four-step research arc), `animals_full` / SQL / JSON / archival matrix, and BDC showcase tiers (Idea 3 + 6). Align summit dates with [biodesignchallenge.org](https://biodesignchallenge.org).*

---

## Next steps (submission-facing)

- Expand database exports to full **87** species in production pipeline.  
- Prototype full **WebXR** experience (maintain epistemic + ethics spine).  
- Complete **physical AR** models where schedule allows (else QR + one anchor).  
- Prepare **1–5 min** project video (licence-cleared archival clips).  

## References & works cited

Consolidate citations from: (1) this planning document (mammoth / thylacine / pigeon / ethics slots); (2) [`02_research/biology/biodigital_chronobiology_research.md`](02_research/biology/biodigital_chronobiology_research.md) **Works cited**; (3) BDC context docs as required by course. Slide PDFs and deck rebuild: `python3 docs/bdc-umwelt-archive/scripts/build_extinction_archive_slides.py`.
