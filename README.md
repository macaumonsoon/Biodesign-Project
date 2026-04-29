# Biodesign-Project · BDC 2026 Summit<br />Biodesign-Project · BDC 2026 峰会

**Art / design project（设计与艺术类题目｜final title）：**  
*Extinction Archive: AI Memorial for Lost Species – Umwelt Archive: A Sensory Time Capsule*

**Zh：** 《灭绝档案》——面向逝去物种的 AI 纪念空间；“周遭世界档案”（Umwelt Archive）：感官时间胶囊。

Biodesign Challenge 2026 — **Umwelt Archive / Extinction Archive**：documentation, slide exports, build scripts, and future prototype code.

**Zh：** 文档、幻灯导出、构建脚本以及后续原型代码均在本仓库。

---

## Canonical GitHub copy · 上游参考与副本

- **Upstream｜上游：** [github.com/macaumonsoon/Biodesign-Project](https://github.com/macaumonsoon/Biodesign-Project) · branch **`main`**
- **Zh：** 若只维护你自己的仓库、不 push 到上游，请将本地 `git remote` 指向你的 GitHub 仓库；进展页 [`docs/index.html`](docs/index.html) 底部的 **`GITHUB_REPO`** 需改为 `你的用户名/仓库名`，GitHub Pages 按钮与链接才会正确。
- **En：** If you only maintain your own fork, point `git remote` at your repo; set **`GITHUB_REPO`** at the bottom of [`docs/index.html`](docs/index.html) to `username/repo` so Pages/GitHub links resolve correctly.

---

## Quick links · 快速链接

| Document｜文档 | Zh｜中文说明 | En｜Description |
|----------------|--------------|------------------|
| [PROJECT_PLAN.md](PROJECT_PLAN.md) | 主计划（团队、里程碑、仓库地图） | Master project plan (team, milestones, repo map) |
| [BDC_2026_Extinction_Archive_Planning_Document.md](BDC_2026_Extinction_Archive_Planning_Document.md) | 引用、分镜 ID、T5 语境与核验备注 | Citations, storyboard IDs, T5 context, verification notes |
| [index.html](index.html) | GitHub Pages **主页入口**（进展页、原型、介绍素材） | **Landing page** for GitHub Pages (progress page, prototypes, intro assets) |
| [templates/reflection-log-webxr.html](templates/reflection-log-webxr.html) | 体验结束反思界面模板 | End-of-experience reflection UI template |
| [docs/GITHUB_PDF_PREVIEW.md](docs/GITHUB_PDF_PREVIEW.md) | 峰会幻灯 PDF 在 GitHub 内预览链接写法 | How to link summit PDF preview in-browser on GitHub |
| [docs/index.html](docs/index.html) | **项目进展一览**；填写 `GITHUB_REPO`。建议在 Settings → Pages 使用 **GitHub Actions**（[workflow](.github/workflows/deploy-github-pages.yml)）发布**整仓**，可同时访问 `prototype/` | **Progress overview**; set `GITHUB_REPO`. Prefer **GitHub Actions** for Pages to publish the **whole repo** (includes `prototype/`) |
| [assets/media/intro-presentation.pdf](assets/media/intro-presentation.pdf) | 介绍 PPT（PDF，Pages 内可预览） | Intro deck PDF (previewable on Pages) |
| [assets/media/intro-video.mp4](assets/media/intro-video.mp4) | 介绍视频（压缩版，适配 Pages） | Intro video (web-ready compressed export) |

**Zh：** Pages 根地址通常为 `https://<用户名>.github.io/<仓库名>/`，进展页路径为 `/docs/index.html`。  

**En:** Typical Pages URL `https://<user>.github.io/<repo>/`; progress page at `/docs/index.html`.

### Summit slide deck · 峰会幻灯（PDF / GitHub）

**Zh**

- 小体量预览：`slides/export/[FINAL-SMALL] Extinction Archive Umwelt Hypothesis Dossiers_BDC2026.pdf`
- 完整 PPTX（可选）：`slides/export/[FINAL] Extinction Archive Umwelt Hypothesis Dossiers_BDC2026.pptx`
- 打开说明：[`slides/export/HOW_TO_OPEN_PPTX.md`](slides/export/HOW_TO_OPEN_PPTX.md)
- 合并 / 构建脚本：`scripts/merge_extinction_final_deck.py`、`scripts/build_final_presentation.py`、`scripts/beautify_extinction_summit_visual.py`

**En**

- Small export (preview): same paths as above.
- Full PPTX (optional): same path.
- Opening help: [`slides/export/HOW_TO_OPEN_PPTX.md`](slides/export/HOW_TO_OPEN_PPTX.md)
- Build / merge scripts: `scripts/merge_extinction_final_deck.py`, `scripts/build_final_presentation.py`, `scripts/beautify_extinction_summit_visual.py`

### Intro media for Pages · Pages 介绍素材

| Item｜条目 | Zh | En |
|------------|----|-----|
| PDF | `assets/media/intro-presentation.pdf` | Intro PDF (exported from PPT) |
| Video | `assets/media/intro-video.mp4` | Intro video (web-ready) |
| Poster | `assets/media/intro-poster.jpg` | Poster still / thumbnail |
| Embedded | `docs/index.html#intro-media` | Section with embedded preview + player |

---

## Documents (Umwelt tree) · 文档树（Umwelt）

| Path | Zh | En |
|------|----|-----|
| [docs/bdc-umwelt-archive/PROJECT_PLAN.md](docs/bdc-umwelt-archive/PROJECT_PLAN.md) | 完整项目计划（与根目录副本对应） | Full project plan (duplicate tree) |
| [docs/bdc-umwelt-archive/SLIDE_DECK.md](docs/bdc-umwelt-archive/SLIDE_DECK.md) | 幻灯大纲与演示脚本 | Slide outline + demo script |
| [docs/bdc-umwelt-archive/README.md](docs/bdc-umwelt-archive/README.md) | `docs` 文件夹内索引 | Index inside docs folder |

### BDC 2026 course reference · 课程与赛制参考

**Zh：** 竞赛指南与 Cursor 上下文位于 **`BDC2026_context-docs/`**。  

**En:** Competition guides and Cursor context live under **`BDC2026_context-docs/`**.

| Path | Zh | En |
|------|----|-----|
| [BDC2026_context-docs/biodesign_cursor_agent.md](BDC2026_context-docs/biodesign_cursor_agent.md) | Cursor / AI 协作语境 | Cursor / AI partner context |
| [BDC2026_context-docs/The complete guide to the 2026 Biodesign Challenge.md](BDC2026_context-docs/The%20complete%20guide%20to%20the%202026%20Biodesign%20Challenge.md) | 2026 BDC 总览 | Full 2026 BDC overview |
| Other `BDC2026_context-docs/*.md` | 资源指南、点子、备忘单等 | Resource guide, ideas, cheat sheet |
| `BDC2026_context-docs/*.docx` | 适用处的 Word 导出 | Word exports where applicable |

### Workspace layout · 工作区结构

| Path | Zh | En |
|------|----|-----|
| `01_ideation/` | BDC 创意工作簿步骤 | BDC ideation workbook steps |
| `02_research/` | 生物学、先行作品、参考文献 | Biology, prior art, references |
| `03_prototype/` | 代码、资源、实体模型笔记 | Code, assets, physical model notes |
| `04_deliverables/` | 演讲、视频、渲染、网站 | Presentation, video, renderings, website |
| `05_sprint_plan/` | 时间线与冲刺记录 | Timeline / sprint notes |

---

## Tech direction · 技术方向（Extinction Archive）

**Zh**

- **WebXR：** A-Frame / Three.js  
- **Summit / v1：** 以 Web 为主；最小实体锚点 + QR；v1 不要求活体生物传感器演示。

**En**

- **WebXR:** A-Frame / Three.js  
- **Summit / v1:** web-first; minimal physical anchor + QR; no living biosensor demo required for v1.

---

## Related repo · 相关仓库

**Zh：** **Portfolio-ReStyle-AI** 为独立产品/仓库——请勿在其中重复放置 BDC 文档。  

**En:** **Portfolio-ReStyle-AI** is a separate product/repo — do not duplicate BDC docs there.

---

## Open in Cursor (macOS) · 在 Cursor 中打开（macOS）

### Dock 只会显示一个 Cursor 图标（正常）· Single Dock icon is normal

**Zh：** macOS 将同一 App 的所有窗口归在一个 Dock 图标下；可按住 Dock 中的 Cursor 图标，或使用 **⌘\`** 切换窗口。  

**En:** macOS groups all windows of one app under one Dock icon; hold the Cursor icon in Dock or use **⌘\`** to switch windows.

### 不要只在 Cursor 内置终端里运行 `cursor …` · Avoid `cursor` CLI from built-in terminal

**Zh：** 内置终端带有 `VSCODE_*` / `CURSOR_*` 环境变量，CLI 容易连回当前 Cursor 实例。  

**En:** The integrated terminal sets `VSCODE_*` / `CURSOR_*`; the CLI often attaches to the current Cursor session.

1. **Zh：** **Finder：** 双击 **`Open-in-Cursor.command`**（若存在于仓库根目录）。  
   **En:** **Finder:** double-click **`Open-in-Cursor.command`** (if present at repo root).
2. **Zh：** **系统终端：** `cd` 到本仓库后执行 `open -a "Cursor" "$PWD"`。  
   **En:** **Terminal.app:** `cd` to this repo, then `open -a "Cursor" "$PWD"`.

### 已经开了 Cursor，但左侧没有文件树？· No file tree on the left?

**Zh：** **⌘B** 显示侧栏 · **⌘⇧E** 资源管理器 · **File → Open Folder…** 重新打开本目录。  

**En:** **⌘B** toggle sidebar · **⌘⇧E** Explorer · **File → Open Folder…** to reopen this folder.

---

## Sync · 同步

```bash
cd /path/to/this/repo
git pull origin main
git push origin main
```

**Zh：** 当 `origin` 指向你自己的仓库时，上述命令只与你本人远程同步，不会自动推到上游主仓。首次建库与 remote 说明见 **[docs/GITHUB_SYNC.md](docs/GITHUB_SYNC.md)**。  

**En:** When `origin` is your repo, these commands sync only with your remote, not the upstream by default. See **[docs/GITHUB_SYNC.md](docs/GITHUB_SYNC.md)** for first-time setup.

---

## Project overview · 项目简介

**Zh：** **《灭绝档案》** 参赛方案：以 **古生物钟学** 与 **时间生态位** 为核心，结合 WebXR、不确定度 UI 与伦理分叉，讨论去灭绝与生物多样性记忆。详细文献与分镜见 **`BDC_2026_Extinction_Archive_Planning_Document.md`**。

**En:** **Extinction Archive** pitches a WebXR memorial that foregrounds **chronobiology** and **temporal niche**, with uncertainty-aware UI and ethical forks, reflecting on de-extinction and biodiversity memory. See **`BDC_2026_Extinction_Archive_Planning_Document.md`** for citations and storyboard detail.
