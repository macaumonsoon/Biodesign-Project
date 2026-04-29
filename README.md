# Biodesign-Project · BDC 2026 Summit<br />Biodesign-Project · BDC 2026 峰会

本 README 按「介绍稿」逻辑编排：**赛制与团队 → 我们要解决的问题 → 方案与差异点 → 交付与 MVP 旅程 → 技术取向 → 如何浏览本仓库 → 幻灯与 Pages → 上游仓库与同步**。末尾附有简短的开发与编辑器备忘。

This README follows an **introduction-style arc**: competition & team → problem → approach & differentiation → deliverables & MVP journey → tech orientation → how to navigate the repo → decks & Pages → upstream & sync — plus brief notes for contributors.

---

## 1. Competition & presentation · 赛制与呈现类别

| | **En** | **中文** |
|---|--------|----------|
| **Competition** | [Biodesign Challenge 2026](https://biodesignchallenge.org) | Biodesign Challenge 2026 |
| **Track / theme** | *Convergent Life* — **Art / design project** | **设计与艺术类题目**，展览主题 **Convergent Life（聚合生命）** |
| **Award focus** | Biodigital Excellence; strong Narrative, Context, Reflection | 侧重 **Biodigital Excellence**，并在叙事、语境与反思维度做好对齐 |

**Official project title · 正式题目**

- **En:** *Extinction Archive: AI Memorial for Lost Species – Umwelt Archive: A Sensory Time Capsule*
- **Zh:** 《灭绝档案》——面向逝去物种的 AI 纪念空间；“周遭世界档案”（Umwelt Archive）：感官时间胶囊。

---

## 2. Team · 团队

| Role | **En** | **中文** |
|------|--------|----------|
| **Institution** | Macau University | 澳门大学 |
| **Mentor** | Atticus SIMS | Atticus SIMS |
| **Members** | **GUO Xiao Yue** (MC569254) — experience / narrative / ethics / dossier · **LIU Jia Qun** (MC569293) — tech / WebXR / generative & epistemic UI | **郭晓玥**（MC569254）体验 / 叙事 / 伦理 / 档案策展 · **刘嘉郡**（MC569293）技术 / WebXR / 生成式与认识论界面 |

---

## 3. Concept summary · 核心概念（与 [`PROJECT_PLAN.md`](PROJECT_PLAN.md) §2 对齐）

**Problem · 问题**

- **En:** Extinction removes more than DNA — it removes **temporal niches** (day/year rhythms). Public memory often collapses into flat images, not **time-in-the-world**.
- **Zh:** 物种灭绝带走的不仅是遗传信息，还有其在昼夜与季节中的 **时间生态位**；公众记忆常被压成图像，而非「在世界中的时间」。

**Approach · 方案**

- **En:** A WebXR **memorial** that reconstructs **temporal phenotypes** for focal species (e.g. woolly mammoth, thylacine), with an **epistemic UI** (Cited / Interpolated / Speculative), an **ethics fork**, and a **reflection** step — grounded in literature and honest uncertainty.
- **Zh:** 以 WebXR **纪念空间** 重建关键物种的 **时间表现型**（如猛犸象、袋狼），界面区分引用层级（Cited / Interpolated / Speculative），并包含 **伦理分叉** 与 **反思** 环节；叙事建立在文献与可核验不确定度之上。

**Differentiators · 差异点**

- **En:** Chronobiology + transparent limits of AI / aDNA inference + Indigenous sovereignty framing where relevant + **sensory time capsule** (rhythm & niche, not only visuals).
- **Zh:** 古生物钟学与节律叙事 + 对 AI / 古 DNA 推断 **诚实边界** + 在袋狼等案例中纳入 **原住民主权** 语境 + **感官时间胶囊**（节律与生态位，而非仅外观）。

Canonical citations, storyboard IDs, and verification notes live in **[`BDC_2026_Extinction_Archive_Planning_Document.md`](BDC_2026_Extinction_Archive_Planning_Document.md)**.

---

## 4. Deliverables & MVP journey · 交付物与用户旅程

**BDC deliverables (summary) · BDC 交付概览**

| Deliverable | **En** | **中文** |
|-------------|--------|----------|
| Summit talk | 10 min + 5 min Q&A | 10 分钟演讲 + 5 分钟问答 |
| Visuals | Storyboard tied to scene IDs in the detailed plan | 视觉与分镜，对齐详细规划中的场景 ID |
| Anchor | Minimal physical object + QR → experience | 极简实体锚点 + QR 进入体验 |
| Video | 1–5 min creative video | 1–5 分钟创意视频 |
| Slides | Maps to Narrative · Concept · Context · Reflection | 幻灯对应叙事 · 概念 · 语境 · 反思 |

**MVP journey · MVP 路径**

- **En:** Immersion → uncertainty layers → **one ethical choice** → **reflection input** (see [`templates/reflection-log-webxr.html`](templates/reflection-log-webxr.html)).
- **Zh:** 沉浸 → 不确定度分层 → **一次伦理选择** → **反思输入**（见 [`templates/reflection-log-webxr.html`](templates/reflection-log-webxr.html)）。

**Build constraint · 实现约束**

- **En:** Web-first shipped MVP; **no** living biosensor demo for v1 (`PROJECT_PLAN.md`: depth of science & citation over hardware).
- **Zh：** v1 以 Web 交付为主，**不要求**活体生物传感器演示；策略是 **重内容、轻装置**。

---

## 5. Tech orientation · 技术方向

| | **En** | **中文** |
|---|--------|----------|
| **Stack** | WebXR with **A-Frame** / **Three.js** | WebXR：**A-Frame** / **Three.js** |
| **v1** | Web-first; minimal physical anchor + QR | 以网页为主；最小实体锚点 + QR |

Key prototypes (see `PROJECT_PLAN.md` §5):

| Path | **En** | **中文** |
|------|--------|----------|
| [`prototype/index.html`](prototype/index.html) | Interactive extinction globe | 互动地球仪入口 |
| [`prototype/webxr/index.html`](prototype/webxr/index.html) | Three.js planet · WebXR shell | WebXR 行星球 |
| [`web/extinction-archive/index.html`](web/extinction-archive/index.html) | A-Frame archive · ethics fork · reflection bridge | A-Frame 档案原型 · 伦理分叉 · 反思桥接 |

---

## 6. Navigate this repository · 如何阅读本仓库

**Start here · 建议阅读顺序**

1. **[`PROJECT_PLAN.md`](PROJECT_PLAN.md)** — Executive plan (team, milestones, repo map).
2. **[`BDC_2026_Extinction_Archive_Planning_Document.md`](BDC_2026_Extinction_Archive_Planning_Document.md)** — Full hypothesis, citations, scene IDs.
3. **`slides/export/`** — Summit PDF/PPTX exports · [`slides/export/HOW_TO_OPEN_PPTX.md`](slides/export/HOW_TO_OPEN_PPTX.md).

**GitHub Pages · 面向访客的静态入口**

| Page | **En** | **中文** |
|------|--------|----------|
| [`index.html`](index.html) | Landing hub → docs & prototypes | 站点首页 → 进展页与原型 |
| [`docs/index.html`](docs/index.html) | Progress overview (set `GITHUB_REPO` at bottom for GitHub buttons) | 项目进展一览（页底填写 `GITHUB_REPO` 以修正 GitHub 按钮） |

Deploy with **[`.github/workflows/deploy-github-pages.yml`](.github/workflows/deploy-github-pages.yml)** — Settings → Pages → **Source: GitHub Actions** (whole-repo publish includes `prototype/`). Typical URL: `https://<user>.github.io/<repo>/`.

**Intro media (embedded on [`docs/index.html#intro-media`](docs/index.html#intro-media)) · 介绍素材**

| File | **En** | **中文** |
|------|--------|----------|
| [`assets/media/intro-presentation.pdf`](assets/media/intro-presentation.pdf) | Intro deck (PDF) | 介绍 PPT（导出 PDF） |
| [`assets/media/intro-video.mp4`](assets/media/intro-video.mp4) | Intro video (web-ready) | 介绍视频 |
| [`assets/media/intro-poster.jpg`](assets/media/intro-poster.jpg) | Poster still | 海报 / 视频封面 |

**Course context · 课程与赛制资料**

- **`BDC2026_context-docs/`** — e.g. [`The complete guide to the 2026 Biodesign Challenge.md`](BDC2026_context-docs/The%20complete%20guide%20to%20the%202026%20Biodesign%20Challenge.md), [`biodesign_cursor_agent.md`](BDC2026_context-docs/biodesign_cursor_agent.md).

**Folder map · 文件夹地图**

| Path | **En** | **中文** |
|------|--------|----------|
| `01_ideation/` | Ideation workbook | 创意工作簿 |
| `02_research/` | Research notes | 研究笔记 |
| `03_prototype/` | Prototype notes | 原型笔记 |
| `04_deliverables/` | Presentation, video, exhibition | 演讲、视频、展板等交付 |
| `05_sprint_plan/` | Sprint notes | 冲刺与时间线 |
| `docs/` | Extended docs & Pages HTML | 扩展文档与 Pages 页面 |

---

## 7. Canonical GitHub copy · 上游与自用副本

- **Upstream｜上游：** [`github.com/macaumonsoon/Biodesign-Project`](https://github.com/macaumonsoon/Biodesign-Project) · branch **`main`**
- **Fork workflow｜自用仓库：** Point `git remote` at **your** repo; set **`GITHUB_REPO`** at the bottom of [`docs/index.html`](docs/index.html) to `username/repo` so Pages links resolve. First-time sync: **[`docs/GITHUB_SYNC.md`](docs/GITHUB_SYNC.md)**.

---

## 8. Related repo · 相关仓库

**En:** **Portfolio-ReStyle-AI** is a separate product — do not duplicate BDC materials there.

**Zh：** **Portfolio-ReStyle-AI** 为独立项目仓库，请勿在其中重复存放本赛题文档。

---

## 9. Maintainer notes · 维护备忘（可选）

**Sync · 同步**

```bash
cd /path/to/this/repo
git pull origin main
git push origin main
```

See **[`docs/GITHUB_SYNC.md`](docs/GITHUB_SYNC.md)** when `origin` is your fork.

**Open in Cursor (macOS) · 在 Cursor 中打开**

- **Zh：** 勿仅在 Cursor 内置终端运行 `cursor …`（环境变量易连回当前实例）。可用 **`Open-in-Cursor.command`**（若存在），或在 **Terminal.app** 执行 `open -a "Cursor" "$PWD"`。
- **En:** Avoid running `cursor` CLI only from the integrated terminal; use **`Open-in-Cursor.command`** or Terminal.app: `open -a "Cursor" "$PWD"`.

**Dock｜侧栏：** macOS 同一 App 多窗口共用一个 Dock 图标 · **⌘\`** window switch · **⌘B** sidebar · **⌘⇧E** Explorer.

---

*Course context (example): Digital Art & AI Technology (MDes), April 2026.*
