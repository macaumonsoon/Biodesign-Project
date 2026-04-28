# 《灭绝档案馆 · Umwelt 假说档案夹》FINAL-SMALL 版演讲稿 / 中英对照

**配套 PDF**：`slides/export/[FINAL-SMALL] Extinction Archive Umwelt Hypothesis Dossiers_BDC2026.pdf`（共 **15** 页）  
**说明**：此稿与 `BDC2026_10min_Extinction_Archive.md`（10 分钟叙事版 Marp）**不是同一套幻灯片**——本 PDF 偏评委/技术档案夹叙事（仓库证据层、模块、物种分层与案例锚点）。  
**区别于**：公开答辩用的叙事终稿请使用 **`0429[FINAL] Extinction Archive … BDC2026.pdf`（13 页）** 或仓库副本 `slides/export/0429_FINAL_Extinction_Archive_Umwelt_Hypothesis_Dossiers_BDC2026.pdf`，演讲稿请对照 **`BDC2026_10min_SpeakerNotes_zh-CN_bilingual.md`**。

---

## 第 1 页 / Title · 题目页

**中文口播**  
大家好。这是 **Extinction Archive / Umwelt Hypothesis Dossiers**，也就是把灭绝物种做成一种**可被叙述的感官时间胶囊**。我们强调：**文献与仓库证据打底，而不是复活叙事**。交付形态是 **WebXR + 仓库里的数据层**：重证据、轻硬件。

**English**  
This deck introduces **Extinction Archive / Umwelt Hypothesis Dossiers**: a literature-grounded sensory time capsule for lost species—not a resurrection pitch. The shipped emphasis is **WebXR plus an in-repository data layer**: heavy evidence, light hardware.

---

## 第 2 页 / Repository & research layer · 仓库与研究层

**中文口播**  
先交代课程版本的工程边界：我们是 **浏览器 / WebXR** 交付，不做现场生物传感器 Demo；现场可以用 **一张 QR + 可选引用页**。数据上，`animals_full.csv` 当前是 **51 个分类单元**，配套 **archive.json** 与 **PostgreSQL 导入脚本**。另有 **archival_media_research.csv** 约 **349** 条策展行，来源覆盖 IUCN、GBIF、BHL、澳大利亚 NFSA、史密森等。规划与分层见仓库里的规划文档与 showcase shortlist；生物学叙事主轴见 **biodigital chronobiology** 研究文档，并可由脚本再生。

**English**  
Course build ships as **browser / WebXR**—no live biosensor demo; one QR plus optional citations. **51 taxa** live in `animals_full.csv`, with **archive.json** and **archive_import.sql**. **archival_media_research.csv** holds ~349 curated rows across IUCN, GBIF, BHL, NFSA, SI, BOW, PMC, etc. Planning lives in-repo; the literature spine is **biodigital chronobiology**, regenerable via scripts.

---

## 第 3 页 / The fracture · 断裂（Umwelt + 时间）

**中文口播**  
灭绝带走的不仅是 DNA 与生态位，还有**时间里的生态位**：昼夜、季节、群体同步。公众记忆常常把物种压成图标，于是我们失去了「另一种生命如何在时间里活着」。同时还有对生物多样性完整性的**集体失忆**：基线漂移、去灭绝话语过热。档案夹的目标，是让「缺席」在**结构化不确定性**下仍可被叙述。

**English**  
Extinction removes genetics and roles—and **temporal niches**: day, season, social synchrony. Public memory flattens species into icons. We also risk collective amnesia about biodiversity integrity—shifting baselines and de-extinction hype. The dossier makes absence **narratable with structured uncertainty**.

---

## 第 4 页 / Three guiding questions · 三个引导问题

**中文口播**  
我们把自己锚在三句话上：第一，灭绝带来的缺席，怎样能被感知，同时避免虚假精确？第二，AI 加生物数据怎样**透明地**唤起记忆——不把 AI 当成保育或原住民知识的替代品？第三，触觉、视觉、嗅觉、听觉怎样作为**可选、轻柔**的线索层，而不是感官过载？

**English**  
Three guiding questions: How can extinction-absence become perceivable **without false precision**? How can AI plus biological data evoke memory **transparently**—not replacing conservation or Indigenous knowledge? How can touch, sight, smell, sound act as **gentle, optional cues**—no sensory overload?

---

## 第 5 页 / Experience spine · 体验骨架

**中文口播**  
体验骨架是：从**行星地图**落到**坐标**，再打开**物种档案**。愿景如此；当前 WebXR MVP 我们会把深度放在**两个物种案例**. 生物层包括基因组、形态、同位素、博物馆与 GBIF 记录。数字层是用**受约束的生成场景**，加上 Web Audio：声景化、甚至用「声部」隐喻群体节律。出口不是煽情收尾，而是**伦理分叉与反思**：把照护引向**仍在世的物种与 stewardship**。

**English**  
Spine: planetary map → coordinate → dossier—vision; WebXR MVP focuses depth on **two species**. Bio layer: genomics, morphology, isotopes, museum and GBIF records. Digital layer: constrained generative scenes plus Web Audio sonification / stem metaphor. Exit: ethics fork—**stewardship of extant life**.

---

## 第 6 页 / Three load-bearing modules · 三个承重模块

**中文口播**  
我们用三个模块撑起整条体验。**Species Dossier**：证据卡片、感官代理、灭绝驱动——场景始终能回到引用。**Polyphony Mixer**：季节、昼夜、迁徙、密度——听见的可以是和谐，也可以是崩溃。**Ethics Console**：资金、入侵风险、主权等权衡，再加一道「证据门」——不让伦理话术绕过资料边界。

**English**  
Three modules: **Species Dossier**—evidence cards, sensory proxies, drivers—scene ties back to citations. **Polyphony Mixer**—seasonal, diel, migration, density—harmony versus collapse. **Ethics Console**—trade-offs plus an **evidence gate**.

---

## 第 7 页 / Species tiers · 物种分层（研究 + 搭建）

**中文口播**  
这是研究与搭建的分层表。**P0 WebXR**：猛犸与袋狼——完整交互深度；时间生物学加轨道视角；引用条常驻。**P0 档案**：旅鸽——玛莎、同步性、声学缺席；xeno-canto 可能为空，我们就诚实写 UI。**P1 档案**：渡渡鸟与大海雀——每条 **14+** 策展链接——岛屿语境、BHL、史密森——先做 Context lane，不进 WebXR v1。

**English**  
Tiered build: **P0 WebXR** mammoth and thylacine—full depth, chronobiology + orbit/POV, citation strip. **P0 dossier** passenger pigeon—Martha, synchrony, acoustic absence—honest empty-archive copy. **P1 dossier** dodo and great auk—14+ curated URLs each—islands, BHL, SI—context lane, not WebXR v1.

---

## 第 8 页 / Bio + Digital（网页已 ship 的版本）

**中文口播**  
网页已 ship 的版本里：生物学一侧强调**古生物钟**、同位素轨迹——例如长牙迁移——论文优先。数字一侧是 **A-Frame / Three.js WebXR**；生成环境带着提示词与约束文档；**认识论界面**常驻屏幕。课程构建不做现场生物传感器；若时间允许，可加「公开日照 API」对照古纬度的可选层。

**English**  
Shipped web build: biology—palaeo-chronobiology, isotope trails (e.g., tusk mobility)—papers first. Digital—A-Frame / Three.js WebXR; generative env with prompt + constraint doc; **epistemic UI always on-screen**. No live biosensor—optional daylight API versus palaeo-latitude if time allows.

---

## 第 9 页 / Honesty UI · 诚实标注

**中文口播**  
我们把界面语言拆成三层：**Cited**——同行评议论文、博物馆目录或数据集行；**Interpolated**——有理由的推断；**Speculative**——创造性延伸，绝不说成「复原的现实」。档案影像来自 NFSA、SI 等机构时，上映或嵌入前先走**许可核查**。

**English**  
Honesty UI: **Cited**—peer-reviewed, museum catalogue, dataset row. **Interpolated**—justified inference. **Speculative**—creative extension, never sold as recovered reality. Archival media—licence check before trailer or embed.

---

## 第 10 页 / Data layer in repository · 仓库里的数据层

**中文口播**  
这张表对照仓库资产：`animals_full.csv`（51）、前端 bundle 与数据库脚本、`archival_media_research.csv`（约 349 行），以及面向未来的 **schema**——地图站点、重建层、场景。

**English**  
Asset map: CSV bundle, archive JSON/SQL, media research sheet, schema files for future map sites and reconstruction layers.

---

## 第 11 页 / Mammoth · 猛犸——引用锚点

**中文口播**  
猛犸案例把证据钉在几处硬锚点上：比较基因组学与节律相关基因富集——我们对 PER2 之类表述保守，直到 PDF 逐项核实。栖息地用 **Zimov** 等的草原框架。迁徙输入来自 **Wooller**  Science 长牙同位素——迁徙可以直接进入声景或 sonification。

**English**  
Mammoth anchors: comparative genomics and circadian enrichment—conservative on PER2 pending PDF checks. Steppe framing—Zimov et al. Mobility—Wooller et al. isotope migration as sonification input.

---

## 第 12 页 / Thylacine · 袋狼——档案与伦理

**中文口播**  
袋狼一线连接眼眶结构与黄昏/夜行生态位；「视角滤镜」来自方法论文献，标注为 **Interpolated**。活动影像在 NFSA——清权前置；标本叙事可看 TMAG、NMA。语境层必须纳入 **Palawa** 主导来源与主权论述——对照 **Clements / Schlunke** 对去灭绝奇观化的批评。

**English**  
Thylacine: orbit to crepuscular/nocturnal niche—POV filter interpolated from methods literature. NFSA moving image—clearance required. Context—Palawa-led sources and sovereignty versus de-extinction spectacle—Clements / Schlunke.

---

## 第 13 页 / Passenger pigeon · 旅鸽——档案节拍

**中文口播**  
旅鸽节拍：**史密森玛莎**、Project Passenger Pigeon、Birds of the World 账户。群体同步性崩溃——我们用「相位锁定断裂」的声学隐喻。声档案稀疏或空白——那不是失误，而是**声学丧失的证据**——文案要写诚实。

**English**  
Passenger pigeon beat: Smithsonian Martha plus canonical accounts. Social synchrony collapse—sonic metaphor of phase lock breaking. Sparse archives—evidence of acoustic loss—honest UI copy.

---

## 第 14 页 / BDC judging map · BDC 评审映射

**中文口播**  
对照 BDC 维度：**叙事**——沉浸节奏 → 不确定性 → 伦理分叉。**概念**——Umwelt、时间中的表型、生物—数字耦合。**语境**——去灭绝权衡；若相关则点到药材/贸易；殖民档案政治。**反思**——AI 边界、档案遗漏、用户反思占位。

**English**  
Judging map: Narrative—rhythm, uncertainty, ethical fork. Concept—Umwelt, temporal phenotype, biodigital coupling. Context—de-extinction trade-offs; pharm/trade if relevant; colonial archive politics. Reflection—AI limits, archival omissions, reflection stub.

---

## 第 15 页 / Deliverables & 4-week spine · 交付与四周骨架

**中文口播**  
交付清单：**线上 WebXR**、引用网格、至少一道伦理选择与反思、预告片、QR 锚点。英文 PDF 路径在幻灯片里已写明；幻灯片可由仓库脚本重建。四周骨架：**第一周**文献与 URL；**第二周**猛犸加 UI；**第三周**袋狼加伦理；**第四周**打磨与 Q&A——目标对齐 **Biodigital Excellence**。

**English**  
Deliverables: live WebXR, citation grid, one ethical choice plus reflection, trailer, QR anchor; EN PDF paths in-repo; rebuild script noted. Sprint: W1 literature/URLs → W2 mammoth + UI → W3 thylacine + ethics → W4 polish + Q&A—toward **Biodigital Excellence**.
